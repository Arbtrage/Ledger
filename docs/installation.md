# Installation

## Distribution channels

| Platform | Command | Status |
|---|---|---|
| macOS | `brew install ledger-org/tap/ledger` | Scaffold |
| Linux | `pipx install ledger` | PyPI (alpha) |
| Windows | `winget install Ledger.Ledger` | Scaffold |
| Docker | `docker run ghcr.io/ledger-org/ledger` | Scaffold |

## pipx (recommended for Linux)

```bash
pipx install ledger
ledger --version
```

## Development install

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Native tools

Ledger shells out to native database tools. Install the clients for your DBMS:

| DBMS | Tool |
|---|---|
| PostgreSQL | `pg_dump`, `psql` |
| MySQL | `mysqldump`, `mysql` |
| MongoDB | `mongodump`, `mongorestore` |
| SQLite | `sqlite3` |
