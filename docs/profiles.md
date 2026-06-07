# Profiles

Profiles are named database + storage configurations stored in `~/.ledger/profiles/`.

## Layout

```text
~/.ledger/
├── profiles/          # postgres-prod.yaml, mongo-dev.yaml, ...
├── storage/           # local backup artifacts
├── history.db         # backup explorer data
└── logs/              # structured logs
```

## Commands

```bash
ledger init                    # create a profile (wizard)
ledger profiles                # list all profiles
ledger profiles remove <name>  # delete a profile
ledger backup <profile>        # run backup
ledger backup <profile> --dry-run  # preview steps
```

## Example profile

```yaml
database:
  db_type: postgres
  host: localhost
  port: 5432
  database: myapp
  username: postgres
storage:
  storage_type: s3
  bucket: my-backups
  region: us-east-1
compression: gzip
encrypt: false
```

Passwords are **never** stored in profile files — use `LEDGER_DB_PASSWORD` or keyring.
