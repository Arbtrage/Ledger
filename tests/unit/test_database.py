"""Unit tests for database adapters (mocked subprocess boundary)."""

import pytest

from database import get_adapter
from database.mysql import MySQLAdapter
from utils.models import DatabaseType, DBConfig


@pytest.mark.unit
def test_get_adapter_mysql() -> None:
    assert get_adapter(DatabaseType.MYSQL) is MySQLAdapter


@pytest.mark.unit
def test_mysql_adapter_test_connection_not_implemented(mysql_config: DBConfig) -> None:
    adapter = MySQLAdapter(mysql_config)
    with pytest.raises(NotImplementedError):
        adapter.test_connection()


@pytest.mark.unit
@pytest.mark.parametrize(
    "db_type",
    [DatabaseType.MYSQL, DatabaseType.POSTGRES, DatabaseType.MONGODB, DatabaseType.SQLITE],
)
def test_all_database_adapters_registered(db_type: DatabaseType) -> None:
    adapter_cls = get_adapter(db_type)
    assert adapter_cls is not None
