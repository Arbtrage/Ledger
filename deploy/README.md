# Deploy assets (maintainers)

Distribution and integration-test infrastructure for the Ledger CLI.

| Path | Purpose |
|---|---|
| `docker/Dockerfile` | Official container image |
| `packaging/homebrew/` | Homebrew formula |
| `packaging/winget/` | Windows package manifest |
| `docker-compose.test.yml` | Test databases for CI |

```bash
docker compose -f deploy/docker-compose.test.yml up -d
docker compose -f deploy/docker-compose.test.yml down -v
```

For running Ledger in production, see the user-facing [Deployment guide](../docs/deployment.md).
