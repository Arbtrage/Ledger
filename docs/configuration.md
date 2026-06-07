# Configuration

Ledger stores your settings in `~/.ledger/`. You rarely need a config file — profiles and environment variables cover most use cases.

## Home directory

```text
~/.ledger/
├── profiles/       # one YAML file per profile
├── storage/        # local backup artifacts
├── history.db      # backup explorer
└── logs/
```

Override with `LEDGER_HOME`:

```bash
export LEDGER_HOME=/var/lib/ledger
```

## Environment variables

All use the `LEDGER_` prefix:

| Variable | Purpose |
|---|---|
| `LEDGER_LOG_LEVEL` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `LEDGER_LOG_JSON` | `true` for JSON logs (production) |
| `LEDGER_DB_PASSWORD` | Database password (never in profile YAML) |
| `LEDGER_STORAGE_BUCKET` | Default S3/GCS bucket |
| `LEDGER_SLACK_WEBHOOK_URL` | Notification webhook |

See [.env.example](https://github.com/ledger-org/ledger/blob/main/.env.example) for the full list.

## Secrets

Passwords, API keys, and encryption keys **must** come from environment variables or `keyring` — never from profile YAML files.

```bash
export LEDGER_DB_PASSWORD="$(cat /run/secrets/db_password)"
ledger backup postgres-prod
```

## File-based config (advanced)

For CI/CD pipelines, an example YAML template is available at `examples/ledger.example.yaml`. Profiles in `~/.ledger/profiles/` are the recommended approach for day-to-day use.
