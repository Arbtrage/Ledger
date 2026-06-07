"""Interactive setup wizard — `ledger init`."""

from __future__ import annotations

import typer
from rich.prompt import Confirm, Prompt

from core.paths import ensure_ledger_home
from core.profiles import ProfileStore
from ui.banner import print_banner
from ui.console import get_console
from utils.models import (
    CompressionType,
    DatabaseType,
    DBConfig,
    Profile,
    StorageConfig,
    StorageType,
)


def init_wizard(
    profile_name: str | None = typer.Option(
        None, "--name", "-n", help="Profile name (skip prompt)."
    ),
    yes: bool = typer.Option(False, "--yes", "-y", help="Accept defaults where possible."),
) -> None:
    """Run the interactive setup wizard and save a profile to ~/.ledger/."""
    print_banner(subtitle="Setup Wizard")
    ensure_ledger_home()
    console = get_console()

    if profile_name:  # noqa: SIM108 — ternary confuses mypy on Prompt.ask return type
        name = profile_name
    else:
        name = Prompt.ask("[bold]Profile name[/bold]", default="postgres-prod")

    db_type_str = Prompt.ask(
        "[bold]Database type[/bold]",
        choices=["mysql", "postgres", "mongodb", "sqlite"],
        default="postgres",
    )
    host = Prompt.ask("[bold]Host[/bold]", default="localhost")
    port_str = Prompt.ask("[bold]Port[/bold]", default=_default_port(db_type_str))
    database = Prompt.ask("[bold]Database name[/bold]", default="myapp")
    username = Prompt.ask("[bold]Username[/bold]", default="postgres") if not yes else "postgres"

    storage_str = Prompt.ask(
        "[bold]Storage[/bold]",
        choices=["local", "s3", "gcs", "azure"],
        default="local",
    )
    bucket: str | None = None
    if storage_str != "local":
        bucket = Prompt.ask("[bold]Bucket[/bold]", default="my-backups")

    profile = Profile(
        name=name,
        database=DBConfig(
            db_type=DatabaseType(db_type_str),
            host=host,
            port=int(port_str) if port_str else None,
            database=database,
            username=username,
        ),
        storage=StorageConfig(
            storage_type=StorageType(storage_str),
            path=str(ensure_ledger_home() / "storage") if storage_str == "local" else None,
            bucket=bucket,
        ),
        compression=CompressionType.GZIP,
    )

    if not Confirm.ask(f"Save profile [cyan]{name}[/cyan]?", default=True):
        console.print("[yellow]Setup cancelled.[/yellow]")
        raise typer.Exit(code=0)

    path = ProfileStore().save(profile)
    console.print(f"[green]✓[/green] Profile saved to [dim]{path}[/dim]")
    console.print(f"\nRun: [bold cyan]ledger backup {name}[/bold cyan]")


def _default_port(db_type: str) -> str:
    return {"mysql": "3306", "postgres": "5432", "mongodb": "27017", "sqlite": ""}.get(db_type, "")
