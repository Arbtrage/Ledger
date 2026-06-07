"""Restore CLI — `ledger restore` (interactive explorer)."""

from __future__ import annotations

import typer
from rich.prompt import Prompt

from core.history import HistoryStore
from core.profiles import ProfileStore
from ui.banner import print_banner
from ui.console import get_console
from ui.tables import print_backup_table


def restore(
    profile: str | None = typer.Argument(
        None, help="Profile to restore (optional — prompts if omitted)."
    ),
    backup_id: str | None = typer.Option(
        None, "--backup", "-b", help="Backup ID to restore."
    ),
    interactive: bool = typer.Option(
        True, "--interactive/--no-interactive", help="Interactive picker."
    ),
) -> None:
    """Restore a database from backup history (interactive by default)."""
    print_banner(subtitle="Restore Explorer")
    console = get_console()
    history = HistoryStore()
    history.initialize()

    if profile is None and interactive:
        profiles = ProfileStore().list_names()
        if not profiles:
            console.print("[yellow]No profiles configured.[/yellow] Run [bold]ledger init[/bold]")
            raise typer.Exit(code=1)
        profile = Prompt.ask("[bold]Profile[/bold]", choices=profiles)

    entries = history.list_backups(profile_name=profile, limit=10)
    if not entries and interactive:
        console.print("[yellow]No backups found for this profile.[/yellow]")
        raise typer.Exit(code=0)

    if interactive and entries:
        print_backup_table(entries)
        backup_id = backup_id or Prompt.ask("[bold]Backup ID[/bold] (first 8 chars)")

    console.print(f"[dim]Restore scaffold — would restore {backup_id} for {profile}[/dim]")
    raise typer.Exit(code=0)
