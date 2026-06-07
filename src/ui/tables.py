"""Rich tables for profiles, backups, and restore explorer."""

from __future__ import annotations

from rich.table import Table

from ui.console import get_console
from utils.models import BackupHistoryEntry, Profile


def print_profile_table(profiles: list[Profile]) -> None:
    """Render configured database profiles."""
    table = Table(title="Database Profiles", show_header=True, header_style="bold cyan")
    table.add_column("Name", style="green")
    table.add_column("Type")
    table.add_column("Host")
    table.add_column("Database")
    table.add_column("Storage")
    for p in profiles:
        table.add_row(
            p.name,
            p.database.db_type.value,
            p.database.host,
            p.database.database,
            p.storage.storage_type.value,
        )
    get_console().print(table)


def print_backup_table(backups: list[BackupHistoryEntry]) -> None:
    """Render backup history explorer."""
    table = Table(title="Recent Backups", show_header=True, header_style="bold cyan")
    table.add_column("ID", style="dim")
    table.add_column("Profile")
    table.add_column("Date")
    table.add_column("Size")
    table.add_column("Status")
    table.add_column("Verified")
    for b in backups:
        verified = "✓" if b.verified else "—"
        table.add_row(
            b.id[:8],
            b.profile_name,
            b.created_at.strftime("%Y-%m-%d %H:%M"),
            _format_bytes(b.size_bytes),
            b.status.value,
            verified,
        )
    get_console().print(table)


def print_compression_stats(*, original_bytes: int, compressed_bytes: int) -> None:
    """Show compression savings panel."""
    saved_pct = (1 - compressed_bytes / original_bytes) * 100 if original_bytes else 0
    console = get_console()
    console.print(f"[bold]Original[/bold]   {_format_bytes(original_bytes)}")
    console.print(f"[bold]Compressed[/bold] {_format_bytes(compressed_bytes)}")
    console.print(f"[bold green]Saved[/bold green]      {saved_pct:.0f}%")


def _format_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n //= 1024
    return f"{n} PB"
