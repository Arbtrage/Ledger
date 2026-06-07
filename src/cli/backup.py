"""Backup CLI — `ledger backup <profile>`."""

from __future__ import annotations

import typer

from core.profiles import ProfileStore
from core.verification import BackupVerifier
from ui.banner import print_banner
from ui.console import get_console
from utils.models import BackupType


def backup(
    profile: str = typer.Argument(..., help="Profile name (e.g. postgres-prod)."),
    backup_type: BackupType = typer.Option(BackupType.FULL, "--type", help="Backup type."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show plan without executing."),
    verify: bool = typer.Option(True, "--verify/--no-verify", help="Verify backup after write."),
) -> None:
    """Back up a database using a saved profile."""
    print_banner()
    console = get_console()
    store = ProfileStore()

    if not store.exists(profile):
        console.print(f"[red]Profile not found:[/red] {profile}")
        console.print("Run [bold]ledger init[/bold] or [bold]ledger profiles[/bold]")
        raise typer.Exit(code=1)

    loaded = store.load(profile)

    if dry_run:
        console.print(f"[bold]Dry run[/bold] — [cyan]{profile}[/cyan]\n")
        steps = BackupVerifier().dry_run_plan(profile)
        for i, step in enumerate(steps, 1):
            console.print(f"  {i}. {step}")
        raise typer.Exit(code=0)

    db = loaded.database
    console.print(f"Backing up [cyan]{db.database}[/cyan] ({db.db_type.value})")
    console.print("[dim]Backup pipeline scaffold — implementation pending.[/dim]")
    if verify:
        console.print("[dim]Verification will run after backup completes.[/dim]")
    raise typer.Exit(code=0)
