"""
Build System Configuration Module
=================================
Handles configuration loading and path constants.
"""

import json
from pathlib import Path

# =============================================================================
# Path Constants
# =============================================================================

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
CONFIG_FILE = PROJECT_ROOT / "config" / "config.json"
BUILD_DIR = PROJECT_ROOT / "_build"
COUNTER_STATE_FILE = BUILD_DIR / ".counter_state.json"
THEOREM_MANIFEST_FILE = BUILD_DIR / "theorems.json"
CROSSREF_LABELS_FILE = BUILD_DIR / "crossref_labels.json"


# =============================================================================
# Configuration Loading
# =============================================================================

def load_config() -> dict:
    """Load configuration from config.json."""
    with open(CONFIG_FILE) as f:
        return json.load(f)


# =============================================================================
# Counter State Management
# =============================================================================

def load_counter_state() -> dict:
    """Load counter state from disk, or return empty state."""
    if COUNTER_STATE_FILE.exists():
        with open(COUNTER_STATE_FILE) as f:
            return json.load(f)
    return {
        "shared": {},
        "independent": {},
        "labels": {}
    }


def save_counter_state(state: dict):
    """Save counter state to disk."""
    COUNTER_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(COUNTER_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def reset_counter_state():
    """Reset counter state for fresh build."""
    if COUNTER_STATE_FILE.exists():
        COUNTER_STATE_FILE.unlink()
    if CROSSREF_LABELS_FILE.exists():
        CROSSREF_LABELS_FILE.unlink()
