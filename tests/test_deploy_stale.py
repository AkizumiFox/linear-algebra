"""The deploy step must not publish a chapter directory the book no longer uses.

This is the pair of rules that let the Chapter 2/3/4 reorder ship: stale output is
skipped, and `write_redirects` then has a free path to write the redirect. Break either
and an old URL serves a page from before the reorder instead of pointing at the new one.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build.deploy import is_stale_chapter_dir, write_redirects, REDIRECT_PAGE


LIVE = {"ch02-linear-maps", "ch03-linear-systems", "ch04-matrices-of-maps", "ch24a-notation"}


class StaleChapterDir(unittest.TestCase):
    def test_live_chapters_are_published(self):
        for name in sorted(LIVE):
            self.assertFalse(is_stale_chapter_dir(name, LIVE), name)

    def test_renamed_chapters_are_skipped(self):
        for name in ("ch03-linear-maps", "ch02-linear-systems", "ch12-psd-and-svd"):
            self.assertTrue(is_stale_chapter_dir(name, LIVE), name)

    def test_a_lettered_chapter_is_skipped_too(self):
        """The regression. `ch\\d+-` does not match `ch23a-notation`, so before the letter
        was allowed for, the old notation page was republished at its old URL and no
        redirect was written there."""
        self.assertTrue(is_stale_chapter_dir("ch23a-notation", LIVE))
        self.assertFalse(is_stale_chapter_dir("ch24a-notation", LIVE))

    def test_non_chapter_directories_are_always_published(self):
        for name in ("assets", "widgets", "results", "index.html"):
            self.assertFalse(is_stale_chapter_dir(name, LIVE), name)


class _Book:
    """The two attributes write_redirects reads."""

    def __init__(self, html_dir, redirects):
        self.html_dir = html_dir
        self.config = {"redirects": redirects}


class WriteRedirects(unittest.TestCase):
    def setUp(self):
        import tempfile

        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.html = self.root / "html"
        self.deploy = self.root / "site"
        for d in (self.html, self.deploy):
            d.mkdir()
        (self.html / "ch24a-notation").mkdir()
        (self.html / "ch24a-notation" / "index.html").write_text("new", encoding="utf-8")
        self.addCleanup(self._tmp.cleanup)

    def test_directory_key_expands_over_the_new_chapter(self):
        book = _Book(self.html, {"ch23a-notation/": "ch24a-notation/"})
        self.assertEqual(write_redirects(book, self.deploy), 1)
        stub = self.deploy / "ch23a-notation" / "index.html"
        self.assertIn("../ch24a-notation/index.html", stub.read_text(encoding="utf-8"))

    def test_a_page_already_there_suppresses_the_redirect(self):
        """Documents the interaction that made the bug invisible: publishing stale output
        at the old URL silently costs you the redirect."""
        (self.deploy / "ch23a-notation").mkdir()
        (self.deploy / "ch23a-notation" / "index.html").write_text("stale", encoding="utf-8")
        book = _Book(self.html, {"ch23a-notation/": "ch24a-notation/"})
        self.assertEqual(write_redirects(book, self.deploy), 0)
        self.assertEqual((self.deploy / "ch23a-notation" / "index.html").read_text(encoding="utf-8"), "stale")

    def test_an_explicit_file_key_beats_the_directory_key_that_follows_it(self):
        """The split chapter relies on this order: five pages of the old ch03-linear-maps
        go to ch04, the rest of the directory goes to ch02. First writer wins, so the
        specific entries must come first in config."""
        for name in ("01-linear-maps.html", "06-matrix-of-a-map.html"):
            (self.html / "ch02-linear-maps").mkdir(exist_ok=True)
            (self.html / "ch02-linear-maps" / name).write_text("x", encoding="utf-8")
        book = _Book(self.html, {
            "ch03-linear-maps/06-matrix-of-a-map.html": "ch04-matrices-of-maps/01-matrix-of-a-map.html",
            "ch03-linear-maps/": "ch02-linear-maps/",
        })
        write_redirects(book, self.deploy)
        split = (self.deploy / "ch03-linear-maps" / "06-matrix-of-a-map.html").read_text(encoding="utf-8")
        self.assertIn("ch04-matrices-of-maps/01-matrix-of-a-map.html", split)
        stayed = (self.deploy / "ch03-linear-maps" / "01-linear-maps.html").read_text(encoding="utf-8")
        self.assertIn("ch02-linear-maps/01-linear-maps.html", stayed)


if __name__ == "__main__":
    unittest.main()
