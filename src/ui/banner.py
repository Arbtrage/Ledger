"""Branded header panels for Ledger CLI."""

from __future__ import annotations

from rich.panel import Panel
from rich.text import Text

from ui.console import get_console


def print_banner(*, subtitle: str = "Database Backup Orchestration") -> None:
    """Print the Ledger branded header."""
    console = get_console()
    title = Text("Ledger", style="bold cyan")
    body = Text(f"\n{subtitle}", style="dim")
    console.print(Panel(title + body, border_style="cyan", padding=(1, 2)))
