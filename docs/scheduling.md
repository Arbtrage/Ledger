# Scheduling

```bash
ledger schedule add --job-id nightly --cron "0 2 * * *" --profile postgres-prod
ledger schedule list
ledger schedule daemon
```

Scheduler uses APScheduler with a persistent SQLite job store at `~/.ledger/scheduler_jobs.sqlite`.

> **Status:** Scaffold — implementation pending Phase 3.
