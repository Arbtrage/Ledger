# Deploy

Distribution and runtime assets — kept out of the repo root to reduce clutter.

| Path | Purpose |
|---|---|
| `docker/` | Container image (`Dockerfile`) |
| `packaging/` | Homebrew formula, WinGet manifest |
| `docker-compose.test.yml` | Integration test databases (MySQL, PostgreSQL, MongoDB) |

```bash
# Start test databases
docker compose -f deploy/docker-compose.test.yml up -d

# Stop
docker compose -f deploy/docker-compose.test.yml down -v
```
