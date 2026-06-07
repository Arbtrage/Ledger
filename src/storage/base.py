"""Abstract storage backend interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import BinaryIO

from utils.models import StorageConfig


class AbstractStorageBackend(ABC):
    """Abstract interface for writing and reading backup artifacts.

    All writes use atomic rename: write to .tmp, then os.rename() to final path.
    """

    def __init__(self, config: StorageConfig) -> None:
        self.config = config

    @abstractmethod
    def write(self, key: str, source: BinaryIO, *, content_length: int | None = None) -> str:
        """Write backup bytes to storage. Returns the final storage path/URI."""
        ...

    @abstractmethod
    def read(self, key: str) -> BinaryIO:
        """Open a readable stream for the given backup key."""
        ...

    @abstractmethod
    def list_backups(self, prefix: str = "") -> list[str]:
        """List backup keys under an optional prefix."""
        ...

    @abstractmethod
    def delete(self, key: str) -> None:
        """Delete a backup artifact."""
        ...

    @abstractmethod
    def iter_chunks(self, key: str, *, chunk_size: int = 8 * 1024 * 1024) -> Iterator[bytes]:
        """Stream backup bytes in fixed-size chunks (default 8 MB)."""
        ...
