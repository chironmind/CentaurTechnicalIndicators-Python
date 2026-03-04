# AI Onboarding

Start here when an AI agent begins work in `CentaurTechnicalIndicators-Python`.

## Goal

Provide one deterministic startup flow so agents can orient quickly, avoid policy misses, and make minimal, safe changes without altering public APIs unintentionally.

## Startup Flow (in order)

1. Read repository rules:
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   - `CONTRIBUTING.md`
2. Read project orientation:
   - `docs/REPO_MAP.md`
   - `AI_FRIENDLY_ROADMAP.md`
3. Use machine-readable policy source:
   - `ai-policy.yaml` (machine-readable contribution policy)
4. Confirm affected modules in `src/` and keep scope focused.

## Non-Negotiable Rules

- Preserve the `bulk`/`single` API pattern for all indicator functions.
- Keep public API behavior stable unless explicitly asked to introduce a breaking change.
- Add/adjust tests in `tests/` to match any binding changes in `src/`.
- Add a `CHANGELOG.md` entry for each user-facing change.
- Always rebuild bindings after Rust source changes: `maturin develop`.

## Agent-Friendly Change Strategy

1. Identify the smallest module/file that can satisfy the task.
2. Prefer additive or internal-only edits over broad refactors.
3. If changing output semantics, update tests and document compatibility impact.
4. If touching public function signatures or enum strings, include clear compatibility notes.

## Required Local Validation Gates

Run from repository root (after activating the virtual environment):

```bash
pip install -r test_requirements.txt
maturin develop
python -m pytest
cargo fmt --check
```

## PR/Report Output Format

Use this structure:

1. `Summary`
2. `Scope`
3. `Compatibility`
4. `Validation`
5. `Changelog`

## Quick Pointers

- Python module wiring and type enums: `src/lib.rs`
- Indicator binding implementations: `src/<module_name>.rs`
- Python-facing tests: `tests/test_<module_name>.py`
- Dependency versions: `Cargo.toml` (Rust), `test_requirements.txt` (Python)
- Package metadata: `pyproject.toml`
