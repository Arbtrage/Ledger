# Roadmap

**Vision:** The Docker / kubectl / gh of database backups.

**Current status:** UX scaffold complete (init wizard, profiles, Rich UI, Textual dashboard). Backup pipeline implementation next.

---

## Phase 1 — UX Foundation (Week 1–2) ✅

| Task | Status |
|---|---|
| Profile system (`~/.ledger/profiles/`) | ✅ Done |
| `ledger init` interactive wizard | ✅ Done |
| `ledger backup <profile>` command | ✅ Scaffold |
| Rich banner, tables, progress stubs | ✅ Done |
| Textual dashboard scaffold | ✅ Done |
| `ledger backups` explorer | ✅ Scaffold |
| `ledger restore` interactive picker | ✅ Scaffold |
| Dry-run + verification stubs | ✅ Done |
| MkDocs Material docs site | ✅ Done |
| Homebrew / WinGet / Docker scaffolds | ✅ Done |

**Exit criteria:** `ledger init` → `ledger backup postgres-prod --dry-run` shows a polished plan.

---

## Phase 2 — Backup pipeline (Week 3)

| Task | Status |
|---|---|
| PostgreSQL adapter (`pg_dump` streaming) | ⬜ Pending |
| MySQL adapter (`mysqldump`) | ⬜ Pending |
| MongoDB + SQLite adapters | ⬜ Pending |
| Rich live progress (speed, ETA, compression stats) | ⬜ Pending |
| `history.db` write on completion | ⬜ Pending |
| Unit tests (mocked subprocess) | ⬜ Pending |

**Exit criteria:** `ledger backup postgres-prod` produces a verified `.sql.gz` with live progress.

---

## Phase 3 — Cloud + scheduling (Week 4–5)

| Task | Status |
|---|---|
| S3 / GCS / Azure upload with progress | ⬜ Pending |
| `ledger schedule --profile` cron daemon | ⬜ Pending |
| AES-256-GCM encryption layer | ⬜ Pending |
| Post-backup verification (checksum + restore test) | ⬜ Pending |

---

## Phase 4 — Ship it (Week 6)

| Task | Status |
|---|---|
| `pipx install ledger` on PyPI | ⬜ Pending |
| Homebrew tap publish | ⬜ Pending |
| Product Hunt GIFs (init, backup, restore, dashboard) | ⬜ Pending |
| Landing page (docs / GitHub Pages) | ⬜ Pending |
| Integration tests in CI | ⬜ Pending |
| Coverage ≥ 80% | ⬜ Pending |

---

## Premium (post v1.0)

| Feature | Notes |
|---|---|
| Cloud dashboard | SaaS |
| Team backups | Multi-user profiles |
| Monitoring + alerting | Slack, PagerDuty |
| Backup analytics | Size trends, savings |
| Multi-region storage | DR |

## Free tier

Unlimited local backups — free forever.

## Milestones

| Version | Highlights |
|---|---|
| `0.1.0` | Scaffold, profiles, Rich/Textual UI |
| `0.2.0` | Working backup pipeline + progress |
| `0.3.0` | Cloud storage + scheduling + verification |
| `1.0.0` | PyPI, Homebrew, Product Hunt launch |
