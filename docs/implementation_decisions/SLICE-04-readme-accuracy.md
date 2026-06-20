---
type: brief
id: S4
title: "README accuracy + docstring keyword fixes + chart_trends See: links"
status: ready
effort: high
wave: 2
depends_on: ["S0", "S2"]
touches:
  - README.md
  - pyproject.toml
  - src/chart_trends.rs
  - src/candle_indicators.rs
  - src/other_indicators.rs
  - CHANGELOG.md
forbidden:
  - "src/lib.rs  (S5 owns the alias docstrings — merged; do not touch)"
  - "pyproject.toml [tool.maturin] table  (S7 owns it)"
  - "pyproject.toml author/maintainer email  (knowingly retained for 1.3.0)"
  - "tests/**  (no test changes in this batch)"
branch: "docs/readme-accuracy"
pr_target: "main"
related:
  - "[[PLAN]]"
decisive_test: "A1"
created: 2026-06-20
tags: [brief]
---

# S4 — README accuracy + docstring keyword fixes + chart_trends See: links

> **Self-contained.** Repo conventions (branch/commit/PR format, the pre-PR gates,
> stop-and-report) live in `AGENTS.md` / `CLAUDE.md` and are assumed. **Done = the
> named acceptance checks pass.** Stop and report if anything blocks you.

## Mission

Fix the broken README quick-start, close documentation drift (indicator list, library structure,
benchmark/list inconsistency, ecosystem naming, indicator count), add the missing `chart_trends`
`See:` links, and correct two docstring keyword names that cause real `TypeError`s. Documentation +
docstrings only — **no behavior, binding, or test changes.**

## Context

- Crate-independent; built on **S0** (fmt baseline) and **S2** (favorable-move — this branch is cut
  from `feat/favorable-move`, so the two new functions exist and belong in the README list).
- **Docstring keyword bugs are real `TypeError`s, not typos.** PyO3 exposes parameters as keyword
  arguments under the **Rust parameter name**, so a docstring naming the wrong keyword makes a
  copy-pasted call raise `TypeError: unexpected keyword argument`. Verified in source on 2026-06-20:
  - `supertrend` single (`src/candle_indicators.rs:500`) and bulk (`:532`) docstrings say
    `constant_type_model`; the real kwarg is `constant_model_type` (`:513`, `:546`).
  - `true_range` single (`src/other_indicators.rs:102`) docstring labels arg 1 `previous_close`;
    the real kwarg is `close` (`:111`). (The **bulk** true_range docstring is already correct.)
- S5 (alias docs in `src/lib.rs`) and S6 (pyproject URL + classifiers) are already merged — do not
  redo or collide with them. The string-alias **README table**, if any, is also S5-adjacent; this
  batch only fixes README *structure/accuracy*, not the alias vocabulary.

## Verify first (re-confirm at session start)

| Claim | How to check | Expected |
|-------|--------------|----------|
| README count claim | `grep -n '60+' README.md` | hit at the header (`60+ technical indicators`) |
| README ecosystem line | `grep -n 'Centaur Capital' README.md` | one hit (`Part of the Centaur Capital ecosystem.`) |
| README legacy link | `grep -n 'centaurlabs.pages.dev' README.md` | one hit (Explanations link) |
| supertrend docstring typo | `grep -n 'constant_type_model' src/candle_indicators.rs` | 2 hits (single + bulk) |
| true_range docstring kwarg | `grep -n 'previous_close' src/other_indicators.rs` | 1 hit (single) |
| chart_trends has no See: links | `grep -c 'See:' src/chart_trends.rs` | `0` |

## Changes (in order)

### A. README (`README.md`)

1. **Quick-start.** Locate the quick-start example. `cti.moving_average(prices, "simple")` raises
   `TypeError: 'module' object is not callable` — `moving_average` is a submodule. Correct to
   `cti.moving_average.single.moving_average(prices, "simple")`. The documented result **`100.352`
   is unchanged** — only the call path changes (confirm by running it).
2. **"Available Indicators" — add every bound-but-unlisted indicator:**
   - momentum: `stochastic_oscillator`, `slow_stochastic`, `slowest_stochastic`,
     `percentage_price_oscillator` (PPO), `chande_momentum_oscillator` (CMO), `signal_line` (MACD
     signal), `mcginley_dynamic_commodity_channel_index`, `mcginley_dynamic_macd_line`
   - candle: `mcginley_dynamic_envelopes`, `mcginley_dynamic_bands`
   - strength: `volume_index`
   - other: `positivity_indicator`
   - chart trends: `peak_favorable_move`, `valley_favorable_move`
3. **"Library Structure" — describe the real (asymmetric) shape.** The blanket "every module has
   bulk and single" is false: `chart_trends` is flat (no `single`/`bulk`); `volatility_indicators`
   has `single` only for `ulcer_index` and `volatility_system` is bulk-only; `other` / `strength` /
   `trend` are asymmetric.
4. **Benchmark consistency.** The benchmark prose discusses Stochastic / PPO / CMO / MACD-signal —
   the indicators item 2 just added; confirm the two sections now agree.
5. **Scope note.** State plainly that statistical primitives available in Python's
   `statistics`/`math` (the Rust `basic_indicators` surface) are intentionally **not** re-bound.
   Pre-empts the recurring "module parity" question.
6. **Ecosystem naming.** Replace "Part of the Centaur Capital ecosystem" with "Part of the CRT
   (Centaur Research & Technologies) ecosystem". Update the legacy `centaurlabs.pages.dev`
   Explanations link to the current docs domain (the live docs the `See:` links point at:
   `https://tech.centaurresearchtechnologies.com/` — confirm the exact root before committing).
7. **Indicator count.** Change "60+" → "50+" in the README header.

### B. `pyproject.toml` (description string ONLY)

8. Apply the **same** two edits to the `description`: "Centaur Capital" → "CRT (Centaur Research &
   Technologies)", and "60+" → "50+". Touch **nothing else** in `pyproject.toml` (not `[tool.maturin]`,
   not the email, not the URLs/classifiers S6 set).

### C. Docstrings (no logic; fmt-clean after)

9. **`src/chart_trends.rs` — add `See:` links** to all six docstrings (`peaks`, `valleys`,
   `peak_trend`, `valley_trend`, `overall_trend`, `break_down_trends`), matching the format used
   elsewhere, e.g. `/// See: <https://tech.centaurresearchtechnologies.com/indicators/chart-trends/<fn>/>`
   (confirm the exact category slug against an existing module's `See:` URL). Do **not** add `See:`
   links to the two favorable-move functions unless an upstream doc page exists for them — note it
   in the report if unsure.
10. **`src/candle_indicators.rs` — supertrend docstrings.** Change `constant_type_model` →
    `constant_model_type` in both the single (`:500`) and bulk (`:532`) docstrings.
11. **`src/other_indicators.rs` — true_range single docstring.** Change `previous_close` → `close`
    (`:102`). Leave the bulk docstring (already correct).
12. **Repro (file the severity, do not change the fix).** Before committing, run a one-line repro to
    confirm the keyword really raises `TypeError` (e.g. call `supertrend(..., constant_type_model=…)`
    and observe the error). The docstring fix is identical regardless; this just confirms the
    changelog severity.

### D. Changelog (`CHANGELOG.md`)

13. Under the existing `## [Unreleased]` (do not add a second heading), add bullets:
    ```
    ### Fixed
    - README quick-start example called `cti.moving_average(...)` (a submodule, not callable)
      instead of `cti.moving_average.single.moving_average(...)`.
    - Docstring keyword-name mismatches that could raise `TypeError` (`supertrend`
      `constant_type_model` → `constant_model_type`; `true_range` `previous_close` → `close`).
    - README "Available Indicators" / "Library Structure" drift and benchmark-vs-list inconsistency.

    ### Changed
    - Updated ecosystem naming from "Centaur Capital" to "CRT (Centaur Research & Technologies)"
      and the legacy `centaurlabs.pages.dev` documentation link.
    - Adjusted the indicator-count claim from "60+" to "50+".

    ### Added
    - `See:` reference links on all `chart_trends` docstrings.
    - README scope note: statistical primitives (the Rust `basic_indicators` surface) are
      intentionally not re-bound.
    ```

## Acceptance tests (named; all must pass)

- **A1 (decisive)** — the corrected quick-start, copy-pasted from the README, runs and returns
  `100.352`: `cti.moving_average.single.moving_average(prices, "simple")` (use the README's `prices`).
- **A2** — `grep -c 'See:' src/chart_trends.rs` == 6; `grep -c 'constant_type_model'
  src/candle_indicators.rs` == 0; `grep -c 'previous_close' src/other_indicators.rs` == 0.
- **A3** — no "Centaur Capital", "60+", or "centaurlabs.pages.dev" remains in `README.md` or the
  `pyproject.toml` description.
- **A4 (suite)** — pre-PR gates green: `maturin develop`, `python -m pytest` (docstrings don't change
  behavior — suite stays green), `cargo fmt --all -- --check`; no new dependency.

## Out of scope (do not touch)

- `src/lib.rs` (S5's alias docstrings). The `[tool.maturin]` table and the author/maintainer email
  in `pyproject.toml` (S7 / intentionally retained).
- Any **binding logic**, signatures, or tests. The alias **vocabulary** (S5).
- Re-binding `basic_indicators` (it is deliberately out of scope — document, don't implement).

## Definition of done

- [ ] Acceptance checks A1–A3 green; A4 gates green.
- [ ] Only files in `touches` changed; nothing in `forbidden` moved.
- [ ] `[Unreleased]` updated (Fixed / Changed / Added as above).
- [ ] PR opened against `main` (rebased on `main` once S2/#38 has merged).

## Report (per AGENTS.md)

Summary · Scope (files touched; what was left untouched) · Compatibility (none — docs/docstrings
only) · Validation (paste gate output + the quick-start repro returning 100.352 + the `TypeError`
repro) · Changelog — plus each acceptance check with its result, and anything flagged.
