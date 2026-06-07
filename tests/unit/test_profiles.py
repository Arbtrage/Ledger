"""Unit tests for profile store."""

from pathlib import Path

import pytest

from core.profiles import ProfileStore
from utils.models import DatabaseType, DBConfig, Profile, StorageConfig, StorageType


@pytest.mark.unit
def test_profile_save_and_load(tmp_path: Path) -> None:
    base = tmp_path / "profiles"
    base.mkdir()
    store = ProfileStore(base_dir=base)
    profile = Profile(
        name="test-pg",
        database=DBConfig(db_type=DatabaseType.POSTGRES, database="myapp", host="localhost"),
        storage=StorageConfig(storage_type=StorageType.LOCAL, path="/tmp/backups"),
    )
    store.save(profile)
    loaded = store.load("test-pg")
    assert loaded.name == "test-pg"
    assert loaded.database.database == "myapp"


@pytest.mark.unit
def test_profile_list_names(tmp_path: Path) -> None:
    base = tmp_path / "profiles2"
    base.mkdir()
    store = ProfileStore(base_dir=base)
    assert store.list_names() == []
