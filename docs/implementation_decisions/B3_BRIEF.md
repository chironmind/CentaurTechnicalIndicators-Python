---
type: brief
id: B3
title: "Refresh AGENTS.md 'Core-crate version & source of truth' (drift fix)"
status: ready
effort: low
wave: A
depends_on: []
touches:
  - AGENTS.md
forbidden:
  - "any AGENTS.md section other than 'Core-crate version & source of truth'"
  - "docs/REPO_MAP.md  (the 'full rule' lives there; not in scope)"
  - "Cargo.toml / CHANGELOG.md / src/** / tests/** / CI / pyproject.toml"
branch: "docs/agents-source-of-truth"
pr_target: "main"
changelog: "exempt — non-user-facing governance/docs (AGENTS.md changelog-coupling exception)"
related:
  - "[[PLAN-1.3.1]]"
decisive_test: "B3-A1"
created: 2026-06-21
tags: [brief, docs]
---

# B3 — AGENTS.md source-of-truth refresh (drift fix)

> **Self-contained.** Repo conventions live in `AGENTS.md` / `CLAUDE.md`. **Independent of B1/B2** —
> runs concurrently in Wave A; its footprint (`AGENTS.md`) is disjoint from both. **This batch must
> merge before Final** so the version-divergence rule is documented *before* the version bump enacts it.

## Authorization (this batch edits a governance doc)

`AGENTS.md` is normally read-only (`AGENTS.md` L97, L151: governance docs are not edited unless
explicitly requested). The maintainer **explicitly authorized this edit** on 2026-06-21, verbatim:

> *"please include your flagged drift items in 1.3.1 plan."*

That authorization is scoped to the **"Core-crate version & source of truth"** section only. Touch
no other part of `AGENTS.md`.

## Mission

Resolve a stale note and govern (rather than leave ad hoc) the binding-only-patch version divergence
that 1.3.1 introduces. Two parts, both inside the "Core-crate version & source of truth" section:

1. **Remove the stale in-flight line.** It still claims `[package] version` is "held at 1.2.2 until
   the release cut" — but the 1.3.0 cut already shipped (`Cargo.toml [package] version = 1.3.0`).
2. **Document the divergence rule.** A binding-only patch release (e.g. a security patch like 1.3.1)
   may move `[package] version` ahead of the `centaur_technical_indicators` core crate, which stays
   put. The version-match rule is the default; binding-only patches are the documented exception.

## Verify first (re-confirm at session start)

| Claim | How to check | Expected |
|-------|--------------|----------|
| stale note still present | `grep -nE 'held at .?1\.2\.2.? until the release cut' AGENTS.md` | one match (~L116) |
| package version already cut | `grep -nE '^version' Cargo.toml` | `version = "1.3.0"` |
| section exists | `grep -n 'Core-crate version & source of truth' AGENTS.md` | one match (~L114) |

If the stale line is already gone (someone fixed it), **stop and report** — the drift is resolved and
this batch is a no-op.

## Changes

Edit only the second bullet of the **"Core-crate version & source of truth"** section. Current text:

```
- Current in-flight state on `main`: the dependency is pinned to `1.3.0` while `[package] version`
  is intentionally held at `1.2.2` until the release cut — deferred deliberately, not forgotten.
```

Replace it with a durable rule (so it does not re-stale every release) plus the worked example —
suggested wording (the implementer may tighten phrasing, but must keep both ideas):

```
- `[package] version` need **not** always equal the core-crate version. A **binding-only patch
  release** — one that changes only the bindings/tooling (e.g. the 1.3.1 security patch: PyO3 and
  test-tooling bumps, no core-crate code) — may move `[package] version` ahead while the
  `centaur_technical_indicators` dependency stays put. The version-match rule above is the default;
  binding-only patches are the documented exception. *(Example: 1.3.1 ships `[package] version =
  1.3.1` against core crate `1.3.0`.)*
```

Leave the first bullet (the match-rule + `docs/REPO_MAP.md` pointer) unchanged.

## Acceptance tests (named; all must pass)

- **B3-A1 (decisive)** — the stale `"held at 1.2.2 until the release cut"` text is **gone**, and the
  section now states both (a) the default version-match rule and (b) the binding-only-patch
  divergence exception with 1.3.1 as the example. `grep -n '1\.2\.2' AGENTS.md` returns no match in
  this section.
- **B3-A2** — `git diff --stat` shows **only `AGENTS.md`** changed, and the diff is confined to the
  "Core-crate version & source of truth" section (no other section, no `REPO_MAP.md`).
- **B3-A3** — gates pass trivially (no code touched): `maturin develop` clean, `python -m pytest`
  green, `cargo fmt --all -- --check` clean.

## Out of scope / Do NOT

- **Do NOT** edit any other `AGENTS.md` section, `docs/REPO_MAP.md`'s "full rule", `Cargo.toml`,
  `CHANGELOG.md`, `src/**`, `tests/**`, CI, or `pyproject.toml`.
- **Do NOT** perform the version bump itself (that is Final).
- **Changelog: none** — this is a non-user-facing governance/docs change (the `AGENTS.md`
  changelog-coupling exception). Do **not** add a `CHANGELOG.md` entry.

## Definition of done

- [ ] B3-A1, B3-A2, B3-A3 green.
- [ ] Branch `docs/agents-source-of-truth` off latest `origin/main`; PR against `main`; commit
      prefixed `docs:` with the `Co-Authored-By: Claude Opus 4.8 (1M context)` trailer.
- [ ] PR report restates the maintainer authorization (so the governance-doc edit is not flagged as
      unauthorized), and discloses AI assistance.

## Report (per AGENTS.md)

Summary · Scope (`AGENTS.md` "Core-crate version & source of truth" only) · Compatibility (N/A —
docs) · Validation (gates green; `grep` shows the stale `1.2.2` text removed) · Changelog (exempt —
non-user-facing) — plus the quoted maintainer authorization and B3-A1–A3 results.
