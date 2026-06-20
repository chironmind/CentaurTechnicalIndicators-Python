# S2 — Bind favorable-move + tests (standalone session brief)

> Self-contained. You do **not** need to read `PLAN.md`. Predecessor to **S7** (the stub pass
> covers these two functions). Needs **S1** (dep on Rust `1.3.0`) ✓ already merged.

## Mission

Expose the two new Rust 1.3.0 chart-trend functions as **flat** functions on the `chart_trends`
module (matching `peaks` / `valleys`; **not** under `single` / `bulk`):

```
chart_trends.peak_favorable_move(prices, index, period)   -> float
chart_trends.valley_favorable_move(prices, index, period) -> float
```

## Verified upstream facts (installed `1.3.0` crate)

- `pub fn peak_favorable_move(prices: &[f64], index: usize, period: usize) -> crate::Result<f64>`
  (and `valley_*`). Forward window is the **inclusive** range `[index + 1, index + period]`.
- Bodies: `peak = prices[index] - min(window)`; `valley = max(window) - prices[index]`. Signed
  (not floored): a peak move is negative when no window price drops below the reference; a valley
  move is negative when none rises above it.
- Errors (all → map to `PyValueError`, consistent with the module): empty prices → `EmptyData`;
  `period == 0` → `InvalidPeriod`; forward window past the end → `InvalidPeriod`. In-bounds **iff**
  `index + period < len(prices)` (verified in `assert_favorable_window`, uses `checked_add`).

## Repo facts

- PyO3/maturin project. `.venv` has `maturin` + `pytest`. Gates: `maturin develop`,
  `python -m pytest`, `cargo fmt --check`.

## Steps

1. In `src/chart_trends.rs`: register both functions in the `#[pymodule]` and add the two
   `#[pyfunction]`s, mirroring the existing flat style (`ct::<fn>(&prices, index, period)
   .map_err(|e| PyValueError::new_err(e.to_string()))`). Give each a docstring with `Args` /
   `Returns` like the other functions. (Reference `See:` links are **S4**'s job, not here.)
2. In `tests/test_chart_trends.py`: add the four exact-value assertions (below) and a
   `pytest.raises(ValueError)` test for empty input, zero period, and an out-of-bounds window.
3. Gates: `maturin develop` + `python -m pytest` + `cargo fmt --all -- --check`.

## Test values (traced through the 1.3.0 algorithm; confirmed by running the binding)

```python
assert chart_trends.peak_favorable_move([107.0, 104.0, 100.0, 102.0], 0, 3) == 7.0
assert chart_trends.peak_favorable_move([100.0, 101.0, 102.0, 103.0], 0, 3) == -1.0
assert chart_trends.valley_favorable_move([100.0, 102.0, 107.0, 104.0], 0, 3) == 7.0
assert chart_trends.valley_favorable_move([105.0, 104.0, 103.0, 102.0], 0, 3) == -1.0
```

> Stub coverage (`.pyi`) for these two functions is added in **S7**, not here.

## CHANGELOG (under the existing `## [Unreleased]`, `### Added`)

```
- `chart_trends.peak_favorable_move` and `chart_trends.valley_favorable_move` bindings (maximum
  favorable excursion over a forward window), mirroring Rust 1.3.0.
```

## Commit / PR

- Branch: `git switch -c feat/favorable-move` off fresh `main`. Stage `src/chart_trends.rs`,
  `tests/test_chart_trends.py`, `CHANGELOG.md`. Don't `git add` untracked scratch.
- Commit prefix `feat:`; end with
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- PR body: **Summary** / **Compatibility** (none — purely additive) / **Validation** / **Changelog**.

## Done criteria

- Both functions bound + registered; four exact-value tests + the `ValueError` cases pass.
- `maturin develop` clean; `pytest` green; `cargo fmt --check` clean. CHANGELOG updated. PR opened.

## Do NOT

- Do NOT nest under `single` / `bulk` (these are flat). Do NOT hand-edit a test value to pass —
  re-derive against the installed crate, or stop and report. Do NOT add `See:` links (S4). Do NOT
  add dependencies. Do NOT bump any version.

## Effort: **medium**
