# Quick Start

## Install

=== "macOS (Homebrew)"

    ```bash
    brew install ledger-org/tap/ledger
    ```

=== "Linux (pipx)"

    ```bash
    pipx install ledger
    ```

=== "Windows (winget)"

    ```powershell
    winget install Ledger.Ledger
    ```

=== "From source"

    ```bash
    git clone https://github.com/ledger-org/ledger.git
    cd ledger
    pip install -e ".[dev]"
    ```

## Initialize

```bash
ledger init
```

Interactive wizard:

```text
╭──────────────────────────╮
│ Ledger                   │
│ Setup Wizard             │
╰──────────────────────────╯

Profile name? postgres-prod
Database type? PostgreSQL
Host? localhost
...
```

Creates `~/.ledger/profiles/postgres-prod.yaml`.

## First backup

```bash
ledger backup postgres-prod
```

## Explore

```bash
ledger profiles    # list profiles
ledger backups     # backup history
ledger restore     # interactive restore picker
ledger dashboard   # Textual TUI
```
