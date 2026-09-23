# Linear Algebra: A Proof-Based Development

One source, Pandoc Markdown in `src/`, built by `build.py` into both the website and the PDFs.

| Task | Command |
|---|---|
| Write with live preview | `./build.py serve` → http://127.0.0.1:8000 (rebuilds and reloads on save) |
| Build the HTML site | `./build.py html` |
| Build the book PDF | `./build.py book` (writes `_build/pdf/book.pdf`) |
| Everything | `./build.py all` (see `BUILD.md`) |
| Validate references and numbering | `./build.py check` |
| Publish | `./build.py deploy --push` → linear-algebra.akizumifox.com (see `DEPLOY.md`) |

## Reading the site

A toolbar at the top of each page folds the book contents (left) and "On this page" (right)
away, which widens the text, and switches between light and dark themes (following the
system setting until chosen). These choices are remembered in the browser. On phones the
same toolbar opens the contents as a drawer. Press `/` to search, ← and → to turn pages.
Solutions start folded; the start page offers "Continue reading". The sidebar links to a
list of all results and a dependency graph.

## Layout

- `src/`: the book, 24 chapters in six parts, plus the preface and the notation page.
- `config/config.json`: this book's settings (chapters, environments and counters, deploy target). `latex/macros.tex`: the macros, used by both the PDF and the website.
- `build/`, `filters/`, `templates/`, `latex/*.sty`: the engine, shared by any book built with it (see "Another book" in `BUILD.md`).
- `spelling.txt`: words the spell check accepts. `.github/workflows/`: build and deploy on push (see `BUILD.md`).
- `widgets/`: interactive widgets available to `::: {.widget}` (see "Interactive components" in `BUILD.md`).
- `tests/`: engine tests and the small fixture book they build (`python3 -m unittest discover -s tests`).
- `site/`: a gitignored clone of the public deploy repo AkizumiFox/linear-algebra. `_build/` and `docs/` are gitignored build output.

## History

- The Markdown edition was `~/blog/my-book-project`, which was never under version control, and it grew out of `~/blog/LinearAlgebra` (GitHub: AkizumiFox/LinearAlgebra, Quarto).
- On 2026-09-14 the separate LaTeX edition (`main.tex`, `chapters/`, `book-template.sty`) was retired:
  - Every definition, theorem, proof and example in its ch00–ch01 was already in `src/`.
  - Its ch03 and ch04 fragments moved to `drafts/`, and were deleted on 2026-09-23 once
    Chapters 6, 8 and 11 had superseded them, as the blueprints for those chapters directed.
  - It remains in the tex git history.
- The same day, these fixes went into `src/`:
  - ℚ now requires q ≠ 0.
  - The zero vector of C(D) is the zero function.
  - The sifting example no longer uses dimension before it is defined, and an ℝ² sifting example was added.
  - The proof of "Dimension Implies Equality" now cites the linear dependence lemma.
  - The ch02 overview is written out.
