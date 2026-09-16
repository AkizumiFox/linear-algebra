"""
Build System CLI Module
=======================
Command-line interface and main entry point.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

from .config import PROJECT_ROOT, load_config, reset_counter_state
from .discovery import discover_markdown_files
from .html import build_html
from .pdf import build_pdf, build_book
from .manifest import scan_labels, generate_theorem_manifest, generate_navigation_manifest
from .deploy import deploy
from .utils import print_info, print_header, print_error


# =============================================================================
# Utility Functions
# =============================================================================

def extract_title_from_markdown(filepath: Path) -> str:
    """Extract the first H1 title from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == '---':
                    for line in f:
                        if line.strip() == '---':
                            break
                    continue
                if line.startswith('# '):
                    return line[2:].strip()
    except Exception:
        pass
    return filepath.stem.replace('-', ' ').replace('_', ' ').title()


def get_chapter_display_name(chapter_dir: str) -> str:
    """Get display name for a chapter from its directory name or index.md."""
    chapter_path = PROJECT_ROOT / chapter_dir
    
    index_file = chapter_path / "index.md"
    if index_file.exists():
        title = extract_title_from_markdown(index_file)
        if title:
            return title
    
    dir_name = chapter_path.name
    match = re.match(r'^ch(\d+)-(.+)$', dir_name)
    if match:
        name_part = match.group(2).replace('-', ' ').title()
        return name_part
    
    return dir_name.replace('-', ' ').title()


def clean(config: dict):
    """Remove build directory."""
    build_dir = PROJECT_ROOT / "_build"
    if not build_dir.exists():
        print_info("Nothing to clean")
        return
    try:
        shutil.rmtree(build_dir)
        print_info(f"Removed: {build_dir}")
    except OSError as e:
        print_error(f"Failed to remove {build_dir}: {e}")
        print_error("Close any open PDFs or files from _build/ and try again.")


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    print_header("Pandoc Book Build System")

    parser = argparse.ArgumentParser(
        description="Pandoc Book Build System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python build.py html                Build all HTML files
    python build.py html src/ch01/01.md Build specific HTML file
    python build.py pdf                 Build all PDF files
    python build.py book                Build combined book PDF
    python build.py all                 Build everything
    python build.py clean               Remove _build directory
    python build.py manifest            Generate theorems.json only
    python build.py deploy              Build and copy to site/ (add --push to push)
        """
    )
    
    parser.add_argument(
        "command",
        choices=["html", "pdf", "book", "all", "clean", "manifest", "scan", "deploy"],
        help="Build command to run"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Optional: specific file to build"
    )
    parser.add_argument(
        "--no-build",
        action="store_true",
        help="Deploy only: skip build, just copy existing _build/html to deploy-dir"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Deploy: after copying, run git add, commit, push from deploy-dir"
    )
    
    args = parser.parse_args()
    
    if args.command == "clean":
        config = load_config()
        clean(config)
        return
    
    config = load_config()
    
    if args.command == "scan":
        scan_labels(config)
    elif args.command == "manifest":
        generate_theorem_manifest(config)
    elif args.command == "html":
        specific_file = Path(args.file).resolve() if args.file else None
        if not specific_file:
            scan_labels(config)
        
        def nav_manifest_wrapper(cfg, output_dir):
            generate_navigation_manifest(cfg, output_dir, extract_title_from_markdown)
        
        build_html(
            config, 
            specific_file,
            extract_title_func=extract_title_from_markdown,
            get_chapter_display_name_func=get_chapter_display_name,
            scan_labels_func=scan_labels,
            generate_theorem_manifest_func=generate_theorem_manifest,
            generate_navigation_manifest_func=nav_manifest_wrapper,
        )
    elif args.command == "pdf":
        specific_file = Path(args.file).resolve() if args.file else None
        build_pdf(
            config, 
            specific_file,
            extract_title_func=extract_title_from_markdown,
            get_chapter_display_name_func=get_chapter_display_name,
        )
    elif args.command == "book":
        build_book(config)
    elif args.command == "deploy":
        deploy(config, run_build=not args.no_build, push=args.push)
    elif args.command == "all":
        reset_counter_state()
        scan_labels(config)
        
        def nav_manifest_wrapper(cfg, output_dir):
            generate_navigation_manifest(cfg, output_dir, extract_title_from_markdown)
        
        build_html(
            config, 
            None,
            extract_title_func=extract_title_from_markdown,
            get_chapter_display_name_func=get_chapter_display_name,
            scan_labels_func=scan_labels,
            generate_theorem_manifest_func=generate_theorem_manifest,
            generate_navigation_manifest_func=nav_manifest_wrapper,
        )
        build_pdf(
            config, 
            None,
            extract_title_func=extract_title_from_markdown,
            get_chapter_display_name_func=get_chapter_display_name,
        )
        build_book(config)


if __name__ == "__main__":
    main()
