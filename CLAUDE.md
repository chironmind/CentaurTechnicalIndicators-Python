# CLAUDE.md

Claude Code operating notes for this repo. **[`AGENTS.md`](AGENTS.md) is
canonical** for every standing convention — pre-PR gates, branch/commit format,
PR shape, scope discipline, stop-and-report, changelog coupling, and worktree
isolation. This file adds only the Claude-Code-facing bits for running a slice; it
does not repeat `AGENTS.md`.

## Running a slice
- Work is organized as slice briefs (`S*_BRIEF.md`) tracked by `PLAN.md`. `PLAN.md` is the planning channel — implement against the briefs; do not edit `PLAN.md`.
- Read order at session start: the slice brief (it is self-contained) → `AGENTS.md` (standing conventions). You don't need to read `PLAN.md` to execute a self-contained brief.
- **One slice per session**, in its **own git worktree with its own `.venv`** (per `AGENTS.md` → Worktree & isolation).

## Effort
Set the session effort from the brief's `Effort:` line (`low` / `medium` / `high`) with `/effort <level>`.

## Plan before auto-editing
For a non-trivial slice, plan before editing — use plan mode before auto-applying changes. Honor the stop-and-report rule in `AGENTS.md`: when a gate fails unexpectedly or a test value shifts, stop and report rather than working around it.

## Running the gates
Inside the worktree's `.venv`: `maturin develop` → `python -m pytest` (pass signal `N passed`) → `cargo fmt --all -- --check`. Full gate definitions and the CI-divergence note live in `AGENTS.md`.
