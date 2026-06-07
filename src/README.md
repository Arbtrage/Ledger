# Source layout (maintainers)

Application code for the Ledger CLI. End users install via `pipx install ledger` — they do not interact with this directory.

| Package | Role |
|---|---|
| `cli/` | Typer commands (`init`, `backup`, `restore`, …) |
| `core/` | Orchestrator, profiles, history, scheduler, verification |
| `database/` | DBMS adapters (PostgreSQL, MySQL, MongoDB, SQLite) |
| `storage/` | Local and cloud storage backends |
| `ui/` | Rich terminal components |
| `tui/` | Textual dashboard |
| `utils/` | Models, exceptions, compression, encryption, logging |

Imports are flat (`from core.profiles import …`) — `src/` is on `PYTHONPATH` via `pyproject.toml`.
