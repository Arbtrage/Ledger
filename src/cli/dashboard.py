"""Terminal dashboard — `ledger dashboard`."""

from __future__ import annotations

import typer

app = typer.Typer(help="Launch the interactive terminal dashboard.")


@app.callback(invoke_without_command=True)
def dashboard() -> None:
    """Open the Textual dashboard (profiles, backups, storage usage)."""
    from tui import run_dashboard

    run_dashboard()
