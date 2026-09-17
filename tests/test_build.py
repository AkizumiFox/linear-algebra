"""
End-to-end tests: build tests/fixture-book with the engine and inspect the output.

Run from the project root:  python3 -m unittest discover -s tests
The book builds need pandoc, pdflatex and pdftocairo (see ./build.py doctor).
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ENGINE_ROOT = Path(__file__).resolve().parent.parent
FIXTURE = Path(__file__).resolve().parent / "fixture-book"
sys.path.insert(0, str(ENGINE_ROOT))

from build.book import Book  # noqa: E402
from build.check import check_xref_links  # noqa: E402


def run_build(book_dir: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ENGINE_ROOT / "build.py"), *args, "--book", str(book_dir)],
        capture_output=True, text=True,
    )


class FixtureBookCase(unittest.TestCase):
    """Copies the fixture book to a temporary directory and builds it once per class."""

    build_commands = [("html",)]

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="book-test-")
        cls.book_dir = Path(cls.tmp.name) / "book"
        shutil.copytree(FIXTURE, cls.book_dir)
        cls.prepare(cls.book_dir)
        cls.results = {}
        for command in cls.build_commands:
            result = run_build(cls.book_dir, *command)
            cls.results[command] = result
            if result.returncode != 0:
                raise AssertionError(f"build {command} failed:\n{result.stdout}\n{result.stderr}")
        cls.book = Book(cls.book_dir)
        cls.html = cls.book.html_dir

    @classmethod
    def prepare(cls, book_dir: Path):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def page(self, path: str) -> str:
        return (self.html / path).read_text(encoding="utf-8")

    def labels(self) -> dict:
        return json.loads(self.book.labels_file.read_text())["crossref_labels"]


BROKEN_COMPONENTS = """# Broken Components

::: {.plot fn="sin(2x)"}
:::

::: {.widget src="widgets/missing.js"}
No print block.
:::
"""


class TestHtmlBuild(FixtureBookCase):

    @classmethod
    def prepare(cls, book_dir: Path):
        (book_dir / "src" / "ch02-more" / "03-broken.md").write_text(BROKEN_COMPONENTS)

    def test_numbering_shared_and_independent_counters(self):
        numbers = {k: v["number"] for k, v in self.labels().items()}
        self.assertEqual(numbers["def-thing"], "1.1.1")     # own counter
        self.assertEqual(numbers["thm-main"], "1.1.1")      # "main" counter
        self.assertEqual(numbers["lem-helper"], "1.1.2")    # shares "main" with theorems
        self.assertEqual(numbers["eq-sum"], "1.1.1")
        self.assertEqual(numbers["thm-second"], "1.2.1")    # counters restart per section
        self.assertEqual(numbers["exm-titled"], "")         # unnumbered

    def test_cross_chapter_reference(self):
        page = self.page("ch02-more/01-refs.html")
        self.assertRegex(page, r'href="\.\./ch01-basics/01-first\.html#thm-main"')
        self.assertIn('data-shard="ch01-basics"', page)
        self.assertIn("Theorem 1.1.1", page)

    def test_unnumbered_reference_uses_title(self):
        self.assertIn("Example (Titled Example)", self.page("ch02-more/01-refs.html"))

    def test_all_reference_links_resolve(self):
        self.assertEqual(check_xref_links(self.html), [])

    def test_nested_environments(self):
        page = self.page("ch01-basics/01-first.html")
        proof = page.index('class="proof small-env"')
        claim = page.index('class="claim small-env"')
        self.assertLess(proof, claim)

    def test_tikz_figure(self):
        page = self.page("ch01-basics/01-first.html")
        match = re.search(r'src="\.\./tikz/([0-9a-f]{40})\.svg"', page)
        self.assertIsNotNone(match, "no TikZ image in page")
        self.assertTrue((self.html / "tikz" / f"{match.group(1)}.svg").exists())

    def test_labeled_list(self):
        page = self.page("ch01-basics/01-first.html")
        self.assertIn(">(A1)</span>", page)
        self.assertIn(">(A2)</span>", page)

    def test_chapter_titles_and_navigation(self):
        navigation = json.loads((self.html / "navigation.json").read_text())
        self.assertEqual([c["title"] for c in navigation["chapters"]], ["Basics", "More Topics"])
        self.assertEqual(navigation["home"], {"title": "Preface", "path": "index.html"})
        self.assertEqual(navigation["chapters"][0]["sections"][1]["number"], "1.2")
        self.assertNotIn("{.unnumbered}", self.page("ch02-more/index.html"))

    def test_tooltip_shards(self):
        shard = json.loads((self.html / "theorems" / "ch01-basics.json").read_text())
        self.assertIn("thm-main", shard)
        self.assertEqual(shard["thm-main"]["title"], "Main Theorem")
        self.assertIn("exm-titled", json.loads((self.html / "theorems" / "ch02-more.json").read_text()))

    def test_macros_generated_from_book(self):
        macros = (self.html / "mathjax-macros.js").read_text()
        self.assertIn('"nR": "\\\\mathbb{R}"', macros)
        self.assertIn('"norm": [', macros)
        self.assertIn('"rank": "\\\\operatorname{rank}"', macros)

    def test_search_index(self):
        index = json.loads((self.html / "search.json").read_text())
        entry = next(e for e in index if e["url"] == "ch01-basics/02-second.html")
        self.assertEqual(entry["title"], "1.2 Second Section")
        self.assertIn("builds on", entry["content"])

    def test_search_index_has_results(self):
        index = json.loads((self.html / "search.json").read_text())
        result = next(e for e in index if e["url"] == "ch01-basics/01-first.html#thm-main")
        self.assertEqual(result["kind"], "result")
        self.assertEqual(result["title"], "Theorem 1.1.1 (Main Theorem)")
        self.assertEqual(result["page"], "1.1 First Section")
        page = next(e for e in index if e["url"] == "ch01-basics/02-second.html")
        self.assertEqual(page["title"], "1.2 Second Section")

    def test_page_metadata_and_site_files(self):
        page = self.page("ch01-basics/index.html")
        self.assertIn('<meta name="description" content="The first chapter.">', page)
        self.assertIn('rel="icon" href="../favicon.svg"', page)
        self.assertNotIn('rel="canonical"', page)            # no deploy-domain in the fixture
        self.assertTrue((self.html / "favicon.svg").exists())
        self.assertIn("Page not found", (self.html / "404.html").read_text())
        self.assertFalse((self.html / "sitemap.xml").exists())

    def test_tikz_svg_scaled_for_the_web(self):
        svg = next((self.html / "tikz").glob("*.svg")).read_text()
        width = float(re.search(r'<svg[^>]*\bwidth="([\d.]+)"', svg).group(1))
        view_width = float(re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+)', svg).group(1))
        self.assertAlmostEqual(width / view_width, 1.5, places=2)

    def test_unchanged_rebuild_skips_pages(self):
        result = run_build(self.book_dir, "html")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("0/0 built", result.stdout)

    def test_check_reports_broken_reference(self):
        result = run_build(self.book_dir, "check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("unresolved reference @thm-missing in src/ch02-more/01-refs.md", result.stdout)

    def test_check_reports_broken_components(self):
        result = run_build(self.book_dir, "check")
        self.assertIn('plot fn="sin(2x)" in src/ch02-more/03-broken.md: missing \'*\' before \'x\'', result.stdout)
        self.assertIn("widget file not found: widgets/missing.js", result.stdout)
        self.assertIn("has no ::: {.print} content", result.stdout)

    # -- Interactive components ------------------------------------------------

    def test_code_cells(self):
        page = self.page("ch02-more/02-interactive.html")
        self.assertRegex(page, r'<div id="cell-matrix" class="code-cell"\s+data-lang="python"')
        self.assertEqual(page.count('class="code-cell-run"'), 2)
        self.assertIn('class="sourceCode python"', page)          # the plain listing is not a cell
        self.assertIn("<style>", page)                             # highlighting CSS is included

    def test_components_script_only_where_used(self):
        self.assertIn("components.js?v=", self.page("ch02-more/02-interactive.html"))
        self.assertNotIn("components.js", self.page("ch02-more/01-refs.html"))
        for name in ("cell.js", "pyodide-worker.js", "plot.js", "expression.js", "widget.js", "jsxgraph.js"):
            self.assertTrue((self.html / "components" / name).exists(), name)
        self.assertTrue((self.html / "widgets" / "linear-map.js").exists())

    def test_plot_and_widget_html(self):
        page = self.page("ch02-more/02-interactive.html")
        self.assertIn('data-fn="sin(a*x); a*cos(x)/2"', page)
        self.assertIn('data-params="a=1:0..3"', page)
        self.assertIn('class="plot-caption"', page)
        self.assertIn('data-src="../widgets/linear-map.js"', page)
        self.assertIn('class="widget-fallback"', page)


class TestFullBuild(FixtureBookCase):
    """Without the broken reference, the whole book builds and check passes, which
    includes comparing every label number in the PDFs with the website."""

    build_commands = [("all",)]

    @classmethod
    def prepare(cls, book_dir: Path):
        refs = book_dir / "src" / "ch02-more" / "01-refs.md"
        refs.write_text(refs.read_text().replace("A broken reference: @thm-missing.\n", ""))

    def test_check_passes(self):
        result = run_build(self.book_dir, "check")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("Check passed", result.stdout)

    def test_pdfs_exist(self):
        self.assertTrue(self.book.book_pdf.exists())
        self.assertTrue((self.book.pdf_dir / "ch01-basics" / "01-first.pdf").exists())
        self.assertTrue((self.html / "book" / "book.pdf").exists())

    def test_pdf_components(self):
        tex = (self.book.build_dir / "tmp" / "pdf-single" / "ch02-more" / "02-interactive.tex").read_text()
        self.assertEqual(tex.count(r"\begin{lstlisting}[language=Python]"), 2)
        self.assertIn(r"\addplot[thick, blue] {sin(((1)*x))};", tex)       # parameter at its default
        self.assertIn(r"\addplot[thick, blue] {((x^3)-(3*x))};", tex)
        self.assertIn("parallelogram spanned by the columns", tex)          # widget print content
        self.assertNotIn("widget-mount", tex)

    def test_pdf_reference_text(self):
        tex = (self.book.build_dir / "tmp" / "latex-book" / "book.tex").read_text()
        self.assertIn(r"\hyperref[thm-main]{Theorem~\ref*{thm-main}}", tex)
        self.assertIn(r"\begin{enumerate}[label=(A\arabic*)]", tex)


if __name__ == "__main__":
    unittest.main()
