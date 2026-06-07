# CLI Reference

```bash
ledger [OPTIONS] COMMAND [ARGS]...
```

## Commands

| Command | Description |
|---|---|
| `ledger init` | Interactive setup wizard — creates a profile |
| `ledger backup <profile>` | Run a backup for a saved profile |
| `ledger backup <profile> --dry-run` | Preview steps without executing |
| `ledger restore [profile]` | Interactive restore explorer |
| `ledger backups` | List backup history |
| `ledger profiles` | List configured profiles |
| `ledger profiles remove <name>` | Delete a profile |
| `ledger schedule` | Manage cron-style backup jobs |
| `ledger dashboard` | Open the Textual terminal dashboard |
| `ledger --version` | Print version and exit |

## `ledger backup`

```bash
ledger backup <profile> [OPTIONS]
```

| Option | Description | Default |
|---|---|---|
| `--type` | `full`, `incremental`, `differential` | `full` |
| `--dry-run` | Show plan, no I/O | off |
| `--verify/--no-verify` | Verify after backup | `--verify` |

## `ledger init`

```bash
ledger init [OPTIONS]
```

| Option | Description |
|---|---|
| `--name`, `-n` | Profile name (skip prompt) |
| `--yes`, `-y` | Accept defaults where possible |

## Global options

| Option | Env var | Default |
|---|---|---|
| `--log-level` | `LEDGER_LOG_LEVEL` | `INFO` |
| `--log-json` | `LEDGER_LOG_JSON` | `false` |
| `--version`, `-V` | — | — |

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Success |
| `1` | Error (missing profile, connection failure, etc.) |
