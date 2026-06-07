"""PostgreSQL adapter — psycopg2 for connection test, pg_dump for backup."""

from __future__ import annotations

from typing import BinaryIO

from database.base import AbstractDBAdapter


class PostgresAdapter(AbstractDBAdapter):
    """PostgreSQL backup adapter."""

    def test_connection(self) -> bool:
        raise NotImplementedError

    def full_backup(self) -> BinaryIO:
        raise NotImplementedError

    def incremental_backup(self) -> BinaryIO:
        raise NotImplementedError

    def restore(self, source: BinaryIO, *, target_database: str | None = None) -> None:
        raise NotImplementedError

    def list_restorable_objects(self, source: BinaryIO) -> list[str]:
        raise NotImplementedError
