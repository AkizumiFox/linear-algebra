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

## Layout

- `src/`: the published chapters: ch00 foundations, ch01 vector spaces, ch02 linear transformations.
- `drafts/`: chapters that are not built yet, ch03 determinants and ch04 diagonalization. To publish one, see the note at the top of the file.
- `config/config.json`: this book's settings (chapters, environments and counters, deploy target). `latex/macros.tex`: the macros, used by both the PDF and the website.
- `build/`, `filters/`, `templates/`, `latex/*.sty`: the engine, shared by any book built with it (see "Another book" in `BUILD.md`).
- `widgets/`: interactive widgets available to `::: {.widget}` (see "Interactive components" in `BUILD.md`).
- `tests/`: engine tests and the small fixture book they build (`python3 -m unittest discover -s tests`).
- `site/`: a gitignored clone of the public deploy repo AkizumiFox/linear-algebra. `_build/` and `docs/` are gitignored build output.

## History

- The Markdown edition was `~/blog/my-book-project`, which was never under version control, and it grew out of `~/blog/LinearAlgebra` (GitHub: AkizumiFox/LinearAlgebra, Quarto).
- On 2026-09-14 the separate LaTeX edition (`main.tex`, `chapters/`, `book-template.sty`) was retired:
  - Every definition, theorem, proof and example in its ch00–ch01 was already in `src/`.
  - Its ch03 and ch04 fragments moved to `drafts/`.
  - It remains in the tex git history.
- The same day, these fixes went into `src/`:
  - ℚ now requires q ≠ 0.
  - The zero vector of C(D) is the zero function.
  - The sifting example no longer uses dimension before it is defined, and an ℝ² sifting example was added.
  - The proof of "Dimension Implies Equality" now cites the linear dependence lemma.
  - The ch02 overview is written out.
