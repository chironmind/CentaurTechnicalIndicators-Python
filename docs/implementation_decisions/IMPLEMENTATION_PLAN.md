---
type: implementation-plan
title: "Release 1.3.0 — CentaurTechnicalIndicators-Python"
status: in-progress
baseline: "main @ 90816b3 (v1.2.2): dep `centaur_technical_indicators = 1.2.2`; `maturin develop` + `pytest` green (100 passed); `cargo fmt --check` failing on pre-existing committed drift (cleared by S0)"
integration_branch: "main — serial PRs (no dedicated release branch; each batch branches off fresh origin/main and merges back)"
related:
  - "[[AGENTS]]"
  - "[[RESUME]]"
  - "[[docs/REPO_MAP]]"
  - "[[docs/2.0.0]]"
created: 2026-06-18
updated: 2026-06-20
tags: [plan, release]
---

# Release 1.3.0 — CentaurTechnicalIndicators-Python

> v1.3.0 mirrors the new Rust 1.3.0 chart-trend functions and ships a batch of DX, documentation,
> and metadata improvements for `chironmind/CentaurTechnicalIndicators-Python`. The wrapper layer
> has **no calculation or wiring bugs** (audit-confirmed across all nine binding modules), so the
> substance is the upstream mirror plus DX / docs / packaging — calculation fixes live in the Rust
> crate, not here. The whole release is a **semver-clean minor**: additive + docs + metadata only.
> The first batch (**S0**) establishes a `cargo fmt` baseline so the formatting gate can hold for
> every later session; the final batches consolidate the durable decisions into `docs/` (**S11**,
> runs before the cut so the tag contains them) and then cut and publish the release (**S10**, runs
> last and removes the spent scratch as its final step). One plan = the 1.3.0 release, broken into
> small, separately-mergeable batches, one per fresh Claude Code session.

## Why this work (context)

The binding is correct but its surface has drifted from the Rust crate and from its own docs, and
Rust 1.3.0 adds two chart-trend functions plus a set of degenerate-input fixes that are observable
at the Python layer. This release closes that gap and pays down DX/packaging debt. The shape of the
solution is a sequence of tiny, attributable PRs — each leaves the tree green and appends its own
`CHANGELOG.md` entry — culminating in a single release cut.

A read-only audit against the live repo and the cached crate sources for both `1.2.2` and `1.3.0`
drove the plan and changed two things versus the first draft:

1. **The release gate is already open.** `centaur_technical_indicators 1.3.0` is published to
   crates.io (verified in the local registry cache; the sibling Rust repo is at `version = 1.3.0`).
   The original Phase A / Phase B gating is gone — the dependency bump is step one (**S1**).
2. **`__version__` would have silently failed.** Adding `m.add("__version__", env!(...))` to the
   inner module does not survive maturin's auto-generated `from .ext import *` (dunders aren't
   re-exported), so `cti.__version__` would be absent and the release-cut check would fail. This is
   resolved by the mixed-layout restructure (**S7**), which also fixes the type-stub mechanism and
   removes the stale `python/` directory in one move.

The audit also confirmed the substantive technical claims hold against ground truth: no wiring bugs
in any of the nine binding modules, the favorable-move semantics, the inherited fixes, the three
string-alias regimes, the module structure, and the TSI swap. The one starting-state blemish was
that `cargo fmt --check` **failed** on pre-existing committed drift (~84 hunks across 9 of 10
`src/*.rs` files) — which is exactly why **S0** runs first.

## Standing rules (defer to AGENTS.md — list deltas only)

`AGENTS.md` / `CLAUDE.md` govern branch naming, commit format, the pre-PR validation gates, the
PR-report shape, the no-new-dependencies rule, and stop-and-report. Every batch inherits them. The
pre-PR gates for **every** session are: `maturin develop`, `python -m pytest`, `cargo fmt --check`;
PR bodies use `Summary` / `Compatibility` / `Validation` / `Changelog`. Recorded here are only the
deltas specific to *this* plan:

- **One slice per fresh session.** Each batch is its own Claude Code session and its own PR, leaves
  the tree green on all three gates, and appends its entry under `## [Unreleased]` in `CHANGELOG.md`.
  **S10** promotes `[Unreleased]` → `[1.3.0]`.
- **CHANGELOG exemptions (2 batches only):** **S0** (formatting baseline) and **S11** (internal docs
  only) are not user-facing and are the only batches exempt from the "every change gets a paired
  `CHANGELOG.md` entry" CI policy gate. Record the rationale in their PR descriptions. *(Scratch
  removal is **S10's** final step, not S11 — see the swap below.)*
- **Staged version, mixed-state window.** The `[package] version` in `Cargo.toml` stays `1.2.2`
  through **S1–S9** and is bumped to `1.3.0` only at the release cut (**S10**). This is a deliberate
  deviation from `docs/REPO_MAP.md`'s "also bump the package `version` when bumping the upstream
  crate" rule, because this is a staged multi-PR release: bumping it mid-stream would make `main`
  (and, via `dynamic`, the wheel version) advertise `1.3.0` before it is cut. So from S1 to S10 the
  build ships half-migrated — dep at `1.3.0`, package version still `1.2.2` — which is acceptable
  because the release cuts exactly once, at S10. **State this explicitly in the S1 PR description**
  (a review bot flagged exactly this on the first attempt).
- **Own worktree + own venv per session.** A shared venv's installed extension gets clobbered by
  concurrent `maturin develop` runs, so each parallel session gets its own git worktree and venv.
- **Test methodology is binding for S1–S3** — see the [Test methodology](#appendix-b--test-methodology-binding-for-s1s3)
  appendix. In short: exact-value expectations are *generated by running against the installed
  1.3.0 crate*, never hand-computed; stop-and-report on any mismatch; prefer FFI-boundary
  (no-panic / NaN-result) assertions over re-testing extremum internals.

## Sequence at a glance

1. **S0** — `cargo fmt --all` baseline (unblocks the per-session + CI formatting gate; blocks all). *(merged)*
2. **S1** — bump Rust dep `1.2.2` → `1.3.0` (unblocks S2, S3, S10). *(merged)*
3. **S2** — bind `peak_favorable_move` / `valley_favorable_move` + tests (depends on S1; unblocks S7).
4. **S3** — Python regression tests for the inherited 1.3.0 fixes **+ the carryover `Fixed` entry**.
5. **S4** — README accuracy + docstring keyword fixes + `chart_trends` `See:` links.
6. **S5** — document + pin the three string-alias regimes (crate-independent). *(merged)*
7. **S6** — package-metadata cleanup: Documentation URL + classifiers. *(merged)*
8. **S7** — mixed layout: `.pyi` stubs + `py.typed` + `__version__` + remove stale dir (depends on S2).
9. **S8** — add `cargo fmt --check` to CI (`verify` job in `CI.yml`). *(merged)*
10. **S9** — create `docs/2.0.0.md` breaking-change backlog. *(merged)*
11. **S11** — consolidate 1.3.0 decisions into `docs/` (runs **before** the cut so the tag contains them).
12. **S10** — release cut: bump `[package] version`, promote changelog, verify `__version__`, tag + publish (final); removes the spent scratch as its last step.

> **Hard gates / ordering constraints:** S0 before everything (the whole-crate `cargo fmt --check`
> gate cannot pass until the committed drift is cleared). S1 before S2 / S3 / S10. S2 before S7 (the
> stub pass is written once over the complete surface, including favorable-move). S7 before S10 (the
> cut verifies `cti.__version__ == "1.3.0"`, which only resolves after the mixed layout lands). **S11
> before S10** (decided 2026-06-20: the 1.3.0 *tag* must contain the decision docs, so the docs
> consolidation lands first; S10 removes the spent scratch as its final step). Everything else is
> order-independent (but **not**
> merge-independent — see the shared-file hotspots).

## Batches

The table is the at-a-glance contract. **`Touches` is the file footprint** — it drives the waves and
the hotspot list, so keep it accurate and matched to each brief's frontmatter `touches`.

| ID | Goal (one line) | Depends on | Touches (paths) | Wave | Effort |
|----|-----------------|-----------|-----------------|------|--------|
| S0 | `cargo fmt --all` baseline so the fmt gate can pass | — | `src/*.rs` (fmt only) | 0 | low |
| S1 | Bump Rust dep `1.2.2` → `1.3.0` | S0 | `Cargo.toml`, `Cargo.lock`, `CHANGELOG.md` | 1 | medium |
| S5 | Document + pin the three string-alias regimes | S0 | `src/lib.rs`, `tests/test_string_aliases.py` (new), `CHANGELOG.md` | 1 | high |
| S6 | Documentation URL + Python classifiers | S0 | `pyproject.toml` (`[project]`), `CHANGELOG.md` | 1 | medium |
| S8 | `cargo fmt --check` step in CI | S0 | `.github/workflows/CI.yml`, `CHANGELOG.md` | 1 | medium |
| S9 | `docs/2.0.0.md` breaking-change backlog | S0 | `docs/2.0.0.md` (new), `CHANGELOG.md` | 1 | low |
| S2 | Bind `peak_/valley_favorable_move` + tests | S1 | `src/chart_trends.rs`, `tests/test_chart_trends.py`, `CHANGELOG.md` | 2 | medium |
| S3 | Inherited-fix regression tests + carryover `Fixed` entry | S1 | `tests/test_chart_trends.py`, `tests/test_momentum_indicators.py`, `tests/test_trend_indicators.py`, `tests/test_candle_indicators.py`, `CHANGELOG.md` | 2 | medium |
| S4 | README accuracy + docstring keyword fixes + `See:` links | S0 (soft S2) | `README.md`, `pyproject.toml` (description), `src/chart_trends.rs`, `src/candle_indicators.rs`, `src/other_indicators.rs`, `CHANGELOG.md` | 2 | high |
| S7 | Mixed layout: stubs + `py.typed` + `__version__` + stale-dir removal | S2 | `pyproject.toml` (`[tool.maturin]`), `python/centaur_technical_indicators/__init__.py` (new), `…/py.typed` (new), `…/*.pyi` (new), `.gitignore`, `CHANGELOG.md` | 3 | xhigh |
| S11 | Consolidate 1.3.0 decisions into `docs/` (before the cut) | S7 | `docs/DECISIONS-1.3.0.md` (new), `docs/REPO_MAP.md` | Final | medium |
| S10 | Release cut: version bump, changelog promote, tag + publish; remove scratch (last) | S1, S2, S3, S7, S11 | `Cargo.toml` (`[package] version`), `Cargo.lock`, `CHANGELOG.md` | Final | medium |

## Batch summaries

Light but self-standing. Briefs marked *(merged)* already exist and landed; briefs marked
*(to author)* must be written like the Wave-1 briefs before their session runs.

### S0 — Formatting baseline
**Depends on:** — · **Wave:** 0 · **Effort:** low · **Brief:** `[[S0_BRIEF]]` *(merged — PR #31)*
- **Objective:** Run `cargo fmt --all` so `cargo fmt --check` passes and can serve as a real
  per-session and CI gate. Whole-crate, because `cargo fmt --check` is whole-crate — no later
  session can satisfy its own formatting gate while any file still drifts.
- **Changes (summary):** Reformat all of `src/*.rs` (formatting only — zero logic changes). Record
  the rustfmt / toolchain version in the PR so S8's CI runner can match it.
- **Out of scope:** Any logic change, rename, dependency or version bump, or non-`src` edit. This is
  the single batch that is the explicit, acknowledged exception to the "no opportunistic refactor"
  rule — and (with S11) one of the two CHANGELOG-exempt batches.

### S1 — Dependency bump
**Depends on:** S0 · **Wave:** 1 · **Effort:** medium · **Brief:** `[[S1_BRIEF]]` *(merged — PR #32)*
- **Objective:** Move the binding onto Rust 1.3.0, isolated so any fallout is attributable.
- **Changes (summary):** Bump `[dependencies] centaur_technical_indicators` `1.2.2` → `1.3.0` in
  `Cargo.toml`; **leave `[package] version` at `1.2.2`** (bumped only at S10 — see Standing rules).
  This is *not* dependency-only: it inherits user-visible behavior changes, so the CHANGELOG `Fixed`
  entry documents them (`chart_trends.peaks` / `valleys` index-0 & retained-after-monotonic-run
  corrections; `aroon_up` / `aroon_down` / `stochastic_oscillator` return `NaN` instead of panicking
  on all-NaN input). Forward-compat is zero-risk — every upstream signature this binding calls is
  byte-identical 1.2.2 → 1.3.0.
- **Out of scope:** The `[package] version` bump; any `src` / test / README edit; hand-editing any
  shifted test expectation (re-derive against the installed 1.3.0 crate, or stop and report).
- **⚠ Carryover:** the inherited-behavior `Fixed` entry **never landed on `main`** (PR #32 merged
  without it). It is re-folded into **S3**, alongside the regression tests for the same behaviors.

### S2 — Bind favorable-move + tests
**Depends on:** S1 · **Wave:** 2 · **Effort:** medium · **Brief:** `[[S2_BRIEF]]` *(ready — implemented; PR #38)*
- **Objective:** Expose the two new chart-trend functions, flat on the `chart_trends` module
  (matching `peaks` / `valleys`; **not** under `single` / `bulk`).
- **Changes (summary):** Add `chart_trends.peak_favorable_move(prices, index, period) -> float` and
  `valley_favorable_move(...)` in `src/chart_trends.rs`, mapping the upstream `crate::Result<f64>`
  error to `PyValueError`; add value + `ValueError` tests in `tests/test_chart_trends.py`. Semantics,
  the four traced test vectors, and the in-bounds rule are the locked spec in
  [Appendix A](#appendix-a--favorable-move-semantics-locked-spec).
- **Out of scope:** Stub coverage (added once, in S7); any `single` / `bulk` nesting for these flat
  functions.

### S3 — Inherited-fix regression tests
**Depends on:** S1 · **Wave:** 2 · **Effort:** medium · **Brief:** `[[S3_BRIEF]]` *(in review — PR #39)*
- **Objective:** Prove the inherited Rust 1.3.0 fixes hold at the binding boundary, and land the
  carryover `Fixed` CHANGELOG entry that S1 missed.
- **Changes (summary):** (a) FFI no-panic / NaN-result tests for the directly-exposed hardened
  functions (`trend_indicators.single.aroon_up` / `aroon_down`,
  `momentum_indicators.single.stochastic_oscillator`), plus an *indirect* cauchy exercise via
  `candle_indicators.single.moving_constant_bands(..., "cauchy", ...)` on degenerate input (there is
  **no** `cauchy_iqr_scale` binding). (b) A sparing set of exact-value extremum tests (index-0 and
  retained-after-monotonic-run) — values **generated**, not hand-computed. Fold in the S1-missed
  `Fixed` entry.
- **Out of scope:** Exhaustive extremum testing (the Rust repo's job); calling a non-existent
  `cauchy_iqr_scale` binding; hand-computing any expected value.

### S4 — README accuracy + docstring keyword fixes + `See:` links
**Depends on:** S0 (soft-depends on S2 for the favorable-move README listing) · **Wave:** 2 ·
**Effort:** high · **Brief:** `[[S4_BRIEF]]` *(in review — PR #40)*
- **Objective:** Fix the broken quick-start, close documentation drift, and correct docstring
  keyword names that raise real `TypeError`s.
- **Changes (summary):** README — fix the quick-start call path
  (`cti.moving_average.single.moving_average(...)`, still yielding `100.352` — only the path changes,
  not the result), complete "Available Indicators" and make "Library Structure" accurate (the blanket
  "every module has bulk and single" is false; the explicit indicator-name list and the per-module
  `single`/`bulk` asymmetries are the locked inventory in
  [Appendix E](#appendix-e--s4-readme-inventory-locked-list)), reconcile the
  benchmark/list inconsistency, add the `basic_indicators`-out-of-scope note, update ecosystem naming
  ("Centaur Capital" → "CRT (Centaur Research & Technologies)") and the legacy `centaurlabs.pages.dev`
  link, and change "60+" → "50+". `pyproject.toml` description gets the same naming + count edits.
  (`See:` links were intended for the six `chart_trends` docstrings but are **deferred** — the
  upstream docs pages 404; see Appendix E.) Fix docstring keyword mismatches
  (`supertrend` `constant_type_model` → `constant_model_type`; `true_range` `previous_close` →
  `close`) — confirm the `TypeError` severity with a one-line repro before committing.
- **Out of scope:** The `[tool.maturin]` table (S7 owns it) and the author/maintainer email
  (intentionally retained). The string-alias README table is S5's; do not also edit `src/lib.rs`.

### S5 — String aliases: document + pin
**Depends on:** S0 · **Wave:** 1 · **Effort:** high · **Brief:** `[[S5_BRIEF]]` *(merged — PR #36)*
- **Objective:** Make the accepted string aliases honest and tested, without changing behavior.
- **Changes (summary):** In `src/lib.rs` **docstrings + `from_string` error messages only**, document
  the full accepted set for each of the three regimes (`PyConstantModelType` — all three
  vocabularies incl. the real `sma`→Smoothed / `ma`→Simple inversion; `PyDeviationModel` — one-word +
  abbreviations + snake_case; `PyMovingAverageType` — only `simple`/`smoothed`/`exponential`). Add a
  **new** `tests/test_string_aliases.py` pinning every alias to its result.
- **Out of scope:** Any match-arm pattern or mapping change (behavior must be identical); adding new
  aliases; editing `README.md` or per-module docstrings (other sessions own those).

### S6 — Package metadata cleanup
**Depends on:** S0 · **Wave:** 1 · **Effort:** medium · **Brief:** `[[S6_BRIEF]]` *(merged — PR #33)*
- **Objective:** Fix `pyproject.toml` metadata drift (Documentation URL + classifiers only).
- **Changes (summary):** Repoint `[project.urls] Documentation` from the GitHub `/wiki` to the
  ReadTheDocs root; expand `classifiers` to declare Python 3.10–3.14 (matching
  `python-package.yml`). `cti.__all__` needs no code change — PyO3 0.25 auto-populates it with the
  nine submodules (verification-only).
- **Out of scope:** The `description` string (S4), the `[tool.maturin]` table (S7), the email
  placeholders (retained), and `__version__` (S7).

### S7 — Mixed layout: stubs + `py.typed` + `__version__` + remove stale dir
**Depends on:** S2 · **Wave:** 3 · **Effort:** xhigh · **Brief:** `[[S7_BRIEF]]` *(in review — PR #41)*
- **Objective:** One structural change resolving three problems together — ship type info, make
  `__version__` reachable, and clean up the stale `python/` directory. The highest-value item in the
  release.
- **Changes (summary):** In `[tool.maturin]` (sole owner of this table) set `python-source = "python"`
  and exclude internal `docs/` from the sdist. Remove the stale gitignored `.so` under
  `python/centaur_technical_indicators/` and repurpose the directory as the source root. Hand-author
  `__init__.py` (the **proven** body in [Appendix C](#appendix-c--s7-__init__py-locked-body) — it
  replicates maturin's shim, preserves `__doc__` / `__all__`, and adds `__version__` via
  `importlib.metadata`). Add `py.typed` and per-submodule `.pyi` stubs covering the complete surface
  (incl. the flat `chart_trends` functions and favorable-move). Ensure the new files are git-tracked
  (the `*.so` / `__pycache__` gitignores must keep ignoring the rebuilt artifact).
- **Out of scope:** Any public-API change (verify with the existing suite); a manual
  `m.add("__all__", …)` (would only overwrite the identical auto-populated value); a `[tool.maturin]
  include` for the stubs (files under `python-source` auto-bundle).

### S8 — CI: formatting gate
**Depends on:** S0 · **Wave:** 1 · **Effort:** medium · **Brief:** `[[S8_BRIEF]]` *(merged — PR #34)*
- **Objective:** Make CI enforce the repo's own stated `cargo fmt --check` pre-PR gate.
- **Changes (summary):** Add a native `cargo fmt --all -- --check` step to the **`verify`** job in
  `.github/workflows/CI.yml` (the approved CI-edit exception; no third-party Actions).
- **Out of scope:** `cargo clippy -D warnings` (parked — needs J's approval); any edit to
  `python-package.yml` or other jobs. Toolchain skew vs. the S0 baseline → stop and report.

### S9 — Create `docs/2.0.0.md`
**Depends on:** S0 · **Wave:** 1 · **Effort:** low · **Brief:** `[[S9_BRIEF]]` *(merged — PR #35)*
- **Objective:** Log the breaking-change backlog so the deferred items are neither re-litigated nor
  accidentally "fixed" in a minor.
- **Changes (summary):** Create `docs/2.0.0.md` verbatim with the four deferred items (misleading
  model-type aliases; TSI single/bulk argument-order mismatch; deprecated upstream functions exposed
  without a Python signal; Python-unreachable parameterized enum variants).
- **Out of scope:** Any code change; the wider decisions consolidation (S11).

### S10 — Release cut
**Depends on:** S1, S2, S3, S7, S11 · **Wave:** Final (runs **after** S11) · **Effort:** medium · **Brief:** `[[S10_BRIEF]]` *(ready)*
- **Objective:** Finalize and publish 1.3.0.
- **Changes (summary):** Bump `[package] version` `1.2.2` → `1.3.0` in `Cargo.toml` (this one edit
  drives both the wheel version and, via `importlib.metadata`, `cti.__version__`). Promote
  `[Unreleased]` → `[1.3.0] - <date>`. Final gate run + **confirm `cti.__version__ == "1.3.0"`**
  (the check the original plan would have failed; now passes because of S7). Then **hand the `v1.3.0`
  tag to the maintainer** (tag-triggered CI builds wheels + sdist and `uv publish`es to PyPI — the
  irreversible, outward-facing step). As the **final** step after publish, remove the spent scratch
  (`PLAN.md`, `RESUME.md`, `*_BRIEF.md`).
- **Out of scope:** Any new feature work; the author/maintainer email (still deferred to 1.3.1);
  pushing the tag / publishing without authorization.

### S11 — Documentation consolidation (runs BEFORE the cut)
**Depends on:** S7 (runs **before** S10) · **Wave:** Final · **Effort:** medium · **Brief:** `[[S11_BRIEF]]` *(ready)*
- **Objective:** Preserve the durable decisions in `docs/` so the "why" survives the scratch deletion,
  landing **before** S10 so the 1.3.0 tag contains them.
- **Changes (summary):** Create `docs/DECISIONS-1.3.0.md` (scope incl. `basic_indicators`;
  gate/semantics/inherited-fix inventory; DX/packaging `__version__` rationale; quality notes incl.
  the #40 Codex catches; 2.0 pointer; resolved sub-decisions; deferred email); add a pointer from
  `docs/REPO_MAP.md` to it and to `2.0.0.md`. **CHANGELOG-exempt** (internal docs, like S0). Does
  **not** remove the scratch — that moves to S10's final step (the cut still reads `PLAN.md`).
- **Out of scope:** Any user-facing or shipped-wheel change (`docs/` is already excluded from the
  sdist by S7). Second CHANGELOG-exempt batch.

## Assumptions to verify (step 3)

The repo-state claims this plan depends on. Most were confirmed by the read-only audit and then by
Wave 0/1 landing; the one remaining `pending` item (A8) is S4-local and non-blocking. Do not author
a brief while any blocking assumption is `contradicted` or `stale`.

| ID | Assumption (repo-state claim) | Expected evidence (file/symbol/cmd) | Risk if wrong | Status |
|----|-------------------------------|-------------------------------------|---------------|--------|
| A1 | `centaur_technical_indicators 1.3.0` is published and resolvable | `cargo tree -i centaur_technical_indicators`; local registry cache | S1 cannot bump | verified (S1 merged) |
| A2 | Every upstream signature this binding calls is byte-identical 1.2.2 → 1.3.0 (only NaN-hardening bodies + `#[allow(unreachable_patterns)]` differ) | audit vs. cached crate sources; suite stays green | Hidden behavior break under the bump | verified |
| A3 | `chart_trends` is flat (no `single`/`bulk`); upstream `peak_favorable_move(prices,index,period) -> Result<f64>` (and `valley_*`) | `src/chart_trends.rs`; upstream 1.3.0 source | S2 binds the wrong shape | verified (audit) |
| A4 | PyO3 0.25 auto-populates `cti.__all__` with exactly the nine submodules | `python -c "import centaur_technical_indicators as c; print(c.__all__)"` | S6/S7 add redundant or regressing `__all__` | verified |
| A5 | maturin places the ext as submodule `<pkg>/<pkg>.so`, so `from .centaur_technical_indicators import *` targets the submodule (no shadow/recursion) | S7 second review: built, installed, imported (`ext is package` → False) | S7 `__init__.py` recurses or shadows | verified (2nd review) |
| A6 | `python/centaur_technical_indicators/` is a stale untracked artifact (gitignored `.so`) at the path S7 wants as source root | `ls python/centaur_technical_indicators/` → stale `.so` + `__pycache__` | S7 collides with a live path | verified (current tree) |
| A7 | `cargo fmt --check` failed on committed drift before S0 (~84 hunks, 9/10 `src/*.rs`) | `cargo fmt --all -- --check` exit 1 pre-S0 | S0 unjustified / gate can't hold | verified (S0 = PR #31, commit `bf21afe`) |
| A8 | Docstring keyword mismatches raise `TypeError` (`supertrend` `constant_type_model`; `true_range` `previous_close`) | one-line repro calling with the wrong kwarg | Mis-files S4 severity (fix is identical) | verified (docstrings confirmed wrong in source 2026-06-20; live repro in S4) |
| A9 | Two workflows exist; the `verify` job in `CI.yml` is the fmt-gate home | `.github/workflows/CI.yml`, `python-package.yml` | S8 edits the wrong workflow | verified (S8 merged) |

## Parallelization (git worktrees)

**Sequential backbone (cannot be collapsed):** S0 → S1 → S2 → S7 → S11 → S10. (S3 also needs S1;
S4 soft-needs S2.)

This release uses **serial PRs onto `main`** rather than a dedicated `release/1.3.0` integration
branch: each batch branches off fresh `origin/main`, and same-wave batches run concurrently only
when their `Touches` are file-disjoint. "Order-independent" is **not** "merge-independent."

**Waves** — each cell is one worktree / Claude Code session (numbering matches `RESUME.md`):

| Wave | After | Run concurrently | Max worktrees |
|------|-------|------------------|---------------|
| 0 | — | S0 (solo; tiny; blocks all) | 1 |
| 1 | S0 merged | S1, S5, S6, S8, S9 (file-disjoint apart from `CHANGELOG.md`) | 5 |
| 2 | S1 merged | S2, then S3 + S4 rebased on it (see hotspots) | up to 3 |
| 3 | S2 merged | S7 (solo; needs the full surface incl. favorable-move) | 1 |
| Final | S1+S2+S3+S7 merged | S11, then S10 | 1 |

**Shared-file hotspots** — any path appearing in more than one batch's `Touches`. Concurrent batches
within a wave must be file-disjoint; anything contended is serialized or rebased:

- `CHANGELOG.md` — every non-exempt batch appends under `[Unreleased]`; expect a trivial append
  conflict, rebase on `main` and re-append.
- `src/chart_trends.rs` — **S2** (favorable-move bindings) and **S4** (`See:` links). Land S2 first,
  rebase S4.
- `tests/test_chart_trends.py` — **S2** (favorable-move tests) and **S3** (extremum regression
  tests). Land S2 first, rebase S3.
- `pyproject.toml` — **S4** (`description`), **S6** (`[project.urls]` + classifiers), **S7**
  (`[tool.maturin]`). Disjoint *tables*, but the same file — S6 lands in Wave 1; S4 (Wave 2) and S7
  (Wave 3) rebase. S7 is the sole owner of `[tool.maturin]`.
- `Cargo.toml` — **S1** (`[dependencies]`) and **S10** (`[package] version`) edit the same file but
  in different waves (Wave 1 vs. Final) and different tables, so they never overlap; listed for
  completeness per the derivation rule.
- momentum / trend / candle test files (`tests/test_momentum_indicators.py` /
  `test_trend_indicators.py` / `test_candle_indicators.py`) — touched **only by S3**. Not a shared
  path: **S5** deliberately used a *new* `tests/test_string_aliases.py` to avoid colliding here, so
  there is no contention. Noted so the avoidance isn't re-litigated.

**Mechanics:**

    git switch main && git pull --ff-only                        # fresh base (no dedicated integration branch)
    git worktree add ../cti-wt/<id> -b <branch> origin/main      # one per batch; own venv each
    # run a Claude Code session in each worktree dir; before merging each branch:
    git -C ../cti-wt/<id> rebase main                            # resolves CHANGELOG, etc.
    # open PR → merge into main; then: git worktree remove ../cti-wt/<id>
    # tag/cut only after S10 (and S11 if the tag must contain the docs)

---

# Running log

Append decisions, blockers, and per-batch outcomes here as work proceeds. This is the durable record.

## Status

- **Verification (step 3):** the read-only audit served as plan verification — verdict
  *ready-with-edits*. Two edits applied: the release gate was found already open (S1 moved to step
  one) and the `env!`-based `__version__` was found unworkable (resolved by the S7 mixed layout).
  Assumptions A1–A7, A9 are `verified`; A8 is `pending` (S4-local, non-blocking).
- **S0 + all of Wave 1 merged** (per `RESUME.md`, 2026-06-19). `origin/main` is at `26aabd9`:
  - S0 — PR #31 — `style/cargo-fmt-baseline` — repo-wide `cargo fmt` baseline.
  - S1 — PR #32 — `chore/bump-cti-1.3.0` — dep `1.2.2` → `1.3.0` (`[package] version` still `1.2.2`).
  - S5 — PR #36 — `docs/string-aliases` — alias docs + new `tests/test_string_aliases.py`.
  - S6 — PR #33 — `chore/pyproject-metadata` — Documentation URL fix + classifiers 3.10–3.14.
  - S8 — PR #34 — `ci/add-fmt-check` — `cargo fmt --check` in the `CI.yml` verify job.
  - S9 — PR #35 — `docs/2.0-backlog` — `docs/2.0.0.md`.
  - `[Unreleased]` already contains: dep bump, classifiers, Documentation-URL fix, fmt-CI step,
    `docs/2.0.0.md`, alias tests + alias docs.
- **⚠ Open carryover (do not lose):** the inherited-behavior `Fixed` CHANGELOG entry is **missing on
  `main`** — PR #32 merged without it (the brief was updated after the PR opened). Fold it into
  **S3**. Exact wording: the S1 batch summary above and [Appendix D](#appendix-d--target-130-changelog).
- **2026-06-20 — S2 implemented + in review (PR #38), Wave 2 set up.** Local `main` synced to
  `origin/main` (`26aabd9`). S2 (`feat/favorable-move`) bound `peak_/valley_favorable_move` + tests
  (106 passed, gates green) and opened PR #38. Briefs authored to the `TEMPLATE-brief.md` standard
  for **S3, S4** (Wave 2, parallel) and **S7** (Wave 3). Worktrees + per-worktree venvs provisioned
  at `cti-wt/S3` (`test/inherited-fix-regressions`) and `cti-wt/S4` (`docs/readme-accuracy`), both
  branched off `feat/favorable-move`; S3 build certified. Confirmed against the installed build: the
  S4 docstring `TypeError`s are real (Assumption **A8** → `verified`); all S3 expected values
  (aroon/stochastic NaN, cauchy-indirect no-panic, the two extrema) reproduce.
- **2026-06-20 (cont.) — S3 + S4 implemented + in review.** Run via a Sonnet workflow (S3 effort
  medium, S4 effort high) in their worktrees; diffs reviewed clean, gates green (S3 112 passed; S4
  106 passed). Opened as **stacked PRs #39 (S3) and #40 (S4)** based on `feat/favorable-move`. The S4
  agent correctly declined to over-apply the `previous_close`→`close` rename (the brief's A2
  grep-count check was too literal: `positivity_indicator` legitimately uses `previous_close`).
- **2026-06-20 — Codex review fixes on #37 + #40.** #37: corrected the AGENTS.md CI gate note
  (`cargo fmt` IS a CI gate via `CI.yml`'s verify job, not local-only) — pushed `3c3f074`. #40
  (commit `0f76898`): **two valid findings, both originating in Appendix E** — (F1) the six
  `chart_trends` `See:` URLs 404 (chart-trends docs pages unpublished; verified 200 on existing
  module pages), so they were removed; (F2) `ulcer_index` actually has **both** bulk + single
  (only `volatility_system` is bulk-only), README corrected. **Appendix E and the target changelog
  here were corrected to match** so the errors don't propagate to S11's decisions doc. Gates stayed
  green (106 passed).
- **2026-06-20 — Wave 2 merged (#37–#40); S7 implemented + in review (#41).** `origin/main` at
  `6cb6756`; local `main` synced; all spent worktrees/branches pruned. S7 (`feat/mixed-layout-stubs`)
  done by me in the primary checkout (Opus/high): mixed layout, hand-authored `__init__.py`,
  `__version__` via `importlib.metadata`, `py.typed` + `.pyi` stubs for the full surface (97 fns,
  **generated** from binding signatures and **cross-checked against the runtime — exact match**),
  stale `.so` removed, `docs/` excluded from sdist. Verified end-to-end (A1–A4 all pass: `__version__`
  resolves, `__all__`/`__doc__`/nested API intact, wheel bundles stubs, sdist 0 `docs/`, 112 passed,
  fmt clean). Opened PR #41.
- **2026-06-20 — S10 + S11 briefs authored; order swapped (S11 → S10).** Decided the 1.3.0 *tag*
  must contain the decision docs, so **S11 runs before S10**. Both briefs written to
  `TEMPLATE-brief.md` and verified (template / repo-facts / plan-consistency). Scratch removal moved
  to **S10's final step** (the cut still reads `PLAN.md`).
- **2026-06-20 — Codex fix on #41 (S7), commit `79a7d33`.** Valid P2: the `.pyi` stubs advertised
  `import centaur_technical_indicators.<sub>` / `from …<sub> import …` paths that raised
  `ModuleNotFoundError` at runtime (`from .<ext> import *` only bound submodules as attributes). Fixed
  by registering each submodule in `sys.modules` under its qualified name in `__init__.py`; added
  `tests/test_package_layout.py` (4 import-path tests). Verified: all patterns resolve, 116 passed.
- **Next:** merge **#41** → **S11** (decision docs; must land first so the tag contains them) →
  **S10** (release cut — bump `[package] version`, promote changelog, confirm
  `cti.__version__ == "1.3.0"`; the `v1.3.0` tag/publish is J's; final step removes the scratch).
- **Housekeeping:** workspace is clean (single worktree on `main`, branches pruned). Untracked scratch
  (`PLAN.md`, `*_BRIEF.md`, `RESUME.md`) survives checkouts — removed at the **end of S10**.

## Open questions / deferred

- **Open sub-decision 1 — new disambiguating model-type aliases?** Default **no** — S5 documents and
  pins the existing set only. (Adding aliases is parked.)
- **Open sub-decision 2 — `cargo clippy -D warnings` in CI?** Default **no / parked** — risk of
  macro-generated lint noise on a PyO3 crate; needs J's approval.
- **Resolved — `2.0.0.md` location:** `docs/2.0.0.md` (S9 created it there; S11 consolidates the rest).
- **Pending input — author/maintainer email.** The `your@email.com` placeholder in `pyproject.toml`
  is knowingly retained for 1.3.0 (no-PII rule; no CRT address yet). Fix in a 1.3.1 follow-up once
  the address exists — do **not** guess it and do **not** drop the placeholder silently.
- **Out of scope (decided, not deferred) — binding the Rust `basic_indicators` module.** It is a
  statistical-primitives module (mean/median/mode/variance/std/abs-dev/min/max/quantile); Python's
  `statistics` and `math` provide these natively, so re-binding through PyO3 would ship a slower,
  FFI-marshalled stdlib. Documented in the README (S4) to pre-empt the recurring "module parity"
  question.
- **Deferred to 2.0 (breaking — logged in `docs/2.0.0.md`, not touched in 1.3.0):** the `sma`/`ma`
  alias remap; TSI single/bulk argument-order reconciliation; deprecated upstream functions exposed
  without a Python deprecation signal (`slow_stochastic`, `slowest_stochastic`, `signal_line`,
  `volatility_system`); Python-unreachable parameterized enum variants (`PersonalisedMovingAverage`;
  `Personalised`; `CustomAbsoluteDeviation` / `StudentT` / `EmpiricalQuantileRange`).

---

# Appendices

Bespoke locked specs the batches reference. These are durable reference material that has no brief
home yet (S2 / S7 / S10 briefs are still to author) — preserve them until those briefs absorb them.

## Appendix A — favorable-move semantics (locked spec)

Window is inclusive `[index+1, index+period]`; results are **signed** (not floored). In-bounds iff
`index + period < len(prices)`. Map upstream errors to `ValueError`: empty prices → `EmptyData`;
`period == 0` → `InvalidPeriod`; out-of-bounds → `InvalidPeriod`.

- `peak_favorable_move`  = `prices[index] − min(window)`
- `valley_favorable_move` = `max(window) − prices[index]`

| Call | Reference | Forward window | Result |
|------|-----------|----------------|--------|
| `peak_favorable_move([107,104,100,102], 0, 3)` | 107 | [104,100,102] | 107 − min(100) = **7.0** |
| `peak_favorable_move([100,101,102,103], 0, 3)` | 100 | [101,102,103] | 100 − min(101) = **−1.0** |
| `valley_favorable_move([100,102,107,104], 0, 3)` | 100 | [102,107,104] | max(107) − 100 = **7.0** |
| `valley_favorable_move([105,104,103,102], 0, 3)` | 105 | [104,103,102] | max(104) − 105 = **−1.0** |

A "peak move" is negative when price never drops below the reference in the window; a "valley move"
is negative when price never rises above it. (All four: index 0, period 3, len 4 → 3 < 4, in bounds.)
Plus `pytest.raises(ValueError)` for empty input, zero period, and an out-of-bounds window. All
four values were traced through the 1.3.0 algorithm and confirmed; any **further** exact-value case
must be generated against the installed crate, never hand-computed.

## Appendix B — Test methodology (binding for S1–S3)

1. **Generated, not hand-derived.** Any exact-value test, and any existing expectation that shifts
   after S1, gets its expected output produced by running against the installed `1.3.0` crate.
   Hand-computed expectations are prohibited for algorithm-dependent values — even the audit-confirmed
   cases are confirmations, not licenses to hand-compute new ones.
2. **Stop-and-report on mismatch.** If a generated value contradicts what the docs imply (including
   the favorable-move values), report it — don't edit the test to pass.
3. **Test the boundary, not the internals.** Prefer no-panic / NaN-result assertions (the FFI
   contract — a Rust panic crossing FFI is observable at the Python layer) over re-testing extremum
   values (the Rust repo's job).
4. **Smoke-test character preserved.** These confirm wiring and inherited behavior; they are not a
   port of the Rust edge-case suite.

## Appendix C — S7 `__init__.py` (locked body)

Proven end-to-end in the second review (built, installed into a throwaway venv, imported; nested API,
`__version__`, `__all__`, and `__doc__` all verified). It replicates maturin's auto-shim **and** adds
the version. Use exactly this:

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

- **Preserve `__doc__` and `__all__`** — a naive `from .ext import *` + `__version__` would silently
  regress both (a public-surface regression two steps after S6 confirmed `__all__`). The two extra
  lines carry them over.
- **Name collision — resolved.** maturin places the compiled extension as the submodule
  `centaur_technical_indicators.centaur_technical_indicators` (`<pkg>/<pkg>.so`), so the relative
  import targets the submodule, not this package — no shadowing, no recursion. The extension needs no
  different internal name.
- `__version__` via `importlib.metadata` reads the wheel dist-info (derived from `Cargo.toml [package]
  version`), needs no `env!` macro, and is unaffected by the `import *` dunder problem; the
  `try/except` guards the editable/source-tree case.

Also in S7: `py.typed` (PEP 561 inline), and per-submodule `.pyi` stubs — `__init__.pyi` (top-level
`__version__`, `__all__`, flat `chart_trends` fns incl. favorable-move) plus one `<submodule>.pyi`
per Rust submodule, expressing the `single` / `bulk` levels as nested `class single:` / `class bulk:`
namespaces. Files under `python-source` auto-bundle into the wheel — no `[tool.maturin] include`
needed. `[tool.maturin]` also gains `exclude = [{ path = "docs/**/*", format = "sdist" }]` (confirm
the exact key/format against the maturin 1.9–2.0 config docs).

## Appendix D — target `[1.3.0]` changelog

Assembled from per-session `[Unreleased]` entries; finalized in S10.

```
### Added
- `chart_trends.peak_favorable_move` and `chart_trends.valley_favorable_move` bindings
  (maximum favorable excursion over a forward window), mirroring Rust 1.3.0.
- Type stubs (`.pyi`) and `py.typed` marker; mixed package layout with a hand-authored
  `__init__.py`.
- `__version__` on the top-level package (resolved via `importlib.metadata`).
- Python regression tests for inherited Rust 1.3.0 chart-trend / degenerate-input fixes.
- Tests pinning accepted model-type / deviation-model / moving-average-type string aliases.
- `cargo fmt --check` to CI.
- README scope note: statistical primitives (the Rust `basic_indicators` surface) are
  intentionally not re-bound.
- `docs/2.0.0.md` breaking-change backlog.

### Fixed
- Inherited Rust 1.3.0 indicator-behavior fixes, now user-visible through the bindings:
  `chart_trends.peaks` / `chart_trends.valleys` corrected for an extremum at index 0 and for an
  extremum retained after a monotonic run; and `trend_indicators.single.aroon_up` / `aroon_down`
  and `momentum_indicators.single.stochastic_oscillator` return `NaN` instead of panicking on
  all-NaN input.
- README quick-start example called `cti.moving_average(...)` (a submodule, not callable)
  instead of `cti.moving_average.single.moving_average(...)`.
- Docstring keyword-name mismatches that could raise `TypeError` (`supertrend`
  `constant_type_model` → `constant_model_type`; `true_range` `previous_close` → `close`).
- README "Available Indicators" / "Library Structure" drift and benchmark-vs-list
  inconsistency.
- Incorrect `Documentation` URL in package metadata.

### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.2.2` to `1.3.0`.
- Expanded PyPI classifiers to declare Python 3.10–3.14.
- Updated ecosystem naming from "Centaur Capital" to "CRT (Centaur Research & Technologies)"
  and the legacy `centaurlabs.pages.dev` documentation link.
- Adjusted the indicator-count claim from "60+" to "50+".
```

Not in the changelog: the author/maintainer email (intentionally unchanged for 1.3.0); `__all__` (no
change — verification-only); and the S0 formatting baseline and S11 docs consolidation (both
internal, not user-facing).

## Appendix E — S4 README inventory (locked list)

The specific additions S4 owes the README (and the `pyproject.toml` `description`), preserved here
until `S4_BRIEF.md` is authored so the enumeration the audit already produced is not lost.

**Quick-start fix.** `cti.moving_average(prices, "simple")` raises `TypeError: 'module' object is not
callable` — `moving_average` is a submodule. Correct to
`cti.moving_average.single.moving_average(prices, "simple")`. The expected result `100.352` is
**unchanged** — only the call path changes.

**"Available Indicators" — add every bound-but-unlisted indicator:**
- momentum: `stochastic_oscillator`, `slow_stochastic`, `slowest_stochastic`,
  `percentage_price_oscillator` (PPO), `chande_momentum_oscillator` (CMO), `signal_line` (MACD
  signal), `mcginley_dynamic_commodity_channel_index`, `mcginley_dynamic_macd_line`
- candle: `mcginley_dynamic_envelopes`, `mcginley_dynamic_bands`
- strength: `volume_index`
- other: `positivity_indicator`
- chart trends: `peak_favorable_move`, `valley_favorable_move` (after S2)

**"Library Structure" — the real (asymmetric) shape.** The blanket "every module has bulk and single"
is false: `chart_trends` is flat (no `single`/`bulk`); `volatility_indicators` — `volatility_system`
is **bulk-only**, while `ulcer_index` has **both** (`register_bulk_module` + `register_single_module`
register `bulk_ulcer_index` and `single_ulcer_index`); `other` / `strength` / `trend` are asymmetric.
Describe the real shape. *(Correction 2026-06-20: an earlier draft of this note wrongly said
`ulcer_index` was single-only — Codex caught it on PR #40; verified against
`src/volatility_indicators.rs`.)*

**Benchmark consistency.** The benchmark prose discusses Stochastic / PPO / CMO / MACD-signal — the
exact indicators the list omitted (resolved by the additions above); confirm the two sections agree.

**`See:` links — BLOCKED until the docs pages exist (do not add yet).** The intent was to add
reference links to all six `chart_trends` docstrings (`peaks`, `valleys`, `peak_trend`,
`valley_trend`, `overall_trend`, `break_down_trends`) to match other modules. **But verified
2026-06-20 (Codex caught this on PR #40): every `…/indicators/chart-trends/<fn>/` URL returns 404
and the `chart-trends/` category index itself 404s, while existing module pages (e.g.
`candle-indicators/supertrend`) return 200 — the chart-trends docs pages are simply not published.**
S4 therefore added **no** `See:` links. Re-add them (and a CHANGELOG bullet) only once the upstream
docs pages exist — likely tracked on the Rust/docs side, not here.

**Docstring keyword-name fixes (real `TypeError` risk — PyO3 exposes params as kwargs):** `supertrend`
(single + bulk) docstrings say `constant_type_model`; the actual kwarg is `constant_model_type`.
`other_indicators` `true_range` (single) labels arg 1 `previous_close`; the actual kwarg is `close`.
Correct the docstrings to the real parameter names; confirm severity with a one-line repro before
committing.
