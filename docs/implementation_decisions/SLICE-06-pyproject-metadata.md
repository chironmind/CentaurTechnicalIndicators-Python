# S6 — Package Metadata Cleanup (standalone session brief)

> Self-contained. You do **not** need to read `PLAN.md`. **The author/maintainer email is
> intentionally NOT touched.** Crate-version-agnostic.

## Mission

Fix two pieces of `pyproject.toml` metadata drift — the Documentation URL and the Python
classifiers. Nothing else.

## Repo facts

- PyO3/maturin project. `.venv` has `maturin` + `pytest`. Gates: `maturin develop`,
  `python -m pytest`, `cargo fmt --check`. Own worktree + own venv.

## Steps (edit the `[project]` table of `pyproject.toml` only)

1. **Documentation URL:** `[project.urls] "Documentation"` currently points at the GitHub
   `/wiki`. Repoint it to the ReadTheDocs root used by the README docs badge:
   `https://centaurtechnicalindicators-python.readthedocs.io/en/latest/`
2. **Classifiers:** add the per-minor Python classifiers (keep the existing generic
   `"Programming Language :: Python :: 3"`):
   ```
   "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: 3.11",
   "Programming Language :: Python :: 3.12",
   "Programming Language :: Python :: 3.13",
   "Programming Language :: Python :: 3.14",
   ```
   (These match the test matrix in `.github/workflows/python-package.yml`.)
3. Run the gates, add CHANGELOG, open PR.

## Hands off (other sessions own these — do not touch)

- The `description` string (ecosystem naming + "50+" belong to a different session).
- The `[tool.maturin]` table (a different session adds `python-source` / `exclude`).
- The author/maintainer `email` placeholders — knowingly retained for 1.3.0.
- `__all__` needs **no** change — PyO3 already auto-populates `cti.__all__` with the nine
  submodules. You may confirm with
  `python -c "import centaur_technical_indicators as c; print(c.__all__)"`, but there's nothing
  to add.

## CHANGELOG (under the existing `## [Unreleased]`)

```
### Fixed
- Incorrect `Documentation` URL in package metadata (pointed at the GitHub wiki).

### Changed
- Expanded PyPI classifiers to declare Python 3.10–3.14.
```

## Commit / PR

- Branch: `git checkout -b chore/pyproject-metadata`. Stage `pyproject.toml`, `CHANGELOG.md`.
- Commit prefix `chore:`; end with
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- PR body: **Summary** / **Compatibility** (none) / **Validation** / **Changelog**.

## Done criteria

- Documentation URL = ReadTheDocs root; classifiers list 3.10–3.14 plus the generic `:: 3`.
- `description`, `[tool.maturin]`, and emails untouched. Gates green. PR opened.

## Effort: **medium**
