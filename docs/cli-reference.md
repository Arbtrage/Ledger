# CLI Reference

| Command | Description |
|---|---|
| `ledger init` | Interactive setup wizard |
| `ledger backup <profile>` | Run backup for a profile |
| `ledger backup <profile> --dry-run` | Preview backup steps |
| `ledger restore [profile]` | Interactive restore explorer |
| `ledger backups` | List backup history |
| `ledger profiles` | List configured profiles |
| `ledger profiles remove <name>` | Delete a profile |
| `ledger schedule` | Cron scheduling (scaffold) |
| `ledger dashboard` | Textual terminal dashboard |
| `ledger --version` | Show version |

## Global flags

| Flag | Env var | Default |
|---|---|---|
| `--log-level` | `LEDGER_LOG_LEVEL` | `INFO` |
| `--log-json` | `LEDGER_LOG_JSON` | `false` |
