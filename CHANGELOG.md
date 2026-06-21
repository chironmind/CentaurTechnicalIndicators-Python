# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Security
- Bumped PyO3 from 0.25 to 0.29, resolving GHSA-36hh-v3qg-5jq4 (out-of-bounds read in the
  `nth`/`nth_back` iterators of `PyList`/`PyTuple`) and GHSA-chgr-c6px-7xpp (missing `Sync` bound
  on `PyCFunction::new_closure`). Neither vulnerable path is exercised by these bindings; the bump
  clears both advisories at the dependency level.

### Changed
- Declared `rust-version = "1.83"` in `Cargo.toml` — the minimum supported Rust the PyO3 0.29
  bump requires (no impact on prebuilt wheels; relevant only when building from source).

---

## [1.3.0] - 2026-06-20

### Fixed
- Incorrect `Documentation` URL in package metadata (pointed at the GitHub wiki).
- README quick-start example called `cti.moving_average(...)` (a submodule, not callable)
  instead of `cti.moving_average.single.moving_average(...)`.
- Docstring keyword-name mismatches that could raise `TypeError` (`supertrend`
  `constant_type_model` → `constant_model_type`; `true_range` `previous_close` → `close`).
- README "Available Indicators" / "Library Structure" drift and benchmark-vs-list inconsistency.
- Inherited Rust 1.3.0 behavior changes, now user-visible through the bindings:
  `chart_trends.peaks` / `chart_trends.valleys` corrected for index-0 and
  retained-after-monotonic-run extrema; and `aroon_up` / `aroon_down` /
  `stochastic_oscillator` return `NaN` instead of panicking on all-NaN input.

### Added
- Python regression tests for inherited Rust 1.3.0 chart-trend / degenerate-input fixes.
- `chart_trends.peak_favorable_move` and `chart_trends.valley_favorable_move` bindings (maximum
  favorable excursion over a forward window), mirroring Rust 1.3.0.
- `cargo fmt --check` step to CI (the `verify` job in `CI.yml`).
- `docs/2.0.0.md` breaking-change backlog.
- Tests pinning accepted model-type / deviation-model / moving-average-type string aliases.
- Documentation of the full accepted string-alias set for each regime (incl. the `sma`→Smoothed
  / `ma`→Simple aliases), with `from_string` error messages reconciled to match.
- README scope note: statistical primitives (the Rust `basic_indicators` surface) are
  intentionally not re-bound.
- Type stubs (`.pyi`) and a `py.typed` marker (PEP 561 inline typing) for the full API surface.
- `__version__` on the top-level package, resolved via `importlib.metadata`.
- Mixed package layout with a hand-authored `__init__.py` (adopts maturin `python-source`).

### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.2.2` to `1.3.0`.
- Expanded PyPI classifiers to declare Python 3.10–3.14.
- Updated ecosystem naming from "Centaur Capital" to "CRT (Centaur Research & Technologies)"
  and the legacy `centaurlabs.pages.dev` documentation link.
- Adjusted the indicator-count claim from "60+" to "50+".
- Exclude internal `docs/` from the source distribution (sdist).

## [1.2.2] - 2026-04-04

### Fixed
- Inherited fix for `relative_strength_index` (single and bulk) producing incorrect values via upstream crate update. The internal `previous_gains_loss` helper was only collecting non-zero gains/losses, discarding zero entries and causing misaligned averages.

### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.2.1` to `1.2.2`

### Removed
- Removed `AI_FRIENDLY_ROADMAP.md`, `docs/AI_ONBOARDING.md`, and `.github/copilot-instructions.md` — redundant with `AGENTS.md`
- Removed dangling references to removed files from `AGENTS.md`, `docs/REPO_MAP.md`, and `ai-policy.yaml`
- Simplified PR template from 7 sections to 4 (`Summary`, `Compatibility`, `Validation`, `Changelog`)

---

## [1.2.1] - 2026-03-01

### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.2.0` to `1.2.1`
  - Removed `#[allow(deprecated)]` from `volume_price_trend` binding functions (`src/trend_indicators.rs`) as the upstream crate removed the deprecation marker in `1.2.1`

### Added
- Added `AI_FRIENDLY_ROADMAP.md` with module API surface, contributor-workflow, and library-feature roadmap adapted for this Python binding repository
- Added `docs/AI_ONBOARDING.md` as canonical start-here onboarding flow for coding agents
- Added `docs/REPO_MAP.md` with a quick repository map, extension points, and "if changing X, also check Y" guidance
- Added machine-readable repository policy file `ai-policy.yaml` for required checks, change obligations, and PR section requirements
- Added default pull request template at `.github/pull_request_template.md` with required sections (`Summary`, `Scope`, `Compatibility`, `Validation`, `Changelog`)
- Expanded `AGENTS.md` with change-scope discipline, backward compatibility rules, pre-PR quality gates, CI implementation policy, and required PR summary format
- Updated `CONTRIBUTING.md` with local quality gates and AI-assisted contribution checklist

---

## [1.2.0] - 2026-02-26

### Changed
- Updated `centaur_technical_indicators` Rust crate dependency from `1.0.0` to `1.2.0`
  - Added `#[allow(deprecated)]` to binding functions wrapping deprecated upstream functions (`slow_stochastic`, `slowest_stochastic`, `signal_line`, `volume_price_trend`, `volatility_system`) to preserve the existing Python API surface unchanged

### Added
- Added `/// See: <URL>` reference links to all Python binding function docstrings, mirroring the reference links introduced in the 1.2.0 upstream crate

---

## [1.0.0] - 2026-01-19

### Changed
- **Breaking:** Rebranded from PyTechnicalIndicators to CentaurTechnicalIndicators-Python
  - Updated all documentation, README, and links to reflect the new CentaurTechnicalIndicators branding
  - Updated package metadata to reflect the new name and branding

---

*** /!\ The release notes below cover the PyTechnicalIndicators packages before the rebranding /!\ ***

## [3.0.5] - 2025-10-19

### Changed
- Updated rust_ti dependency from 2.1.5 to 2.2.0

### Added
- Added support for new probability distribution deviation models from rust_ti 2.2.0:
	- `LogStandardDeviation` - Log-scale standard deviation for analyzing log-returns
	- `LaplaceStdEquivalent` - Laplace (double exponential) distribution scaled to standard deviation
	- `CauchyIQRScale` - Cauchy distribution scaled by interquartile range for extreme outliers
- Added string aliases for new deviation models: `"log"`, `"logstd"`, `"laplace"`, `"cauchy"`
- Enhanced `PyDeviationModel::from_string()` to support the new deviation models

### Fixed
- Updated test expectations for median and mode absolute deviation calculations due to improved algorithms in rust_ti 2.2.0

---

## [3.0.4] - 2025-10-08

### Changed
- Updated rust_ti dependency from 2.1.4 to 2.1.5
	- Updated `break_down_trends` function to use new `TrendBreakConfig` struct from rust_ti 2.1.5
	- Updated parameter names in `break_down_trends`

---

## [3.0.3] - 2025-08-13

### Added
- Updated README.md to add links to How-Tos, a summary of benchmarks, and a badge linking to Read the Docs.

---

## [3.0.2] - 2025-08-07

### Changed
- Minor document updates
- Updated RustTI version to include volatilty system fix

### Added
- Better badges to README

---

## [3.0.1] - 2025-08-04

### Changed
- Updated the package version number...

---

## [3.0.0] - 2025-08-04

### Added
- Added bindings using PyO3 and Maturin

### Changed
- Major changes to all functions, they are now bindings for the same functions in RustTI

### Removed
- Pure python functionality

---

Older releases aren't tracked in this file but some information can be found [here](https://github.com/chironmind/PyTechnicalIndicators/releases)

