# Copilot Instructions for PyTechnicalIndicators

## Repository Overview

**PyTechnicalIndicators** is a production-ready Python library providing 60+ technical indicators for financial analysis, built on a high-performance Rust backend (RustTI). The project uses PyO3 and maturin to create Python bindings for the underlying Rust implementation.

**Key Stats:**
- **Languages:** Rust (backend), Python (bindings/tests)  
- **Build System:** maturin (Rust-Python integration)
- **Python Support:** 3.10+ (tested through 3.14)
- **Test Suite:** 107 tests, ~0.31s runtime
- **License:** MIT

## Build Instructions & Validated Commands

### Bootstrap & Environment Setup (Required)
**Always create a virtual environment before building:**
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Install Dependencies (Required)
```bash
pip install -r test_requirements.txt
```
**Contents:** maturin==1.9.1, pytest==8.4.1, and supporting packages

### Build the Project (Required)
```bash
maturin develop
```
- **Duration:** ~14 seconds for full compilation
- **Function:** Compiles Rust code and installs Python package in editable mode
- **Output:** Installs `pytechnicalindicators` package locally

### Run Tests (Validation)
```bash
python -m pytest
```
- **Expected:** 107 tests pass in ~0.31s
- **Coverage:** All indicator modules with bulk/single function variants

### Format Code (Optional)
```bash
cargo fmt          # Format Rust code
rustfmt --check    # Check Rust formatting
```

### Environment Versions (Reference)
- **Python:** 3.12.3+ 
- **Rust:** 1.89.0+
- **maturin:** 1.9.1

## Project Layout & Architecture

### Root Directory Structure
```
/
├── .github/           # Workflows, issue templates, CODEOWNERS
├── src/              # Rust source modules
├── tests/            # Python test files (mirror src/ structure)
├── assets/           # Documentation assets, banner images
├── pyproject.toml    # Python project configuration, maturin settings
├── Cargo.toml        # Rust project configuration, dependencies
├── requirements.txt  # Runtime dependencies (minimal)
├── test_requirements.txt  # Development/test dependencies
└── README.md         # Comprehensive project documentation
```

### Source Code Architecture (`src/`)
**Modular Design by Analysis Area:**
- `lib.rs` - Main module, PyO3 bindings setup, type definitions
- `candle_indicators.rs` - Ichimoku, Bollinger Bands, Keltner, Supertrend
- `momentum_indicators.rs` - RSI, MACD, CCI, Williams %R, Stochastic
- `moving_average.rs` - Simple, Exponential, Smoothed, McGinley Dynamic
- `standard_indicators.rs` - Basic indicators, moving averages
- `trend_indicators.rs` - Aroon, Parabolic SAR, DM, TSI
- `volatility_indicators.rs` - Ulcer Index, Volatility System
- `strength_indicators.rs` - A/D, PVI, NVI, RVI
- `chart_trends.rs` - Trend analysis, peak/valley detection
- `correlation_indicators.rs` - Asset price correlation
- `other_indicators.rs` - ROI, True Range, ATR

### API Design Patterns
- **Dual Function Variants:** Each indicator has `bulk` (returns list) and `single` (returns scalar) versions
- **Type System:** Custom enums (`PyConstantModelType`, `DeviationModel`, `MovingAverageType`) for configuration
- **Error Handling:** Uses `PyValueError` for invalid inputs with descriptive messages

### Test Structure (`tests/`)
- **Naming Convention:** `test_<module_name>.py` mirrors `src/<module_name>.rs`
- **Purpose:** Binding verification, not exhaustive testing (core logic tested in RustTI)
- **Pattern:** Basic smoke tests to ensure Python-Rust interface works

## CI/CD & Validation Pipelines

### GitHub Workflows
1. **`python-package.yml`** - Pull request validation
   - Tests across Python 3.10-3.14 on Ubuntu
   - Steps: checkout → setup Python → install deps → maturin develop → pytest

2. **`CI.yml`** - Release pipeline (maturin-generated)
   - Multi-platform wheel building (Linux, Windows, macOS)
   - Multiple architectures (x86_64, ARM, etc.)
   - Automatic PyPI publication on tags

### Pre-commit Validation Steps
```bash
# Recommended validation sequence:
source .venv/bin/activate
pip install -r test_requirements.txt
maturin develop
python -m pytest
cargo fmt --check  # Optional: check Rust formatting
```

## Development Guidelines

### Making Code Changes
1. **Rust Changes:** Edit files in `src/`, then run `maturin develop` to rebuild
2. **Python Tests:** Add corresponding tests in `tests/` following existing patterns
3. **API Consistency:** Maintain `bulk`/`single` function variants for new indicators
4. **Type Safety:** Use existing enum types or add new ones following the pattern in `lib.rs`

### Performance Considerations
- **Rust Backend:** Core calculations optimized for microsecond-level performance
- **Bulk vs Single:** Use `bulk` for time series, `single` for latest values
- **Memory:** Rust handles memory management; Python side is minimal overhead

### Dependencies & Updates
- **Rust Dependencies:** Managed in `Cargo.toml` (pyo3, rust_ti)
- **Python Dependencies:** Keep `test_requirements.txt` minimal
- **Version Constraints:** Python 3.10+ required for modern features

## Common Workflows & Commands

### Complete Development Setup
```bash
git clone <repo>
cd PyTechnicalIndicators
python -m venv .venv
source .venv/bin/activate
pip install -r test_requirements.txt
maturin develop
python -m pytest
```

### Iterative Development
```bash
# After making Rust changes:
maturin develop  # Rebuild and reinstall
python -m pytest  # Verify no regressions

# After making Python test changes:
python -m pytest  # Run updated tests
```

### Release Preparation
```bash
cargo fmt  # Format Rust code
python -m pytest  # Ensure all tests pass
# CI handles wheel building and PyPI publication
```

## Key Files & Configuration

### Build Configuration
- **`pyproject.toml`:** Python packaging, maturin settings, project metadata
- **`Cargo.toml`:** Rust compilation, dependencies (pyo3, rust_ti)
- **`.gitignore`:** Excludes `target/`, `.venv/`, `__pycache__/`, build artifacts

### Documentation Resources
- **`README.md`:** Complete user documentation, examples, API reference
- **`CONTRIBUTING.md`:** Contribution guidelines, new indicator process
- **Wiki:** Full API reference and usage examples
- **External:** Tutorials, benchmarks, and how-to guides in separate repos

## Trust These Instructions

These instructions are validated and complete. Only perform additional repository exploration if:
- The build process fails unexpectedly
- Dependencies have changed significantly
- New requirements are introduced in documentation

The provided build sequence works reliably and efficiently for the current codebase.