"""Integration tests for PostgreSQL backup (requires docker-compose.test.yml)."""

import pytest


@pytest.mark.integration
@pytest.mark.skip(reason="Requires PostgreSQL container — enable after adapter implementation")
def test_postgres_full_backup_roundtrip() -> None:
    pass
