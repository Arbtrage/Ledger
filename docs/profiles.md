# Profiles

A **profile** is a named backup configuration — database connection, storage target, compression, and encryption settings. Profiles are how you avoid passing flags every time you run a backup.

## Create a profile

```bash
ledger init
```

Or copy an example:

```bash
cp examples/postgres-prod.yaml ~/.ledger/profiles/postgres-prod.yaml
```

## Use a profile

```bash
ledger backup postgres-prod
ledger backup staging-mysql --dry-run
ledger restore postgres-prod
```

## Manage profiles

```bash
ledger profiles                  # list all profiles
ledger profiles remove old-staging
```

## Profile file format

Stored at `~/.ledger/profiles/<name>.yaml`:

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
  prefix: prod/
compression: gzip
encrypt: true
```

Passwords are **not** stored here. Set `LEDGER_DB_PASSWORD` in your environment or use `keyring`.

## Multiple environments

```text
~/.ledger/profiles/
├── postgres-prod.yaml
├── postgres-staging.yaml
├── mysql-analytics.yaml
└── mongo-dev.yaml
```

```bash
ledger backup postgres-prod
ledger backup postgres-staging
```
