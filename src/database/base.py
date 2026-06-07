"""Abstract database adapter interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import BinaryIO

from utils.models import DBConfig


class AbstractDBAdapter(ABC):
    """Abstract interface for database backup and restore operations.

    All concrete adapters invoke native CLI tools via subprocess (never shell=True)
    and stream output in fixed-size chunks for constant memory usage.
    """

    def __init__(self, config: DBConfig) -> None:
        self.config = config

    @abstractmethod
    def test_connection(self) -> bool:
        """Verify connectivity to the database."""
        ...

    @abstractmethod
    def full_backup(self) -> BinaryIO:
        """Produce a full backup as a readable byte stream."""
        ...

    @abstractmethod
    def incremental_backup(self) -> BinaryIO:
        """Produce an incremental backup (DBMS-specific; may raise NotImplementedError)."""
        ...

    @abstractmethod
    def restore(self, source: BinaryIO, *, target_database: str | None = None) -> None:
        """Restore from a readable backup stream."""
        ...

    @abstractmethod
    def list_restorable_objects(self, source: BinaryIO) -> list[str]:
        """List tables/collections available for selective restore."""
        ...
