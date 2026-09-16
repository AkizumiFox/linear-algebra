"""
Build System HTML Module
========================
Handles HTML output building.
"""

import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from .config import PROJECT_ROOT, CROSSREF_LABELS_FILE
from .discovery import discover_markdown_files, get_relative_output_path
from .pandoc import build_pandoc_command, run_pandoc
from .search import generate_search_index
from .utils import print_step, print_file_action, print_success, print_warning, print_error


# =============================================================================
# HTML Building
# =============================================================================

def build_html(
    config: dict, 
    specific_file: Optional[Path] = None,
    extract_title_func=None,
    get_chapter_display_name_func=None,
    scan_labels_func=None,
    generate_theorem_manifest_func=None,
    generate_navigation_manifest_func=None,
):
    """Build HTML output."""
    print_step("Building HTML...")
    
    # Always scan labels first for accurate cross-refs
    if not specific_file and not CROSSREF_LABELS_FILE.exists():
        if scan_labels_func:
            scan_labels_func(config)
    elif specific_file and not CROSSREF_LABELS_FILE.exists():
        print_warning("Building single file without full label scan. Cross-refs may be broken.")
    
    output_dir = PROJECT_ROOT / config["output"]["html"]
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Remove any LaTeX/PDF artifacts (PDFs and LaTeX intermediates live in _build/pdf only)
    for f in ("book.tex", "book.aux", "book.log", "book.out", "book.toc", "book.pdf"):
        (output_dir / f).unlink(missing_ok=True)
    for pdf in output_dir.rglob("*.pdf"):
        pdf.unlink(missing_ok=True)
    
    # Copy assets
    copy_html_assets(config, output_dir)
    copy_chapter_assets(config, output_dir)
    
    files = discover_markdown_files(config)
    if specific_file:
        specific_file = Path(specific_file).resolve()
        files = [(c, s, f) for c, s, f in files if f == specific_file]
        if not files:
            print_error(f"File not found in chapters: {specific_file}")
            return
    
    # Precompute commands with prev/next metadata for all files
    def build_task(i: int, chapter_num: int, section_num: int, source_file: Path):
        output_file = get_relative_output_path(source_file, output_dir, ".html")
        cmd = build_pandoc_command(
            source_file, output_file, "html", config, chapter_num, section_num,
            extract_title_func, get_chapter_display_name_func, get_relative_output_path
        )
        if i > 0:
            p_chap, p_sec, prev_src = flat_files[i - 1]
            prev_out = get_relative_output_path(prev_src, output_dir, ".html")
            try:
                rel_prev = os.path.relpath(prev_out, output_file.parent)
                prev_title = extract_title_func(prev_src) if extract_title_func else ""
                prev_num = "" if (p_chap == 0 and p_sec == 0) or p_sec == 0 else (
                    f"{p_chap}.{p_sec} " if p_chap > 0 else f"0.{p_sec} "
                )
                cmd.extend([
                    "--metadata", f"prev-page-url={rel_prev}",
                    "--metadata", f"prev-page-title={prev_title}",
                    "--metadata", f"prev-page-number={prev_num}"
                ])
            except ValueError:
                pass
        if i < len(flat_files) - 1:
            n_chap, n_sec, next_src = flat_files[i + 1]
            next_out = get_relative_output_path(next_src, output_dir, ".html")
            try:
                rel_next = os.path.relpath(next_out, output_file.parent)
                next_title = extract_title_func(next_src) if extract_title_func else ""
                next_num = "" if (n_chap == 0 and n_sec == 0) or n_sec == 0 else (
                    f"{n_chap}.{n_sec} " if n_chap > 0 else f"0.{n_sec} "
                )
                cmd.extend([
                    "--metadata", f"next-page-url={rel_next}",
                    "--metadata", f"next-page-title={next_title}",
                    "--metadata", f"next-page-number={next_num}"
                ])
            except ValueError:
                pass
        return (source_file.name, output_file.name, cmd)

    flat_files = files
    tasks = [build_task(i, c, s, f) for i, (c, s, f) in enumerate(files)]
    max_workers = min(8, len(tasks))
    success_count = 0

    def run_one(task):
        return run_pandoc(task[2], verbose=False)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_one, task): task for task in tasks}
        for future in as_completed(futures):
            task = futures[future]
            try:
                if future.result():
                    success_count += 1
                print_file_action("Built", task[0], task[1])
            except Exception:
                pass

    print_success(f"HTML build complete: {success_count}/{len(files)} files")
    
    # Generate manifests
    if generate_theorem_manifest_func:
        generate_theorem_manifest_func(config)
    if generate_navigation_manifest_func:
        generate_navigation_manifest_func(config, output_dir)
        
    # Generate search index
    if not specific_file:
        generate_search_index(config)


def copy_html_assets(config: dict, output_dir: Path):
    """Copy CSS, JS, and other assets to HTML output directory."""
    styles_src = PROJECT_ROOT / config["styles"]["html"]
    if styles_src.exists():
        styles_dst = output_dir / "styles.css"
        shutil.copy(styles_src, styles_dst)
    
    js_src = PROJECT_ROOT / "templates" / "html" / "main.js"
    if js_src.exists():
        js_dst = output_dir / "main.js"
        shutil.copy(js_src, js_dst)


def copy_chapter_assets(config: dict, output_dir: Path):
    """Copy images and other assets from chapter directories to output."""
    count = 0
    for chapter_dir in config["chapters"]:
        src_dir = PROJECT_ROOT / chapter_dir
        if not src_dir.exists():
            continue
            
        dst_dir = output_dir / src_dir.name
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        # Extensions to copy
        extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg']
        
        for ext in extensions:
            for src_file in src_dir.glob(ext):
                dst_file = dst_dir / src_file.name
                
                # Copy if destination doesn't exist or source is newer
                if not dst_file.exists() or src_file.stat().st_mtime > dst_file.stat().st_mtime:
                    shutil.copy2(src_file, dst_file)
                    print_file_action("Copying asset", src_file.name, dst_file.name)
                    count += 1
    
    if count > 0:
        print_success(f"Copied {count} chapter assets")
