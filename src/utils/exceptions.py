"""Custom exception hierarchy for Ledger."""


class LedgerError(Exception):
    """Base exception for all Ledger errors."""

    def __init__(self, message: str, *, context: dict[str, str] | None = None) -> None:
        self.context = context or {}
        super().__init__(message)


class ConnectionError(LedgerError):
    """Raised when a database connection test or handshake fails."""


class BackupError(LedgerError):
    """Raised when a backup operation fails."""


class StorageError(LedgerError):
    """Raised when reading from or writing to a storage backend fails."""


class RestoreError(LedgerError):
    """Raised when a restore operation fails."""


class ConfigError(LedgerError):
    """Raised when configuration is invalid or incomplete."""


class EncryptionError(LedgerError):
    """Raised when encryption or decryption fails."""


class SchedulerError(LedgerError):
    """Raised when scheduling operations fail."""
