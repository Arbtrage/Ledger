"""Storage backends for backup artifacts."""

from storage.azure import AzureStorageBackend
from storage.base import AbstractStorageBackend
from storage.gcs import GCSStorageBackend
from storage.local import LocalStorageBackend
from storage.s3 import S3StorageBackend
from utils.models import StorageType

__all__ = [
    "AbstractStorageBackend",
    "AzureStorageBackend",
    "GCSStorageBackend",
    "LocalStorageBackend",
    "S3StorageBackend",
    "get_storage_backend",
]


def get_storage_backend(storage_type: StorageType) -> type[AbstractStorageBackend]:
    """Return the storage backend class for a storage type."""
    mapping = {
        StorageType.LOCAL: LocalStorageBackend,
        StorageType.S3: S3StorageBackend,
        StorageType.GCS: GCSStorageBackend,
        StorageType.AZURE: AzureStorageBackend,
    }
    return mapping[storage_type]
