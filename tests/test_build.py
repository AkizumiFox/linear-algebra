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


class TestHtmlBuild(FixtureBookCase):

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
        self.assertEqual(entry["title"], "Second Section")
        self.assertIn("builds on", entry["content"])

    def test_unchanged_rebuild_skips_pages(self):
        result = run_build(self.book_dir, "html")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("0/0 built", result.stdout)

    def test_check_reports_broken_reference(self):
        result = run_build(self.book_dir, "check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("unresolved reference @thm-missing in src/ch02-more/01-refs.md", result.stdout)


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

    def test_pdf_reference_text(self):
        tex = (self.book.build_dir / "tmp" / "latex-book" / "book.tex").read_text()
        self.assertIn(r"\hyperref[thm-main]{Theorem~\ref*{thm-main}}", tex)
        self.assertIn(r"\begin{enumerate}[label=(A\arabic*)]", tex)


if __name__ == "__main__":
    unittest.main()
