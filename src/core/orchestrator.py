"""Backup and restore orchestrators — coordinate adapters, compression, storage."""

from __future__ import annotations

from core.config import AppSettings
from database.base import AbstractDBAdapter
from storage.base import AbstractStorageBackend
from utils.models import BackupRecord, BackupType


class BackupOrchestrator:
    """Coordinates the backup pipeline: adapter → compression → encryption → storage.

    Streams data in 8 MB chunks; never loads full backup into memory.
    """

    CHUNK_SIZE = 8 * 1024 * 1024

    def __init__(
        self,
        adapter: AbstractDBAdapter,
        storage: AbstractStorageBackend,
        settings: AppSettings,
    ) -> None:
        self.adapter = adapter
        self.storage = storage
        self.settings = settings

    def run(
        self,
        *,
        backup_type: BackupType = BackupType.FULL,
    ) -> BackupRecord:
        """Execute a backup and return metadata for the completed artifact."""
        raise NotImplementedError

    def test_connection(self) -> bool:
        """Verify database connectivity before backup."""
        raise NotImplementedError


class RestoreOrchestrator:
    """Coordinates the restore pipeline: storage → decryption → decompression → adapter."""

    def __init__(
        self,
        adapter: AbstractDBAdapter,
        storage: AbstractStorageBackend,
        settings: AppSettings,
    ) -> None:
        self.adapter = adapter
        self.storage = storage
        self.settings = settings

    def run(
        self,
        backup_key: str,
        *,
        target_database: str | None = None,
        selective_objects: list[str] | None = None,
    ) -> None:
        """Restore from a stored backup artifact."""
        raise NotImplementedError
