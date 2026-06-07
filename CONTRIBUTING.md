# Contributing to Ledger

Ledger is an open-source CLI tool. This guide is for developers who want to contribute to the tool itself.

## Set up a dev environment

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
pytest tests/unit -m unit
```

## Architecture

Ledger uses a layered plugin design — read [docs/architecture.md](docs/architecture.md) before opening a PR. New database or storage support = new adapter class, no orchestrator changes.

## Branch strategy

| Branch | Purpose |
|---|---|
| `main` | Stable releases |
| `develop` | Integration branch |
| `feature/*` | New features |
| `fix/*` | Bug fixes |

## Code standards

- **Abstract interfaces first** — new DB or storage = new adapter, no orchestrator changes
- **Subprocess, not shell** — `subprocess.run()` with `shlex.split()`, never `shell=True`
- **Stream, don't buffer** — 8 MB chunks; never load full backups into memory
- **No credentials in logs** — even at DEBUG
- **Tests mock at subprocess boundary** — unit tests must not require live databases

## Pull request checklist

- [ ] Tests added or updated
- [ ] `ruff check src tests` and `mypy src` pass
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] No secrets or `.env` files committed

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(mysql): implement full backup via mysqldump streaming
fix(storage): atomic rename on Windows for local backend
docs: add systemd deployment guide
```

## Source layout

Application code lives in `src/` — see [src/README.md](src/README.md).
