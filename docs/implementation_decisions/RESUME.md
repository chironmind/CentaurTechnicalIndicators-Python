# RESUME — CentaurTechnicalIndicators-Python v1.3.0 release

> Last updated: **2026-06-20**. Authoritative plan = `PLAN.md` (implementation-plan template).
> This file = current state + next actions for a cold start. Read this first.

## TL;DR

**All slices implemented. S7 merged; S11 + S10 in review — the release is fully prepped.** `main`
is at `cf040b7`. The only remaining actions are the maintainer's: **merge #42 (decision docs +
knowledge base) → merge #43 (release cut) → push the `v1.3.0` tag** (tag-triggered CI publishes to
PyPI). **The work history is preserved** under `docs/implementation_decisions/` (this file, the
plan, and the slice briefs) — superseding the original "delete the scratch" step; nothing is
removed.

## Merged on `main`

S0 fmt (#31) · S1 dep `1.3.0` (#32) · S2 favorable-move (#38) · S3 regressions + carryover `Fixed` (#39)
· S4 README/docstrings (#40) · S5 aliases (#36) · S6 metadata (#33) · S7 stubs/`__version__` (#41) ·
S8 CI-fmt (#34) · S9 `docs/2.0.0.md` (#35). Plus #37 (AGENTS.md authoritative + `CLAUDE.md`).

`[Unreleased]` was fully assembled; PR #43 promotes it to `## [1.3.0] - 2026-06-20` and bumps
`[package] version` `1.2.2`→`1.3.0` (confirmed `cti.__version__ == "1.3.0"`).

## In review

- **S7 — PR #41** (`feat/mixed-layout-stubs`): mixed package layout (`python-source`), hand-authored
  `__init__.py`, `__version__` via `importlib.metadata`, `py.typed` + `.pyi` stubs for the full
  surface (97 fns, generated from binding signatures + cross-checked against runtime, exact match),
  stale `python/` `.so` removed, `docs/` excluded from sdist. Verified end-to-end: `__version__`
  resolves (`1.2.2` → `1.3.0` at the cut), `__all__`/`__doc__`/nested API intact, wheel bundles the
  stubs, sdist has 0 `docs/` entries, 112 pytest passed, fmt clean.

## Remaining (order swapped — S11 before S10)

Decided 2026-06-20: **S11 runs before S10** so the 1.3.0 tag contains the decision docs. Both briefs
are written (`S11_BRIEF.md`, `S10_BRIEF.md`).

- **S11 — docs consolidation** *(brief ready)*. Needs S7 merged. Create `docs/DECISIONS-1.3.0.md` +
  a pointer from `docs/REPO_MAP.md` to it and `2.0.0.md`. CHANGELOG-exempt. Does **not** remove the
  scratch (still needed during S10).
- **S10 — release cut** *(brief ready)*. Needs S7 **and** S11 merged. Bump `[package] version`
  `1.2.2`→`1.3.0` (drives the wheel version **and** `cti.__version__`), promote
  `[Unreleased]`→`[1.3.0] - <date>`, final gates, **confirm `cti.__version__ == "1.3.0"`**, then
  **hand the `v1.3.0` tag to J** (tag-triggered CI builds wheels + sdist and `uv publish`es to PyPI —
  irreversible/outward-facing). Final step after publish: remove the untracked scratch.

## Deferred (not in 1.3.0)

- `pyproject.toml` author/maintainer **email** placeholder — intentionally retained (no-PII); fix in
  1.3.1.
- The 2.0 backlog lives in `docs/2.0.0.md` (alias remap, TSI arg-order, deprecated fns, unreachable
  enum variants).

## Worktrees / branches

Clean: single worktree on `main`; all spent feature branches pruned. The current S7 work is on
branch `feat/mixed-layout-stubs` (primary checkout). Untracked scratch (`PLAN.md`, `*_BRIEF.md`,
`RESUME.md`) survives checkouts — leave until S11.

## Cold-start checklist

1. `git fetch origin`; if #41 merged → `git checkout main && git pull --ff-only`.
2. Run **S11** (`S11_BRIEF.md`) — decision docs; merge it first so the tag will contain them.
3. Then **S10** (`S10_BRIEF.md`) — the cut; recommend the primary checkout. Hand the `v1.3.0` tag to
   J (the publish is outward-facing). S10's final step removes the scratch.

## Standing environment facts

- `centaur_technical_indicators` 1.3.0 published + cached. Mixed layout in effect after #41.
- Gates: `maturin develop`, `python -m pytest` (112 passed), `cargo fmt --all -- --check` (a CI gate).
- Briefs follow `~/Projects/TEMPLATE-brief.md`; `PLAN.md` follows `~/Projects/TEMPLATE-implementation-plan.md`.
