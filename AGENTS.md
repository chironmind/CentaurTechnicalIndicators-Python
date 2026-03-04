# AGENTS.md

Guidance for coding agents working in this repository.

## Project at a glance
- **Repo type:** Python package with a Rust core exposed via PyO3/maturin.
- **Primary goal:** Keep Python bindings stable while preserving Rust-side correctness and performance.
- **Main source directories:**
  - `src/` → Rust implementation + Python bindings
  - `tests/` → Python-facing smoke/behavior tests for bindings

## Docs to review before coding
- `docs/AI_ONBOARDING.md`
- `.github/copilot-instructions.md`
- `AI_FRIENDLY_ROADMAP.md`
- `docs/REPO_MAP.md`
- `CONTRIBUTING.md`

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

## Change scope discipline
- Keep changes minimal and focused on the requested task.
- Do not include opportunistic refactors unless explicitly requested.
- If you identify unrelated issues, note them separately instead of bundling them into the same change.
- Preserve existing file organization and naming conventions unless the task requires a structural change.

## Backward compatibility rules
When changing public Python APIs, preserve compatibility unless the task explicitly allows a breaking change:

1. Do not silently change indicator semantics, output ordering, or warmup behavior.
2. Do not remove or rename public functions, types, enums, or parameters without explicit approval.
3. If behavior changes are required, document them in docstrings and `CHANGELOG.md` with clear migration notes.

## Pre-PR quality gates (must pass)
Run these before opening a PR:

1. `maturin develop` (bindings compile cleanly)
2. `python -m pytest` (all tests pass)
3. `cargo fmt --check` (no formatting diffs)

## CI implementation policy
- Prefer native Python/maturin/cargo commands in workflows.
- Do not introduce third-party GitHub Actions unless explicitly approved by maintainers.

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

## PR expectations for agents
- Keep PRs focused and minimal.
- Summarize what the agent changed and what was manually verified.
- Include command output summary for the required quality gates.
- Explicitly note the `CHANGELOG.md` entry.

### Required PR summary format
Use this structure in PR descriptions/comments:

1. `Summary`: what changed and why.
2. `Scope`: files/modules touched and what was intentionally not changed.
3. `Compatibility`: any user-facing behavior/API impact.
4. `Validation`: results summary for `maturin develop`, `pytest`, and `cargo fmt`.
5. `Changelog`: exact `CHANGELOG.md` entry added/updated.

## Repository expectations
- This is a public Python/Rust library. Prioritize correctness, determinism, and backward compatibility.
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

