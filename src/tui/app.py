"""Textual dashboard — profiles, recent backups, storage usage."""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header, Label, Static


class LedgerDashboard(App[None]):
    """Interactive terminal dashboard (scaffold)."""

    TITLE = "Ledger"
    SUB_TITLE = "Database Backup Orchestration"

    CSS = """
    Screen { background: $surface; }
    #profiles { height: auto; margin: 1 2; }
  """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            yield Static("[bold cyan]Databases[/bold cyan]", id="profiles-title")
            with Vertical(id="profiles"):
                yield Label("  ✓ postgres-prod  [dim](scaffold)[/dim]")
                yield Label("  ✓ mongo-dev      [dim](scaffold)[/dim]")
            yield Static("")
            yield Static("[bold cyan]Recent Backups[/bold cyan]")
            yield Label("  SUCCESS  2 mins ago  [dim](scaffold)[/dim]")
            yield Static("")
            yield Static("[bold cyan]Storage Usage[/bold cyan]")
            yield Label("  ████████████░░░░  82%  [dim](scaffold)[/dim]")
        yield Footer()

    def on_mount(self) -> None:
        self.sub_title = "Press q to quit"


def run_dashboard() -> None:
    """Launch the Textual dashboard (blocking)."""
    LedgerDashboard().run()
