"""Unit tests for backup verification dry-run."""

import pytest

from core.paths import ensure_ledger_home
from core.profiles import ProfileStore
from core.verification import BackupVerifier
from utils.models import DatabaseType, DBConfig, Profile, StorageConfig, StorageType


@pytest.mark.unit
def test_dry_run_plan(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEDGER_HOME", str(tmp_path))
    ensure_ledger_home()
    ProfileStore().save(
        Profile(
            name="prod",
            database=DBConfig(db_type=DatabaseType.POSTGRES, database="myapp"),
            storage=StorageConfig(storage_type=StorageType.S3, bucket="backups"),
        )
    )
    steps = BackupVerifier().dry_run_plan("prod")
    assert len(steps) >= 4
    assert any("postgres" in s.lower() for s in steps)
