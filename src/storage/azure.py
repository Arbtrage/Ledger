"""Azure Blob Storage backend."""

from __future__ import annotations

from collections.abc import Iterator
from typing import BinaryIO

from storage.base import AbstractStorageBackend


class AzureStorageBackend(AbstractStorageBackend):
    """Store backups in Azure Blob Storage."""

    def write(self, key: str, source: BinaryIO, *, content_length: int | None = None) -> str:
        raise NotImplementedError

    def read(self, key: str) -> BinaryIO:
        raise NotImplementedError

    def list_backups(self, prefix: str = "") -> list[str]:
        raise NotImplementedError

    def delete(self, key: str) -> None:
        raise NotImplementedError

    def iter_chunks(self, key: str, *, chunk_size: int = 8 * 1024 * 1024) -> Iterator[bytes]:
        raise NotImplementedError
