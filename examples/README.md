# Examples

| Example | Description |
|---|---|
| [postgres-prod.yaml](postgres-prod.yaml) | Sample profile for PostgreSQL + S3 |
| [ledger.example.yaml](ledger.example.yaml) | Legacy YAML config template |
| [cron-nightly.sh](cron-nightly.sh) | Cron wrapper for `ledger backup` |

```bash
cp postgres-prod.yaml ~/.ledger/profiles/postgres-prod.yaml
ledger backup postgres-prod
```
