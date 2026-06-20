---
type: brief
id: S11
title: "Consolidate 1.3.0 decisions into docs/ (runs BEFORE the cut)"
status: ready
effort: medium
wave: Final
depends_on: ["S7"]
touches:
  - docs/DECISIONS-1.3.0.md
  - docs/REPO_MAP.md
forbidden:
  - "Cargo.toml [package] version  (S10 owns the bump)"
  - "CHANGELOG.md  (S10 promotes [Unreleased]; do not touch)"
  - "the untracked scratch (PLAN.md / RESUME.md / *_BRIEF.md)  (still needed during S10 — removed at the END of S10, not here)"
branch: "docs/decisions-1.3.0"
pr_target: "main"
related:
  - "[[PLAN]]"
  - "[[docs/2.0.0]]"
decisive_test: "A1"
created: 2026-06-20
tags: [brief]
---

# S11 — Consolidate 1.3.0 decisions into docs/ (runs BEFORE the cut)

> **Self-contained — except** this batch's whole job is to harvest the release's decisions, so
> reading `PLAN.md` (its *Why*, Appendices, and Running log) **is** the task; treat it as the source.
> Repo conventions (branch/commit/PR, gates, stop-and-report) live in `AGENTS.md` / `CLAUDE.md`.
> **Done = the acceptance checks below pass.** Stop and report if blocked.

## Mission

Create `docs/DECISIONS-1.3.0.md` capturing the durable decisions and rationale from the 1.3.0 release
so the "why" survives after the scratch files are deleted, and add a pointer from `docs/REPO_MAP.md`
to it and to `docs/2.0.0.md`. **Internal docs only — nothing user-facing, nothing shipped** (`docs/`
is excluded from the sdist by S7's `[tool.maturin] exclude`, and never enters the wheel).

## Context

- **Order swap (deliberate):** this runs **before S10**, not after, so the **1.3.0 tag contains the
  decision docs**. S10 (the cut) `depends_on` this batch.
- Source material is `PLAN.md` at repo root (untracked scratch) — its *Why this work*, the Appendices
  (favorable-move semantics, the `__init__.py` body, target changelog, the S4 README inventory), and
  the Running log (which records the audit findings, the Codex catches on #40, and the resolved
  sub-decisions). Synthesize; do not copy wholesale.
- **CHANGELOG-exempt.** Like S0, this batch is internal/non-user-facing and is the second of the two
  sessions exempt from the "every change gets a `CHANGELOG.md` entry" rule. Record the rationale in
  the PR description; do **not** edit `CHANGELOG.md`.

## Prerequisites (confirm; do not perform here)

- **S7 merged** (the packaging story is final): on `main`,
  `python -c "import centaur_technical_indicators as c; print(c.__version__)"` resolves (not
  `0.0.0+unknown`), and `python/centaur_technical_indicators/__init__.py` + `*.pyi` exist. If not,
  stop — the `__version__`/mixed-layout decision isn't final yet.
- `docs/` exists and holds `REPO_MAP.md` + `2.0.0.md` (from S9).

## Changes (in order)

1. **Create `docs/DECISIONS-1.3.0.md`.** A concise decision record (not a tutorial). Cover, each with
   a one-line *why*:
   - **Scope:** what shipped in 1.3.0 (favorable-move bindings; inherited-fix regression tests; README
     accuracy + docstring `TypeError` fixes; string-alias docs/pins; metadata; CI fmt gate; type
     stubs + `py.typed` + `__version__` + mixed layout; `docs/2.0.0.md`). The **`basic_indicators`
     out-of-scope** decision (statistical primitives already in Python's `statistics`/`math`).
   - **Gate & semantics:** 1.3.0 was already published upstream; favorable-move semantics (inclusive
     `[index+1, index+period]`, signed); the inherited-fix inventory (index-0 extrema,
     retained-after-monotonic-run, all-NaN no-panic for aroon/stochastic, cauchy IQR hardening reached
     only via `deviation_model="cauchy"`).
   - **DX / packaging:** why `__version__` uses the mixed layout + `importlib.metadata` (the original
     `env!` value does not survive maturin's `import *`); the stale `python/` cleanup; `__all__` is
     PyO3-auto-populated (verification-only); the `.pyi` stubs were **generated from the binding
     signatures and cross-checked against the runtime**.
   - **Quality:** the S0 `cargo fmt` baseline and why; the indicator-count recount (~55 distinct →
     "50+"); the docstring keyword `TypeError`s fixed in S4; **the Codex catches on #40** — the six
     `chart_trends` `See:` links were **deferred** (target docs pages 404, unpublished), and
     `ulcer_index` has **both** `single`+`bulk` (only `volatility_system` is bulk-only); **and on #41
     (S7)** — the `.pyi` stubs advertised submodule import paths that failed at runtime, fixed by
     registering each submodule in `sys.modules` under its qualified name (guarded by
     `tests/test_package_layout.py`).
   - **2.0 deferrals:** one-line pointer to `docs/2.0.0.md`.
   - **Open sub-decisions + resolutions:** new disambiguating aliases — **no** (document/pin only);
     `cargo clippy -D warnings` in CI — **parked** (needs maintainer approval).
   - **Pending input:** the author/maintainer **email** placeholder is intentionally retained for
     1.3.0 (no-PII); fix in 1.3.1.
2. **Pointer in `docs/REPO_MAP.md`.** Add a short "Release decision records" note (sensible location —
   near the top map or a dedicated short section) linking `DECISIONS-1.3.0.md` and `2.0.0.md` so they
   are discoverable.

## Acceptance tests (named; all must pass)

- **A1 (decisive)** — `docs/DECISIONS-1.3.0.md` exists and covers all seven areas above (scope incl.
  `basic_indicators`; gate+semantics+inherited-fix inventory; DX/packaging `__version__` rationale;
  quality incl. the #40 + #41 Codex catches; 2.0 pointer; open sub-decisions; deferred email). The output
  is a *document*, so there is no test fn; mechanical proxy = `grep -c '^## ' docs/DECISIONS-1.3.0.md`
  ≥ 7 and the file is non-empty, with full coverage confirmed by reviewer inspection.
- **A2** — `docs/REPO_MAP.md` links both `DECISIONS-1.3.0.md` and `2.0.0.md`.
- **A3 (suite)** — pre-PR gates pass as confirmation (no code changed): `maturin develop`,
  `python -m pytest`, `cargo fmt --all -- --check`. `docs/` stays out of the sdist (`maturin sdist`
  → 0 `docs/` entries). No new dependency.

## Out of scope (do not touch)

- **Do NOT remove the scratch** (`PLAN.md`, `RESUME.md`, `*_BRIEF.md`) — S10 still reads them during
  the cut; their removal is the **final** step of S10.
- `Cargo.toml` version (S10) and `CHANGELOG.md` (S10 promotes it). The author email (1.3.1).
- Anything that would ship in the wheel/sdist (this is repo-only docs).

## Definition of done

- [ ] A1–A2 green; A3 gates/confirmation green.
- [ ] Only `docs/DECISIONS-1.3.0.md` (new) + `docs/REPO_MAP.md` changed.
- [ ] **No** `CHANGELOG.md` entry (exempt; rationale in the PR description).
- [ ] PR opened against `main`.

## Report (per AGENTS.md)

Summary · Scope · Compatibility (none — internal docs) · Validation (gate output; `maturin sdist`
0 `docs/` entries) · Changelog (N/A — exempt, with rationale) — plus A1/A2 results and anything flagged.
