"""Pydantic data models for configuration and backup records."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, SecretStr


class DatabaseType(StrEnum):
    MYSQL = "mysql"
    POSTGRES = "postgres"
    MONGODB = "mongodb"
    SQLITE = "sqlite"


class BackupType(StrEnum):
    FULL = "full"
    INCREMENTAL = "incremental"
    DIFFERENTIAL = "differential"


class CompressionType(StrEnum):
    GZIP = "gzip"
    BZ2 = "bz2"
    LZMA = "lzma"
    NONE = "none"


class StorageType(StrEnum):
    LOCAL = "local"
    S3 = "s3"
    GCS = "gcs"
    AZURE = "azure"


class DBConfig(BaseModel):
    """Database connection configuration."""

    db_type: DatabaseType
    host: str = "localhost"
    port: int | None = None
    database: str
    username: str | None = None
    password: SecretStr | None = None
    extra: dict[str, Any] = Field(default_factory=dict)


class StorageConfig(BaseModel):
    """Storage backend configuration."""

    storage_type: StorageType
    path: str | None = None
    bucket: str | None = None
    prefix: str = ""
    region: str | None = None
    extra: dict[str, Any] = Field(default_factory=dict)


class BackupStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    VERIFIED = "verified"


class Profile(BaseModel):
    """Named backup profile — database + storage saved under ~/.ledger/profiles/."""

    name: str
    database: DBConfig
    storage: StorageConfig
    compression: CompressionType = CompressionType.GZIP
    encrypt: bool = False
    description: str = ""


class BackupRecord(BaseModel):
    """Metadata record for a completed backup."""

    id: str
    database: str
    db_type: DatabaseType
    backup_type: BackupType
    storage_path: str
    size_bytes: int
    checksum_sha256: str | None = None
    compressed: bool = True
    encrypted: bool = False
    created_at: datetime
    metadata: dict[str, Any] = Field(default_factory=dict)


class BackupHistoryEntry(BaseModel):
    """Row in ~/.ledger/history.db for backup explorer."""

    id: str
    profile_name: str
    created_at: datetime
    size_bytes: int
    storage_path: str
    status: BackupStatus
    verified: bool = False
    original_bytes: int | None = None
    compressed_bytes: int | None = None


class VerificationResult(BaseModel):
    """Outcome of post-backup verification."""

    valid: bool
    checksum_ok: bool = False
    restore_test_ok: bool = False
    message: str = ""
