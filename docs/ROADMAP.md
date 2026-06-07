# What's Coming

Ledger is in active development. Here's what's available today and what's on the way.

## Available now (v0.1)

| Feature | Command |
|---|---|
| Interactive setup | `ledger init` |
| Named profiles | `ledger profiles` |
| Backup (dry-run) | `ledger backup <profile> --dry-run` |
| Restore explorer | `ledger restore` |
| Backup history | `ledger backups` |
| Terminal dashboard | `ledger dashboard` |
| Rich terminal UI | progress bars, tables, banners |

## Coming next

### Backup & restore engine

- Live backup with streaming progress (speed, ETA, compression stats)
- PostgreSQL, MySQL, MongoDB, SQLite adapters
- Post-backup verification (checksum + optional restore test)
- Cloud upload progress for S3, GCS, Azure

### Scheduling & automation

- `ledger schedule` cron daemon with persistent job store
- AES-256-GCM encryption at rest
- Slack notifications on success/failure

### Distribution

- `brew install ledger` (Homebrew tap)
- `winget install Ledger.Ledger` (Windows)
- Official Docker image on `ghcr.io`

## Future

| Feature | Description |
|---|---|
| Cloud dashboard | Web UI for backup history and monitoring |
| Team profiles | Shared profile management |
| Backup analytics | Size trends, compression savings |
| Multi-region storage | DR-ready replication |

## Free tier

Unlimited local backups — free forever.

## Version milestones

| Version | Focus |
|---|---|
| `0.1.x` | CLI, profiles, UI (current) |
| `0.2.x` | Working backup pipeline + live progress |
| `0.3.x` | Cloud storage, scheduling, verification |
| `1.0.0` | Stable release on PyPI, Homebrew, winget |
