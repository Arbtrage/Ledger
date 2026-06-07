"""Unit tests for compression strategies."""

import pytest

from utils.compression import NoOpCompressor, get_compressor
from utils.models import CompressionType


@pytest.mark.unit
def test_get_compressor_gzip() -> None:
    compressor = get_compressor(CompressionType.GZIP)
    assert compressor.file_extension == ".gz"


@pytest.mark.unit
def test_noop_compressor_passthrough() -> None:
    import io

    data = io.BytesIO(b"hello backup")
    compressor = NoOpCompressor()
    assert compressor.compress_stream(data) is data
    assert compressor.file_extension == ""


@pytest.mark.unit
@pytest.mark.parametrize(
    "compression_type,expected_ext",
    [
        (CompressionType.GZIP, ".gz"),
        (CompressionType.BZ2, ".bz2"),
        (CompressionType.LZMA, ".xz"),
        (CompressionType.NONE, ""),
    ],
)
def test_compressor_extensions(compression_type: CompressionType, expected_ext: str) -> None:
    assert get_compressor(compression_type).file_extension == expected_ext
