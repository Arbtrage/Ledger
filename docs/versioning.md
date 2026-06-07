# Versioning Strategy

*Maintainers only.* How the Ledger CLI is versioned and released.

Ledger follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

| Segment | When to bump |
|---|---|
| **MAJOR** | Breaking CLI flags, config schema changes, removed adapters |
| **MINOR** | New adapter, new storage backend, new feature (backward compatible) |
| **PATCH** | Bug fixes, security patches, documentation-only releases |
| **PRERELEASE** | `alpha`, `beta`, `rc1` — pre-stable releases |

## Current version

The canonical version lives in two places (kept in sync at release time):

1. `VERSION` file at repo root
2. `version` field in `pyproject.toml`

Runtime version is read from installed package metadata (`importlib.metadata`).

## Pre-1.0 policy

While below `1.0.0`, minor versions may include breaking changes. Document all breaking changes clearly in `CHANGELOG.md`. After `1.0.0`, breaking changes require a major bump.

## Version bump workflow

Releases are cut by maintainers — **do not bump version in feature PRs**.

```bash
# 1. Ensure CHANGELOG.md has an [X.Y.Z] section with today's date
# 2. Update VERSION and pyproject.toml
echo "0.2.0" > VERSION
# Edit pyproject.toml: version = "0.2.0"

# 3. Commit
git add VERSION pyproject.toml CHANGELOG.md
git commit -m "chore: release v0.2.0"

# 4. Tag (must match VERSION exactly)
git tag -a v0.2.0 -m "v0.2.0"

# 5. Push
git push origin main --tags
```

The [release workflow](.github/workflows/release.yml) validates that the git tag matches `VERSION`, runs tests, builds the package, and creates a GitHub Release.

## Changelog conventions

Follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/):

- `Added` — new features
- `Changed` — changes to existing behavior
- `Deprecated` — soon-to-be removed
- `Removed` — removed features
- `Fixed` — bug fixes
- `Security` — vulnerability fixes

All unreleased work goes under `## [Unreleased]` at the top of `CHANGELOG.md`.

## Dependency versioning

| File | Strategy |
|---|---|
| `pyproject.toml` | Loose bounds (`>=X.Y,<NEXT_MAJOR`) for library consumers |
| `requirements.txt` | Editable install with `[dev]` extras for local dev |
| CI | Installs from `pyproject.toml` — no separate lock file yet |

A `requirements-lock.txt` (via `pip-compile`) may be added before `1.0.0` for reproducible CI builds.

## API stability guarantees

| Surface | Stability |
|---|---|
| CLI flags (`ledger backup run --db ...`) | Stable after 1.0.0 |
| `AbstractDBAdapter` interface | Stable — extend, don't break |
| `AbstractStorageBackend` interface | Stable — extend, don't break |
| YAML config schema | Stable after 1.0.0; deprecate with warnings first |
| Python internal modules | No stability guarantee — use CLI or public ABCs |
