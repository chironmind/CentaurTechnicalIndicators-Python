# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Changed
- Updated rust_ti dependency from 2.1.4 to 2.1.5
- Updated `break_down_trends` function to use new `TrendBreakConfig` struct from rust_ti 2.1.5
- **Breaking Change**: `break_down_trends` now accepts either a preset configuration string or all custom parameters:
  - Preset options: `"default"`, `"conservative"`, `"moderate"`, `"aggressive"`
  - Custom parameters (all 9 must be provided): `max_outliers`, `soft_adj_r_squared_minimum`, `hard_adj_r_squared_minimum`, `soft_rmse_multiplier`, `hard_rmse_multiplier`, `soft_durbin_watson_min`, `soft_durbin_watson_max`, `hard_durbin_watson_min`, `hard_durbin_watson_max`

### Added
- Added `PyTrendBreakConfig` enum in lib.rs that provides preset configurations for trend detection
- Preset configurations:
  - `"default"`: Balanced settings for general use
  - `"conservative"`: More tolerant to noise, produces fewer trend breaks
  - `"moderate"`: Same as default
  - `"aggressive"`: Less tolerant to noise, produces more trend breaks

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

