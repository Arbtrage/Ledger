# Release Strategy

How Ledger versions are cut, tested, published, and announced.

## Release cadence

| Type | Frequency | Trigger |
|---|---|---|
| **Patch** | As needed | Security fixes, critical bugs |
| **Minor** | Every 2–4 weeks during active development | Completed roadmap phase |
| **Major** | Rare | Breaking changes (post 1.0) |

## Release branches

```
main ─────────────────────────────────────► stable releases (tagged)
  │
  └── develop ──► feature PRs merge here first
```

1. Feature PRs merge into `develop`
2. When a phase/milestone is complete, `develop` merges to `main`
3. Maintainer cuts release from `main`

Hotfixes branch from `main` as `fix/*`, merge back to both `main` and `develop`.

## Release checklist

### Pre-release

- [ ] All CI checks green on `main`
- [ ] Roadmap milestone tasks marked complete in [ROADMAP.md](ROADMAP.md)
- [ ] `CHANGELOG.md`: move `[Unreleased]` items to `[X.Y.Z] - YYYY-MM-DD`
- [ ] Update `VERSION` and `pyproject.toml` version field
- [ ] Integration tests pass against Docker Compose services
- [ ] No open security advisories

### Cut release

```bash
git checkout main && git pull
echo "0.2.0" > VERSION
# Update pyproject.toml version
git add VERSION pyproject.toml CHANGELOG.md docs/ROADMAP.md
git commit -m "chore: release v0.2.0"
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin main --tags
```

### Automated pipeline (`.github/workflows/release.yml`)

Triggered on `v*.*.*` tag push:

1. **Validate tag** — tag must match `VERSION` file
2. **Test** — run unit test suite
3. **Build** — `python -m build` → sdist + wheel
4. **GitHub Release** — attach artifacts, changelog body
5. **PyPI publish** — via trusted publishing (OIDC) when configured

### Post-release

- [ ] Verify GitHub Release page has correct notes and artifacts
- [ ] Verify `pip install ledger==X.Y.Z` works (after PyPI publish enabled)
- [ ] Add new empty `## [Unreleased]` section to `CHANGELOG.md`
- [ ] Announce in release notes / project channels

## Pre-releases

Alpha/beta/RC versions use prerelease tags:

```bash
git tag -a v0.3.0-beta.1 -m "Beta: cloud storage"
```

GitHub Release workflow sets `prerelease: true` when the tag contains `-`.

## PyPI publishing

Publishing uses [trusted publishing](https://docs.pypi.org/trusted-publishers/) (OIDC) — no long-lived API tokens in secrets.

Setup (one-time):

1. Register `ledger` on PyPI
2. Add GitHub as trusted publisher (repo: `ledger-org/ledger`, workflow: `release.yml`)
3. Uncomment `publish-pypi` job steps in `.github/workflows/release.yml`

## Rollback

PyPI packages **cannot be permanently deleted** (only yanked). To rollback:

1. Yank the bad version on PyPI: `pip yank ledger==X.Y.Z --reason "..."`
2. Cut a patch release with the fix: `vX.Y.Z+1`
3. Update GitHub Release with rollback notice

## Artifact retention

| Artifact | Location | Retention |
|---|---|---|
| sdist + wheel | GitHub Release | Permanent |
| CI build artifacts | GitHub Actions | 90 days |
| Coverage reports | Codecov | Per Codecov policy |
