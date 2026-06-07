# Ledger

**A CLI tool for database backups.**

Ledger gives developers and platform teams a single command to back up, verify, and restore PostgreSQL, MySQL, MongoDB, and SQLite — with the UX you'd expect from `docker`, `kubectl`, or `gh`.

## Install in seconds

```bash
pipx install ledger
ledger init
ledger backup postgres-prod
```

## What you get

- **Profile-based workflows** — `ledger backup prod`, not 50 flags
- **Interactive setup** — `ledger init` wizard saves configs to `~/.ledger/`
- **Rich terminal UI** — progress bars, tables, compression stats
- **Terminal dashboard** — `ledger dashboard` (Textual)
- **Backup verification** — integrity checks after every run
- **Cloud sync** — S3, GCS, Azure Blob
- **Cross-platform** — macOS, Linux, Windows

## Guides

- [Quick start](getting-started.md) — install, init, first backup
- [Profiles](profiles.md) — manage database connections
- [Backup & restore](backup-restore.md) — dry-run, verification, explorer
- [Installation](installation.md) — pipx, Homebrew, winget, Docker
- [CLI reference](cli-reference.md) — every command and flag

## Free tier

Unlimited local backups. Free forever.

## What's coming

Cloud dashboard, team profiles, monitoring, and multi-region storage — see the [roadmap](ROADMAP.md).
