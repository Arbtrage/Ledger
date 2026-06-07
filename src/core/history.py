"""Backup history store (~/.ledger/history.db)."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from core.paths import ensure_ledger_home, history_db_path
from utils.models import BackupHistoryEntry


class HistoryStore:
    """SQLite-backed backup history for explorer and dashboard."""

    SCHEMA = """
    CREATE TABLE IF NOT EXISTS backups (
        id TEXT PRIMARY KEY,
        profile_name TEXT NOT NULL,
        created_at TEXT NOT NULL,
        size_bytes INTEGER NOT NULL,
        storage_path TEXT NOT NULL,
        status TEXT NOT NULL,
        verified INTEGER DEFAULT 0,
        original_bytes INTEGER,
        compressed_bytes INTEGER
    );
    """

    def __init__(self, db_path: Path | None = None) -> None:
        self._db_path = db_path or history_db_path()

    def initialize(self) -> None:
        """Create history.db and schema if missing."""
        ensure_ledger_home()
        with self._connect() as conn:
            conn.execute(self.SCHEMA)
            conn.commit()

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def list_backups(
        self, *, profile_name: str | None = None, limit: int = 50
    ) -> list[BackupHistoryEntry]:
        """List recent backups, optionally filtered by profile."""
        raise NotImplementedError

    def record_backup(self, entry: BackupHistoryEntry) -> None:
        """Persist a completed backup to history."""
        raise NotImplementedError

    def get_by_id(self, backup_id: str) -> BackupHistoryEntry | None:
        """Fetch a single backup record by ID."""
        raise NotImplementedError
