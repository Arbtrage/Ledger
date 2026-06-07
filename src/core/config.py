"""Application configuration — YAML file + environment variables."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from utils.models import CompressionType, DatabaseType, StorageType


class AppSettings(BaseSettings):
    """Top-level application settings loaded from env vars and optional YAML.

    Passwords and secrets must come from environment variables or keyring —
    never from committed config files.
    """

    model_config = SettingsConfigDict(
        env_prefix="LEDGER_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    config_file: Path | None = None
    log_level: str = "INFO"
    log_json: bool = False

    # Default database target (overridable per command)
    db_type: DatabaseType = DatabaseType.MYSQL
    db_host: str = "localhost"
    db_port: int | None = None
    db_name: str = ""
    db_user: str | None = None
    db_password: SecretStr | None = None

    # Default storage
    storage_type: StorageType = StorageType.LOCAL
    storage_path: Path = Path("./backups")
    storage_bucket: str | None = None
    storage_prefix: str = ""
    storage_region: str | None = None

    # Backup defaults
    compression: CompressionType = CompressionType.GZIP
    encrypt_backups: bool = False
    encryption_key: SecretStr | None = None

    # Scheduler
    scheduler_job_store: Path = Path("./scheduler_jobs.sqlite")

    # Notifications
    slack_webhook_url: SecretStr | None = None

    @classmethod
    def from_yaml(cls, path: Path) -> AppSettings:
        """Load settings from a YAML file merged with environment variables."""
        raise NotImplementedError

    def to_dict(self, *, redact_secrets: bool = True) -> dict[str, Any]:
        """Serialize settings for logging (secrets redacted by default)."""
        raise NotImplementedError
