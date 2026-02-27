# AGENTS.md

Guidance for coding agents working in this repository.

## Project at a glance
- **Repo type:** Python package with a Rust core exposed via PyO3/maturin.
- **Primary goal:** Keep Python bindings stable while preserving Rust-side correctness and performance.
- **Main source directories:**
  - `src/` → Rust implementation + Python bindings
  - `tests/` → Python-facing smoke/behavior tests for bindings

## Recommended workflow
1. **Set up an isolated environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   pip install -r test_requirements.txt
   ```
2. **Build extension module**
   ```bash
   maturin develop
   ```
3. **Run tests**
   ```bash
   python -m pytest
   ```
4. **(Optional) Check formatting**
   ```bash
   cargo fmt --check
   ```

## What to change (and where)
- Add/update indicator logic in the relevant Rust module under `src/`.
- Keep API exposure and types consistent through `src/lib.rs`.
- Add/adjust Python tests in matching files under `tests/`.
- Update docs (`README.md`, `CHANGELOG.md`) when behavior or API changes.

## Coding expectations
- Preserve the existing **bulk/single** API pattern for indicators.
- Prefer small, focused diffs over large refactors.
- Keep naming and argument conventions consistent with neighboring functions.
- Use clear, user-facing error messages for invalid inputs.

## Validation expectations before finishing
- Rebuild bindings after Rust changes: `maturin develop`.
- Run relevant tests (ideally full `python -m pytest`).
- If tests are skipped for environmental reasons, explicitly report why.

## Pull request checklist for agents
- [ ] Scope is minimal and matches the task.
- [ ] Rust bindings compile (`maturin develop`).
- [ ] Tests pass or limitations are documented.
- [ ] Documentation/changelog updated when needed.
- [ ] Commit message clearly describes the change.

## Repository expectations
- This is a public Rust library. Prioritize correctness, determinism, and backward compatibility.
- Prefer minimal, focused diffs over broad refactors.
- Do not add new dependencies unless explicitly requested.
- Treat public APIs, documented behavior, and examples as stability-sensitive.

## Review guidelines
- Flag breaking API changes.
- Flag silent behavior changes in indicator calculations or defaults.
- Flag documentation drift when public behavior changes.
- Flag unnecessary allocations or obvious performance regressions in hot paths.

## Change boundaries
- Do not modify CI, licensing, security, or contributor-governance files unless explicitly requested.
- Keep unrelated formatting churn to a minimum.
