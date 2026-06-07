"""SQLite adapter — file copy / sqlite3 CLI for backup."""

from __future__ import annotations

from typing import BinaryIO

from database.base import AbstractDBAdapter


class SQLiteAdapter(AbstractDBAdapter):
    """SQLite backup adapter (full backups only)."""

    def test_connection(self) -> bool:
        raise NotImplementedError

    def full_backup(self) -> BinaryIO:
        raise NotImplementedError

    def incremental_backup(self) -> BinaryIO:
        raise NotImplementedError("SQLite incremental backups are not supported in v1")

    def restore(self, source: BinaryIO, *, target_database: str | None = None) -> None:
        raise NotImplementedError

    def list_restorable_objects(self, source: BinaryIO) -> list[str]:
        raise NotImplementedError
