# Changelog

All notable changes to **Ledger** are documented in this file.

## [Unreleased]

### Changed
- Moved application code under `src/` (cli, core, database, storage, ui, tui, utils)
- Grouped deploy assets under `deploy/` (docker, packaging, docker-compose)
- Moved `config/ledger.example.yaml` → `examples/ledger.example.yaml`
- Moved root util modules into `utils/` package
- Removed `website/` folder (docs site covers distribution)

### Added
- Profile-first UX: `ledger init`, `ledger backup <profile>`, `ledger profiles`
- `~/.ledger/` layout: profiles, storage, history.db, logs
- Rich UI module: banner, progress, tables (`ui/`)
- Textual dashboard: `ledger dashboard` (`tui/`)
- Backup explorer: `ledger backups`
- Interactive restore: `ledger restore`
- Dry-run: `ledger backup <profile> --dry-run`
- Backup verification scaffold (`core/verification.py`)
- MkDocs Material docs site + GitHub Pages workflow
- Distribution scaffolds: Homebrew, WinGet, Docker
- `examples/` sample profiles and cron script
- `utils/` package for shared modules (models, exceptions, compression, etc.)

### Changed
- Renamed `adapters/` → `database/`
- Removed flag-heavy `ledger config` in favor of `ledger init` wizard
- CLI tagline: "The Docker of database backups"
- Schedule commands now use `--profile` instead of raw DB flags

## [0.1.0] - 2026-06-08

### Added
- Initial flat-layout project scaffold
- Database adapters, storage backends, orchestrator stubs
- GitHub Actions CI matrix

[Unreleased]: https://github.com/ledger-org/ledger/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ledger-org/ledger/releases/tag/v0.1.0
