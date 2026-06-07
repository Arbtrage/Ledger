"""AES-256-GCM encryption for backup data at rest."""

from __future__ import annotations

from typing import BinaryIO

from utils.exceptions import EncryptionError


class BackupEncryptor:
    """Encrypt and decrypt backup streams using AES-256-GCM."""

    def __init__(self, key: bytes) -> None:
        if len(key) != 32:
            raise EncryptionError("Encryption key must be 32 bytes (AES-256)")
        self._key = key

    def encrypt_stream(self, source: BinaryIO) -> BinaryIO:
        """Encrypt source stream and return readable encrypted bytes."""
        raise NotImplementedError

    def decrypt_stream(self, source: BinaryIO) -> BinaryIO:
        """Decrypt source stream and return readable plaintext bytes."""
        raise NotImplementedError
