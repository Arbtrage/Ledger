"""Ledger home directory layout (~/.ledger/)."""

from __future__ import annotations

from pathlib import Path

LEDGER_HOME_ENV = "LEDGER_HOME"
DEFAULT_HOME = Path.home() / ".ledger"


def ledger_home() -> Path:
    """Return the Ledger config directory (default: ~/.ledger)."""
    import os

    override = os.environ.get(LEDGER_HOME_ENV)
    if override:
        return Path(override).expanduser()
    return DEFAULT_HOME


def profiles_dir() -> Path:
    return ledger_home() / "profiles"


def storage_dir() -> Path:
    return ledger_home() / "storage"


def logs_dir() -> Path:
    return ledger_home() / "logs"


def history_db_path() -> Path:
    return ledger_home() / "history.db"


def profile_path(name: str) -> Path:
    return profiles_dir() / f"{name}.yaml"


def ensure_ledger_home() -> Path:
    """Create ~/.ledger layout if missing. Returns home path."""
    home = ledger_home()
    for sub in (profiles_dir(), storage_dir(), logs_dir()):
        sub.mkdir(parents=True, exist_ok=True)
    return home
