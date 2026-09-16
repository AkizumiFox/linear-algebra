"""
Build System Package
====================
Modular build system for compiling Markdown to HTML and PDF using Pandoc.
"""

from .config import (
    PROJECT_ROOT,
    CONFIG_FILE,
    BUILD_DIR,
    COUNTER_STATE_FILE,
    THEOREM_MANIFEST_FILE,
    CROSSREF_LABELS_FILE,
    load_config,
    load_counter_state,
    save_counter_state,
    reset_counter_state,
)

from .discovery import (
    discover_markdown_files,
    get_relative_output_path,
)

from .pandoc import (
    build_pandoc_command,
    run_pandoc,
)

from .html import (
    build_html,
    copy_html_assets,
)

from .pdf import (
    build_pdf,
    build_book,
)

from .manifest import (
    scan_labels,
    generate_theorem_manifest,
    generate_navigation_manifest,
)

from .cli import (
    main,
    extract_title_from_markdown,
    get_chapter_display_name,
    clean,
)

__all__ = [
    # Config
    "PROJECT_ROOT",
    "CONFIG_FILE",
    "BUILD_DIR",
    "COUNTER_STATE_FILE",
    "THEOREM_MANIFEST_FILE",
    "CROSSREF_LABELS_FILE",
    "load_config",
    "load_counter_state",
    "save_counter_state",
    "reset_counter_state",
    # Discovery
    "discover_markdown_files",
    "get_relative_output_path",
    # Pandoc
    "build_pandoc_command",
    "run_pandoc",
    # HTML
    "build_html",
    "copy_html_assets",
    # PDF
    "build_pdf",
    "build_book",
    # Manifest
    "scan_labels",
    "generate_theorem_manifest",
    "generate_navigation_manifest",
    # CLI
    "main",
    "extract_title_from_markdown",
    "get_chapter_display_name",
    "clean",
]
