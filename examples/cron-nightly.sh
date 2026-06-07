#!/usr/bin/env bash
# Nightly backup via cron — ledger backup <profile>
set -euo pipefail
export LEDGER_HOME="${LEDGER_HOME:-$HOME/.ledger}"
/usr/local/bin/ledger backup postgres-prod >> "$LEDGER_HOME/logs/cron.log" 2>&1
