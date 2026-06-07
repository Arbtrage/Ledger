# Deployment

Run Ledger on a backup host, in CI, or as a scheduled service.

## One-shot cron

The simplest production setup — install Ledger on a host with database network access:

```bash
pipx install ledger
ledger init    # once, creates ~/.ledger/profiles/
```

```cron
# /etc/cron.d/ledger-backup
0 2 * * * ledger backup postgres-prod >> /var/log/ledger/cron.log 2>&1
```

## systemd service

For the built-in scheduler daemon:

```ini
# /etc/systemd/system/ledger.service
[Unit]
Description=Ledger backup scheduler
After=network-online.target

[Service]
Type=simple
User=ledger
EnvironmentFile=/etc/ledger/env
ExecStart=/usr/local/bin/ledger schedule daemon
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now ledger
```

## Docker

```bash
docker run --rm \
  -v ledger-data:/var/lib/ledger \
  -e LEDGER_DB_PASSWORD \
  ghcr.io/ledger-org/ledger \
  backup postgres-prod
```

## Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: ledger-postgres-nightly
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: ledger
              image: ghcr.io/ledger-org/ledger:latest
              command: ["ledger", "backup", "postgres-prod"]
              envFrom:
                - secretRef:
                    name: ledger-secrets
```

## Security checklist

- [ ] Database credentials from a secret manager, not plaintext files
- [ ] `LEDGER_ENCRYPT_BACKUPS=true` for cloud-stored backups
- [ ] S3 bucket has block-public-access enabled
- [ ] Backup IAM role has write-only permissions on the backup prefix
- [ ] Ledger runs as a non-root user
- [ ] Logs do not contain connection strings or passwords

## Notifications

```bash
export LEDGER_SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
ledger backup postgres-prod
```

Slack notifications fire on backup success and failure.
