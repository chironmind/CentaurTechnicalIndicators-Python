# docs/ — knowledge base

Specs, decisions, and the full implementation history for `CentaurTechnicalIndicators-Python`.
**Internal only:** this directory is excluded from the sdist and never ships in the wheel.

## Read order for any session
1. `AGENTS.md` / `CLAUDE.md` (repo root) — the operating rules. Auto-loaded; **must stay at root**.
2. `docs/REPO_MAP.md` — repository orientation map.
3. The decision records in `technical_decisions/` and the plan + slice briefs in
   `implementation_decisions/`, as the task requires.

## technical_decisions/ — decision records
- `DECISIONS-1.3.0.md` — the 1.3.0 release decision record: scope (incl. the `basic_indicators`
  out-of-scope call), gate + favorable-move semantics, the inherited-fix inventory, DX/packaging
  rationale (`__version__` / mixed layout), quality notes, and deferrals. The "why" behind 1.3.0.
- `2.0.0.md` — breaking-change backlog for the next major. Not actionable in 1.x; recorded so the
  items are neither re-litigated nor accidentally "fixed" in a minor.

> Decision records are **read-only** during a coding session: surface drift, don't resolve it.

## implementation_decisions/ — plan + slice briefs
The full work history of the 1.3.0 release: the master plan, every per-slice brief (one session's
contract; the format new briefs follow), and the resume/state doc.

- `IMPLEMENTATION_PLAN.md` — the master plan (was the root `PLAN.md`): scope, ordering, assumptions,
  parallelization, and the running log. Follows `~/Projects/TEMPLATE-implementation-plan.md`.
- `RESUME.md` — session state + next action. Start here when resuming.
- `SLICE-00…11-*.md` — the twelve slice briefs. The slice number **is** the plan's `S`-id (SLICE-07
  = S7). Each follows `~/Projects/TEMPLATE-brief.md`.

| Slice | Brief | What | PR |
|------:|-------|------|----|
| S0  | `SLICE-00-fmt-baseline`        | repo-wide `cargo fmt` baseline               | #31 |
| S1  | `SLICE-01-dep-bump`           | Rust dep `1.2.2` → `1.3.0`                    | #32 |
| S2  | `SLICE-02-favorable-move`     | `peak_/valley_favorable_move` bindings       | #38 |
| S3  | `SLICE-03-inherited-fix-tests`| inherited-fix regression tests + carryover   | #39 |
| S4  | `SLICE-04-readme-accuracy`    | README accuracy + docstring `TypeError` fixes| #40 |
| S5  | `SLICE-05-string-aliases`     | string-alias docs + tests                    | #36 |
| S6  | `SLICE-06-pyproject-metadata` | Documentation URL + classifiers              | #33 |
| S7  | `SLICE-07-mixed-layout-stubs` | `.pyi` stubs + `py.typed` + `__version__`    | #41 |
| S8  | `SLICE-08-ci-fmt-gate`        | `cargo fmt --check` CI gate                  | #34 |
| S9  | `SLICE-09-2.0-backlog`        | `2.0.0.md` breaking-change backlog           | #35 |
| S11 | `SLICE-11-decision-docs`      | this knowledge base                          | #42 |
| S10 | `SLICE-10-release-cut`        | version bump + changelog promote + publish   | #43 |

Execution ran S0–S9, then **S11 before S10** — the 1.3.0 tag had to contain these decision docs.

## Note on preservation
An earlier draft of the plan (SLICE-10 / SLICE-11) called for **deleting** the root scratch
(`PLAN.md`, `RESUME.md`, `*_BRIEF.md`) at the release cut. That was **superseded**: these files are
the record of *what* was done and *why*, so they are preserved here — moved under `docs/`, tracked,
and still excluded from the sdist — rather than removed. (Some briefs still describe the old
"remove scratch" step; they are kept as-written for provenance.)

## Still at repo root (by necessity)
- `AGENTS.md` / `CLAUDE.md` — operating rules; the harness auto-loads them from root.
- `CHANGELOG.md` — required entry point for every user-facing change.
