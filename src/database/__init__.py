"""Database adapters for backup and restore operations."""

from database.base import AbstractDBAdapter
from database.mongodb import MongoDBAdapter
from database.mysql import MySQLAdapter
from database.postgres import PostgresAdapter
from database.sqlite import SQLiteAdapter
from utils.models import DatabaseType

__all__ = [
    "AbstractDBAdapter",
    "MongoDBAdapter",
    "MySQLAdapter",
    "PostgresAdapter",
    "SQLiteAdapter",
    "get_adapter",
]


def get_adapter(db_type: DatabaseType) -> type[AbstractDBAdapter]:
    """Return the adapter class for a database type."""
    mapping = {
        DatabaseType.MYSQL: MySQLAdapter,
        DatabaseType.POSTGRES: PostgresAdapter,
        DatabaseType.MONGODB: MongoDBAdapter,
        DatabaseType.SQLITE: SQLiteAdapter,
    }
    return mapping[db_type]
