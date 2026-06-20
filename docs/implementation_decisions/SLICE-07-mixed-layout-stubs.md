---
type: brief
id: S7
title: "Mixed layout: .pyi stubs + py.typed + __version__ + remove stale dir"
status: ready
effort: xhigh
wave: 3
depends_on: ["S2"]
touches:
  - pyproject.toml
  - python/centaur_technical_indicators/__init__.py
  - python/centaur_technical_indicators/py.typed
  - python/centaur_technical_indicators/__init__.pyi
  - python/centaur_technical_indicators/*.pyi
  - .gitignore
  - CHANGELOG.md
forbidden:
  - "src/**  (no Rust/binding changes — packaging + stubs only)"
  - "pyproject.toml [project] table  (S4/S6 own description/urls/classifiers)"
  - "pyproject.toml author/maintainer email"
branch: "feat/mixed-layout-stubs"
pr_target: "main"
related:
  - "[[PLAN]]"
decisive_test: "A1"
created: 2026-06-20
tags: [brief]
---

# S7 — Mixed layout: .pyi stubs + py.typed + __version__ + remove stale dir

> **Self-contained.** Repo conventions live in `AGENTS.md` / `CLAUDE.md` and are
> assumed. **Run this as its own wave, after S2 (#38) has merged** — it needs the
> complete binding surface (incl. favorable-move) for the stubs, and it edits
> `pyproject.toml`, so do not run it concurrently with S4. **Done = the named
> acceptance tests pass.** Stop and report if anything blocks you.

## Mission

One structural change that resolves three problems together: ship type information (`.pyi` + `py.typed`),
make `__version__` actually reachable on the top-level package, and remove the stale `python/` artifact —
by adopting maturin's mixed layout with a hand-authored `__init__.py`. Public API unchanged.

## Context

- **Why `__version__` needs this.** `[tool.maturin]` currently sets only `features`; with no
  `python-source`, maturin auto-generates an `__init__.py` doing `from .<ext> import *`. `import *`
  does **not** propagate dunders, so the original `env!`-based `__version__` would silently be
  absent. The mixed layout + `importlib.metadata` fixes it.
- **Stale directory.** `python/centaur_technical_indicators/` already exists but is a stale, untracked
  artifact (a gitignored `.so` + `__pycache__`). It sits at exactly the path we want as the source
  root. Remove the stale `.so`; repurpose the directory.
- **Name-collision is resolved, not open.** maturin places the compiled extension as the submodule
  `centaur_technical_indicators.centaur_technical_indicators` (`<pkg>/<pkg>.so`), so a relative
  `from .centaur_technical_indicators import *` targets the **submodule**, not this package — no
  shadowing, no recursion. The extension needs no different internal name.
- The `__init__.py` body below was **proven end-to-end** in review (built, installed into a throwaway
  venv, imported; nested API, `__version__`, `__all__`, `__doc__` all verified). Use it verbatim.

## Prerequisites (confirm; do not perform here)

- S2 merged: `grep -c peak_favorable_move src/chart_trends.rs` ≥ 1 on `main`. If not, stop.
- The nine submodules (for stub coverage + `__all__`): `chart_trends`, `candle_indicators`,
  `correlation_indicators`, `momentum_indicators`, `moving_average`, `other_indicators`,
  `strength_indicators`, `trend_indicators`, `volatility_indicators`.

## Verify first (re-confirm at session start)

| Claim | How to check | Expected |
|-------|--------------|----------|
| stale dir is untracked | `git status --porcelain python/` ; `git ls-files python/` | nothing tracked under `python/` |
| `*.so` + `__pycache__` gitignored | `grep -nE '\*\.so|__pycache__' .gitignore` | both present |
| `__all__` auto-populated | after `maturin develop`: `python -c "import centaur_technical_indicators as c; print(sorted(c.__all__))"` | the nine submodules |
| maturin config docs | confirm `python-source` + sdist `exclude` key/format for the installed maturin (1.11.x) | matches step 1 |

## Changes (in order)

1. **`pyproject.toml` `[tool.maturin]` (sole owner of this table).** Add `python-source = "python"`,
   and exclude internal `docs/` from the sdist:
   ```toml
   python-source = "python"
   exclude = [{ path = "docs/**/*", format = "sdist" }]
   ```
   Keep the existing `features`. Touch nothing in `[project]`.
2. **Remove the stale extension** under `python/centaur_technical_indicators/` (the gitignored `.so`
   + `__pycache__`). Keep `*.so` / `__pycache__/` gitignored so the rebuilt artifact isn't committed.
3. **Author `python/centaur_technical_indicators/__init__.py`** — exactly:
   ```python
   from .centaur_technical_indicators import *
   from . import centaur_technical_indicators as _ext

   __doc__ = _ext.__doc__
   if hasattr(_ext, "__all__"):
       __all__ = list(_ext.__all__)

   from importlib.metadata import version as _version, PackageNotFoundError as _PNFE
   try:
       __version__ = _version("centaur_technical_indicators")
   except _PNFE:  # source tree without installed dist-info
       __version__ = "0.0.0+unknown"

   del _ext, _version, _PNFE
   ```
   Preserve `__doc__` and `__all__` (a naive `import *` + `__version__` would silently regress both).
4. **Add `python/centaur_technical_indicators/py.typed`** (empty PEP 561 marker).
5. **Author `.pyi` stubs over the complete surface.** `__init__.pyi` (top-level: `__version__: str`,
   `__all__`, and the flat `chart_trends` functions **including `peak_favorable_move` /
   `valley_favorable_move`**) plus one `<submodule>.pyi` per Rust submodule. Express the Rust-defined
   `single` / `bulk` levels as nested `class single:` / `class bulk:` namespaces. Files under
   `python-source` auto-bundle into the wheel — **no `[tool.maturin] include` needed.**
6. **Git-track the new files.** `__init__.py`, `py.typed`, and every `.pyi` are **not** covered by the
   `*.so` / `__pycache__` ignores — `git add` them explicitly; confirm none are ignored
   (`git check-ignore <file>` returns nothing).

## Acceptance tests (named; all must pass)

- **A1 (decisive)** — after `maturin develop`: `python -c "import centaur_technical_indicators as c;
  print(c.__version__)"` prints the installed dist version (currently `1.2.2` pre-release-cut; S10
  flips it to `1.3.0`), **not** `0.0.0+unknown`.
- **A2** — `c.__all__` equals the nine submodules; `c.__doc__` is non-empty; the nested API still
  works (e.g. `c.momentum_indicators.single.relative_strength_index`, `c.chart_trends.peak_favorable_move`).
- **A3** — a built wheel bundles the stubs: `maturin build` then unzip-list the wheel shows
  `__init__.py`, `py.typed`, and the `.pyi` files; `docs/` is absent from the **sdist**
  (`maturin sdist` → no `docs/`).
- **A4 (suite)** — pre-PR gates green: `maturin develop`, `python -m pytest` (public API unchanged),
  `cargo fmt --all -- --check`; no new dependency.

## Out of scope (do not touch)

- Any `src/*.rs` (no `m.add("__version__"…)`, no `m.add("__all__"…)` — both are handled in
  `__init__.py` / auto-populated). The `[project]` table (S4/S6) and the email. Tests.
- A `[tool.maturin] include` for stubs (unnecessary — `python-source` auto-bundles).

## Definition of done

- [ ] A1–A3 green; A4 gates green.
- [ ] New files git-tracked; stale `.so` removed; `*.so`/`__pycache__` still ignored.
- [ ] `[Unreleased]` updated (Added: stubs + py.typed + `__version__` + mixed layout; Changed:
      exclude internal `docs/` from sdist).
- [ ] PR opened against `main`.

## Report (per AGENTS.md)

Summary · Scope · Compatibility (public API unchanged — show the suite) · Validation (paste gate
output + A1 `__version__` value + A3 wheel/sdist listings) · Changelog — plus each acceptance test
with its result, and anything flagged.
