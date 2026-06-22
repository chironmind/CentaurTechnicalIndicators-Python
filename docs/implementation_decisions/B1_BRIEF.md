---
type: brief
id: B1
title: "PyO3 0.25 → 0.29 security bump (clears Dependabot #4 HIGH, #5)"
status: ready
effort: medium
wave: A
depends_on: []
touches:
  - Cargo.toml
  - Cargo.lock
  - CHANGELOG.md
forbidden:
  - "src/**, tests/**  (zero source/test changes — the whole point is that 0.29 needs none)"
  - "[package] version in Cargo.toml  (stays 1.3.0 — Final owns the version cut)"
  - "the centaur_technical_indicators dependency line  (stays 1.3.0 — no core bump)"
  - "test_requirements.txt  (B2 owns it)"
  - "AGENTS.md  (B3 owns it)"
  - ".github/workflows/**  (no CI edits — Q3 resolved to runner-default Rust)"
  - "pyproject.toml"
branch: "chore/bump-pyo3-0.29"
pr_target: "main"
changelog: "required — ### Security (+ ### Changed for MSRV)"
related:
  - "[[PLAN-1.3.1]]"
decisive_test: "B1-A1"
created: 2026-06-21
tags: [brief, security]
---

# B1 — PyO3 0.25 → 0.29 security bump

> **Self-contained.** Repo conventions (branch/commit/PR shape, the `maturin develop` →
> `python -m pytest` → `cargo fmt --all -- --check` gates, stop-and-report, changelog coupling,
> worktree+own-`.venv` isolation) live in `AGENTS.md` / `CLAUDE.md` — follow them; this brief adds
> only what is specific to this batch. **Independent of B2/B3** — runs concurrently in Wave A.

## Mission

Bump PyO3 from `0.25.0` to `0.29` to clear the two Rust-side Dependabot advisories, and document
the Rust MSRV the bump introduces. **No `src/` changes are expected** — if any are needed to
compile, **stop and report** (it contradicts the verified audit).

- **GHSA-36hh-v3qg-5jq4** (Dependabot **#4**, **HIGH**, CVSS 8.7) — OOB read in `nth`/`nth_back`
  for `PyList`/`PyTuple` iterators.
- **GHSA-chgr-c6px-7xpp** (Dependabot **#5**, medium) — missing `Sync` bound on
  `PyCFunction::new_closure` closures.

Both are first patched in `0.29.0`, which is also the latest stable PyO3 (released 2026-06-11) —
so the minimal fix and the most-current version are the same release.

## Context (why this is low-risk)

- The binding is entirely on the modern **`Bound` API** (`#[pymodule] fn(m: &Bound<'_, PyModule>)`,
  `wrap_pyfunction!`, `add_function`, `add_submodule`, `PyModule::new`, `PyValueError::new_err`).
  The whole `IntoPyObject` return-value migration (incl. `PyList::new`/`PyTuple::new` becoming
  fallible) landed in PyO3 **0.23.0** — *below* the current 0.25 pin — so nothing in the 0.25→0.29
  window touches the `Vec<f64>` / tuple / `f64` / `bool` returns this code uses.
- **Neither vulnerable path is invoked**: the code never iterates `PyList`/`PyTuple` with
  `nth`/`nth_back`, and never calls `PyCFunction::new_closure`. The advisories are dependency-level;
  the bump clears them without any code path change.
- No `#[pyclass]`, no `.extract()`/`.downcast()`, no GIL APIs, no `Py<T>`, no `Vec<u8>` returns. The
  four `Py*` enums are plain `#[derive(Clone)]` Rust enums that never cross the PyO3 boundary, so the
  one genuinely breaking 0.29 change (removal of the implicit by-value `FromPyObject` impl for
  `#[pyclass]`) cannot bite.
- **MSRV:** PyO3 0.29 requires **Rust ≥ 1.83** (raised in 0.28). GitHub-hosted runners ship current
  stable Rust (≫ 1.83), so this holds with **no CI change** (owner decision Q3 = option (a)). We
  document the floor with `rust-version = "1.83"`; we do **not** add a `rust-toolchain` pin or a CI
  setup step.
- `maturin` 1.11.x / the `>=1.9,<2.0` build pin impose no upper bound on PyO3 0.29.

## Verify first (re-confirm at session start)

| Claim | How to check | Expected |
|-------|--------------|----------|
| pyo3 pin is `0.25.0` | `grep -n 'pyo3' Cargo.toml` | `pyo3 = "0.25.0"` |
| baseline suite is green | `source .venv/bin/activate && maturin develop && python -m pytest` | `N passed` (record **N**) |
| no risky PyO3 APIs in src | `rg -n 'PyList\|PyTuple\|PyCFunction\|new_closure\|\.extract\(\)\|\.downcast\|#\[pyclass\]\|Vec<u8>' src/` | **no matches** |

If any of these is not as expected — especially a risky-API match — **stop and report** before bumping.

## Changes (in order)

1. **`Cargo.toml`** — set `pyo3 = "0.29"` (from `"0.25.0"`), and add `rust-version = "1.83"` to the
   `[package]` table. **Do not** touch `[package] version` (stays `1.3.0`) or the
   `centaur_technical_indicators` dependency (stays `1.3.0`).
2. **Rebuild → regenerate `Cargo.lock`.** `maturin develop` re-resolves pyo3 + `pyo3-ffi` /
   `pyo3-macros` / `pyo3-macros-backend` / `pyo3-build-config` to `0.29.x`. **Stage the regenerated
   `Cargo.lock`; do not hand-edit it** (`AGENTS.md`).
3. **Zero-source gate (decisive).** `maturin develop` must compile with **no `src/*.rs` edit**. If
   the compiler demands *any* source change, **stop and report** — do not work around it.
4. **`python -m pytest`** → expect the **same `N passed`** as the baseline above. A shifted
   expectation here would be surprising (pure dependency bump) → stop and report.
5. **`cargo fmt --all -- --check`** → clean (you edit no Rust source).
6. **`CHANGELOG.md`** — add the entries below. **If `## [Unreleased]` does not exist yet** (B2 may
   not have merged first), create it directly above `## [1.3.0]`; **otherwise append** under the
   existing `## [Unreleased]`. Do **not** create a second `[Unreleased]` and do **not** hand-cut a
   `[1.3.1]` header (that is Final).

## CHANGELOG (under `## [Unreleased]`)

```
### Security
- Bumped PyO3 from 0.25 to 0.29, resolving GHSA-36hh-v3qg-5jq4 (out-of-bounds read in the
  `nth`/`nth_back` iterators of `PyList`/`PyTuple`) and GHSA-chgr-c6px-7xpp (missing `Sync` bound
  on `PyCFunction::new_closure`). Neither vulnerable path is exercised by these bindings; the bump
  clears both advisories at the dependency level.

### Changed
- Declared `rust-version = "1.83"` in `Cargo.toml` — the minimum supported Rust the PyO3 0.29
  bump requires (no impact on prebuilt wheels; relevant only when building from source).
```

## Acceptance tests (named; all must pass)

- **B1-A1 (decisive)** — `maturin develop` compiles cleanly with **zero `src/*.rs` edits**, and
  `python -m pytest` → `N passed` (same N as baseline).
- **B1-A2** — `Cargo.toml`: `pyo3 = "0.29"`, `rust-version = "1.83"`, `[package] version` still
  `1.3.0`, dependency `centaur_technical_indicators` still `1.3.0`; `Cargo.lock` pyo3 ≥ `0.29.0`.
- **B1-A3** — `cargo fmt --all -- --check` clean; only `Cargo.toml`, `Cargo.lock`, `CHANGELOG.md`
  changed; no new dependency added.
- **B1-A4 (post-merge — CI)** — the `verify` job and all wheel-build jobs (linux/musllinux/windows/
  macos across the interpreter matrix) are green, confirming the Rust ≥ 1.83 MSRV on every runner
  (plan assumption **A7**). *Verification, not a step this session forces.*

## Out of scope / Do NOT

- **Do NOT** edit any `src/*.rs`, `tests/**`, README, `pyproject.toml`, `test_requirements.txt`,
  `AGENTS.md`, or CI workflows.
- **Do NOT** bump `[package] version` (Final) or the core-crate dependency.
- **Do NOT** hand-edit `Cargo.lock`, add a `rust-toolchain` file, or add a CI Rust-setup step
  (Q3 = runner-default).
- **Do NOT** silence a compile error by editing source — that is a stop-and-report signal.

## Definition of done

- [ ] B1-A1 (zero-source compile + `N passed`), B1-A2, B1-A3 green.
- [ ] `CHANGELOG.md` has the Security + Changed entries under `## [Unreleased]` (heading created or
      appended-to as appropriate).
- [ ] Branch `chore/bump-pyo3-0.29` off latest `origin/main`; PR opened against `main`; commit
      prefixed `chore:` with the `Co-Authored-By: Claude Opus 4.8 (1M context)` trailer.
- [ ] PR report per `AGENTS.md` (Summary / Scope / Compatibility / Validation / Changelog), AI
      assistance disclosed.

## Report (per AGENTS.md)

Summary · Scope (only `Cargo.toml`/`Cargo.lock`/`CHANGELOG.md`; src untouched) · Compatibility
(N/A — no API/behavior change; dependency security bump) · Validation (paste `maturin develop`
result, the `pytest N passed` line, `cargo fmt` clean) · Changelog (the entries above) — plus the
B1-A1–A3 results and anything flagged (e.g. if any risky-API match or compile surprise occurred).
