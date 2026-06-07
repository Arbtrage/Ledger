"""Unit tests for CLI entry point."""

import pytest
from typer.testing import CliRunner

from cli.main import app

runner = CliRunner()


@pytest.mark.unit
def test_cli_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "ledger" in result.stdout.lower() or "backup" in result.stdout.lower()


@pytest.mark.unit
def test_cli_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout


@pytest.mark.unit
def test_backup_command_help() -> None:
    result = runner.invoke(app, ["backup", "--help"])
    assert result.exit_code == 0
    assert "PROFILE" in result.stdout or "profile" in result.stdout.lower()


@pytest.mark.unit
def test_init_help() -> None:
    result = runner.invoke(app, ["init", "--help"])
    assert result.exit_code == 0


@pytest.mark.unit
def test_profiles_help() -> None:
    result = runner.invoke(app, ["profiles", "--help"])
    assert result.exit_code == 0


@pytest.mark.unit
def test_backup_dry_run_missing_profile(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEDGER_HOME", str(tmp_path))
    result = runner.invoke(app, ["backup", "nonexistent", "--dry-run"])
    assert result.exit_code == 1
