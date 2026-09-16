"""
Build System Check Module
=========================
Validates the book: tool availability (doctor), cross-references, duplicate labels,
and that the PDF numbering matches the web numbering.
"""

import json
import re
import shutil
import subprocess
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

from .book import Book
from .manifest import scan_labels, load_scan
from .utils import print_step, print_success, print_warning, print_error, print_info

MIN_PANDOC = (3, 1)

# (command, version flag, needed for)
TOOLS = [
    ("pandoc", "--version", "all builds"),
    ("pdflatex", "--version", "PDF builds and TikZ figures"),
    ("pdftocairo", "-v", "TikZ figures on the web"),
]


# =============================================================================
# Doctor
# =============================================================================

def doctor() -> bool:
    """Check that the external tools the build needs are installed."""
    print_step("Checking tools...")
    ok = True
    for tool, flag, purpose in TOOLS:
        path = shutil.which(tool)
        if not path:
            print_error(f"{tool}: not found (needed for {purpose})")
            ok = False
            continue
        result = subprocess.run([tool, flag], capture_output=True, text=True)
        first_line = (result.stdout or result.stderr).strip().splitlines()[0:1]
        version = first_line[0] if first_line else "unknown version"
        if tool == "pandoc":
            match = re.search(r"(\d+)\.(\d+)", version)
            if not match or tuple(map(int, match.groups())) < MIN_PANDOC:
                print_error(f"pandoc: {version} (need {'.'.join(map(str, MIN_PANDOC))} or newer)")
                ok = False
                continue
        print_success(f"{tool}: {version}")
    return ok


# =============================================================================
# Check
# =============================================================================

def read_aux_labels(aux_file: Path) -> dict[str, str]:
    """Map label -> printed number from a LaTeX .aux file."""
    text = aux_file.read_text(encoding="latin-1")
    return {m.group(1): m.group(2) for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", text)}


def _compare_numbers(book: Book, labels: dict, aux_file: Path, only: set[str] | None = None) -> list[str]:
    problems = []
    aux = read_aux_labels(aux_file)
    for label_id, info in sorted(labels.items()):
        if only is not None and label_id not in only:
            continue
        web = info.get("number", "")
        if not web:
            continue  # unnumbered environments are referenced by name, not number
        pdf = aux.get(label_id)
        if pdf is None:
            problems.append(f"{label_id}: missing from {aux_file.relative_to(book.root)}")
        elif pdf != web:
            problems.append(f"{label_id}: web {web}, PDF {pdf} ({aux_file.relative_to(book.root)})")
    return problems


class _LinkCollector(HTMLParser):
    """Collects element ids and the hrefs of a.xref links in one page."""

    def __init__(self):
        super().__init__()
        self.ids: set[str] = set()
        self.xrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "xref" in (attrs.get("class") or "").split() and attrs.get("href"):
            self.xrefs.append(attrs["href"])


def check_xref_links(html_dir: Path) -> list[str]:
    """Verify every a.xref link in the built HTML resolves to a page containing the anchor."""
    pages: dict[Path, _LinkCollector] = {}
    for page in sorted(html_dir.rglob("*.html")):
        collector = _LinkCollector()
        collector.feed(page.read_text(encoding="utf-8"))
        pages[page.resolve()] = collector

    problems = []
    for page, collector in pages.items():
        where = page.relative_to(html_dir.resolve())
        for href in collector.xrefs:
            path, _, anchor = href.partition("#")
            target = (page.parent / path).resolve() if path else page
            if target not in pages:
                problems.append(f"broken link {href} in {where}: page not found")
            elif anchor and anchor not in pages[target].ids:
                problems.append(f"broken link {href} in {where}: no #{anchor}")
    return problems


def _newest_source_mtime(book: Book) -> float:
    return max((p.source.stat().st_mtime for p in book.pages), default=0)


def check(book: Book, quiet: bool = False) -> bool:
    """Validate labels and references; compare PDF numbering if PDFs have been built."""
    scan_labels(book)
    scan, labels = load_scan(book)

    errors = []
    warnings = []

    # Chapters listed in the config must exist
    for chapter_dir in book.missing_chapter_dirs():
        errors.append(f"chapter directory not found: {chapter_dir}")

    # Duplicate labels
    defined_in = defaultdict(list)
    for entry in scan["files"].values():
        for label_id in entry["labels"]:
            defined_in[label_id].append(entry["source"])
    for label_id, sources in sorted(defined_in.items()):
        if len(sources) > 1:
            errors.append(f"duplicate label {label_id}: {', '.join(sources)}")

    # Unresolved references (only ids shaped like labels, e.g. thm-foo)
    for entry in sorted(scan["files"].values(), key=lambda e: e["source"]):
        for ref in sorted(set(entry["refs"])):
            if ref not in labels and re.match(r"^[A-Za-z]+-", ref):
                errors.append(f"unresolved reference @{ref} in {entry['source']}")

    # Cross-reference links in the built site must point at an existing page and anchor
    if book.html_dir.exists():
        errors.extend(check_xref_links(book.html_dir))

    # Web vs PDF numbering
    book_aux = book.build_dir / "tmp" / "latex-book" / "book.aux"
    newest_source = _newest_source_mtime(book)
    if book_aux.exists():
        if book_aux.stat().st_mtime < newest_source:
            warnings.append("book PDF is older than the sources; run `./build.py book` for an accurate numbering check")
        errors.extend(_compare_numbers(book, labels, book_aux))
    elif not quiet:
        print_info("No book build found; skipping book numbering check (run `./build.py book`)")

    section_aux_dir = book.build_dir / "tmp" / "pdf-single"
    for aux_file in sorted(section_aux_dir.rglob("*.aux")) if section_aux_dir.exists() else []:
        entry = scan["files"].get(f"{aux_file.parent.name}/{aux_file.stem}.html")
        if entry:
            errors.extend(_compare_numbers(book, labels, aux_file, only=set(entry["labels"])))

    for warning in warnings:
        print_warning(warning)
    if errors:
        for error in errors:
            print_error(error)
        print_error(f"Check failed: {len(errors)} problem(s)")
        return False
    print_success(f"Check passed: {len(labels)} labels, "
                  f"{sum(len(e['refs']) for e in scan['files'].values())} references")
    return True
