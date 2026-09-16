# Build Commands

Use `./build.py` or `python -m build` from the project root.

## HTML

| Goal | Command |
|------|---------|
| Build all HTML | `./build.py html` |
| Build single HTML | `./build.py html src/ch02-linear-transformations/03-rank-nullity.md` |

## PDF

| Goal | Command |
|------|---------|
| Build all PDFs | `./build.py pdf` |
| Build single PDF | `./build.py pdf src/ch02-linear-transformations/03-rank-nullity.md` |

## Book

| Goal | Command |
|------|---------|
| Build combined book PDF | `./build.py book` |

## Full build

| Goal | Command |
|------|---------|
| Build everything (HTML + PDFs + book) | `./build.py all` |

## Clean

| Goal | Command |
|------|---------|
| Remove `_build` directory | `./build.py clean` |

## Other

| Goal | Command |
|------|---------|
| Scan labels only | `./build.py scan` |
| Generate theorems manifest only | `./build.py manifest` |
