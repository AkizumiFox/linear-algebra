# Build Commands

Use `./build.py <command>` (or `python -m build <command>`) from the project root.

## Everyday

| Goal | Command |
|------|---------|
| Live preview while writing | `./build.py serve` (`--port 8000`) |
| Build the website | `./build.py html` |
| Build one page | `./build.py html src/ch02-linear-transformations/03-rank-nullity.md` |
| Build per-section PDFs | `./build.py pdf` (or one file, as above) |
| Build the combined book PDF | `./build.py book` |
| Build everything | `./build.py all` |
| Remove `_build/` | `./build.py clean` |

`html` and `pdf` skip pages whose inputs are unchanged: the source file, the filters,
templates, config and macros, the page's previous/next pages, and the numbers and titles
of the labels it references. `clean` forces a full rebuild.

`serve` builds the site, serves `_build/html` on http://127.0.0.1:8000, and rebuilds when
anything in `src/`, `filters/`, `templates/html/`, the config or the macros changes. Open
pages reload by themselves. Pages built by `serve` contain the reload script; the next
`html` or `deploy` rebuilds them without it.

## Checks

| Goal | Command |
|------|---------|
| Verify required tools (pandoc, pdflatex, pdftocairo) | `./build.py doctor` |
| Validate references, links, and web vs PDF numbering | `./build.py check` |
| Run the engine tests | `python3 -m unittest discover -s tests` |

`check` fails on unresolved `@refs`, duplicate labels, cross-reference links in `_build/html`
that point nowhere, and any label whose number in the PDFs differs from the website. Run it
after `./build.py all`, since the numbering comparison reads the LaTeX `.aux` files.
`deploy` runs `all` and `check` first and stops if either fails.

## Writing

- Environments: `::: {#thm-name}` … `:::` (prefixes and counters in `environment_settings` in
  the config), small environments `::: {.proof}`. Environments nest.
- References: `@thm-name`, `@eq-name`. Numbered targets read "Theorem 1.2.3"; unnumbered
  ones (examples) read "Example (Title)".
- Equations: `\[ … \]{#eq-name}`.
- Labeled lists: `::: {.enumerate options="label=(VS\arabic*)"}` around a numbered list.
- Figures: TikZ or tikz-cd (e.g. exported from quiver) as raw LaTeX. The PDF uses it directly;
  the website gets an SVG compiled once and cached in `_build/cache/tikz/`.
- Macros: add them to `latex/macros.tex` (`\def`, `\newcommand`, `\providecommand`,
  `\DeclareMathOperator`). The website's MathJax macros are generated from this file.

## Another book

The engine (`build/`, `filters/`, `templates/`, `latex/*.sty`) can build any book directory:

```
./build.py serve --book ../my-other-book
```

A book directory contains `book.json` (or `config/config.json`), its Markdown sources and a
macro file. Paths in the config are relative to the book directory, and output goes to its
own `_build/`. To change a template or style for one book, put a file at the same relative
path in the book directory (e.g. `templates/html/styles.css`); it takes precedence over the
engine's copy. `tests/fixture-book/` is a minimal example.

Config keys: `title`, `author`, `chapters` (directory strings, or `{"dir": …, "title": …}`;
the title defaults to the chapter's `index.md` heading), `src` (default `src`), `preface`
(default `src/index.md`), `macros`, `environment_settings`, `output`, `templates`, `styles`,
`repo-url` (optional source link in the sidebar), `deploy-dir`, `deploy-repo`,
`deploy-domain`, `deploy-push-url`.

## Other

| Goal | Command |
|------|---------|
| Scan labels only | `./build.py scan` |
| Regenerate tooltip data only | `./build.py manifest` |
