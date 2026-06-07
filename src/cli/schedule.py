"""Schedule CLI commands — cron-style backups per profile."""

from __future__ import annotations

import typer

app = typer.Typer(help="Schedule recurring backups.")


@app.command("add")
def schedule_add(
    job_id: str = typer.Option(..., "--job-id", help="Unique job identifier."),
    cron: str = typer.Option(..., "--cron", help='Cron expression (e.g. "0 2 * * *").'),
    profile: str = typer.Option(..., "--profile", "-p", help="Profile to back up."),
) -> None:
    """Register a cron-scheduled backup job for a profile."""
    typer.echo(f"Schedule add scaffold — would schedule {profile} as {job_id}")
    raise typer.Exit(code=0)


@app.command("list")
def schedule_list() -> None:
    """List all scheduled backup jobs."""
    typer.echo("Schedule list scaffold — implementation pending.")
    raise typer.Exit(code=0)


@app.command("remove")
def schedule_remove(
    job_id: str = typer.Option(..., "--job-id", help="Job ID to remove."),
) -> None:
    """Remove a scheduled backup job."""
    typer.echo("Schedule remove scaffold — implementation pending.")
    raise typer.Exit(code=0)


@app.command("daemon")
def schedule_daemon() -> None:
    """Start the scheduler daemon (blocking)."""
    typer.echo("Schedule daemon scaffold — implementation pending.")
    raise typer.Exit(code=0)
