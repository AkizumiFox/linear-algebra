"""
Build System Manifest Module
============================
Scans every page for labels, references and search text (cached per page), and writes
the data files the website loads: tooltip shards, navigation and the search index.
"""

import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

from .book import Book, Page
from .utils import print_step, print_success, print_warning, print_error, run_with_crash_retry


# =============================================================================
# Label Scanning
# =============================================================================

def _scan_meta_file(book: Book):
    path = book.build_dir / "tmp" / "scan_meta.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"environment_settings": book.environment_settings}), encoding="utf-8")
    return path


def _scan_key(book: Book, page: Page) -> str:
    digest = hashlib.sha1()
    digest.update((book.filters_dir / "theorems.lua").read_bytes())
    digest.update((book.filters_dir / "components.lua").read_bytes())
    digest.update(json.dumps(book.environment_settings, sort_keys=True).encode())
    digest.update(f"{page.chapter_number}:{page.section}:{page.html_path}".encode())
    digest.update(page.source.read_bytes())
    return digest.hexdigest()


def _scan_page(book: Book, page: Page, meta_file) -> dict | None:
    cache_file = book.cache_dir / "scan" / f"{_scan_key(book, page)}.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    cmd = [
        "pandoc", str(page.source),
        "--from", "markdown+tex_math_single_backslash",
        "--to", "json",
        "--lua-filter", str(book.filters_dir / "components.lua"),
        "--lua-filter", str(book.filters_dir / "theorems.lua"),
        "--metadata-file", str(meta_file),
        "--metadata", "scan_mode=true",
        "--metadata", f"book-root={book.root}",
        "--metadata", f"engine-root={book.filters_dir.parent}",
        "--metadata", f"source-path={page.source.relative_to(book.root)}",
        "--metadata", f"chapter-num={page.chapter_number}",
        "--metadata", f"section-num={page.section}",
    ]
    try:
        result = run_with_crash_retry(cmd)
    except subprocess.CalledProcessError as e:
        print_error(f"Error scanning {page.source.name}")
        for line in (e.stderr or "").strip().splitlines():
            print(f"    {line}")
        return None
    if result.stderr and result.stderr.strip():
        print_warning(f"Scan warning for {page.source.name}:")
        for line in result.stderr.strip().splitlines():
            print(f"    {line}")

    errors = [json.loads(line[len("COMPONENT_ERROR:"):])["message"]
              for line in result.stdout.splitlines() if line.startswith("COMPONENT_ERROR:")]
    for line in result.stdout.splitlines():
        if line.startswith("SCAN_RESULT:"):
            data = json.loads(line[len("SCAN_RESULT:"):])
            data = {"labels": data.get("labels") or {}, "refs": data.get("refs") or [], "text": data.get("text") or "",
                    "errors": errors}
            cache_file.parent.mkdir(parents=True, exist_ok=True)
            cache_file.write_text(json.dumps(data), encoding="utf-8")
            return data
    print_error(f"No scan result for {page.source.name}")
    return None


def scan_labels(book: Book) -> dict:
    """
    Scan all pages. Writes crossref_labels.json (label registry used by the filters) and
    scan.json (per-page labels, references and text). Returns the scan data.
    """
    print_step("Scanning labels...")
    meta_file = _scan_meta_file(book)
    pages = book.pages
    with ThreadPoolExecutor(max_workers=min(8, len(pages) or 1)) as executor:
        results = list(executor.map(lambda p: _scan_page(book, p, meta_file), pages))

    global_labels = {}
    scan_files = {}
    for page, data in zip(pages, results):
        if data is None:
            continue
        for label_id, info in data["labels"].items():
            info = dict(info, file=page.html_path, shard=page.shard)
            global_labels.setdefault(label_id, info)
        scan_files[page.html_path] = {
            "source": str(page.source.relative_to(book.root)),
            "labels": sorted(data["labels"]),
            "refs": data["refs"],
            "text": data["text"],
            "errors": data.get("errors", []),
        }

    book.build_dir.mkdir(parents=True, exist_ok=True)
    book.labels_file.write_text(json.dumps({"crossref_labels": global_labels}, indent=2), encoding="utf-8")
    scan = {"files": scan_files}
    book.scan_file.write_text(json.dumps(scan, indent=2), encoding="utf-8")
    print_success(f"Scanned {len(global_labels)} labels.")
    return scan


def load_scan(book: Book) -> tuple[dict, dict]:
    """(scan data, label registry) from the last scan."""
    scan = json.loads(book.scan_file.read_text(encoding="utf-8"))
    labels = json.loads(book.labels_file.read_text(encoding="utf-8"))["crossref_labels"]
    return scan, labels


# =============================================================================
# Website Data Files
# =============================================================================

def generate_theorem_manifest(book: Book):
    """Write tooltip data as one shard per chapter: theorems/<chapter-slug>.json."""
    _, labels = load_scan(book)
    shards: dict[str, dict] = {}
    for label_id, info in labels.items():
        shards.setdefault(info["shard"], {})[label_id] = {
            "type": info.get("type", "unknown"),
            "type_name": info.get("type_name", ""),
            "number": info.get("number", ""),
            "title": info.get("title", ""),
            "title_html": info.get("title_html", ""),
            "html": info.get("html_content", ""),
            "file": info.get("file", ""),
        }

    out_dir = book.html_dir / "theorems"
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("*.json"):
        if stale.stem not in shards:
            stale.unlink()
    for shard, entries in shards.items():
        _write_if_changed(out_dir / f"{shard}.json", json.dumps(dict(sorted(entries.items())), indent=2))
    print_success(f"Theorem manifest: {len(labels)} entries in {len(shards)} shards")


def generate_navigation_manifest(book: Book):
    """Write navigation.json for the sidebar."""
    pages = book.pages
    preface = next((p for p in pages if p.is_preface), None)
    navigation = {
        "title": book.title,
        "author": book.author,
        "home": {"title": preface.title, "path": preface.html_path} if preface else None,
        "chapters": [],
    }
    for chapter in book.chapters:
        chapter_pages = [p for p in pages if p.chapter is chapter]
        index = next((p for p in chapter_pages if p.section == 0), None)
        navigation["chapters"].append({
            "title": chapter.title,
            "number": chapter.number,
            "collapsed": False,
            "path": index.html_path if index else None,
            "sections": [
                {"title": p.title, "number": p.number, "path": p.html_path, "filename": p.source.name}
                for p in chapter_pages if p.section > 0
            ],
        })
    _write_if_changed(book.html_dir / "navigation.json", json.dumps(navigation, indent=2, ensure_ascii=False))
    print_success(f"Navigation manifest: {sum(len(c['sections']) for c in navigation['chapters'])} sections")


def generate_search_index(book: Book):
    """Write search.json from the text collected during the scan."""
    scan, _ = load_scan(book)
    index = []
    for page in book.pages:
        entry = scan["files"].get(page.html_path)
        if entry:
            index.append({"title": page.title, "url": page.html_path, "content": entry["text"].strip()})
    _write_if_changed(book.html_dir / "search.json", json.dumps(index, indent=2, ensure_ascii=False))
    print_success(f"Search index generated with {len(index)} entries")


def _write_if_changed(path, text: str):
    """Keep the file's timestamp when nothing changed (the dev server watches outputs)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")
