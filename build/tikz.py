"""
Build System TikZ Module
========================
Compiles the TikZ pictures collected by filters/tikz.lua into SVG for the website.
Each picture is compiled once as a standalone document and cached by content hash.
"""

import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .config import PROJECT_ROOT, BUILD_DIR
from .utils import print_step, print_success, print_error, print_warning

TIKZ_CACHE_DIR = BUILD_DIR / "cache" / "tikz"

STANDALONE_TEMPLATE = r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb,amsthm,mathtools,bbm}
\usepackage{tikz-cd}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,shapes.geometric,calc,positioning,patterns}
\input{%(macros)s}
\begin{document}
%(picture)s
\end{document}
"""


def _compile_one(tex_source: Path, macros_file: Path) -> tuple[Path, str | None]:
    """Compile one picture to SVG next to its source. Returns (source, error or None)."""
    svg = tex_source.with_suffix(".svg")
    with tempfile.TemporaryDirectory(prefix="tikz-") as tmp:
        tmp_dir = Path(tmp)
        doc = tmp_dir / "picture.tex"
        doc.write_text(STANDALONE_TEMPLATE % {
            "macros": macros_file.as_posix(),
            "picture": tex_source.read_text(encoding="utf-8"),
        }, encoding="utf-8")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", doc.name],
            cwd=tmp_dir, capture_output=True, text=True, errors="replace",
        )
        pdf = tmp_dir / "picture.pdf"
        if result.returncode != 0 or not pdf.exists():
            errors = [line for line in result.stdout.splitlines() if line.startswith("!")]
            return tex_source, "; ".join(errors[:3]) or "pdflatex failed"
        result = subprocess.run(["pdftocairo", "-svg", str(pdf), str(svg)], capture_output=True, text=True)
        if result.returncode != 0:
            return tex_source, result.stderr.strip() or "pdftocairo failed"
    return tex_source, None


def build_tikz_figures(config: dict, output_dir: Path):
    """Compile pending TikZ sources and copy every SVG into the HTML output."""
    if not TIKZ_CACHE_DIR.exists():
        return
    sources = sorted(TIKZ_CACHE_DIR.glob("*.tex"))
    if not sources:
        return

    macros_file = PROJECT_ROOT / config["macros"]
    macros_mtime = macros_file.stat().st_mtime if macros_file.exists() else 0
    pending = [
        src for src in sources
        if not src.with_suffix(".svg").exists() or src.with_suffix(".svg").stat().st_mtime < macros_mtime
    ]

    if pending:
        if not shutil.which("pdflatex") or not shutil.which("pdftocairo"):
            print_warning("pdflatex or pdftocairo not found; TikZ figures will be missing from the website")
        else:
            print_step(f"Compiling {len(pending)} TikZ figure(s)...")
            with ThreadPoolExecutor(max_workers=min(4, len(pending))) as executor:
                for src, error in executor.map(lambda s: _compile_one(s, macros_file), pending):
                    if error:
                        print_error(f"TikZ figure {src.stem[:12]} failed: {error}")

    dest = output_dir / "tikz"
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for svg in TIKZ_CACHE_DIR.glob("*.svg"):
        shutil.copy2(svg, dest / svg.name)
        count += 1
    print_success(f"TikZ figures: {count}")
