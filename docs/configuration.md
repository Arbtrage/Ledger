# Configuration

## Home directory

Default: `~/.ledger/` (override with `LEDGER_HOME`).

## Environment variables

All use the `LEDGER_` prefix. See `.env.example` for the full list.

Secrets (passwords, API keys) must come from environment variables or keyring — never from profile YAML files.

## Legacy project config

For CI/CD or monorepo use, `examples/ledger.example.yaml` and `.env` remain supported alongside profiles.
