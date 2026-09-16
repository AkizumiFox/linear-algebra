"""
Build System PDF Module
=======================
Handles PDF output building.
"""

import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from .config import PROJECT_ROOT
from .discovery import discover_markdown_files, get_relative_output_path
from .pandoc import build_pandoc_command, run_pandoc
from .utils import print_step, print_file_action, print_success, print_error


# =============================================================================
# PDF Building
# =============================================================================

def build_pdf(
    config: dict, 
    specific_file: Optional[Path] = None,
    extract_title_func=None,
    get_chapter_display_name_func=None,
):
    """Build PDF output (per-file). Uses two-step: pandoc -> .tex, then pdflatex."""
    print_step("Building PDF...")
    
    output_dir = PROJECT_ROOT / config["output"]["pdf"]
    output_dir.mkdir(parents=True, exist_ok=True)
    tex_tmp = PROJECT_ROOT / "_build" / "tmp" / "pdf-single"
    tex_tmp.mkdir(parents=True, exist_ok=True)
    
    files = discover_markdown_files(config)
    if specific_file:
        specific_file = Path(specific_file).resolve()
        files = [(c, s, f) for c, s, f in files if f == specific_file]
        if not files:
            print_error(f"File not found in chapters: {specific_file}")
            return
    
    pdf_env = {**os.environ, "TEXINPUTS": f".:{PROJECT_ROOT}//:"}

    def build_one(chapter_num: int, section_num: int, source_file: Path) -> tuple[str, str, bool]:
        """Build one PDF. Returns (source_name, output_name, success)."""
        output_file = get_relative_output_path(source_file, output_dir, ".pdf")
        tex_file = tex_tmp / output_file.relative_to(output_dir).with_suffix(".tex")
        tex_file.parent.mkdir(parents=True, exist_ok=True)

        cmd = build_pandoc_command(
            source_file, tex_file, "pdf", config, chapter_num, section_num,
            extract_title_func, get_chapter_display_name_func, get_relative_output_path
        )
        cmd = [c for c in cmd if c != "--pdf-engine" and c != "pdflatex"]
        idx = cmd.index("-o")
        cmd[idx + 1] = str(tex_file)

        if not run_pandoc(cmd, verbose=False, cwd=PROJECT_ROOT, env=pdf_env):
            return (source_file.name, output_file.name, False)

        try:
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", tex_file.name],
                cwd=str(tex_file.parent),
                env=pdf_env,
                capture_output=True,
                text=True,
            )
            out_pdf = tex_file.with_suffix(".pdf")
            if out_pdf.exists():
                output_file.parent.mkdir(parents=True, exist_ok=True)
                out_pdf.replace(output_file)
                return (source_file.name, output_file.name, True)
        except Exception as e:
            print_error(f"pdflatex failed for {source_file.name}: {e}")
        return (source_file.name, output_file.name, False)

    max_workers = min(4, len(files))
    success_count = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(build_one, c, s, f): (c, s, f)
            for c, s, f in files
        }
        for future in as_completed(futures):
            try:
                src_name, out_name, ok = future.result()
                if ok:
                    success_count += 1
                print_file_action("Built", src_name, out_name)
            except Exception as e:
                print_error(str(e))

    print_success(f"PDF build complete: {success_count}/{len(files)} files")

    # Sync all per-section PDFs to HTML output so links work (including index pages)
    _sync_pdfs_to_html(config)


def _sync_pdfs_to_html(config: dict):
    """Copy all per-section PDFs from _build/pdf to _build/html/pdf."""
    pdf_dir = PROJECT_ROOT / config["output"]["pdf"]
    html_dir = PROJECT_ROOT / config["output"]["html"]
    dest_dir = html_dir / "pdf"
    if not pdf_dir.exists():
        return
    dest_dir.mkdir(parents=True, exist_ok=True)
    for src in pdf_dir.rglob("*.pdf"):
        if src.name == "book.pdf":
            continue
        rel = src.relative_to(pdf_dir)
        dst = dest_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def build_book(config: dict):
    """Build combined book PDF."""
    print_step("Building combined book PDF...")
    
    output_file = PROJECT_ROOT / config["output"]["book"]
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Use temp dir for LaTeX intermediates so _build/pdf stays clean (no .tex, .aux, .log, .out, .toc)
    latex_tmp = PROJECT_ROOT / "_build" / "tmp" / "latex-book"
    latex_tmp.mkdir(parents=True, exist_ok=True)
    tex_file = latex_tmp / "book.tex"
    
    files = discover_markdown_files(config)
    if not files:
        print_error("No source files found")
        return
    
    # Build combined markdown with file-boundary markers (for per-file preface/chapter in book)
    # Include all files (root index, chapter indices, sections) so index appears in front of each chapter
    combined_parts = []
    from .cli import get_chapter_display_name
    for i, (chapter_num, section_num, source_file) in enumerate(files):
        content = source_file.read_text(encoding="utf-8")
        is_preface = (i == 0 and chapter_num == 0 and section_num == 0)
        chap_title = ""
        if section_num >= 1:
            chap_dir = str(source_file.parent.relative_to(PROJECT_ROOT))
            chap_title = get_chapter_display_name(chap_dir)
        attrs = f'data-chapter="{chapter_num}" data-section="{section_num}"'
        if is_preface:
            attrs += ' data-preface="true"'
        if chap_title:
            attrs += f' data-chapter-title="{chap_title}"'
        marker = f'\n\n::: {{.file-boundary {attrs}}}\n:::\n\n'
        combined_parts.append(marker + content)
    combined_md = "\n\n".join(combined_parts)
    combined_path = latex_tmp / "_combined.md"
    combined_path.write_text(combined_md, encoding="utf-8")
    
    # Metadata for book: environment_settings, book-mode, is-preface (for template counters)
    import json
    book_meta = latex_tmp / "_book_meta.yaml"
    env_settings = config.get("environment_settings", {})
    with open(book_meta, "w", encoding="utf-8") as f:
        f.write("---\nbook-mode: true\nis-preface: true\nenvironment_settings:\n")
        json_str = json.dumps(env_settings, indent=2)
        for line in json_str.splitlines():
            f.write(f"  {line}\n")
        f.write("---\n")
    
    cmd = [
        "pandoc",
        str(combined_path),
        "-f", "markdown+tex_math_single_backslash",
        "-o", str(tex_file),
        "--standalone",
        "--toc",
        "--toc-depth", "2",
        "--variable", "titlepage",
        "--top-level-division", "chapter",
        "--metadata-file", str(book_meta),
        "--metadata", f"title={config.get('title', 'Untitled')}",
        "--metadata", f"author={config.get('author', 'Anonymous')}",
    ]
    
    # Resource path so images from all chapter dirs are findable
    resource_paths = [str(PROJECT_ROOT / "src")] + [
        str(PROJECT_ROOT / ch) for ch in config.get("chapters", [])
    ]
    cmd.extend(["--resource-path", ":".join(resource_paths)])
    
    template_path = PROJECT_ROOT / config.get("templates", {}).get(
        "latex", "templates/latex/template.tex"
    )
    if template_path.exists():
        cmd.extend(["--template", str(template_path)])
    
    filters_dir = PROJECT_ROOT / "filters"
    if (filters_dir / "format-visibility.lua").exists():
        cmd.extend(["--lua-filter", str(filters_dir / "format-visibility.lua")])
    if (filters_dir / "theorems.lua").exists():
        cmd.extend(["--lua-filter", str(filters_dir / "theorems.lua")])
    if (filters_dir / "macros.lua").exists():
        cmd.extend(["--lua-filter", str(filters_dir / "macros.lua")])
    
    preamble_file = PROJECT_ROOT / "latex" / "preamble-book.tex"
    if preamble_file.exists():
        cmd.extend(["--include-in-header", str(preamble_file)])
    
    macros_file = PROJECT_ROOT / config["macros"]
    if macros_file.exists():
        cmd.extend(["--include-in-header", str(macros_file)])
    
    if not run_pandoc(cmd, cwd=PROJECT_ROOT):
        return
    
    # Compile .tex to PDF with pdflatex (avoids xelatex/xdvipdfmx font issues)
    import subprocess
    import os
    pdf_env = {**os.environ, "TEXINPUTS": f".:{PROJECT_ROOT}//:"}
    pdf_cmd = ["pdflatex", "-interaction=nonstopmode", str(tex_file.name)]
    try:
        # Run from tex dir so aux/output go there; TEXINPUTS finds project packages
        result = subprocess.run(
            pdf_cmd,
            cwd=str(tex_file.parent),
            env=pdf_env,
            capture_output=True,
            text=True,
        )
        # Second run for TOC/cross-refs
        subprocess.run(pdf_cmd, cwd=str(tex_file.parent), env=pdf_env, capture_output=True)
        out_pdf = tex_file.with_suffix(".pdf")
        if out_pdf.exists():
            out_pdf.replace(output_file)
            print_success(f"Book PDF created: {output_file}")
            # Copy to HTML output so the PDF link in the sidebar works
            html_dir = PROJECT_ROOT / config["output"]["html"]
            book_in_html = html_dir / "book" / "book.pdf"
            book_in_html.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(output_file, book_in_html)
        else:
            print_error("pdflatex did not produce PDF")
            if result.stderr:
                print(result.stderr[-2000:])  # last 2k chars
    except Exception as e:
        print_error(f"pdflatex failed: {e}")
