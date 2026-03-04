# AI-Friendly Roadmap

This document is a practical map for contributors and coding agents working in `CentaurTechnicalIndicators-Python`.

## How to use this roadmap

- `Now`: high-confidence, near-term items that improve contributor and agent reliability.
- `Next`: medium-term items that build on completed `Now` work.
- `Later`: directional items that should not block current PRs.
- Each milestone includes acceptance criteria and non-goals to keep the implementation scope clear.

## Current API surface by module

This package exposes Python bindings for the following indicator modules from the upstream Rust crate, each with `single` and/or `bulk` submodules where applicable:

- `candle_indicators`: candle-derived indicators (bands/channels/envelopes and related tools).
- `chart_trends`: peak/valley and trend-structure analysis.
- `correlation_indicators`: pairwise/statistical relationship indicators.
- `momentum_indicators`: momentum and oscillator families.
- `moving_average`: core moving-average implementations.
- `other_indicators`: miscellaneous indicators.
- `strength_indicators`: strength/volume participation indicators.
- `trend_indicators`: trend direction/strength systems.
- `volatility_indicators`: volatility and range-expansion indicators.

Shared Python-side support:

- `lib.rs`: PyO3 module wiring, shared type enum definitions.
- `PyConstantModelType`, `DeviationModel`, `MovingAverageType`: shared enums passed as strings from Python.

## Binding design conventions

1. **Preserve the bulk/single API pattern** — each indicator exposes a `bulk` (returns list) and `single` (returns scalar) variant.
2. **Accept enum arguments as strings** — all model/type parameters are accepted as Python strings and resolved in Rust with user-friendly error messages on invalid input.
3. **Use `PyValueError`** for all user-facing error surfaces at the Python boundary.
4. **Do not silently change indicator semantics** — bindings delegate all calculation logic to the upstream Rust crate.

## Testing/validation expectations

Before opening a PR, contributors should run and report:

1. `maturin develop` (bindings compile cleanly)
2. `python -m pytest` (all tests pass)
3. `cargo fmt --check` (no formatting diffs)

## Contributor workflow roadmap

This section tracks changes that make the repository easier for both human contributors and coding agents to work in safely.

### Now

1. **PR quality report standardization**
   - Goal: all AI/human PRs present the same validation summary shape.
   - Acceptance criteria:
     - `AGENTS.md` defines a required PR summary format.
     - PR descriptions consistently include `Summary`, `Scope`, `Compatibility`, `Validation`, and `Changelog`.
   - Non-goals:
     - Enforcing via CI in this milestone.
2. **Repository orientation map**
   - Goal: reduce onboarding/search time for contributors and agents.
   - Acceptance criteria:
     - `docs/REPO_MAP.md` exists with key directories, extension points, and "if changing X, also check Y" guidance.
   - Non-goals:
     - Exhaustive architecture documentation.
3. **Machine-readable contribution policy**
   - Goal: enable deterministic checks by automation/bots.
   - Acceptance criteria:
     - `ai-policy.yaml` lists required checks and user-facing change obligations.
     - Policy contents match `AGENTS.md`/`CONTRIBUTING.md`.
   - Non-goals:
     - Full custom policy engine implementation.

### Next

1. **CI guardrails for contribution policy**
   - Goal: make contributor requirements executable rather than advisory.
   - Acceptance criteria:
     - CI checks for required validation commands.
     - CI checks for `CHANGELOG.md` updates on user-facing changes.
   - Non-goals:
     - Blocking on benchmark jobs in the main CI pipeline.

### Later

1. **Agent bootstrap command**
   - Goal: provide a one-command local setup and verification flow for new contributors/agents.
   - Acceptance criteria:
     - Script or task runner target that documents and runs core checks in order.
   - Non-goals:
     - Replacing existing contributor docs.
