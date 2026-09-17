"""
Build System Extra Pages
========================
Pages generated from the label registry rather than written by the author:

- results.html: every definition, theorem, example, ... grouped by chapter and section,
  with filters and hover previews.
- graph.html: the dependency graph of results (templates/html/graph.js), from
  @references and from theorem titles mentioned in statements and proofs.

They use the book's HTML template, so they have the same sidebar, toolbar and theme.
"""

import json
import re
from html import escape
from pathlib import Path

from .book import Book, Page
from .manifest import load_scan, STATEMENT_TYPES
from .pandoc import build_pandoc_command, page_metadata, run_pandoc
from .utils import print_success, print_error

RESULTS_PAGE = "results.html"
GRAPH_PAGE = "graph.html"

# Filter groups on the results page: (group, label, environment types)
RESULT_GROUPS = [
    ("statements", "Theorems and lemmas", STATEMENT_TYPES | {"conjecture"}),
    ("definitions", "Definitions", {"definition"}),
    ("examples", "Examples", {"example"}),
    ("exercises", "Exercises", {"exercise"}),
]


BLACKBOARD = {"R": "ℝ", "Q": "ℚ", "C": "ℂ", "Z": "ℤ", "N": "ℕ", "F": "𝔽"}
SYMBOLS = {"sqrt": "√", "cdot": "·", "times": "×", "to": "→", "leq": "≤", "geq": "≥", "neq": "≠",
           "in": "∈", "subseteq": "⊆", "oplus": "⊕", "cap": "∩", "cup": "∪", "infty": "∞"}


def plain_title(title: str) -> str:
    """A title for places that cannot typeset math (graph labels): TeX to readable text."""
    title = re.sub(r"\\n([A-Z])\b", lambda m: BLACKBOARD.get(m.group(1), m.group(1)), title)
    title = re.sub(r"\\[()\[\]]", "", title)
    title = re.sub(r"\\([A-Za-z]+)", lambda m: SYMBOLS.get(m.group(1), m.group(1)), title)
    title = title.replace("{", "").replace("}", "")
    return " ".join(title.split())


def _group_of(env_type: str) -> str:
    return next((group for group, _, types in RESULT_GROUPS if env_type in types), "other")


def _env_colors(book: Book) -> dict[str, str]:
    colors = {}
    for env in book.environment_settings.get("big_envs", []):
        key = env["name"].lower().replace(" ", "-")
        if env.get("color"):
            colors[key] = env["color"]
    return colors


def _results_by_page(book: Book, labels: dict) -> dict[str, list[tuple[str, dict]]]:
    """Labeled environments (not equations) per page, in reading order."""
    scan, _ = load_scan(book)
    grouped = {}
    for page in book.pages:
        entry = scan["files"].get(page.html_path)
        if not entry:
            continue
        # scan.json lists labels sorted by id; order them as they appear in the page text
        items = [(label, labels[label]) for label in entry["labels"]
                 if label in labels and labels[label].get("type") != "equation"]
        text = page.source.read_text(encoding="utf-8")
        items.sort(key=lambda item: text.find("#" + item[0]))
        if items:
            grouped[page.html_path] = items
    return grouped


def _results_body(book: Book, labels: dict) -> str:
    grouped = _results_by_page(book, labels)
    counts = {group: 0 for group, _, _ in RESULT_GROUPS}
    for items in grouped.values():
        for _, info in items:
            group = _group_of(info.get("type", ""))
            if group in counts:
                counts[group] += 1

    parts = ['<div class="results-filters" role="group" aria-label="Filter results">']
    for group, label, _ in RESULT_GROUPS:
        if counts[group]:
            parts.append(
                f'<label class="results-filter"><input type="checkbox" value="{group}" checked> '
                f'{escape(label)} <span class="results-count">{counts[group]}</span></label>')
    parts.append('<input type="search" class="results-search" placeholder="Filter by name or number" '
                 'aria-label="Filter results by name or number">')
    parts.append('</div>')

    for chapter in book.chapters:
        chapter_pages = [p for p in book.pages if p.chapter is chapter and p.html_path in grouped]
        if not chapter_pages:
            continue
        parts.append(f'<section class="results-chapter">')
        parts.append(f'<h2 id="chapter-{escape(chapter.slug)}">{escape(chapter.title)}</h2>')
        for page in chapter_pages:
            heading = f"{page.number} {page.title}" if page.number else page.title
            parts.append(f'<div class="results-section">')
            parts.append(f'<h3><a href="{escape(page.html_path)}">{escape(heading)}</a></h3>')
            parts.append('<ul class="results-list">')
            for label, info in grouped[page.html_path]:
                name = " ".join(filter(None, [info.get("type_name"), info.get("number")]))
                title = info.get("title_html") or ""
                search_text = f"{name} {info.get('title', '')}".lower()
                parts.append(
                    f'<li class="result" data-group="{_group_of(info.get("type", ""))}" '
                    f'data-search="{escape(search_text)}" style="--env-color: {_env_colors(book).get(info.get("type"), "var(--muted)")}">'
                    f'<a class="xref result-name" href="{escape(info["file"])}#{escape(label)}" '
                    f'data-ref="{escape(label)}" data-shard="{escape(info.get("shard", ""))}">{escape(name)}</a>'
                    + (f' <span class="result-title">{title}</span>' if title else "")
                    + '</li>')
            parts.append('</ul></div>')
        parts.append('</section>')
    parts.append('<p class="results-empty" hidden>No results match the filter.</p>')
    return "\n".join(parts)


def _graph_data(book: Book, labels: dict) -> dict:
    colors = _env_colors(book)
    chapters = {p.html_path: (p.chapter.title if p.chapter else "") for p in book.pages}
    numbers = {p.html_path: p.chapter.number if p.chapter else -1 for p in book.pages}
    nodes, edges = [], []
    for label, info in labels.items():
        if info.get("type") == "equation" or info.get("file") not in chapters:
            continue
        nodes.append({
            "id": label,
            "type": info.get("type"),
            "group": _group_of(info.get("type", "")),
            "name": " ".join(filter(None, [info.get("type_name"), info.get("number")])),
            "title": plain_title(info.get("title", "")),
            "url": f"{info['file']}#{label}",
            "shard": info.get("shard", ""),
            "chapter": chapters[info["file"]],
            "chapterNumber": numbers[info["file"]],
            "color": colors.get(info.get("type"), "#6b6f7a"),
        })
        for used in info.get("uses", []):
            if used in labels and labels[used].get("type") != "equation":
                edges.append({"source": used, "target": label, "kind": "reference"})
        for used in info.get("mentions", []):
            edges.append({"source": used, "target": label, "kind": "mention"})
    return {"nodes": nodes, "edges": edges}


GRAPH_BODY = """<p class="graph-intro">
An arrow from one result to another means the second uses the first: a solid arrow for a
reference in its statement or proof, a dashed arrow where the proof names the result
without a reference. Hover over a result to see what it builds on and what builds on it;
click to open it.
</p>
<div class="graph-controls">
  <label>Chapter <select class="graph-chapter"><option value="">All chapters</option></select></label>
  <label class="graph-toggle"><input type="checkbox" class="graph-isolated"> Show results without connections</label>
</div>
<div class="graph-frame">
  <div id="dependency-graph" class="dependency-graph" data-graph="graph.json" role="img"
       aria-label="Dependency graph of the book's results"></div>
  <aside class="graph-preview" hidden></aside>
</div>
<noscript><p>The graph needs JavaScript. The <a href="results.html">list of results</a> works without it.</p></noscript>
"""


def _render_page(book: Book, html_path: str, title: str, body_html: str, extra: dict) -> bool:
    source = book.build_dir / "tmp" / "generated" / Path(html_path).with_suffix(".md")
    source.parent.mkdir(parents=True, exist_ok=True)
    # A raw HTML block, so Pandoc passes the markup through unchanged
    # (the title gets its own id, which would otherwise collide with ids in the body)
    source.write_text(f"# {title} {{#page-title}}\n\n```{{=html}}\n{body_html}\n```\n", encoding="utf-8")
    page = Page(source=source, chapter=None, section=0, title=title, html_path=html_path)
    metadata = page_metadata(book, page, "html", extra)
    metadata["breadcrumb-chapter-title"] = book.title
    output = book.html_dir / html_path
    return run_pandoc(build_pandoc_command(book, page, output, "html", metadata))


def generate_extra_pages(book: Book, extra: dict) -> bool:
    """Write results.html, graph.html and graph.json. `extra` is shared page metadata."""
    _, labels = load_scan(book)
    ok = _render_page(book, RESULTS_PAGE, "List of results", _results_body(book, labels), extra)
    (book.html_dir / "graph.json").write_text(json.dumps(_graph_data(book, labels), indent=1), encoding="utf-8")
    ok = _render_page(book, GRAPH_PAGE, "Dependency graph", GRAPH_BODY,
                      dict(extra, **{"page-scripts": ["graph.js"], "wide-page": True})) and ok
    if ok:
        print_success("Generated pages: list of results, dependency graph")
    else:
        print_error("Could not generate the list of results or the dependency graph")
    return ok
