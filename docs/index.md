# Ledger

**The Docker of database backups.**

Ledger is a production-grade database backup orchestration platform with Docker-level UX:

- **30-second setup** — `ledger init` interactive wizard
- **Profile-based** — `ledger backup postgres-prod` (no 50 flags)
- **Rich terminal UI** — progress bars, tables, compression stats
- **Textual dashboard** — `ledger dashboard`
- **Backup verification** — trust signal after every backup
- **PostgreSQL, MySQL, MongoDB, SQLite** — local and cloud storage

```bash
brew install ledger          # macOS (coming soon)
pipx install ledger          # Linux
ledger init                  # interactive wizard
ledger backup postgres-prod  # one command
```

## Free tier

Unlimited **local backups** — free forever.

## Premium (roadmap)

Cloud dashboard, team backups, monitoring, multi-region storage, alerting, backup analytics.
