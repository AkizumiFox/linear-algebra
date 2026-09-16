"""
Build System Manifest Module
============================
Handles theorem manifests and navigation generation.
"""

import json
import re
import shutil
import subprocess
from pathlib import Path

from .config import (
    PROJECT_ROOT, 
    BUILD_DIR,
    CROSSREF_LABELS_FILE, 
    SCAN_FILE,
    THEOREM_MANIFEST_FILE
)
from .discovery import discover_markdown_files
from .utils import print_step, print_success, print_warning, print_error, run_with_crash_retry


# =============================================================================
# Label Scanning
# =============================================================================

def scan_labels(config: dict):
    """
    Scan all markdown files to collect theorem labels.
    Generates crossref_labels.json.
    """
    print_step("Scanning labels...")
    
    files = discover_markdown_files(config)
    global_labels = {}
    scan_files = {}
    
    # Create a temporary metadata file for environment settings
    scan_meta_file = BUILD_DIR / "scan_meta.yaml"
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(scan_meta_file, "w") as f:
        f.write("environment_settings:\n")
        settings = config.get("environment_settings", {})
        json_str = json.dumps(settings, indent=2)
        for line in json_str.splitlines():
            f.write(f"  {line}\n")
    
    for chapter_num, section_num, source_file in files:
        dir_name = source_file.parent.name
        html_filename = source_file.stem + ".html"
        relative_path = f"{dir_name}/{html_filename}"
        
        cmd = [
            "pandoc",
            str(source_file),
            "--from", "markdown+tex_math_single_backslash",
            "--to", "json",
            "--lua-filter", str(PROJECT_ROOT / "filters" / "theorems.lua"),
            "--metadata-file", str(scan_meta_file),
            "--metadata", "scan_mode=true",
            "--metadata", f"chapter-num={chapter_num}",
            "--metadata", f"section-num={section_num}",
        ]
        
        try:
            result = run_with_crash_retry(cmd)
            if result.stderr and result.stderr.strip():
                print_warning(f"Scan warning for {source_file.name}:")
                for line in result.stderr.strip().splitlines():
                    print(f"    {line}")
            output = result.stdout
            
            for line in output.splitlines():
                if line.startswith("SCAN_RESULT:"):
                    result_data = json.loads(line[len("SCAN_RESULT:"):])
                    file_labels = result_data.get("labels") or {}
                    
                    for label_id, info in file_labels.items():
                        info["file"] = relative_path
                        global_labels.setdefault(label_id, info)
                    scan_files[relative_path] = {
                        "source": str(source_file.relative_to(PROJECT_ROOT)),
                        "labels": sorted(file_labels),
                        "refs": result_data.get("refs") or [],
                    }
                    break
                    
        except subprocess.CalledProcessError as e:
            print_error(f"Error scanning {source_file.name}: {e}")
            if e.stderr and e.stderr.strip():
                for line in e.stderr.strip().splitlines():
                    print(f"    {line}")
            continue
            
    CROSSREF_LABELS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CROSSREF_LABELS_FILE, "w") as f:
        json.dump({"crossref_labels": global_labels}, f, indent=2)
    with open(SCAN_FILE, "w") as f:
        json.dump({"files": scan_files}, f, indent=2)
        
    print_success(f"Scanned {len(global_labels)} labels.")
    return global_labels


# =============================================================================
# Theorem Manifest
# =============================================================================

def generate_theorem_manifest(config: dict):
    """Generate theorems.json for tooltip previews from the global label registry."""
    if not CROSSREF_LABELS_FILE.exists():
        print_warning("crossref_labels.json not found. Tooltips may be empty.")
        return

    with open(CROSSREF_LABELS_FILE) as f:
        data = json.load(f)
        labels = data.get("crossref_labels", {})
    
    manifest = {}
    for label_id, info in labels.items():
        manifest[label_id] = {
            "type": info.get("type", "unknown"),
            "number": info.get("number", "?"),
            "type_name": info.get("type_name", ""),
            "title": info.get("title", ""),
            "title_html": info.get("title_html", ""),
            "html": info.get("html_content", f"<p><strong>{info.get('type_name')} {info.get('number')}</strong> ({info.get('title')})</p>"),
            "file": info.get("file", "")
        }
    
    THEOREM_MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(THEOREM_MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)
    
    html_output = PROJECT_ROOT / config["output"]["html"]
    if html_output.exists():
        shutil.copy(THEOREM_MANIFEST_FILE, html_output / "theorems.json")
    
    print_success(f"Theorem manifest: {len(manifest)} entries")


# =============================================================================
# Navigation Manifest
# =============================================================================

def generate_navigation_manifest(config: dict, output_dir: Path, extract_title_func=None):
    """Generate navigation.json for the sidebar."""
    navigation = {
        "title": config.get("title", "Book"),
        "author": config.get("author", ""),
        "chapters": []
    }
    
    chapter_names = {
        "ch00-foundations": "Preliminary",
        "ch01-vector-spaces": "Vector Spaces and Dimensions",  
        "ch02-linear-transformations": "Linear Transformations",
    }
    
    for chapter_idx, chapter_dir in enumerate(config["chapters"]):
        chapter_path = PROJECT_ROOT / chapter_dir
        if not chapter_path.exists():
            continue
        
        dir_basename = chapter_path.name
        chapter_title = chapter_names.get(dir_basename, _get_chapter_display_name(chapter_dir, extract_title_func))
        
        chapter_entry = {
            "title": chapter_title,
            "number": chapter_idx,
            "collapsed": False,
            "sections": [],
            "path": None
        }
        
        if (chapter_path / "index.md").exists():
            chapter_entry["path"] = f"{dir_basename}/index.html"
        
        md_files = sorted([f for f in chapter_path.glob("*.md")])
        
        section_counter = 1
        for md_file in md_files:
            if md_file.name == "index.md":
                continue
                
            title = extract_title_func(md_file) if extract_title_func else md_file.stem
            section_num = f"{chapter_idx}.{section_counter}" if chapter_idx > 0 else f"0.{section_counter}"
            section_counter += 1
            
            relative_html_path = f"{dir_basename}/{md_file.stem}.html"
            
            chapter_entry["sections"].append({
                "title": title,
                "number": section_num,
                "path": relative_html_path,
                "filename": md_file.name
            })
        
        navigation["chapters"].append(chapter_entry)
    
    nav_file = output_dir / "navigation.json"
    with open(nav_file, "w", encoding="utf-8") as f:
        json.dump(navigation, f, indent=2, ensure_ascii=False)
    
    print_success(f"Navigation manifest: {sum(len(c['sections']) for c in navigation['chapters'])} sections")
    
    return navigation


def _get_chapter_display_name(chapter_dir: str, extract_title_func=None) -> str:
    """Get display name for a chapter from its directory name or index.md."""
    chapter_path = PROJECT_ROOT / chapter_dir
    
    index_file = chapter_path / "index.md"
    if index_file.exists() and extract_title_func:
        title = extract_title_func(index_file)
        if title:
            return title
    
    dir_name = chapter_path.name
    match = re.match(r'^ch(\d+)-(.+)$', dir_name)
    if match:
        name_part = match.group(2).replace('-', ' ').title()
        return name_part
    
    return dir_name.replace('-', ' ').title()
