"""
Build System Search Module
==========================
Generates search index for client-side search.
"""

import json
import subprocess
from pathlib import Path

from .config import PROJECT_ROOT
from .discovery import discover_markdown_files, get_relative_output_path
from .utils import print_step, print_success, print_error

def extract_title(filepath: Path) -> str:
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

def generate_search_index(config: dict):
    """Generate search.json index from markdown files."""
    print_step("Generating search index...")
    
    files = discover_markdown_files(config)
    search_index = []
    output_dir = PROJECT_ROOT / config["output"]["html"]
    
    for chapter_num, section_num, source_file in files:
        # Calculate relative path to the HTML file
        output_file = get_relative_output_path(source_file, output_dir, ".html")
        try:
            relative_url = output_file.relative_to(output_dir)
        except ValueError:
            relative_url = output_file.name

        title = extract_title(source_file)
        
        try:
            # Convert markdown to plain text for search content
            # --wrap=none prevents newlines in the middle of sentences
            result = subprocess.run(
                ['pandoc', str(source_file), '-t', 'plain', '--wrap=none'],
                capture_output=True,
                text=True,
                check=True
            )
            content = result.stdout.strip()
            
            # Create search entry
            entry = {
                "title": title,
                "url": str(relative_url),
                "content": content
            }
            search_index.append(entry)
            
        except subprocess.CalledProcessError as e:
            print_error(f"Error processing {source_file.name} for search index: {e}")
            if e.stderr and e.stderr.strip():
                for line in e.stderr.strip().splitlines():
                    print(f"    {line}")
            continue

    # Write search.json
    output_path = output_dir / "search.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)
        
    print_success(f"Search index generated with {len(search_index)} entries")
