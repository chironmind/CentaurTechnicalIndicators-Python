# Repository Map

Quick orientation for contributors and coding agents working in `CentaurTechnicalIndicators-Python`.

## Top-level layout

- `src/`: Rust source files (PyO3 binding implementations for each indicator module).
- `tests/`: Python test files (smoke tests for each binding module).
- `assets/`: Supporting artifacts (documentation assets, banner images).
- `.github/workflows/`: CI workflows (PR validation, release pipeline).
- `docs/`: internal knowledge base (excluded from the sdist, never shipped) — see
  [`docs/README.md`](README.md). Holds `REPO_MAP.md` (this file), `technical_decisions/`
  (the 1.3.0 [decision record](technical_decisions/DECISIONS-1.3.0.md) + the
  [`2.0.0.md`](technical_decisions/2.0.0.md) breaking-change backlog), and `implementation_decisions/`
  (the master plan, the twelve slice briefs, and the resume/state doc).
- `Cargo.toml`: Rust package version and dependency configuration.
- `pyproject.toml`: Python package metadata and maturin build settings.
- `CHANGELOG.md`: required entry point for every user-facing change.
- `AGENTS.md`: agent operating rules and PR/reporting expectations.
- `CONTRIBUTING.md`: contributor expectations and required validation gates.

## Source module map (`src/`)

- `lib.rs`: PyO3 module wiring, shared enum type definitions (`PyConstantModelType`, `DeviationModel`, `MovingAverageType`).
- `candle_indicators.rs`: candle/band/channel/envelope-style indicator bindings.
- `chart_trends.rs`: peak/valley and trend-structure analysis bindings.
- `correlation_indicators.rs`: pairwise/statistical relationship indicator bindings.
- `momentum_indicators.rs`: momentum/oscillator indicator bindings.
- `moving_average.rs`: moving average bindings.
- `other_indicators.rs`: miscellaneous indicator bindings.
- `strength_indicators.rs`: strength/participation indicator bindings.
- `trend_indicators.rs`: trend direction/strength indicator bindings.
- `volatility_indicators.rs`: volatility/range-expansion indicator bindings.

## Test module map (`tests/`)

- `test_<module_name>.py` mirrors `src/<module_name>.rs` — each test file covers binding smoke tests for the matching source module.

## Extension points

- New indicator binding: add to the appropriate `src/*_indicators.rs` file and wire through `src/lib.rs`.
- New shared type/enum: add to `src/lib.rs` following the existing string-dispatch pattern.
- Python tests: add to the matching `tests/test_<module_name>.py` file.
- Public exports: wire through `src/lib.rs`.

## If changing X, also check Y

- If changing an indicator's parameter names or accepted string values:
  - Also update the corresponding docstring in `src/<module_name>.rs`.
  - Also update or add tests in `tests/test_<module_name>.py`.
- If updating the upstream `centaur_technical_indicators` Rust crate version:
  - Also update the package `version` in `Cargo.toml`.
  - Also check for deprecation changes and adjust `#[allow(deprecated)]` annotations accordingly.
  - Also add a user-facing entry in `CHANGELOG.md`.
- If adding/changing public Python-facing APIs:
  - Also update docstrings.
  - Also add a user-facing entry in `CHANGELOG.md`.
- If changing indicator math/outputs:
  - Also update/add tests in the matching test module.
- If adding new user-visible behavior:
  - Also update `README.md` and/or examples when appropriate.
  - Also update `CHANGELOG.md`.

## Required local validation gates

Run these before opening a PR:

1. `maturin develop` (bindings compile cleanly)
2. `python -m pytest` (all tests pass)
3. `cargo fmt --check` (no formatting diffs)

## Minimal PR content checklist

- What changed and why.
- Compatibility/user-impact notes.
- Validation command summary.
- Explicit `CHANGELOG.md` entry note.
