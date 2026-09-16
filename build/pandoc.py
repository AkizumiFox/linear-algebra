"""
Build System Pandoc Module
==========================
Handles Pandoc command building and execution.
"""

import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Optional

from .config import PROJECT_ROOT, CROSSREF_LABELS_FILE
from .tikz import TIKZ_CACHE_DIR
from .utils import print_error, print_info, print_warning, run_with_crash_retry


# =============================================================================
# Pandoc Command Building
# =============================================================================

_build_version = None


def build_version(config: dict) -> str:
    """
    Short hash of everything that shapes the site (sources, filters, templates, config).
    Used as a cache-busting query string, so unchanged rebuilds produce identical pages.
    """
    global _build_version
    if _build_version is None:
        digest = hashlib.sha1()
        roots = [PROJECT_ROOT / "src", PROJECT_ROOT / "filters", PROJECT_ROOT / "templates" / "html",
                 PROJECT_ROOT / "config", PROJECT_ROOT / "latex"]
        for root in roots:
            for path in sorted(p for p in root.rglob("*") if p.is_file()):
                digest.update(str(path.relative_to(PROJECT_ROOT)).encode())
                digest.update(path.read_bytes())
        _build_version = digest.hexdigest()[:10]
    return _build_version


def build_pandoc_command(
    source_file: Path,
    output_file: Path,
    output_format: str,
    config: dict,
    chapter_num: int,
    section_num: int,
    extract_title_func,  # Passed in to avoid circular import
    get_chapter_display_name_func,  # Passed in
    get_relative_output_path_func,  # Passed in
) -> list[str]:
    """Build the pandoc command with appropriate filters and options."""
    
    cmd = [
        "pandoc",
        str(source_file),
        "-o", str(output_file),
        "--standalone",
        "-f", "markdown+tex_math_single_backslash",
    ]
    
    # Add Lua filters
    filters_dir = PROJECT_ROOT / "filters"
    if (filters_dir / "format-visibility.lua").exists():
        cmd.extend(["--lua-filter", str(filters_dir / "format-visibility.lua")])
    cmd.extend(["--lua-filter", str(filters_dir / "tikz.lua")])
    cmd.extend(["--lua-filter", str(filters_dir / "enumerate.lua")])
    if (filters_dir / "theorems.lua").exists():
        cmd.extend(["--lua-filter", str(filters_dir / "theorems.lua")])
    if (filters_dir / "macros.lua").exists() and output_format == "html":
        cmd.extend(["--lua-filter", str(filters_dir / "macros.lua")])
    
    # Calculate relative depth for asset prefix
    if output_format == "html":
        output_dir = PROJECT_ROOT / config["output"]["html"]
        html_output = get_relative_output_path_func(source_file, output_dir, ".html")
        relative_depth = len(html_output.relative_to(output_dir).parts) - 1
        asset_prefix = "../" * relative_depth if relative_depth > 0 else "./"
    else:
        asset_prefix = "./"

    # Extract title
    title = extract_title_func(source_file)
    
    # Format section number
    if (chapter_num == 0 and section_num == 0) or (section_num == 0):
        formatted_number = ""
    elif chapter_num > 0:
        formatted_number = f"{chapter_num}.{section_num}"
    else:
        formatted_number = f"0.{section_num}"

    # Prepare metadata
    is_preface = chapter_num == 0 and section_num == 0
    metadata = {
        "chapter-num": chapter_num,
        "section-num": section_num,
        "is-preface": is_preface,
        "environment_settings": config.get("environment_settings", {}),
        "section-number": formatted_number,
        "project-root": str(PROJECT_ROOT),
        "asset-prefix": asset_prefix,
        "title": config.get("title", ""),  # Book title
        "tikz-cache-dir": str(TIKZ_CACHE_DIR),
        "build-version": build_version(config),
    }
    
    if title:
        # Format pagetitle with number
        if formatted_number:
            metadata["pagetitle"] = f"{formatted_number} {title}"
        else:
            metadata["pagetitle"] = title
            
        metadata["title-text"] = title

    if output_format == "html":
        chapter_dir = source_file.parent.name
        chapter_names = {
            "ch00-foundations": "Preliminary",
            "ch01-vector-spaces": "Vector Spaces and Dimensions",  
            "ch02-linear-transformations": "Linear Transformations",
        }
        chapter_title = chapter_names.get(
            chapter_dir, 
            get_chapter_display_name_func(str(source_file.parent.relative_to(PROJECT_ROOT)))
        )
        
        chapter_url = f"{asset_prefix}{chapter_dir}/index.html"
        page_url = f"{asset_prefix}{chapter_dir}/{output_file.name}"
        
        metadata["breadcrumb-chapter-title"] = chapter_title
        metadata["breadcrumb-chapter-url"] = chapter_url
        metadata["breadcrumb-page-title"] = title
        metadata["breadcrumb-page-url"] = page_url

        # PDF links: per-section PDF in html/pdf/, full book in html/book/
        pdf_rel = html_output.relative_to(output_dir).with_suffix(".pdf")
        metadata["pdf-url"] = f"{asset_prefix}pdf/{pdf_rel}"
        metadata["book-pdf-url"] = f"{asset_prefix}book/book.pdf"

    TIKZ_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # Write metadata to temp file
    file_hash = hashlib.md5(str(source_file).encode()).hexdigest()
    meta_dir = PROJECT_ROOT / "_build" / "tmp" / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_file = meta_dir / f"{file_hash}.yaml"
    
    with open(meta_file, "w") as f:
        f.write("---\n")
        for k, v in metadata.items():
            if k == "breadcrumbs":
                f.write(f"{k}: |\n")
                for line in v.splitlines():
                    f.write(f"  {line}\n")
            elif k == "environment_settings":
                f.write(f"{k}:\n")
                json_str = json.dumps(v, indent=2)
                for line in json_str.splitlines():
                    f.write(f"  {line}\n")
            elif isinstance(v, bool):
                f.write(f"{k}: {str(v).lower()}\n")
            else:
                safe_v = str(v).replace('"', '\\"')
                f.write(f'{k}: "{safe_v}"\n')
        f.write("---\n")

    cmd.extend(["--metadata-file", str(meta_file)])

    # Global label registry for cross-file references (read directly by theorems.lua)
    if CROSSREF_LABELS_FILE.exists():
        cmd.extend(["--metadata", f"crossref-labels-file={CROSSREF_LABELS_FILE}"])

    if output_format == "html":
        template_path = PROJECT_ROOT / config["templates"]["html"]
        if template_path.exists():
            cmd.extend(["--template", str(template_path)])
        
        if (filters_dir / "numbering.lua").exists():
            cmd.extend(["--lua-filter", str(filters_dir / "numbering.lua")])
        
        cmd.append("--mathjax")
        
    elif output_format == "pdf":
        template_path = PROJECT_ROOT / config["templates"]["latex"]
        if template_path.exists():
            cmd.extend(["--template", str(template_path)])

        # # -> chapter (0.4), ## -> section (0.4.1), ### -> subsection (0.4.1.1)
        cmd.extend(["--top-level-division", "chapter"])

        # Resource path so images in source dir (e.g. fig-subspace-1.png) are findable
        resource_paths = [str(source_file.parent.resolve()), str(PROJECT_ROOT / "src")]
        cmd.extend(["--resource-path", ":".join(resource_paths)])
        
        cmd.extend(["--pdf-engine", "pdflatex"])
        
        preamble_file = PROJECT_ROOT / "latex" / "preamble.tex"
        if preamble_file.exists():
            cmd.extend(["--include-in-header", str(preamble_file)])
        
        macros_file = PROJECT_ROOT / config["macros"]
        if macros_file.exists():
            cmd.extend(["--include-in-header", str(macros_file)])
    
    return cmd


# =============================================================================
# Pandoc Execution
# =============================================================================

def run_pandoc(
    cmd: list[str],
    verbose: bool = True,
    *,
    cwd: Optional[Path] = None,
    env: Optional[dict] = None,
) -> bool:
    """Run pandoc command and return success status. Logs errors and warnings."""
    if verbose:
        print_info(f"Running: {' '.join(cmd[:4])}...")
    
    run_kwargs = {"capture_output": True, "text": True, "check": True}
    if cwd is not None:
        run_kwargs["cwd"] = str(cwd)
    if env is not None:
        run_env = os.environ.copy()
        run_env.update(env)
        run_kwargs["env"] = run_env
    
    try:
        run_kwargs.pop("check")
        run_kwargs.pop("capture_output")
        run_kwargs.pop("text")
        result = run_with_crash_retry(cmd, **run_kwargs)
        # Log warnings (stderr) even on success
        if result.stderr and result.stderr.strip():
            print_warning(f"Pandoc stderr for {cmd[2] if len(cmd) > 2 else 'output'}:")
            for line in result.stderr.strip().splitlines():
                print(f"  {line}")
        return True
    except subprocess.CalledProcessError as e:
        print_error("Pandoc failed")
        if e.stdout and e.stdout.strip():
            print(f"  stdout:\n{e.stdout.strip()}")
        if e.stderr and e.stderr.strip():
            print_error(f"  stderr:\n{e.stderr.strip()}")
        return False
