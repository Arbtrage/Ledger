"""Notification backends (Slack, etc.)."""

from __future__ import annotations

from abc import ABC, abstractmethod

from utils.models import BackupRecord


class AbstractNotifier(ABC):
    """Abstract notification backend."""

    @abstractmethod
    def notify_backup_success(self, record: BackupRecord) -> None:
        """Send a success notification."""
        ...

    @abstractmethod
    def notify_backup_failure(self, *, database: str, error: str) -> None:
        """Send a failure notification."""
        ...


class SlackNotifier(AbstractNotifier):
    """Slack webhook / bot token notifier."""

    def __init__(self, webhook_url: str | None = None, token: str | None = None) -> None:
        self._webhook_url = webhook_url
        self._token = token

    def notify_backup_success(self, record: BackupRecord) -> None:
        raise NotImplementedError

    def notify_backup_failure(self, *, database: str, error: str) -> None:
        raise NotImplementedError
