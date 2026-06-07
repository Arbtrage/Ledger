"""Unit tests for Rich UI helpers."""

import io

import pytest
from rich.console import Console

import ui.console as console_mod
from ui.banner import print_banner
from ui.console import get_console
from ui.tables import print_profile_table
from utils.models import DatabaseType, DBConfig, Profile, StorageConfig, StorageType


@pytest.mark.unit
def test_get_console_singleton() -> None:
    console_mod._console = None
    assert get_console() is get_console()


@pytest.mark.unit
def test_print_banner() -> None:
    console_mod._console = Console(file=io.StringIO(), force_terminal=True, width=80)
    print_banner()


@pytest.mark.unit
def test_print_profile_table() -> None:
    console_mod._console = Console(file=io.StringIO(), force_terminal=True, width=80)
    profiles = [
        Profile(
            name="prod",
            database=DBConfig(db_type=DatabaseType.POSTGRES, database="myapp"),
            storage=StorageConfig(storage_type=StorageType.LOCAL, path="/tmp"),
        )
    ]
    print_profile_table(profiles)
