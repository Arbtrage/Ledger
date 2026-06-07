"""Backup explorer — `ledger backups`."""

from __future__ import annotations

import typer

from core.history import HistoryStore
from ui.banner import print_banner
from ui.console import get_console
from ui.tables import print_backup_table

app = typer.Typer(help="Browse backup history.")


@app.callback(invoke_without_command=True)
def backups_list(
    profile: str | None = typer.Option(None, "--profile", "-p", help="Filter by profile."),
    limit: int = typer.Option(20, "--limit", "-n", help="Max rows to show."),
) -> None:
    """List recent backups from ~/.ledger/history.db."""
    print_banner(subtitle="Backup Explorer")
    store = HistoryStore()
    store.initialize()
    entries = store.list_backups(profile_name=profile, limit=limit)
    if not entries:
        get_console().print(
            "[yellow]No backups yet.[/yellow] "
            "Run [bold]ledger backup <profile>[/bold] to create one."
        )
        raise typer.Exit(code=0)
    print_backup_table(entries)
