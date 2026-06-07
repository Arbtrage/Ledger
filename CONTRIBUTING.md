# Contributing to Ledger

Thank you for contributing. This project follows a layered plugin architecture — please read [docs/architecture.md](docs/architecture.md) before opening a PR.

## Getting started

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
pytest tests/unit -m unit
```

## Branch strategy

| Branch | Purpose |
|---|---|
| `main` | Stable, release-ready code |
| `develop` | Integration branch for in-progress features |
| `feature/*` | Individual features |
| `fix/*` | Bug fixes |

Open PRs against `develop` (or `main` for hotfixes).

## Code standards

- **Abstract interfaces first** — new DB or storage support = new adapter class, no changes to orchestrator
- **Subprocess, not shell** — use `subprocess.run()` / `Popen` with `shlex.split()`, never `shell=True`
- **Stream, don't buffer** — read/write in 8 MB chunks; never load full backups into memory
- **No credentials in logs** — even at DEBUG level
- **Pydantic for config** — validate early, fail with clear errors
- **Tests mock at subprocess boundary** — unit tests must not require live databases

## Testing

```bash
# Unit tests (required for every PR)
pytest tests/unit -m unit

# Integration tests (when touching adapters)
docker compose -f deploy/docker-compose.test.yml up -d
pytest tests/integration -m integration
```

Mark tests with `@pytest.mark.unit`, `@pytest.mark.integration`, or `@pytest.mark.slow`.

## Pull request checklist

- [ ] Tests added or updated
- [ ] `ruff check` and `ruff format` pass
- [ ] `mypy` passes (or override documented)
- [ ] CHANGELOG.md updated under `[Unreleased]`
- [ ] No secrets, credentials, or `.env` files committed

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(mysql): implement full backup via mysqldump streaming
fix(storage): atomic rename on Windows for local backend
docs: add deployment guide for systemd
test(postgres): mock pg_dump subprocess in unit tests
```

## Versioning

See [docs/versioning.md](docs/versioning.md). Do not bump `VERSION` in feature PRs — release maintainers handle that at release time.
