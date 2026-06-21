---
type: brief
id: B2
title: "pytest 9.0.3 + Pygments 2.20.0 security bumps (clears Dependabot #3, #2)"
status: ready
effort: low
wave: A
depends_on: []
touches:
  - test_requirements.txt
  - CHANGELOG.md
forbidden:
  - "requirements.txt  (only lists maturin; the ghost alerts #6/#7 are handled in Final)"
  - "pluggy / iniconfig / packaging / maturin pins  (pytest 9.0.3 forces no bump)"
  - "src/**, tests/**, Cargo.*  (B1 owns Cargo.*; no code/test changes)"
  - "AGENTS.md  (B3 owns it)"
  - ".github/workflows/**, pyproject.toml"
branch: "chore/bump-test-deps-security"
pr_target: "main"
changelog: "required — ### Security (security-release transparency; see note)"
related:
  - "[[PLAN-1.3.1]]"
decisive_test: "B2-A1"
created: 2026-06-21
tags: [brief, security]
---

# B2 — pytest 9.0.3 + Pygments 2.20.0 security bumps

> **Self-contained.** Repo conventions (gates, branch/commit/PR, stop-and-report, worktree+own
> `.venv`) live in `AGENTS.md` / `CLAUDE.md`. **Independent of B1/B3** — runs concurrently in Wave A.
> Mechanical bump; the one real check is that the suite passes under pytest 9.

## Mission

Bump the two vulnerable **test-only** pins in `test_requirements.txt` and confirm the suite still
passes under pytest 9:

- **pytest** `8.4.1` → `9.0.3` — **GHSA-6w46-j5rx-g56g** (Dependabot **#3**, medium; vulnerable
  tmpdir handling).
- **Pygments** `2.19.2` → `2.20.0` — **GHSA-5239-wwwm-4pmq** (Dependabot **#2**, low; ReDoS in the
  GUID-matching regex).

## Context (why this is safe)

- **pytest 9.x keeps the Python 3.10 floor** (only 3.9 was dropped) — matches `requires-python
  >=3.10` and the `python-package.yml` 3.10–3.14 matrix exactly.
- **No forced transitive-pin bumps.** pytest 9.0.3 requires `pluggy>=1.5,<2`, `iniconfig>=1.0.1`,
  `packaging>=22`, `pygments>=2.7.2`; the current pins (`pluggy==1.6.0`, `iniconfig==2.1.0`,
  `packaging==25.0`) already satisfy them. **Leave those pins untouched.**
- The suite is plain assert-based **smoke tests** — no `conftest.py`, no plugins, no markers, no
  `yield`/nose idioms, all invocations are plain `python -m pytest`. None of the pytest-9 removals
  (the "PytestRemovedIn9Warning → error" change in particular) apply.
- **Pygments** is a pure transitive dep (never imported in the repo); pytest only ever invokes its
  Python/console lexers for traceback highlighting, never the ADL/archetype lexer the fix touches —
  so traceback rendering is unaffected.
- **Changelog note:** pytest/Pygments ship only in `test_requirements.txt`, never in the user wheel,
  so this is technically non-user-facing. We still record a `### Security` entry **intentionally**,
  for transparency about the advisories 1.3.1 closes (it is a security release). This is a
  deliberate choice, not an oversight — flag it as such if a reviewer queries the entry.

## Verify first (re-confirm at session start)

| Claim | How to check | Expected |
|-------|--------------|----------|
| current test pins | `grep -nE 'pytest\|Pygments' test_requirements.txt` | `pytest==8.4.1`, `Pygments==2.19.2` |
| requirements.txt is maturin-only | `cat requirements.txt` | `maturin==1.11.5` (no pytest/Pygments) |
| baseline suite is green | `source .venv/bin/activate && maturin develop && python -m pytest` | `N passed` (record **N**) |

## Changes (in order)

1. **`test_requirements.txt`** — set `pytest==9.0.3` and `Pygments==2.20.0`. **Do not** change
   `iniconfig`, `packaging`, `pluggy`, or `maturin`.
2. **Reinstall test deps into the worktree `.venv`**: `pip install -r test_requirements.txt`
   (pulls pytest 9.0.3). Confirm with `pytest --version` → `9.0.3`.
3. **`maturin develop && python -m pytest` (decisive)** → expect the **same `N passed`** as baseline,
   now under pytest 9.0.3. If any test errors or a deprecation is raised-as-error, **stop and
   report** — do **not** mask it with `filterwarnings` or a config file (the smoke suite should not
   trip any pytest-9 removal; a failure means something to investigate).
4. **`cargo fmt --all -- --check`** → clean (no Rust touched; run it so the full gate set passes).
5. **`CHANGELOG.md`** — add the entry below. **If `## [Unreleased]` does not exist yet** (B1 may not
   have merged first), create it directly above `## [1.3.0]`; **otherwise append** under the existing
   `## [Unreleased]`. Do not create a second `[Unreleased]`; do not hand-cut a `[1.3.1]` header.

## CHANGELOG (under `## [Unreleased]`)

```
### Security
- Bumped test-only tooling: pytest 8.4.1 → 9.0.3 (resolves GHSA-6w46-j5rx-g56g, vulnerable tmpdir
  handling) and Pygments 2.19.2 → 2.20.0 (resolves GHSA-5239-wwwm-4pmq, ReDoS in the GUID-matching
  regex). Development/CI dependencies only — no runtime or API impact on the installed package.
```

> If B1 has already added a `### Security` block, **merge into it** (one Security list under
> `[Unreleased]`) rather than creating a second `### Security` heading.

## Acceptance tests (named; all must pass)

- **B2-A1 (decisive)** — with `pytest==9.0.3` installed, `maturin develop` then `python -m pytest`
  → `N passed` (same N as baseline), no new errors or deprecation-raised-as-error.
- **B2-A2** — `test_requirements.txt` has `pytest==9.0.3`, `Pygments==2.20.0`; `pluggy`/`iniconfig`/
  `packaging`/`maturin` pins **unchanged**.
- **B2-A3** — only `test_requirements.txt` and `CHANGELOG.md` changed; `cargo fmt` clean.
- **B2-A4 (post-merge — Dependabot/CI)** — the `python-package.yml` matrix (3.10–3.14) is green, and
  on the next default-branch scan Dependabot resolves alerts **#2** and **#3**. *(Note: this does
  NOT clear the ghost alerts #6/#7 on `requirements.txt` — those are dismissed in Final.)*

## Out of scope / Do NOT

- **Do NOT** touch `requirements.txt` (the ghost-alert manifest — Final handles #6/#7).
- **Do NOT** bump `pluggy`/`iniconfig`/`packaging`/`maturin` (pytest 9 does not require it).
- **Do NOT** add a `pytest.ini` / `[tool.pytest.ini_options]` / `conftest.py`, or any
  `filterwarnings` to mask a pytest-9 deprecation.
- **Do NOT** edit `src/**`, `tests/**`, `Cargo.*`, `pyproject.toml`, `AGENTS.md`, or CI.

## Definition of done

- [ ] B2-A1 (suite green under pytest 9.0.3), B2-A2, B2-A3 green.
- [ ] `CHANGELOG.md` Security entry added under `## [Unreleased]` (created or merged into B1's).
- [ ] Branch `chore/bump-test-deps-security` off latest `origin/main`; PR against `main`; commit
      prefixed `chore:` with the `Co-Authored-By: Claude Opus 4.8 (1M context)` trailer.
- [ ] PR report per `AGENTS.md`, AI assistance disclosed.

## Report (per AGENTS.md)

Summary · Scope (`test_requirements.txt` + `CHANGELOG.md` only) · Compatibility (N/A — test-tooling
only, no runtime/API impact) · Validation (`pytest --version` = 9.0.3, the `pytest N passed` line,
`cargo fmt` clean) · Changelog (the entry above; note the intentional Security entry for a test-only
bump) — plus B2-A1–A3 results and anything flagged.
