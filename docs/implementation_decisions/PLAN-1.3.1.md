---
type: implementation-plan
title: "Release 1.3.1 — Dependabot security patch (PyO3 0.29 + test-dep bumps)"
status: done  # implemented + merged (Wave A #44/#45/#46); Final cut → PR #47; all 6 Dependabot alerts fixed
baseline: "Repo chironmind/CentaurTechnicalIndicators-Python @ main bf8353c (v1.3.0 cut, live on PyPI) — this repo's worktree at ~/Projects/CentaurTechnicalIndicators-Python, NOT crt-research-engine or any sibling tree. Cargo.toml [package] version = 1.3.0; pyo3 = \"0.25.0\" (Cargo.lock 0.25.1); test_requirements.txt pytest==8.4.1 / Pygments==2.19.2; CHANGELOG top is [1.3.0] (no [Unreleased] heading)."
integration_branch: "none — PRs target main directly; the release cut promotes [Unreleased] (see AGENTS.md → Worktree & isolation)"
related:
  - "[[IMPLEMENTATION_PLAN]]"
  - "[[DECISIONS-1.3.0]]"
  - "[[2.0.0]]"
created: 2026-06-21
updated: 2026-06-21
tags: [plan, release, security]
---

<!-- FIELD LEGEND (delete once filled)
status:    draft → verified → in-progress → done
           "verified" = PROMPT-plan-verification returned ready / ready-with-edits
baseline:  what the first batch branches off, and the relevant starting condition
related:   links to the long-lived constitution and any locked specs this plan serves
effort:    per-batch effort uses the Claude Code scale — low | medium | high | xhigh | max
This whole file is read-only instruction during a coding session: surface drift, do not resolve it.
-->

# Release 1.3.1 — Dependabot security patch

> 1.3.1 is a **security-only, binding-only patch**. It clears all six open Dependabot
> alerts, which collapse to three distinct fixes: bump **PyO3 0.25 → 0.29** (clears the
> high + medium Rust advisories), bump **pytest → 9.0.3** and **Pygments → 2.20.0** in
> `test_requirements.txt` (clears the medium + low pip advisories), and **manually
> dismiss two ghost alerts** mis-attributed to `requirements.txt`. The first content
> batch (re)introduces a `## [Unreleased]` heading; the Final batch promotes it to
> `[1.3.1]`, bumps `[package] version` to `1.3.1` (the `centaur_technical_indicators`
> core crate stays at `1.3.0` — a deliberate divergence from the version-match rule),
> dismisses the ghost alerts post-tag, and a small docs batch refreshes a now-stale
> `AGENTS.md` governance note (drift fix, **B3**). No `src/` changes are expected.

## Why this work (context)

GitHub Dependabot reports **six open alerts** on `main`. They are the priority for this
release. Deduplicated by advisory:

| Alert(s) | Dependency | Manifest (per alert) | Advisory | Severity | Fix |
|----------|------------|----------------------|----------|----------|-----|
| **#4** | pyo3 `0.25.1` | `Cargo.lock` | GHSA-36hh-v3qg-5jq4 — OOB read in `nth`/`nth_back` for `PyList`/`PyTuple` iterators | **HIGH** (CVSS 8.7) | pyo3 ≥ 0.29.0 |
| **#5** | pyo3 `0.25.1` | `Cargo.lock` | GHSA-chgr-c6px-7xpp — missing `Sync` bound on `PyCFunction::new_closure` | medium (6.3) | pyo3 ≥ 0.29.0 |
| **#3** | pytest `8.4.1` | `test_requirements.txt` | GHSA-6w46-j5rx-g56g — vulnerable tmpdir handling | medium | pytest ≥ 9.0.3 |
| **#2** | Pygments `2.19.2` | `test_requirements.txt` | GHSA-5239-wwwm-4pmq — ReDoS in GUID-matching regex | low | Pygments ≥ 2.20.0 |
| **#7** | pytest | `requirements.txt` *(ghost)* | GHSA-6w46-j5rx-g56g | medium | manual dismiss |
| **#6** | Pygments | `requirements.txt` *(ghost)* | GHSA-5239-wwwm-4pmq | low | manual dismiss |

**The PyO3 bump (the only severity-HIGH item) is low-risk by construction.** A read-only
audit of `src/*.rs` plus an adversarially-verified survey of the PyO3 0.25→0.29 changelog
established that **no source changes are required**:

- The code is entirely on the modern `Bound` API (`#[pymodule] fn(m: &Bound<'_, PyModule>)`,
  `wrap_pyfunction!`, `add_function`, `add_submodule`, `PyModule::new`, `PyValueError::new_err`).
  The whole `IntoPyObject` return-value migration (incl. `PyList::new`/`PyTuple::new`
  becoming fallible) landed in **0.23.0** — *below* the current 0.25 pin — so nothing in the
  0.25→0.29 window touches the `Vec<f64>` / tuple / `f64` / `bool` return types this code uses.
- **Neither vulnerable code path is invoked.** The code never iterates `PyList`/`PyTuple`
  with `nth`/`nth_back` (GHSA-36hh) and never calls `PyCFunction::new_closure` (GHSA-chgr).
  Both advisories are dependency-level and fixed by the version bump alone.
- No `#[pyclass]`, no `.extract()`/`.downcast()`, no GIL APIs (`with_gil`/`allow_threads`),
  no `Py<T>` smart pointers, no byte (`Vec<u8>`) returns. The four `Py*` enums are plain
  `#[derive(Clone)]` Rust enums that **never cross the PyO3 boundary** (used only as
  `PyXxx::from_string(s)?.into()`), so the one genuinely breaking 0.29 change (removal of the
  implicit by-value `FromPyObject` impl for `#[pyclass]`) cannot bite.

`pyo3 = "0.29"` is, unusually, **both** the minimal advisory-clearing version **and** the
latest stable (0.29.0, 2026-06-11) — no minimal-vs-future-proof tradeoff. Its only cost is an
effective **MSRV of Rust 1.83** (raised in 0.28); CI runners use current stable Rust, so this
is satisfied, and we document the floor with `rust-version = "1.83"`.

**The pytest/Pygments bumps are mechanical.** pytest 9.0.3 keeps the Python 3.10 floor
(matches `requires-python >=3.10` and the 3.10–3.14 CI matrix) and forces **no** transitive-pin
changes (current `pluggy==1.6.0` / `iniconfig==2.1.0` / `packaging==25.0` already satisfy pytest
9.0.3's constraints `pluggy>=1.5,<2` / `iniconfig>=1.0.1` / `packaging>=22`). The suite is plain
assert-based smoke tests with no `conftest.py`, plugins, markers, or deprecated idioms, so none
of the pytest-9 removals apply. The Pygments fix is in the niche ADL/archetype lexer that pytest
never invokes. The one empirical step that remains is to **run the suite once under pytest 9.0.3
and confirm the `N passed` line** (this checkout is pinned at 8.4.1).

**The two `requirements.txt` alerts (#6, #7) are ghosts.** `requirements.txt` contains only
`maturin==1.11.5`; pytest/Pygments are not there (pytest was removed at the Rust refactor;
Pygments never appeared there). Dependabot's resolve-on-fix path only fires when a
dependency-graph change lands on the manifest the alert is attributed to — and there is no fix to
push to `requirements.txt` because the vulnerable deps were never in it. Bumping
`test_requirements.txt` therefore clears #2/#3 but **not** #6/#7. Those must be **manually
dismissed** (`dismissed_reason=inaccurate`).

## Standing rules (defer to AGENTS.md — list deltas only)

`AGENTS.md` / `CLAUDE.md` govern branch naming, commit format, the pre-PR gates
(`maturin develop` → `python -m pytest` → `cargo fmt --all -- --check`, run inside the
worktree `.venv`), the PR-report shape, changelog coupling, and stop-and-report. Every
batch inherits them. Deltas specific to *this* plan:

- **No integration branch.** Per `AGENTS.md` → Worktree & isolation, PRs target `main`
  directly; there is no long-lived `release/1.3.1` branch. Each batch branches off fresh
  `origin/main`; the **Final** batch's cut promotes `## [Unreleased]` to `## [1.3.1]`.
- **CHANGELOG starts with no `[Unreleased]` heading** (the 1.3.0 cut promoted it). The
  first content batch to merge **creates** `## [Unreleased]` with a `### Security` block;
  the second rebases and appends under it. Do **not** hand-cut a `[1.3.1]` header in a
  content batch — that is the Final batch's job.
- **`Cargo.lock` is regenerated, never hand-edited** (`AGENTS.md`). In B1, edit only the
  `Cargo.toml` pyo3 pin; `maturin develop` regenerates the pyo3/pyo3-ffi/pyo3-macros/
  pyo3-build-config rows in `Cargo.lock`. Stage the regenerated lock; do not touch it by hand.
- **Zero `src/` edits is the expectation, not a hope.** If B1's `maturin develop` requires
  *any* source change to compile against 0.29, that **contradicts the verified research** →
  **stop and report** (do not work around it); it would mean the audit missed something.
- **Tag = auto-publish; the tag push *is* the approval point.** There is **no in-CI manual
  gate**: `CI.yml`'s `release` job runs `uv publish` to PyPI automatically on any pushed tag
  (`if: startsWith(github.ref, 'refs/tags/')`, `CI.yml` ~L191–213). So **creating/pushing the
  `v1.3.1` tag is itself the publish decision** and needs explicit human go-ahead (workspace
  `~/Projects/CLAUDE.md` → "Execution & approval notes": *"Publishing/deploying always needs
  explicit approval"* — the **repo-local** `CLAUDE.md` has no such section). The Final batch
  prepares the cut and **does not push the tag autonomously**.
- **Ghost-alert dismissal is an out-of-repo action** (`gh api` PATCH of alert state), not a
  file edit. It is reversible and within policy (it touches no CI/governance file). It runs
  **after** the test-dep fix is on `main`, so the real alerts #2/#3 are already resolved.
- **Governance-doc edit authorized (2026-06-21) — owner quote.** The maintainer's verbatim
  instruction: *"please include your flagged drift items in 1.3.1 plan."* This explicitly
  authorizes the `AGENTS.md` "Core-crate version & source of truth" refresh (**B3**), overriding
  the default read-only-governance rule (`AGENTS.md` L97, L151) **for that section only**. No
  other `AGENTS.md` / CI / licensing / contributor-governance content is in scope; B3's brief
  must restate this authorization.
- **Per-PR (step 6):** `PROMPT-adversarial-review`, opposing agent.

## Sequence at a glance

1. **B1 — PyO3 0.29 bump** — clears the HIGH+medium Rust advisories (#4, #5); proves zero
   source changes; adds `rust-version = "1.83"`. (Independent.)
2. **B2 — Test-dep bumps** — pytest 9.0.3 + Pygments 2.20.0 in `test_requirements.txt`;
   clears the real pip advisories (#3, #2). (Independent.)
3. **B3 — `AGENTS.md` source-of-truth refresh** — fix the stale in-flight-version note and
   document the binding-only-patch divergence 1.3.1 enacts. Docs-only, changelog-exempt.
   (Independent.)
4. **Final — 1.3.1 release cut** — promote `[Unreleased]` → `[1.3.1]`; `[package] version`
   1.3.0 → 1.3.1 (core dep stays 1.3.0); tag/publish on approval; **then** dismiss ghost
   alerts #6/#7.

> **Hard gates / ordering constraints:** Cannot promote/tag until **B1 + B2 are both merged**
> and `## [Unreleased]` carries both `### Security` entries. **B3 must land before Final** so the
> binding-only-patch divergence is *documented before it is enacted* by the version bump. Tag →
> PyPI publish is **approval-gated**. Ghost-alert dismissal runs **after B2 is on `main`** (so
> #2/#3 are resolved first and only the genuine ghosts remain). MSRV floor (Rust ≥ 1.83) must
> hold on every CI runner — confirmed by a green `verify`/wheel build, which is part of B1's gate.

## Batches

The table is the at-a-glance contract. `Touches` is the file footprint; it drives the waves
and the hotspot list. It must match each brief's frontmatter `touches`.

| ID | Goal (one line) | Depends on | Touches (paths) | Wave | Effort |
|----|-----------------|-----------|-----------------|------|--------|
| B1 | Bump PyO3 0.25 → 0.29 (clears #4 HIGH, #5); add `rust-version = "1.83"`; prove no src changes | — | `Cargo.toml`, `Cargo.lock`, `CHANGELOG.md` | A | medium |
| B2 | Bump pytest → 9.0.3 + Pygments → 2.20.0 (clears #3, #2) | — | `test_requirements.txt`, `CHANGELOG.md` | A | low |
| B3 | Refresh `AGENTS.md` source-of-truth note (drift fix); govern the binding-only-patch divergence | — | `AGENTS.md` | A | low |
| Final | Cut 1.3.1 (promote `[Unreleased]`; version 1.3.0 → 1.3.1) + dismiss ghost alerts #6/#7 | B1, B2, B3 | `Cargo.toml`, `Cargo.lock`, `CHANGELOG.md` (+ `gh api` alert dismissal, no file) | Final | low |

## Batch summaries

> **Note:** the `[[B1_BRIEF]]` / `[[B2_BRIEF]]` / `[[B3_BRIEF]]` / `[[FINAL_BRIEF]]` links are
> **forward references to briefs not yet generated** — they do not exist at HEAD. They are
> created from this plan (step 4) before each batch is implemented (assumption **A12**).

### B1 — PyO3 0.29 security bump
**Depends on:** — · **Wave:** A · **Effort:** medium · **Brief:** `[[B1_BRIEF]]`
- **Objective:** Clear GHSA-36hh-v3qg-5jq4 (HIGH) and GHSA-chgr-c6px-7xpp (medium) by bumping
  `pyo3 = "0.25.0"` → `"0.29"`, and document the resulting MSRV floor.
- **Changes (summary):**
  - `Cargo.toml`: `pyo3 = "0.29"`; add `rust-version = "1.83"` to `[package]`.
  - `Cargo.lock`: **regenerated** by `maturin develop` (pyo3 + pyo3-ffi/macros/build-config
    rows move to 0.29.x). Not hand-edited.
  - `CHANGELOG.md`: create `## [Unreleased]` (if B1 merges first) with a `### Security`
    entry naming both GHSAs; a `### Changed` note for the documented MSRV 1.83.
  - **`src/*.rs`: no changes** (verified expectation).
- **Verification:** `maturin develop` (compiles, **no** source edit needed) → `python -m pytest`
  (`N passed`) → `cargo fmt --all -- --check`.
- **Out of scope:** any `src/` refactor; the `[package] version` bump (Final); the deprecated-
  function `#[allow(deprecated)]` annotations (unrelated to pyo3); pytest/Pygments. **If 0.29
  needs a source change → stop and report.**

### B2 — Test-dependency security bumps
**Depends on:** — · **Wave:** A · **Effort:** low · **Brief:** `[[B2_BRIEF]]`
- **Objective:** Clear GHSA-6w46-j5rx-g56g (pytest, medium, #3) and GHSA-5239-wwwm-4pmq
  (Pygments, low, #2) by bumping the two pins in `test_requirements.txt`.
- **Changes (summary):**
  - `test_requirements.txt`: `pytest==9.0.3`, `Pygments==2.20.0`. Leave
    `iniconfig`/`packaging`/`pluggy`/`maturin` **untouched** (no forced transitive bumps).
  - `CHANGELOG.md`: `### Security` entry under `## [Unreleased]` (create the heading if B2
    merges first; otherwise append under B1's).
- **Verification:** `pip install -r test_requirements.txt` → `maturin develop` →
  `python -m pytest` (**confirm `N passed` under pytest 9.0.3** — the one empirical step).
- **Out of scope:** `requirements.txt` (only `maturin`; the ghost alerts are handled in Final);
  refreshing `pluggy`/`iniconfig`/`packaging`; any `pytest.ini`/`conftest.py` introduction.

### B3 — AGENTS.md source-of-truth refresh (drift fix)
**Depends on:** — · **Wave:** A · **Effort:** low · **Brief:** `[[B3_BRIEF]]`
- **Objective:** Resolve the stale "Core-crate version & source of truth" note in `AGENTS.md`
  and **govern** (rather than leave ad hoc) the binding-only-patch divergence that 1.3.1 enacts.
- **Changes (summary):** In `AGENTS.md` → "Core-crate version & source of truth":
  1. Replace the stale in-flight line — *"the dependency is pinned to 1.3.0 while `[package]
     version` is intentionally held at 1.2.2 until the release cut"* — that state is gone
     (1.3.0 shipped; `Cargo.toml` version = 1.3.0).
  2. Add one sentence documenting that **binding-only patch releases (e.g. a security patch
     like 1.3.1) may bump `[package] version` ahead of the core crate**, which stays put — so
     the two need not always match. This makes the 1.3.1 divergence governed, not ad hoc.
  - **Changelog-exempt** (governance/docs — the `AGENTS.md` changelog-coupling exception).
- **Verification:** docs-only; gates pass trivially (`maturin develop` / `python -m pytest`
  unchanged; `cargo fmt --all -- --check` clean — no Rust touched). `docs:`-type commit.
- **Out of scope:** rewriting the broader source-of-truth rule or `REPO_MAP.md`'s "full rule";
  the version bump itself (Final); any other `AGENTS.md` section.

### Final — 1.3.1 release cut + ghost-alert dismissal
**Depends on:** B1, B2, B3 (all merged) · **Wave:** Final · **Effort:** low · **Brief:** `[[FINAL_BRIEF]]`
- **Objective:** Cut 1.3.1 and close out the remaining ghost alerts.
- **Changes (summary):**
  - `CHANGELOG.md`: promote `## [Unreleased]` → `## [1.3.1] - <cut date>` (keep the `### Security`
    entries from B1+B2; add the MSRV `### Changed` note if not already present).
  - `Cargo.toml`: `[package] version` `1.3.0` → `1.3.1`. **The `centaur_technical_indicators`
    core dep stays `1.3.0`** (binding-only patch; deliberate divergence — see Context).
  - **Post-merge / post-tag (no file change):** dismiss ghost alerts #6 and #7 via `gh api`
    (`state=dismissed`, `dismissed_reason=inaccurate`) with a comment explaining the
    mis-attribution. Commands in the Running log / brief.
- **Verification:** gates green on the cut commit; after tag, CI `release` job builds wheels +
  publishes (**approval-gated**). After publish, re-query
  `gh api .../dependabot/alerts` and confirm **0 open** (#2/#3 auto-resolved by B2; #4/#5 by B1;
  #6/#7 dismissed).
- **Out of scope:** the `your@email.com` placeholder fix (**kept deferred** this release); the
  `AGENTS.md` refresh itself (that is **B3**, which must land first).

## Assumptions to verify (step 3)

Repo-state claims this plan depends on. Statuses below were resolved inline against `HEAD`
(`bf8353c`) and via an adversarially-verified research workflow (3 dimensions, 6 agents). The
`pending` items (A2b, A4b, A7) are normal in-batch / CI gates, **not** blockers to briefing —
they cover compile/test/CI compatibility that can only be proven by running B1/B2, deliberately
kept distinct from the docs-confirmed facts so "confirmed" never overstates an unrun build.

| ID | Assumption (repo-state claim) | Expected evidence (file/symbol/cmd/test) | Risk if wrong | Status |
|----|-------------------------------|------------------------------------------|---------------|--------|
| A1 | pyo3 pinned `"0.25.0"` in `Cargo.toml`; resolves `0.25.1` in `Cargo.lock` | `grep pyo3 Cargo.toml`; `Cargo.lock` pyo3 block | wrong baseline | **confirmed** |
| A2a | pyo3 `0.29` is latest stable, clears both GHSAs, MSRV = Rust 1.83, and the code uses **none** of the risky APIs (grep: no `PyList`/`PyTuple` iter, `PyCFunction`, `.extract`/`.downcast`, `#[pyclass]`, `Vec<u8>` returns) | PyO3 CHANGELOG/migration guide; GHSA pages; `rg` over `src/` | wrong target / missed API | **confirmed** (docs + grep, adversarially verified) |
| A2b | the crate **compiles against 0.29 with zero `src/` edits** | `maturin develop` in B1 (no build run against 0.29 yet) | source churn / failed compile → stop-and-report | **pending — B1 build gate** |
| A3 | `test_requirements.txt` = `pytest==8.4.1`, `Pygments==2.19.2` (+ iniconfig/packaging/pluggy/maturin); `requirements.txt` = `maturin` only | both files | wrong fix target | **confirmed** |
| A4a | pytest 9.0.3 keeps the Python 3.10 floor and forces **no** transitive-pin bumps (package metadata only) | pytest 9.0.3 PyPI `requires-python` + deps; current pins satisfy `pluggy>=1.5,<2` / `iniconfig>=1.0.1` / `packaging>=22` | broken matrix | **confirmed** (PyPI metadata, adversarially verified) |
| A4b | the smoke suite **passes under pytest 9.0.3** (no deprecation-now-error breakage) | `python -m pytest` in B2 (not run under 9.0.3 yet) | hidden break | **pending — B2 test gate** |
| A5 | `requirements.txt` lacks pytest/Pygments → #6/#7 are ghosts → B2 won't auto-clear them → manual dismiss needed | `requirements.txt`; GitHub Dependabot docs | leaving open alerts / false "auto-fixed" | **confirmed + verified** |
| A6 | The `centaur_technical_indicators` **core crate** stays `1.3.0` (no upstream change this release) | `Cargo.toml` dep line; no core bump intended | accidental core bump | **confirmed** |
| A7 | Every CI/build runner satisfies Rust ≥ 1.83 (the MSRV 0.29 introduces) | GitHub-hosted runners ship current stable Rust (≫ 1.83); no `rust-toolchain*` pin in repo | wheel/`verify` build fails on an old toolchain | **pending — must be confirmed by green B1 CI + wheel builds**; no Rust pin added (owner **Q3 → (a)**) |
| A8 | CHANGELOG has **no** `## [Unreleased]` heading; top is `## [1.3.0]` → first content batch creates it | `grep -n Unreleased CHANGELOG.md` (no match) | double-heading / lost entry | **confirmed** |
| A9 | Gates = `maturin develop` → `python -m pytest` → `cargo fmt --all -- --check`, in the worktree `.venv` | `AGENTS.md` Pre-PR gates | wrong validation | **confirmed** |
| A10 | `AGENTS.md` "Core-crate version & source of truth" still carries the stale in-flight note (held at 1.2.2) | `AGENTS.md` §"Core-crate version & source of truth" (~lines 114–116) | B3 edits the wrong text / drift already fixed | **confirmed** |
| A11 | the B3 `AGENTS.md` edit is **owner-authorized** | maintainer instruction quoted in Standing rules (2026-06-21): *"please include your flagged drift items in 1.3.1 plan"* | unauthorized governance edit | **confirmed** (owner quote) |
| A12 | the `[[B*_BRIEF]]` links are **forward references** — the briefs do **not** exist at HEAD yet | `ls docs/implementation_decisions/` (no `B*_BRIEF`) | implying briefs already exist | **acknowledged** — generated from this plan pre-implementation |

## Parallelization (git worktrees)

**Sequential backbone:** (B1, B2, B3 concurrent) → Final. The three Wave-A batches are
**code-independent**, but B1 and B2 are **not file-disjoint** — both append to `CHANGELOG.md`
(a known same-wave hotspot, serialized by rebase; see below). Only B3's footprint (`AGENTS.md`)
is fully disjoint from the other two.

| Wave | After | Run concurrently | Max worktrees | Same-wave file contention |
|------|-------|------------------|---------------|---------------------------|
| A | baseline (`origin/main`) | B1, B2, B3 | 3 | **B1 ∩ B2 = `CHANGELOG.md`** → rebase-and-re-append; B3 disjoint |
| Final | B1 + B2 + B3 merged | Final (solo) | 1 | — |

**Shared-file hotspots** (paths in more than one batch's `Touches`):

- `CHANGELOG.md` — B1, B2, **and** Final write it (B3 is changelog-exempt, so it does **not**
  contend). First content batch to merge **creates** `## [Unreleased]` + `### Security`; the
  second rebases on `main` and **appends** under the existing heading (do not add a second
  `[Unreleased]`). Final promotes the heading. Expect a trivial append conflict on the second
  merge → rebase and re-append.
- `Cargo.toml` — B1 (pyo3 pin + `rust-version`) and Final (`[package] version`) touch different
  lines; no concurrency (different waves), so no contention.
- `AGENTS.md` — **B3 only**; no contention.

**Mechanics:**

    # no integration branch — each batch branches off fresh origin/main, PRs target main
    git fetch origin
    git worktree add ../CTI-py-b1 -b chore/bump-pyo3-0.29 origin/main   # own .venv
    git worktree add ../CTI-py-b2 -b chore/bump-test-deps-security origin/main  # own .venv
    git worktree add ../CTI-py-b3 -b docs/agents-source-of-truth origin/main    # docs-only
    # run a Claude Code session in each worktree; gates inside that worktree's .venv
    # merge B1 and B2 to main (rebase the 2nd on main first → resolves CHANGELOG); merge B3
    git worktree add ../CTI-py-final -b chore/cut-1.3.1 origin/main     # after B1+B2+B3 merged
    # Final: promote CHANGELOG + bump version; merge; then (with approval) tag → CI publishes
    # post-publish: gh api PATCH dismiss alerts #6/#7; git worktree remove ../CTI-py-*

---

# Running log

## Status
- **Pre-verification (equivalent of step 3):** an adversarially-verified research workflow
  (`release-131-dep-research`, 3 dimensions × find→verify, 6 agents) graded all blocking
  assumptions. PyO3 dimension: `minor_corrections` (3 immaterial version-attribution nits in the
  changelog mapping; the **`[]` source-changes-needed conclusion holds and is stronger than
  argued** — the `IntoPyObject` migration predates the 0.25 pin). pytest dimension:
  `findings_sound` (the load-bearing "did pytest 9 drop 3.10?" was decisively **falsified** — 3.10
  is retained; no forced transitive bumps). Dependabot dimension: `minor_corrections` (the
  *mechanism* for why #6/#7 linger is partly inference, but the **conclusion — manually dismiss,
  reason=`inaccurate`** — is sound for the cleaner documented reason that the alert is
  mis-attributed to a manifest that never held the dep). **Formal `PROMPT-plan-verification` not
  yet run** — recommended before brief generation, though every assumption status is already
  resolved above.
- **Decisions locked (2026-06-21):** (1) version = **1.3.1**, binding-only patch, core dep stays
  1.3.0; (2) `your@email.com` placeholder — **keep deferred** (address still does not exist;
  no-PII rule); (3) ghost alerts #6/#7 — **dismiss via `gh api`** as part of the release; (4) add
  **`rust-version = "1.83"`** to document the MSRV the pyo3 bump introduces; (5) the **`AGENTS.md`
  source-of-truth drift fix is folded in as B3** — the maintainer authorized the governance-doc
  edit, so it is no longer a deferred flag.
- **Codex plan-verification (2026-06-21): `ready-with-edits`.** All 7 required edits applied:
  (1) repo root stated explicitly in `baseline`; (2) Wave-A `CHANGELOG.md` contention surfaced —
  no longer called "disjoint"; (3) A2/A4 split into docs-confirmed (A2a/A4a) vs build/test-pending
  (A2b/A4b); (4) A7 reframed to "confirm by green CI", no Rust pin added; (5) publish-approval
  citation corrected — CI **auto-publishes on tag**, so the tag push is the approval point;
  (6) B3 owner-approval quoted (A11); (7) `[[B*_BRIEF]]` marked forward references (A12). Plus the
  reviewer's A5 note: a **pre-dismiss re-query** step added before PATCHing #6/#7. Reviewer's
  owner Q1 (repo) and Q2 (B3 auth) answered "yes"; **Q3 (CI Rust pin) resolved → option (a)**
  (runner-default Rust + green CI; no Rust pin, no CI change).

## Ghost-alert dismissal commands (Final batch, post-B2-on-main)

**Pre-dismiss re-query (required, A5).** Confirm #6/#7 are *still* `open` and *still* attributed
to `requirements.txt` before PATCHing — state may have changed since this plan was written (e.g.
Dependabot may have independently re-evaluated). Only dismiss those still open on `requirements.txt`:

    for n in 6 7; do gh api /repos/chironmind/CentaurTechnicalIndicators-Python/dependabot/alerts/$n \
      --jq '{number,state,manifest:.dependency.manifest_path,dep:.dependency.package.name}'; done

Then, for each still-open ghost:

    gh api --method PATCH -H "Accept: application/vnd.github+json" \
      /repos/chironmind/CentaurTechnicalIndicators-Python/dependabot/alerts/7 \
      -f state=dismissed -f dismissed_reason=inaccurate \
      -f dismissed_comment="Stale dependency-graph node: requirements.txt lists only maturin==1.11.5; pytest is not present (removed at the Rust refactor). The genuine pytest advisory is tracked on test_requirements.txt (#3), fixed by the 9.0.3 bump in 1.3.1."

    gh api --method PATCH -H "Accept: application/vnd.github+json" \
      /repos/chironmind/CentaurTechnicalIndicators-Python/dependabot/alerts/6 \
      -f state=dismissed -f dismissed_reason=inaccurate \
      -f dismissed_comment="Stale dependency-graph node: requirements.txt lists only maturin==1.11.5; Pygments is not present. The genuine Pygments advisory is tracked on test_requirements.txt (#2), fixed by the 2.20.0 bump in 1.3.1."

Valid `dismissed_reason` values: `fix_started | inaccurate | no_bandwidth | not_used | tolerable_risk`.
Requires a token with **security-events write** (or repo) scope and admin/security-manager rights.
Verify afterward: `gh api .../dependabot/alerts --jq '[.[]|select(.state=="open")]|length'` → `0`.

> **OUTCOME (2026-06-21): the manual dismissal was NOT needed.** The pre-dismiss re-query found that
> when Wave A merged, Dependabot's graph rescan resolved **all six** alerts (#2–#7) to `state=fixed`,
> including the ghosts #6/#7 — they closed as *fixed*, not dismissed. We correctly did **not** PATCH
> already-fixed alerts. The commands above are retained as the record of the planned fallback.

## Open questions / deferred
- **`your@email.com` placeholder** (`pyproject.toml` author/maintainer) — **deferred again**
  (decided 2026-06-21). Gating question: a real CRT-suitable address must exist before it can be
  filled; do not guess, do not silently drop. Re-surface in the next release.
- **Doc drift — now scoped as B3 (resolved):** `AGENTS.md` §"Core-crate version & source of
  truth" still reads *"the dependency is pinned to 1.3.0 while `[package] version` is intentionally
  held at 1.2.2 until the release cut"* — **stale** (the 1.3.0 cut happened; `Cargo.toml` version =
  1.3.0). The maintainer authorized the fix (2026-06-21), so it is no longer deferred — it is
  **B3** (refresh the stale note + document the binding-only-patch divergence), a standalone
  `docs:` change merging before Final.
- **`.github/dependabot.yml`** — intentionally **not** added (out of scope, governance file,
  would not have prevented the ghost-alert artifact). Raise separately if recurrence-prevention is
  wanted later.
- **Owner Q3 (resolved 2026-06-21 → option (a)) — CI Rust toolchain.** Rely on GitHub-runner-
  default Rust (current stable, ≫ 1.83) with **green B1 CI/wheels as proof**; **no Rust pin, no CI
  change**. Option (b) (explicit `rust-version`/`rust-toolchain` pin + setup step in CI) was
  **declined** for 1.3.1 — it can be raised separately if a runner ever ships < 1.83.

## Execution outcomes (2026-06-21)

Implemented the same day in isolated worktrees (Wave A = B1∥B2∥B3 concurrent, then Final), all gates
green — the whole release shipped in one session.

- **B1 — PyO3 0.29** → **PR #44**, merged. `maturin develop` compiled with **zero `src/` edits** (the
  decisive A2b gate — the audit held); **116 passed**; `cargo fmt` clean; `Cargo.lock` pyo3 → 0.29.0
  (lock shrank 20→16 crates). One transient macOS-wheel failure (`Could not resolve host:
  index.crates.io`) — a runner DNS flake, **rerun green**; the full cross-platform wheel matrix then
  passed, confirming **A7** (Rust 1.94 ≫ 1.83 on every runner).
- **B2 — pytest 9.0.3 + Pygments 2.20.0** → **PR #45**, merged. pytest 9.0.3 confirmed; **116 passed**
  (A4b); **no transitive-pin bumps** forced (A4a held); test-tooling only.
- **B3 — AGENTS.md source-of-truth refresh** → **PR #46**, merged. Owner-authorized governance edit;
  one-section change; changelog-exempt.
- **Codex adversarial review (`PROMPT-adversarial-review`):** PR44 `request-changes` (CI-only — the
  transient wheel flake; resolved by rerun), PR45 `approve`, PR46 `approve-with-nits` (validation-
  reporting nit — addressed by citing the green CI `verify` job, which runs all three gates). No
  code/scope defects in any of the three.
- **CHANGELOG consolidation:** B1 and B2 each created `## [Unreleased]` + `### Security`; merged into
  **one** `### Security` block (PyO3 + pytest/Pygments) plus the `### Changed` rust-version entry —
  the planned hotspot, resolved cleanly at merge.
- **Final — 1.3.1 cut** → **PR #47** (commit `e019aea`, branch `chore/cut-1.3.1`). Run as a Workflow:
  one agent cut + gated, two independent adversarial verifiers (release-correctness + scope/gate)
  returned **12/12 checks clean, zero defects**. `[package] version` 1.3.0 → **1.3.1**; core dep stays
  **1.3.0**; CHANGELOG promoted to `## [1.3.1] - 2026-06-21` (no leftover `[Unreleased]`);
  `cti.__version__` == **1.3.1**; **116 passed**; `cargo fmt` clean; only the three release files
  touched; `pyproject.toml` email placeholder intact.
- **Dependabot — Final-A5 satisfied:** all six alerts **#2–#7 are now `state=fixed` (0 open)**. The
  ghosts **#6/#7 auto-resolved as `fixed`** on the merge rescan — the planned manual `gh api`
  dismissal was **unnecessary**, and the pre-dismiss re-query (A5) correctly prevented "dismissing"
  already-fixed alerts. *(The research/Codex caution to plan for non-auto-dismiss was right to have;
  the re-query is what made the better real outcome safe to take.)*
- **Remaining (maintainer-only):** merge **PR #47**, then push the **`v1.3.1`** tag on the merge commit
  → CI `release` job auto-publishes to PyPI (`uv publish`). Final-A4 confirmed once PyPI shows 1.3.1.
  Worktrees: Wave-A removed; `../CTI-py-final` removed after #47 merges.
