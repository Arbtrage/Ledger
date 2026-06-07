"""Unit tests for exception hierarchy."""

import pytest

from utils.exceptions import BackupError, LedgerError, StorageError


@pytest.mark.unit
def test_exception_hierarchy() -> None:
    assert issubclass(BackupError, LedgerError)
    assert issubclass(StorageError, LedgerError)


@pytest.mark.unit
def test_exception_context() -> None:
    err = BackupError("dump failed", context={"database": "myapp", "db_type": "mysql"})
    assert err.context["database"] == "myapp"
    assert str(err) == "dump failed"
