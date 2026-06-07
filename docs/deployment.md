# Deployment Guide

How to deploy and run Ledger in production environments.

> **Note:** This guide describes the target deployment model. Commands will become functional as implementation phases complete (see [ROADMAP.md](ROADMAP.md)).

## Installation methods

### pip (recommended)

```bash
pip install ledger
ledger --version
```

### Editable install (development)

```bash
git clone https://github.com/ledger-org/ledger.git
cd ledger
pip install -e ".[dev]"
```

### From GitHub Release artifact

```bash
pip install https://github.com/ledger-org/ledger/releases/download/v0.1.0/ledger-0.1.0-py3-none-any.whl
```

---

## Configuration

### Environment variables

Copy `.env.example` to `.env` and set values:

```bash
LEDGER_DB_TYPE=postgres
LEDGER_DB_HOST=db.internal
LEDGER_DB_NAME=production
LEDGER_DB_USER=backup_user
LEDGER_DB_PASSWORD=<from-secret-manager>
LEDGER_STORAGE_TYPE=s3
LEDGER_STORAGE_BUCKET=company-db-backups
LEDGER_STORAGE_REGION=us-east-1
LEDGER_ENCRYPT_BACKUPS=true
LEDGER_ENCRYPTION_KEY=<from-secret-manager>
```

### YAML config

```bash
ledger config init -o /etc/ledger/config.yaml
ledger config validate -c /etc/ledger/config.yaml
```

Passwords and API keys **must** come from environment variables — never from the YAML file.

---

## Deployment patterns

### 1. One-shot cron (simplest)

Add to crontab on a backup host with network access to the database:

```cron
# Nightly MySQL backup at 02:00 UTC
0 2 * * * /usr/local/bin/ledger backup run --db mysql --db-name myapp --storage s3 --bucket my-backups >> /var/log/ledger.log 2>&1
```

### 2. Built-in scheduler daemon

For multiple jobs or dynamic scheduling:

```bash
# Register jobs
ledger schedule add --job-id mysql-nightly --cron "0 2 * * *" --db mysql --db-name myapp --storage s3 --bucket my-backups
ledger schedule add --job-id pg-weekly --cron "0 3 * * 0" --db postgres --db-name analytics --storage s3 --bucket my-backups

# Run daemon (blocking)
ledger schedule daemon
```

#### systemd service

```ini
# /etc/systemd/system/ledger.service
[Unit]
Description=Ledger scheduler daemon
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ledger
Group=ledger
EnvironmentFile=/etc/ledger/env
ExecStart=/usr/local/bin/ledger schedule daemon
Restart=on-failure
RestartSec=30

# Security hardening
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/lib/ledger /var/log/ledger

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now ledger
sudo systemctl status ledger
```

### 3. Docker

```dockerfile
# Dockerfile (example — add when implementation is complete)
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-mysql-client postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir ledger

USER nobody
ENTRYPOINT ["ledger"]
CMD ["schedule", "daemon"]
```

```yaml
# docker-compose.yml (example)
services:
  ledger:
    image: ghcr.io/ledger-org/ledger:latest
    env_file: .env
    volumes:
      - ./config:/etc/ledger:ro
      - backup-data:/var/lib/ledger
    restart: unless-stopped

volumes:
  backup-data:
```

### 4. Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: ledger-mysql-nightly
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
              command:
                - ledger
                - backup
                - run
                - --db
                - mysql
                - --db-name
                - myapp
                - --storage
                - s3
                - --bucket
                - my-backups
              envFrom:
                - secretRef:
                    name: ledger-secrets
```

---

## Cloud storage credentials

| Provider | Credential method |
|---|---|
| **AWS S3** | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or IAM role |
| **GCS** | `GOOGLE_APPLICATION_CREDENTIALS` pointing to service account JSON |
| **Azure** | `AZURE_STORAGE_CONNECTION_STRING` or managed identity |

Prefer instance roles / workload identity over long-lived keys.

---

## Security checklist

- [ ] Database credentials from secret manager (not plaintext in config)
- [ ] `LEDGER_ENCRYPT_BACKUPS=true` for cloud-stored backups
- [ ] S3 bucket has block-public-access enabled
- [ ] Backup IAM role has minimum permissions (write-only to backup prefix)
- [ ] Scheduler runs as non-root user
- [ ] Log output does not contain connection strings or passwords
- [ ] Pre-signed download URLs use short TTL (≤ 1 hour)

---

## Monitoring

### Logs

```bash
# JSON logs for log aggregation (ELK, Datadog, etc.)
ledger --log-json --log-level INFO backup run ...
```

### Slack notifications

```bash
LEDGER_SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
```

Notifications fire on backup success and failure (Phase 4).

### Health checks

```bash
# Verify DB connectivity before backup window
ledger backup test-connection --db postgres --db-name myapp
```

---

## Restore procedure

```bash
# List available backups
ledger restore list-objects --backup s3://my-backups/myapp_full_20240608T142301Z.sql.gz

# Full restore
ledger restore run \
  --backup myapp_full_20240608T142301Z.sql.gz \
  --db mysql \
  --db-name myapp_restored \
  --storage s3 \
  --bucket my-backups

# Selective restore (tables)
ledger restore run \
  --backup myapp_full_20240608T142301Z.sql.gz \
  --db mysql \
  --db-name myapp \
  --table users \
  --table orders
```

Always test restores on a non-production database first.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `ConnectionError` | DB unreachable or wrong credentials | Run `test-connection`, check firewall |
| `StorageError` | Missing cloud credentials or bucket permissions | Verify IAM role / env vars |
| `BackupError: dump failed` | Native tool not installed | Install `mysqldump` / `pg_dump` on backup host |
| Scheduler jobs lost on restart | Job store not persistent | Ensure `scheduler_jobs.sqlite` path is writable |
| High memory usage | Buffering instead of streaming | Report bug — streaming should cap at ~8 MB |
