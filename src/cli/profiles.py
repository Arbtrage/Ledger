"""Profile management — `ledger profiles`."""

from __future__ import annotations

import typer

from core.profiles import ProfileStore
from ui.banner import print_banner
from ui.console import get_console
from ui.tables import print_profile_table

app = typer.Typer(help="Manage database profiles.")


@app.callback(invoke_without_command=True)
def profiles_list() -> None:
    """List configured profiles."""
    print_banner()
    store = ProfileStore()
    names = store.list_names()
    if not names:
        console = get_console()
        console.print(
            "[yellow]No profiles yet.[/yellow] Run [bold]ledger init[/bold] to create one."
        )
        raise typer.Exit(code=0)
    profiles = [store.load(n) for n in names]
    print_profile_table(profiles)


@app.command("remove")
def profiles_remove(
    name: str = typer.Argument(..., help="Profile name to remove."),
) -> None:
    """Delete a profile."""
    from ui.console import get_console

    ProfileStore().delete(name)
    get_console().print(f"[green]✓[/green] Removed profile [cyan]{name}[/cyan]")
