"""Integration tests for MongoDB backup (requires docker-compose.test.yml)."""

import pytest


@pytest.mark.integration
@pytest.mark.skip(reason="Requires MongoDB container — enable after adapter implementation")
def test_mongodb_full_backup_roundtrip() -> None:
    pass
