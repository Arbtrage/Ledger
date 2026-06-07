"""Unit tests for Pydantic models."""

import pytest
from pydantic import ValidationError

from utils.models import BackupRecord, DatabaseType, DBConfig


@pytest.mark.unit
def test_db_config_requires_database() -> None:
    with pytest.raises(ValidationError):
        DBConfig(db_type=DatabaseType.MYSQL)  # type: ignore[call-arg]


@pytest.mark.unit
def test_db_config_defaults() -> None:
    config = DBConfig(db_type=DatabaseType.POSTGRES, database="myapp")
    assert config.host == "localhost"
    assert config.port is None


@pytest.mark.unit
def test_backup_record_fields() -> None:
    from datetime import UTC, datetime

    record = BackupRecord(
        id="abc123",
        database="myapp",
        db_type=DatabaseType.MYSQL,
        backup_type="full",
        storage_path="/backups/myapp_full.sql.gz",
        size_bytes=1024,
        created_at=datetime.now(UTC),
    )
    assert record.compressed is True
    assert record.encrypted is False
