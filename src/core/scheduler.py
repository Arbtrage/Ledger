"""APScheduler wrapper for cron-style backup scheduling."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from core.config import AppSettings


class BackupScheduler:
    """Manages scheduled backup jobs with a persistent SQLite job store."""

    def __init__(self, settings: AppSettings) -> None:
        self.settings = settings
        self._job_store_path = settings.scheduler_job_store

    def start(self) -> None:
        """Start the scheduler daemon."""
        raise NotImplementedError

    def stop(self) -> None:
        """Gracefully shut down the scheduler."""
        raise NotImplementedError

    def add_cron_job(
        self,
        job_id: str,
        cron_expression: str,
        backup_fn: Callable[[], None],
    ) -> None:
        """Register a cron-scheduled backup job."""
        raise NotImplementedError

    def remove_job(self, job_id: str) -> None:
        """Remove a scheduled job by ID."""
        raise NotImplementedError

    def list_jobs(self) -> list[dict[str, str]]:
        """List all registered scheduled jobs."""
        raise NotImplementedError

    @staticmethod
    def default_job_store_path() -> Path:
        """Default SQLite job store path for APScheduler persistence."""
        return Path("./scheduler_jobs.sqlite")
