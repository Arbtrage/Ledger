"""Integration tests for MySQL backup (requires docker-compose.test.yml)."""

import pytest


@pytest.mark.integration
@pytest.mark.skip(reason="Requires MySQL container — enable after adapter implementation")
def test_mysql_full_backup_roundtrip() -> None:
    """Backup myapp DB and verify artifact exists in local storage."""
    pass
