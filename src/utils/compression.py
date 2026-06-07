"""Compression strategy pattern for backup streams."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import BinaryIO

from utils.models import CompressionType


class AbstractCompressor(ABC):
    """Abstract compressor for streaming backup data."""

    @abstractmethod
    def compress_stream(self, source: BinaryIO) -> BinaryIO:
        """Return a readable stream of compressed bytes from source."""
        ...

    @abstractmethod
    def decompress_stream(self, source: BinaryIO) -> BinaryIO:
        """Return a readable stream of decompressed bytes from source."""
        ...

    @property
    @abstractmethod
    def file_extension(self) -> str:
        """File extension suffix for this compression type (e.g. '.gz')."""
        ...


class GzipCompressor(AbstractCompressor):
    """gzip compression (default)."""

    def compress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    def decompress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    @property
    def file_extension(self) -> str:
        return ".gz"


class Bz2Compressor(AbstractCompressor):
    """bzip2 compression."""

    def compress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    def decompress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    @property
    def file_extension(self) -> str:
        return ".bz2"


class LzmaCompressor(AbstractCompressor):
    """LZMA compression."""

    def compress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    def decompress_stream(self, source: BinaryIO) -> BinaryIO:
        raise NotImplementedError

    @property
    def file_extension(self) -> str:
        return ".xz"


class NoOpCompressor(AbstractCompressor):
    """Pass-through (no compression)."""

    def compress_stream(self, source: BinaryIO) -> BinaryIO:
        return source

    def decompress_stream(self, source: BinaryIO) -> BinaryIO:
        return source

    @property
    def file_extension(self) -> str:
        return ""


def get_compressor(compression_type: CompressionType) -> AbstractCompressor:
    """Factory for compression strategies."""
    mapping: dict[CompressionType, type[AbstractCompressor]] = {
        CompressionType.GZIP: GzipCompressor,
        CompressionType.BZ2: Bz2Compressor,
        CompressionType.LZMA: LzmaCompressor,
        CompressionType.NONE: NoOpCompressor,
    }
    return mapping[compression_type]()
