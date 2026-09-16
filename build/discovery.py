"""
Build System File Discovery Module
===================================
Handles markdown file discovery and path resolution.
"""

import re
from pathlib import Path

from .config import PROJECT_ROOT


# =============================================================================
# File Discovery
# =============================================================================

def discover_markdown_files(config: dict) -> list[tuple[int, int, Path]]:
    """
    Discover all markdown files in chapter order.
    
    Returns list of (chapter_num, section_num, file_path) tuples.
    Chapter 0 is treated specially (unnumbered preface).
    """
    files = []
    
    # Add src/index.md (Preface) explicitly
    root_index = PROJECT_ROOT / "src" / "index.md"
    if root_index.exists():
        files.append((0, 0, root_index))

    for chapter_dir in config["chapters"]:
        chapter_path = PROJECT_ROOT / chapter_dir
        if not chapter_path.exists():
            print(f"Warning: Chapter directory not found: {chapter_path}")
            continue
        
        # Extract chapter number from folder name (e.g., "ch00-foundations" -> 0)
        folder_name = chapter_path.name
        chapter_num_match = re.match(r"ch(\d+)", folder_name)
        if chapter_num_match:
            chapter_num = int(chapter_num_match.group(1))
        else:
            chapter_num = len(files) + 1
        
        # Find all .md files, sorted by filename
        all_md_files = sorted(chapter_path.glob("*.md"))
        
        # Separate index.md from the rest
        index_files = [f for f in all_md_files if f.name == "index.md"]
        section_files = [f for f in all_md_files if f.name != "index.md"]
        
        # Add index.md first (unnumbered intro)
        if index_files:
            files.append((chapter_num, 0, index_files[0]))
            
        # Add regular sections
        current_section_num = 1
        for md_file in section_files:
            files.append((chapter_num, current_section_num, md_file))
            current_section_num += 1
    
    return files


# =============================================================================
# Path Resolution
# =============================================================================

def get_relative_output_path(source_file: Path, output_dir: Path, extension: str) -> Path:
    """
    Get the output path for a source file, preserving directory structure.
    
    Example: src/ch01-vector-spaces/01-intro.md -> _build/html/ch01-vector-spaces/01-intro.html
             index.md -> _build/html/index.html
    """
    try:
        relative = source_file.relative_to(PROJECT_ROOT / "src").parent
        output_subdir = output_dir / relative
    except ValueError:
        # File is not in src
        relative = source_file.relative_to(PROJECT_ROOT).parent
        output_subdir = output_dir / relative

    output_subdir.mkdir(parents=True, exist_ok=True)
    return output_subdir / (source_file.stem + extension)
