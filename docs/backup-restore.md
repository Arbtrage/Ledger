# Backup & Restore

## Run a backup

```bash
ledger backup postgres-prod
```

Ledger shows live progress: dump → compress → upload → verify.

### Dry run

See exactly what will happen — no database or storage I/O:

```bash
ledger backup postgres-prod --dry-run
```

```text
Dry run — postgres-prod

  1. Connect to postgres at localhost
  2. Run full backup of database 'myapp'
  3. Compress with gzip
  4. Upload to s3 bucket my-backups
  5. Record entry in ~/.ledger/history.db
  6. Verify backup integrity
```

### Verification

Backups are verified by default after write:

```text
✓ Backup Created
Verifying...
✓ Backup Valid
```

Skip with `--no-verify`.

## Restore

```bash
ledger restore
```

Interactive flow: pick a profile → see recent backups → select one to restore.

```bash
ledger restore postgres-prod --backup abc12345
```

## Browse backups

```bash
ledger backups
ledger backups --profile postgres-prod
```

```text
┏━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ ID     ┃ Profile       ┃ Date            ┃ Size   ┃ Status  ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ abc123 │ postgres-prod │ 2026-06-08 14:23│ 2.3 GB │ success │
└────────┴───────────────┴─────────────────┴────────┴─────────┘
```
