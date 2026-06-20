# S1 — Dependency Bump 1.2.2 → 1.3.0 (standalone session brief)

> Self-contained. You do **not** need to read `PLAN.md`. This is the **critical-path** step —
> finishing it unblocks the next wave of work.

## Mission

Move the binding onto the published `centaur_technical_indicators` Rust crate **1.3.0**
(currently pinned to `1.2.2`). Isolated so any fallout is attributable.

## Context

- `1.3.0` is published to crates.io (already in the local cargo cache; `cargo` will resolve it).
- A prior audit verified every upstream signature this binding calls is **byte-identical**
  between 1.2.2 and 1.3.0 (the only diffs are internal NaN-hardening and added
  `#[allow(unreachable_patterns)]`). The suite is expected to stay green — existing tests don't
  exercise the degenerate paths the inherited fixes touch.

## Repo facts

- Rust + Python (PyO3/maturin). A virtualenv exists at `.venv` (has `maturin` + `pytest`).
- Pre-PR gates (`AGENTS.md`): `maturin develop`, `python -m pytest`, `cargo fmt --check` — all
  must pass.
- Work in your **own git worktree with its own venv** (a shared venv's installed extension gets
  clobbered by concurrent `maturin develop` runs).
- Baseline: `pytest` → **100 passed**.

## Steps

1. In `Cargo.toml`, bump `[dependencies] centaur_technical_indicators` from `"1.2.2"` to
   `"1.3.0"`. **Do NOT touch `[package] version`** (it stays `1.2.2` until the release cut, a
   later step). This deliberately deviates from `docs/REPO_MAP.md`'s "also bump the package
   `version`" rule because this is a staged multi-PR release — **say so in the PR description**,
   otherwise it reads as an omission (a review bot already flagged it on the first attempt).
2. `source .venv/bin/activate && maturin develop && python -m pytest` → expect **100 passed**.
3. `cargo fmt --all -- --check` → clean (you are not editing Rust source).
4. **If any existing test expectation shifts:** it is an inherited behavior fix from upstream.
   Re-derive the expected value by running against the now-installed 1.3.0 crate — **do not
   hand-edit a value to pass, and do not guess.** If a shift is surprising or large, **stop and
   report.**
5. **Document the inherited behavior change — this bump is NOT dependency-only.** The
   directly-exposed wrappers call upstream functions whose behavior changed, observable at the
   Python layer: `chart_trends.peaks` / `chart_trends.valleys` now return corrected outputs for
   an extremum at index 0 and for one retained after a monotonic run; and
   `trend_indicators.single.aroon_up` / `aroon_down` and
   `momentum_indicators.single.stochastic_oscillator` now return `NaN` instead of panicking on
   all-NaN input. Capture this in the `Fixed` CHANGELOG entry below. (Regression **tests** for
   these are a separate later step — not part of this PR.)
6. Add the CHANGELOG entries below; open a PR.

## CHANGELOG (under the existing `## [Unreleased]`)

```
### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.2.2` to `1.3.0`.

### Fixed
- Inherited Rust 1.3.0 behavior changes, now user-visible through the bindings:
  `chart_trends.peaks` / `chart_trends.valleys` corrected for index-0 and
  retained-after-monotonic-run extrema; and `aroon_up` / `aroon_down` / `stochastic_oscillator`
  return `NaN` instead of panicking on all-NaN input.
```

## Commit / PR

- Branch off latest `main`: `git checkout -b chore/bump-cti-1.3.0` (if you are already in the
  pre-created worktree, the branch exists — skip this and `git push -u origin chore/bump-cti-1.3.0`
  on first push).
- Stage `Cargo.toml`, `Cargo.lock` (regenerated), `CHANGELOG.md`. Do **not** `git add` untracked
  scratch files (`PLAN.md`, `*_BRIEF.md`).
- Commit prefix `chore:`; end the message with:
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
- PR body: **Summary** / **Compatibility** (call out two things: outputs change for the
  degenerate index-0 / retained-extremum / all-NaN cases — inherited upstream bug fixes, **not**
  breaking; and the package `version` bump is **intentionally deferred** to the release cut) /
  **Validation** (`maturin develop` clean, `pytest` 100 passed, `cargo fmt` clean) /
  **Changelog** (the entries above).

## Done criteria

- `Cargo.toml` dependency = `1.3.0`; `[package] version` still `1.2.2`.
- `maturin develop` clean; `pytest` → 100 passed (or any shift re-derived + explained, or
  stopped-and-reported).
- `cargo fmt --check` clean. CHANGELOG updated (dep-bump **and** the inherited-behavior `Fixed`
  entry). PR description notes the deferred version bump. Branch + PR opened.

## Do NOT

- Don't bump `[package] version`. Don't edit any `src/*.rs`, tests, README, or other files.
- Don't hand-edit test expectations to pass. Don't add dependencies.

## Effort: **medium**
