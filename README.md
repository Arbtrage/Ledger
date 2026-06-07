# Ledger

**The Docker of database backups.**

A CLI tool for developers and platform teams — back up PostgreSQL, MySQL, MongoDB, and SQLite with profiles, a Rich terminal UI, cloud storage, and built-in verification.

```bash
pipx install ledger
ledger init
ledger backup postgres-prod
```

> **Alpha.** The installer, wizard, profiles, and UI are available today. Full backup/restore pipelines are rolling out — see [What's coming](docs/ROADMAP.md).

## Install

| Platform | Command |
|---|---|
| Linux / macOS | `pipx install ledger` |
| macOS (Homebrew) | `brew install ledger-org/tap/ledger` *(coming soon)* |
| Windows | `winget install Ledger.Ledger` *(coming soon)* |
| Docker | `docker run ghcr.io/ledger-org/ledger` *(coming soon)* |

```bash
ledger --version
ledger --help
```

[Full installation guide →](docs/installation.md)

## Quick start

```bash
# 1. Run the setup wizard (creates ~/.ledger/profiles/)
ledger init

# 2. Back up a saved profile
ledger backup postgres-prod

# 3. Preview without running
ledger backup postgres-prod --dry-run
```

## Commands

```bash
ledger init                         # interactive setup wizard
ledger backup <profile>             # run a backup
ledger backup <profile> --dry-run   # preview steps only
ledger restore                      # interactive restore picker
ledger backups                      # browse backup history
ledger profiles                     # list saved profiles
ledger dashboard                    # full-screen terminal UI
ledger schedule add --profile <name> --cron "0 2 * * *"
```

[CLI reference →](docs/cli-reference.md)

## Why developers use Ledger

| Typical backup scripts | Ledger |
|---|---|
| Dozens of flags per run | Named profiles (`ledger backup prod`) |
| Opaque shell scripts | Rich progress, tables, and panels |
| Manual restore hunting | `ledger restore` interactive explorer |
| Unknown backup health | Post-backup verification built in |
| Ad-hoc cron wiring | `ledger schedule` with persistent jobs |

## Where Ledger stores data

```text
~/.ledger/
├── profiles/       # postgres-prod.yaml, staging-mysql.yaml, …
├── storage/        # local backup artifacts
├── history.db      # backup explorer index
└── logs/
```

Override the home directory with `LEDGER_HOME`. Secrets (passwords, API keys) come from environment variables or keyring — never from profile files.

[Configuration guide →](docs/configuration.md)

## Supported databases & storage

| Databases | Storage |
|---|---|
| PostgreSQL | Local disk |
| MySQL / MariaDB | Amazon S3 |
| MongoDB | Google Cloud Storage |
| SQLite | Azure Blob |

## Documentation

| Guide | Description |
|---|---|
| [Quick start](docs/getting-started.md) | Install → init → first backup |
| [Profiles](docs/profiles.md) | Named database + storage configs |
| [Backup & restore](docs/backup-restore.md) | Dry-run, verification, explorer |
| [Cloud storage](docs/cloud-storage.md) | S3, GCS, Azure setup |
| [Scheduling](docs/scheduling.md) | Cron-style unattended backups |
| [Deployment](docs/deployment.md) | systemd, Docker, Kubernetes |

```bash
pip install ledger[docs]
mkdocs serve   # preview docs locally
```

## Free tier

Unlimited **local backups** — free forever.

## Contributing

Ledger is open source. To hack on the CLI itself, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
