"""Unit tests for storage backends."""

import pytest

from storage import get_storage_backend
from storage.local import LocalStorageBackend
from utils.models import StorageType


@pytest.mark.unit
def test_get_storage_backend_local() -> None:
    assert get_storage_backend(StorageType.LOCAL) is LocalStorageBackend


@pytest.mark.unit
@pytest.mark.parametrize(
    "storage_type",
    [StorageType.LOCAL, StorageType.S3, StorageType.GCS, StorageType.AZURE],
)
def test_all_storage_backends_registered(storage_type: StorageType) -> None:
    backend_cls = get_storage_backend(storage_type)
    assert backend_cls is not None
