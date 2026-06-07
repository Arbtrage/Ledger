"""Post-backup verification — trust signal for production use."""

from __future__ import annotations

from core.profiles import ProfileStore
from utils.models import BackupHistoryEntry, VerificationResult


class BackupVerifier:
    """Verify backup integrity after write (checksum, restore-to-temp, etc.)."""

    def verify(self, entry: BackupHistoryEntry) -> VerificationResult:
        """Run verification checks on a completed backup."""
        raise NotImplementedError

    def dry_run_plan(self, profile_name: str) -> list[str]:
        """Return human-readable steps that would run for a backup (no I/O)."""
        profile = ProfileStore().load(profile_name)
        storage = profile.storage.storage_type.value
        return [
            f"Connect to {profile.database.db_type.value} at {profile.database.host}",
            f"Run full backup of database '{profile.database.database}'",
            f"Compress with {profile.compression.value}",
            f"Upload to {storage}"
            + (f" bucket {profile.storage.bucket}" if profile.storage.bucket else ""),
            "Record entry in ~/.ledger/history.db",
            "Verify backup integrity (checksum + optional restore test)",
        ]
