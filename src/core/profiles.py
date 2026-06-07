"""Profile management — named database + storage configurations."""

from __future__ import annotations

from pathlib import Path

import yaml

from core.paths import ensure_ledger_home, profiles_dir
from utils.exceptions import ConfigError
from utils.models import Profile


class ProfileStore:
    """CRUD for profiles stored as YAML in ~/.ledger/profiles/."""

    def __init__(self, base_dir: Path | None = None) -> None:
        self._base_dir = base_dir or profiles_dir()

    def list_names(self) -> list[str]:
        """Return sorted profile names (without .yaml extension)."""
        if not self._base_dir.exists():
            return []
        return sorted(p.stem for p in self._base_dir.glob("*.yaml"))

    def load(self, name: str) -> Profile:
        """Load a profile by name."""
        path = self._base_dir / f"{name}.yaml"
        if not path.exists():
            raise ConfigError(f"Profile not found: {name}", context={"profile": name})
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ConfigError(f"Invalid profile file: {name}")
        return Profile.model_validate({**data, "name": name})

    def save(self, profile: Profile) -> Path:
        """Persist a profile to ~/.ledger/profiles/<name>.yaml."""
        if self._base_dir == profiles_dir():
            ensure_ledger_home()
        self._base_dir.mkdir(parents=True, exist_ok=True)
        path = self._base_dir / f"{profile.name}.yaml"
        payload = profile.model_dump(mode="json", exclude={"name"})
        path.write_text(yaml.safe_dump(payload, default_flow_style=False), encoding="utf-8")
        return path

    def delete(self, name: str) -> None:
        """Remove a profile."""
        path = self._base_dir / f"{name}.yaml"
        if not path.exists():
            raise ConfigError(f"Profile not found: {name}")
        path.unlink()

    def exists(self, name: str) -> bool:
        return (self._base_dir / f"{name}.yaml").exists()
