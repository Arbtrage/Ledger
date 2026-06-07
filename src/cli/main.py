"""CLI entry point — registers all commands."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import typer

from cli import backup, backups, dashboard, init_cmd, profiles, restore, schedule
from utils.logging_config import configure_logging

try:
    __version__ = version("ledger")
except PackageNotFoundError:
    __version__ = "0.1.0"

app = typer.Typer(
    name="ledger",
    help="The Docker of database backups — profiles, rich UI, cloud sync.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

app.command("init")(init_cmd.init_wizard)
app.command("backup")(backup.backup)
app.command("restore")(restore.restore)
app.add_typer(backups.app, name="backups")
app.add_typer(profiles.app, name="profiles")
app.add_typer(schedule.app, name="schedule")
app.add_typer(dashboard.app, name="dashboard")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"ledger {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
    log_level: str = typer.Option("INFO", "--log-level", envvar="LEDGER_LOG_LEVEL"),
    log_json: bool = typer.Option(False, "--log-json", envvar="LEDGER_LOG_JSON"),
) -> None:
    """Ledger — production-grade database backup orchestration."""
    configure_logging(level=log_level, json_output=log_json)
    ctx.ensure_object(dict)


if __name__ == "__main__":
    app()
