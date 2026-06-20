# S0 — Formatting Baseline (standalone session brief)

> This is a **self-contained** task. It is Step 0 of a larger release, but you do **not** need
> to read `PLAN.md` or anything else. Do only what is below. Formatting only — **zero**
> behavior/logic changes.

## Mission

Make `cargo fmt --check` pass on this repo. The committed Rust source is not formatted to the
current toolchain's rustfmt style. This one session reformats it so `cargo fmt --check` can
serve as a real pre-PR / CI gate for the rest of the release.

## Why this exists (context)

- Verified: `cargo fmt --all -- --check` currently **exits `1`** with ~84 diff hunks across **9
  of 10 `src/*.rs` files** (mostly `use`-import ordering and rustfmt's `)\n.map_err(...)`
  method-chain wrapping). It is **pre-existing committed drift** — `git diff src/` is empty, so
  it is not from anyone's feature work.
- `cargo fmt --all -- --check` is **whole-crate**: formatting only the file you touch won't make
  it pass while the other files still drift. So this must be a single, repo-wide pass.

## Repo facts you need

- Rust + Python library (PyO3 / maturin). Rust sources are in `src/*.rs`; tests are Python in
  `tests/`. There are no `.rs` files outside `src/`.
- A virtualenv already exists at `.venv` (has `maturin` and `pytest`).
- `AGENTS.md` is authoritative for conventions. The pre-PR gates are: `maturin develop`,
  `python -m pytest`, `cargo fmt --check`.
- Current green baseline (against the pinned `1.2.2` dependency): `maturin develop` compiles
  clean and `pytest` → **100 passed**. Do not change the dependency or version — that is a
  later step, not this one.

## Steps

1. **Confirm the starting state.**
   - `cargo fmt --all -- --check` → expect exit `1` (drift present).
   - `source .venv/bin/activate && maturin develop && python -m pytest` → expect **100 passed**.
   - Record the toolchain: `rustc --version` and `cargo fmt --version`. Put both in the PR
     description (a later CI step must use a matching rustfmt, or it could re-introduce drift).

2. **Reformat:** `cargo fmt --all`.

3. **Verify it is formatting-only and still green.**
   - `cargo fmt --all -- --check` → now exit `0`.
   - `git diff --stat` → only `src/*.rs` changed.
   - Eyeball `git diff` and confirm every hunk is whitespace / import reordering / line-wrapping
     only — **no logic changes, no renamed identifiers, no changed string literals or numbers.**
   - `maturin develop && python -m pytest` → still **100 passed**.

4. **Commit (branch first — do not commit on `main`).**
   - `git checkout -b style/cargo-fmt-baseline`
   - `git add -u src/` — stage **only** the formatted Rust. Do **not** `git add .` (there are
     untracked planning docs like `PLAN.md` / `S0_BRIEF.md` that must not be committed).
   - Commit message:
     ```
     style: apply cargo fmt baseline across src/

     Pure `cargo fmt --all` pass; no behavior change. Establishes a clean formatting
     baseline so `cargo fmt --check` can gate subsequent release work.
     rustfmt: <paste output of `cargo fmt --version`>

     Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
     ```
   - Open a PR with this body:
     - **Summary:** repo-wide `cargo fmt` baseline; formatting only.
     - **Compatibility:** none — no API or behavior change.
     - **Validation:** `cargo fmt --all -- --check` exit 0; `maturin develop` clean;
       `pytest` → 100 passed. (Include the rustfmt version.)
     - **Changelog:** **none** — formatting-only, not user-facing. This session is the explicit
       exception to the "every change gets a paired `CHANGELOG.md` entry" rule.

## Done criteria

- `cargo fmt --all -- --check` exits `0`.
- `maturin develop` clean; `pytest` → **100 passed** (unchanged).
- Staged diff is `src/*.rs` formatting only; nothing else staged.
- Branch `style/cargo-fmt-baseline` + PR opened; rustfmt version recorded in the PR.

## Do NOT

- Do not change any logic, rename anything, or edit non-`src` files (no `CHANGELOG.md`, no
  `PLAN.md`, no docs, no `Cargo.toml`, no CI files).
- Do not bundle any other work — this is purely the formatting pass.
- Do not add, remove, or upgrade dependencies; do not bump any version.
- If `cargo fmt` produces a change you cannot explain as pure formatting, **stop and report**
  instead of committing.
