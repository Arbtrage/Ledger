# Source

Application code lives here to keep the repository root clean.

| Package | Role |
|---|---|
| `cli/` | Typer commands (`init`, `backup`, `restore`, …) |
| `core/` | Orchestrator, profiles, history, scheduler, verification |
| `database/` | DBMS adapters (PostgreSQL, MySQL, MongoDB, SQLite) |
| `storage/` | Local and cloud storage backends |
| `ui/` | Rich terminal components |
| `tui/` | Textual dashboard |
| `utils/` | Models, exceptions, compression, encryption, logging |

Imports stay flat (`from core.profiles import …`) — `src/` is on `PYTHONPATH` via `pyproject.toml`.
