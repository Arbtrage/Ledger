# Backup & Restore

## Backup

```bash
ledger backup postgres-prod
```

### Dry run

```bash
ledger backup postgres-prod --dry-run
```

Shows exactly what will happen — no I/O.

### Verification

Backups are verified by default after write:

```text
✓ Backup Created
Verifying...
✓ Backup Valid
```

Disable with `--no-verify`.

## Restore

```bash
ledger restore
```

Interactive picker — select profile, then backup from history table.

```bash
ledger restore postgres-prod --backup abc12345
```

## Backup explorer

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
