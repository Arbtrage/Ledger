# Installation

Ledger is distributed as a standalone CLI — install it like any other developer tool.

## Recommended

=== "Linux / macOS — pipx"

    Isolates Ledger from your system Python (recommended):

    ```bash
    pipx install ledger
    pipx upgrade ledger    # update later
    ```

=== "Any platform — pip"

    ```bash
    pip install ledger
    ```

## Platform packages

| Platform | Command | Status |
|---|---|---|
| macOS | `brew install ledger-org/tap/ledger` | Coming soon |
| Windows | `winget install Ledger.Ledger` | Coming soon |
| Docker | `docker run ghcr.io/ledger-org/ledger` | Coming soon |

## Verify

```bash
ledger --version
ledger --help
```

## Prerequisites

Install the native dump tool for each database you plan to back up:

| Database | Required binaries |
|---|---|
| PostgreSQL | `pg_dump`, `psql` |
| MySQL | `mysqldump`, `mysql` |
| MongoDB | `mongodump`, `mongorestore` |
| SQLite | `sqlite3` |

On macOS: `brew install postgresql@16 mysql-client mongodb-database-tools sqlite`

On Debian/Ubuntu: `apt install postgresql-client mysql-client mongodb-database-tools sqlite3`

## Building from source

Only needed if you're contributing to Ledger itself — see [Contributing](contributing.md).

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ledger --version
```
