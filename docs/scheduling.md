# Scheduling

Run unattended backups with Ledger's built-in scheduler.

```bash
ledger schedule add \
  --job-id nightly \
  --cron "0 2 * * *" \
  --profile postgres-prod

ledger schedule list
ledger schedule daemon    # blocking — run under systemd or supervisor
```

Jobs persist across restarts in `~/.ledger/scheduler_jobs.sqlite`.

!!! note "Coming soon"
    The scheduler daemon is under active development. Use system cron as an alternative today — see [Deployment](deployment.md).

## Cron alternative

Until the daemon ships, use system cron:

```bash
0 2 * * * ledger backup postgres-prod >> ~/.ledger/logs/cron.log 2>&1
```

See [examples/cron-nightly.sh](https://github.com/ledger-org/ledger/blob/main/examples/cron-nightly.sh).
