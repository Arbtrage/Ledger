# Ledger

**The Docker of database backups.**

Production-grade database backup orchestration with Docker/kubectl-level UX — profiles, Rich terminal UI, Textual dashboard, cloud sync, and backup verification.

> **Status:** Alpha scaffold — wizard, profiles, and UI shells work; backup pipeline implementation in progress. See [docs/ROADMAP.md](docs/ROADMAP.md).

```bash
pipx install ledger    # or: pip install -e ".[dev]"
ledger init            # 30-second interactive wizard
ledger backup postgres-prod
ledger dashboard       # Textual TUI
```

## Why Ledger?

| College-project CLI | Ledger |
|---|---|
| 50 flags per command | Named profiles |
| `python backup.py` | `ledger backup prod` |
| Plain text output | Rich progress, tables, panels |
| Clone from GitHub | `brew install ledger` / `pipx install ledger` |
| No verification | Post-backup integrity checks |

## Quick start

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

ledger init
ledger profiles
ledger backup <profile> --dry-run
```

## CLI

```bash
ledger init                    # interactive setup wizard → ~/.ledger/
ledger backup postgres-prod    # backup using saved profile
ledger backup prod --dry-run   # preview steps, no I/O
ledger restore                 # interactive restore explorer
ledger backups                 # backup history table
ledger profiles                # list configured profiles
ledger dashboard               # Textual terminal dashboard
ledger schedule add --profile postgres-prod --cron "0 2 * * *"
```

## Config layout

```text
~/.ledger/
├── profiles/       # postgres-prod.yaml, mongo-dev.yaml
├── storage/        # local artifacts
├── history.db      # backup explorer
└── logs/
```

## Project structure

```text
src/          # application code (cli, core, database, storage, ui, tui, utils)
tests/        # unit + integration tests
docs/         # MkDocs Material site
examples/     # sample profiles, cron scripts, config templates
deploy/       # Docker, packaging, docker-compose for integration tests
```

See [src/README.md](src/README.md) and [deploy/README.md](deploy/README.md) for details.

## Documentation

| Resource | Link |
|---|---|
| Docs site | [mkdocs.yml](mkdocs.yml) → `mkdocs serve` |
| Architecture | [docs/architecture.md](docs/architecture.md) |
| Roadmap | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Installation | [docs/installation.md](docs/installation.md) |

```bash
pip install -e ".[docs]"
mkdocs serve
```

## Development

```bash
ruff check src tests
mypy src
pytest tests/unit -m unit
```

## Distribution (roadmap)

| Platform | Command |
|---|---|
| macOS | `brew install ledger-org/tap/ledger` |
| Linux | `pipx install ledger` |
| Windows | `winget install Ledger.Ledger` |
| Docker | `ghcr.io/ledger-org/ledger` |

## Free tier

Unlimited **local backups** — free forever.

## License

MIT — see [LICENSE](LICENSE).
