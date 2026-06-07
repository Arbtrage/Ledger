# Quick Start

Get Ledger running and take your first backup in under a minute.

## Install

=== "pipx (recommended)"

    ```bash
    pipx install ledger
    ledger --version
    ```

=== "macOS (Homebrew)"

    ```bash
    brew install ledger-org/tap/ledger
    ```

=== "Windows (winget)"

    ```powershell
    winget install Ledger.Ledger
    ```

=== "pip"

    ```bash
    pip install ledger
    ```

!!! note "Native database tools"
    Ledger shells out to `pg_dump`, `mysqldump`, `mongodump`, or `sqlite3`. Install the client for your database before backing up.

## Initialize

```bash
ledger init
```

The wizard asks for your database type, connection details, and storage target — then saves a **profile** to `~/.ledger/profiles/`:

```text
╭──────────────────────────╮
│ Ledger                   │
│ Setup Wizard             │
╰──────────────────────────╯

Profile name? postgres-prod
Database type? PostgreSQL
Host? localhost
...
```

## First backup

```bash
ledger backup postgres-prod
```

Preview what will happen without touching your database:

```bash
ledger backup postgres-prod --dry-run
```

## Everyday commands

```bash
ledger profiles          # list saved profiles
ledger backups           # browse backup history
ledger restore           # pick a backup to restore
ledger dashboard         # full-screen terminal UI
```

## Next steps

- [Profiles](profiles.md) — manage multiple databases
- [Cloud storage](cloud-storage.md) — back up to S3, GCS, or Azure
- [Scheduling](scheduling.md) — unattended cron backups
- [Deployment](deployment.md) — run Ledger on a server or in Kubernetes
