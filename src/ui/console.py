"""Shared Rich console instance."""

from __future__ import annotations

from rich.console import Console

_console: Console | None = None


def get_console() -> Console:
    """Return a module-level Rich console (stderr, color-aware)."""
    global _console
    if _console is None:
        _console = Console(stderr=True, highlight=False)
    return _console
