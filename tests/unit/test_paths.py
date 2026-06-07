"""Unit tests for Ledger home paths."""

import pytest

from core.paths import ensure_ledger_home, profiles_dir, storage_dir


@pytest.mark.unit
def test_ensure_ledger_home(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEDGER_HOME", str(tmp_path))
    home = ensure_ledger_home()
    assert home == tmp_path
    assert profiles_dir().exists()
    assert storage_dir().exists()
