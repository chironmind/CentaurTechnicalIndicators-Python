# S8 — CI Formatting Gate (standalone session brief)

> Self-contained. You do **not** need to read `PLAN.md`. Touches **one** CI file.
> Crate-version-agnostic.

## Mission

Make CI enforce the repo's stated `cargo fmt --check` pre-PR gate by adding a formatting step to
the existing `verify` job in `.github/workflows/CI.yml`.

## Context / authorization

- Workspace rules say "don't modify CI without approval" — **this change is the approved
  exception** (a planned release step). Keep it **native** (cargo/shell only); **no third-party
  GitHub Actions.**
- The repo's Rust source is already `cargo fmt`-clean (a formatting baseline landed earlier), so
  the new step passes on properly-formatted branches.

## Repo facts

- Two workflows exist: `CI.yml` (a `verify` job + wheel-build jobs + release) and
  `python-package.yml` (the Python test matrix). **Only edit `CI.yml`.**
- PyO3/maturin project. `.venv` has `maturin` + `pytest`. Gates: `maturin develop`,
  `python -m pytest`, `cargo fmt --check`. Own worktree + own venv.

## Steps

1. In `.github/workflows/CI.yml`, in the **`verify`** job, add a step that runs
   `cargo fmt --all -- --check`. GitHub's `ubuntu` runners ship Rust + rustfmt; add
   `rustup component add rustfmt` first only if needed. Minimal step:
   ```yaml
   - name: Check Rust formatting
     run: cargo fmt --all -- --check
   ```
   Place it before the test step so a formatting failure surfaces early.
2. Do **not** add `cargo clippy` (parked — needs maintainer approval). Do **not** edit
   `python-package.yml` or any other job.
3. **Toolchain caveat:** the formatting baseline was produced with a specific rustfmt version. If
   the runner's rustfmt flags formatting that local `cargo fmt --check` does not, that's a
   version skew — **stop and report** (do not reformat to a different rustfmt's taste; that would
   diverge from the baseline). Pin the toolchain only if skew actually appears.
4. Run the local gates, add CHANGELOG, open PR.

## CHANGELOG (under the existing `## [Unreleased]`)

```
### Added
- `cargo fmt --check` step to CI (the `verify` job in `CI.yml`).
```

## Commit / PR

- Branch: `git checkout -b ci/add-fmt-check`. Stage `.github/workflows/CI.yml`, `CHANGELOG.md`.
- Commit prefix `ci:`; end with
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- PR body: **Summary** / **Compatibility** (none) / **Validation** / **Changelog**.

## Done criteria

- `CI.yml`'s `verify` job runs `cargo fmt --all -- --check`; native, no third-party action, no
  clippy. `python-package.yml` untouched. Local gates green. PR opened.

## Effort: **medium**
