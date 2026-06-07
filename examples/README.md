# Examples

Sample configs you can copy when setting up Ledger.

| File | Use |
|---|---|
| [postgres-prod.yaml](postgres-prod.yaml) | Profile for PostgreSQL + S3 |
| [ledger.example.yaml](ledger.example.yaml) | File-based config template (CI/CD) |
| [cron-nightly.sh](cron-nightly.sh) | Cron wrapper for nightly backups |

```bash
cp postgres-prod.yaml ~/.ledger/profiles/postgres-prod.yaml
# set LEDGER_DB_PASSWORD, then:
ledger backup postgres-prod
```
