---
type: brief
id: S3
title: "Inherited-fix regression tests + carryover Fixed changelog entry"
status: ready
effort: medium
wave: 2
depends_on: ["S1", "S2"]
touches:
  - tests/test_momentum_indicators.py
  - tests/test_trend_indicators.py
  - tests/test_candle_indicators.py
  - tests/test_chart_trends.py
  - CHANGELOG.md
forbidden:
  - "src/**  (tests + changelog only — no Rust/binding changes)"
  - "tests/test_string_aliases.py  (S5's, already merged)"
branch: "test/inherited-fix-regressions"
pr_target: "main"
related:
  - "[[PLAN]]"
decisive_test: "A1"
created: 2026-06-20
tags: [brief]
---

# S3 — Inherited-fix regression tests + carryover Fixed changelog entry

> **Self-contained.** Repo conventions (branch/commit/PR format, the pre-PR gates,
> stop-and-report) live in `AGENTS.md` / `CLAUDE.md` and are assumed; this brief
> carries only what is specific to the batch. **Done = the named acceptance tests
> pass.** Stop and report if anything blocks you.

## Mission

Add a small, targeted regression layer at the FFI boundary proving the inherited Rust 1.3.0 fixes
hold through the bindings, and land the **carryover `Fixed` changelog entry** that the S1 dep-bump
PR (#32) merged without. Tests + changelog **only** — no Rust/binding source changes. Done looks
like: the all-NaN functions return `NaN` (not a panic crossing FFI), the two extremum cases return
the corrected outputs, and `[Unreleased]` documents the inherited behavior change.

## Context

- Built on **S1** (dep on Rust `1.3.0`, merged) and **S2** (favorable-move bindings — this branch
  is cut from `feat/favorable-move`, so S2's code is already present).
- **The carryover (do not lose this).** PR #32 documented the dep bump but **omitted** the
  inherited user-visible behavior change (the brief was updated after the PR opened). `[Unreleased]`
  currently has only the Documentation-URL `Fixed` entry. This batch adds the missing one.
- **Landmine — cauchy is not directly exposed.** There is **no `cauchy_iqr_scale` binding**; the
  hardened cauchy path is reachable only as `deviation_model="cauchy"`. Exercise it **indirectly**
  via `candle_indicators.single.moving_constant_bands(...)`. Do **not** try to call a
  `cauchy_iqr_scale` function — it does not exist.
- **Test values are generated, not hand-computed.** Every value below was produced by running the
  installed 1.3.0 build; if any assertion fails when you run it, **stop and report** — do not edit
  the expected value to pass.

## Prerequisites (confirm; do not perform here)

- Dep is `1.3.0`: `grep centaur_technical_indicators Cargo.toml` → `… = "1.3.0"`. If not, stop.
- S2 present in the base (this branch is off `feat/favorable-move`):
  `grep -c peak_favorable_move src/chart_trends.rs` → ≥ 1.

## Verify first (re-confirm at session start)

Each row was confirmed against the installed build on 2026-06-20. Re-locate by symbol if a line
moved; if a behavior differs, stop and report.

| Claim | How to check (after `maturin develop`) | Expected |
|-------|----------------------------------------|----------|
| stochastic all-NaN → NaN | `momentum_indicators.single.stochastic_oscillator([nan, nan])` | `nan` (no exception) |
| aroon all-NaN → NaN | `trend_indicators.single.aroon_up([nan, nan])` / `aroon_down([nan, nan])` | `nan`, `nan` |
| cauchy degenerate → no panic | `candle_indicators.single.moving_constant_bands([100.,100.,100.,100.], "simple", "cauchy", 3.0)` | `(100.0, 100.0, 100.0)` (no exception) |
| index-0 peak kept | `chart_trends.peaks([110.,109.,108.,107.], 2, 1)` | `[(110.0, 0)]` |
| retained-after-monotonic-run | `chart_trends.peaks([110.,109.,108.,120.], 2, 2)` | `[(110.0, 0), (120.0, 3)]` |

## Changes (in order)

Add `import math` where you assert `math.isnan(...)`. Prefer the no-panic / NaN assertions (the FFI
contract) over piling on exact-value cases.

1. **NaN no-panic — `tests/test_momentum_indicators.py`.** A test that calls
   `stochastic_oscillator([float("nan"), float("nan")])` and asserts `math.isnan(result)` (a Rust
   panic crossing FFI would surface as an exception, so this tests the binding contract):
   ```python
   def test_all_nan_stochastic_returns_nan_not_panic():
       result = momentum_indicators.single.stochastic_oscillator([float("nan"), float("nan")])
       assert math.isnan(result)
   ```
2. **NaN no-panic — `tests/test_trend_indicators.py`.** Analogous tests for
   `trend_indicators.single.aroon_up` and `aroon_down` on `[nan, nan]`, asserting `math.isnan`.
3. **Cauchy no-panic (indirect) — `tests/test_candle_indicators.py`.** Assert
   `candle_indicators.single.moving_constant_bands([100.,100.,100.,100.], "simple", "cauchy", 3.0)`
   returns finite bands and does not raise (degenerate flat input → IQR scale 0, the hardened case).
   Use the existing import style in that file. **Needs ≥ 4 prices** (fewer trips a length check
   before reaching the cauchy path).
4. **Exact-value extrema — `tests/test_chart_trends.py`.** Add the two sparing cases (values from the
   table above), e.g. `test_peaks_keeps_valid_index_zero_peak` and
   `test_peaks_does_not_drop_retained_peak_after_monotonic_run`. Keep these few — exhaustive extremum
   testing is the Rust repo's job.
5. **Changelog — `CHANGELOG.md`.** Under the existing `## [Unreleased]` (do **not** add a second
   heading): append the carryover bullet to `### Fixed`, and the regression-tests bullet to
   `### Added`:
   ```
   ### Fixed
   - Inherited Rust 1.3.0 behavior changes, now user-visible through the bindings:
     `chart_trends.peaks` / `chart_trends.valleys` corrected for index-0 and
     retained-after-monotonic-run extrema; and `aroon_up` / `aroon_down` /
     `stochastic_oscillator` return `NaN` instead of panicking on all-NaN input.

   ### Added
   - Python regression tests for inherited Rust 1.3.0 chart-trend / degenerate-input fixes.
   ```

## Acceptance tests (named; all must pass)

- **A1 (decisive)** — `test_all_nan_stochastic_returns_nan_not_panic` passes: all-NaN
  `stochastic_oscillator` returns NaN, no exception.
- **A2** — aroon all-NaN tests pass (`aroon_up`, `aroon_down` → NaN).
- **A3** — cauchy indirect test passes (no panic on degenerate `moving_constant_bands` input).
- **A4** — the two extremum exact-value tests pass with the values above.
- **A5 (suite)** — pre-PR gates green: `maturin develop`, `python -m pytest` (full suite),
  `cargo fmt --all -- --check`; no new dependency; `Cargo.lock` unchanged.

## Out of scope (do not touch)

- **Any `src/*.rs`** — this is tests + changelog only; the bindings are already correct.
- A `cauchy_iqr_scale` binding — it does not exist; do not add one or call one.
- `tests/test_string_aliases.py` (S5, merged) and the favorable-move tests S2 added.
- Exhaustive Rust-style edge-case porting — keep the smoke-test character.

## Definition of done

- [ ] Acceptance tests A1–A4 green; A5 suite/gates green.
- [ ] `[Unreleased]` carries **both** the carryover `Fixed` entry and the `Added` entry.
- [ ] Only files in `touches` changed; nothing in `forbidden` moved.
- [ ] PR opened against `main` (rebased on `main` once S2/#38 has merged).

## Report (per AGENTS.md)

Summary · Scope · Compatibility (none — additive tests + doc) · Validation (paste gate output) ·
Changelog — plus each acceptance-test name with its pass output verbatim (incl. A1), and anything
flagged.
