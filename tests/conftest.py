"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from utils.models import DatabaseType, DBConfig, StorageConfig, StorageType


@pytest.fixture
def tmp_backup_dir(tmp_path: Path) -> Path:
    """Empty directory for local backup artifacts."""
    backup_dir = tmp_path / "backups"
    backup_dir.mkdir()
    return backup_dir


@pytest.fixture
def mysql_config() -> DBConfig:
    return DBConfig(
        db_type=DatabaseType.MYSQL,
        host="localhost",
        port=3306,
        database="testdb",
        username="root",
    )


@pytest.fixture
def postgres_config() -> DBConfig:
    return DBConfig(
        db_type=DatabaseType.POSTGRES,
        host="localhost",
        port=5432,
        database="testdb",
        username="postgres",
    )


@pytest.fixture
def local_storage_config(tmp_backup_dir: Path) -> StorageConfig:
    return StorageConfig(
        storage_type=StorageType.LOCAL,
        path=str(tmp_backup_dir),
    )


@pytest.fixture
def mock_subprocess_stdout(mocker: Any) -> Any:
    """Patch subprocess.Popen to return fake backup bytes."""
    return mocker.patch("subprocess.Popen")
