# S5 — String Aliases: Document + Pin (standalone session brief)

> Self-contained. You do **not** need to read `PLAN.md`. **Behavior must stay identical** — this
> is documentation + tests only. Crate-version-agnostic (works whether the dep is 1.2.2 or 1.3.0).

## Mission

Make the accepted model-type / deviation-model / moving-average-type string aliases **honest and
tested**, without changing any behavior:
1. document the full accepted alias set for each of the three regimes (incl. the abbreviations
   and snake_case forms the docstrings omit), making the `sma`/`ma` trap explicit;
2. reconcile the `from_string` error messages so they list the full set too;
3. add tests pinning **every** accepted alias to its result, so the mapping can't silently drift.

## The exact accepted sets (source of truth: `src/lib.rs`, lowercased input)

**`PyConstantModelType::from_string`:**
- `simple` | `ma` | `simple_moving_average` → Simple   ← **trap: `ma` = Simple**
- `smoothed` | `sma` | `smoothed_moving_average` → Smoothed   ← **trap: `sma` = Smoothed**
- `exponential` | `ema` | `exponential_moving_average` → Exponential
- `median` | `smm` | `simple_moving_median` → Median
- `mode` | `simple_moving_mode` → Mode   (no 3-letter abbreviation)

**`PyDeviationModel::from_string`:**
- `standard` | `std` | `standard_deviation`
- `mean` | `mean_absolute_deviation`
- `median` | `median_absolute_deviation`
- `mode` | `mode_absolute_deviation`
- `ulcer` | `ulcer_index`
- `log` | `log_standard_deviation` | `logstd`
- `laplace` | `laplace_std_equivalent`
- `cauchy` | `cauchy_iqr_scale`

**`PyMovingAverageType::from_string`:** `simple` | `smoothed` | `exponential` — **ONLY**. No
abbreviations, no snake_case. So `"ma"`/`"sma"`/`"ema"` and snake_case **raise `ValueError`** here
— the opposite of `ConstantModelType`. (Worth an explicit test.)

Three vocabularies are in play today: **primary one-word** (used in tests + error messages),
**abbreviations** (only in the match arms — undocumented), **long snake_case** (what docstrings
show).

## Repo facts

- PyO3/maturin project. `.venv` has `maturin` + `pytest`. Gates: `maturin develop`,
  `python -m pytest`, `cargo fmt --check`. Own worktree + own venv.

## Steps

1. **Document — in `src/lib.rs` only.** Above each `from_string`, expand the doc comment to list
   the complete accepted set for that regime, with `sma` → Smoothed and `ma` → Simple called out
   explicitly. Update each `_ =>` **error-message string** to list the full accepted set (or the
   canonical forms plus an explicit note that the abbreviations + snake_case are also accepted).
   This reconciles the error-message-vs-docstring drift.
2. **Do NOT change any match PATTERN or its mapping** — only doc comments and error-message
   strings. Editing the error string is allowed (it doesn't change behavior); changing which
   strings are accepted, or which variant they map to, is **not**.
3. **Add tests in a NEW file `tests/test_string_aliases.py`** (a new file deliberately avoids
   colliding with other in-flight sessions that edit existing test files). Pin every alias by
   asserting an alias returns the **same result as its canonical form**, and that invalid strings
   raise `ValueError`:
   ```python
   import math
   import pytest
   from centaur_technical_indicators import momentum_indicators as mom
   from centaur_technical_indicators import candle_indicators as can
   from centaur_technical_indicators import moving_average as ma

   PRICES = [100.0, 101.0, 102.0, 101.5, 102.5, 103.0, 102.0]

   def same(a, b):  # NaN != NaN, so treat two NaNs as equal
       if isinstance(a, float) and isinstance(b, float):
           return a == b or (math.isnan(a) and math.isnan(b))
       return a == b  # tuples compare elementwise

   def test_constant_model_aliases():
       rsi = lambda m: mom.single.relative_strength_index(PRICES, m)
       assert same(rsi("ma"), rsi("simple")) and same(rsi("simple_moving_average"), rsi("simple"))
       assert same(rsi("sma"), rsi("smoothed")) and same(rsi("smoothed_moving_average"), rsi("smoothed"))
       assert same(rsi("ema"), rsi("exponential")) and same(rsi("exponential_moving_average"), rsi("exponential"))
       assert same(rsi("smm"), rsi("median")) and same(rsi("simple_moving_median"), rsi("median"))
       assert same(rsi("simple_moving_mode"), rsi("mode"))
       with pytest.raises(ValueError):
           rsi("not_a_model")

   def test_deviation_model_aliases():
       band = lambda d: can.single.moving_constant_bands(PRICES, "simple", d, 3.0)
       assert band("std") == band("standard") == band("standard_deviation")
       assert band("mean") == band("mean_absolute_deviation")
       assert band("median") == band("median_absolute_deviation")
       assert band("mode") == band("mode_absolute_deviation")
       assert band("ulcer") == band("ulcer_index")
       assert band("log") == band("logstd") == band("log_standard_deviation")
       assert band("laplace") == band("laplace_std_equivalent")
       assert band("cauchy") == band("cauchy_iqr_scale")
       with pytest.raises(ValueError):
           band("not_a_model")

   def test_moving_average_type_only_three():
       mav = lambda m: ma.single.moving_average(PRICES, m)
       mav("simple"); mav("smoothed"); mav("exponential")  # accepted
       for rejected in ("ma", "sma", "ema", "simple_moving_average", "nope"):
           with pytest.raises(ValueError):
               mav(rejected)
   ```
   Adjust the representative calls/args if a signature differs — the **pattern** is the
   requirement (alias result == canonical result; invalid → `ValueError`; MA-type rejects
   abbreviations). Use `same()` for any scalar that could be NaN.
4. Run the gates; add CHANGELOG; open PR.

## CHANGELOG (under the existing `## [Unreleased]`)

```
### Added
- Tests pinning accepted model-type / deviation-model / moving-average-type string aliases.
- Documentation of the full accepted string-alias set for each regime (incl. the `sma`→Smoothed
  / `ma`→Simple aliases), with `from_string` error messages reconciled to match.
```

## Commit / PR

- Branch: `git checkout -b docs/string-aliases`. Stage `src/lib.rs`,
  `tests/test_string_aliases.py`, `CHANGELOG.md`. Don't `git add` untracked scratch.
- Commit prefix `docs:` (or `test:`); end with
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- PR body: **Summary** / **Compatibility** (none — behavior identical) / **Validation** /
  **Changelog**.

## Done criteria

- `src/lib.rs` doc comments + error messages list the full accepted set; `sma`/`ma` explicit.
- `tests/test_string_aliases.py` pins all aliases across all three regimes (incl. MA-type
  rejecting abbreviations); all tests pass. Match patterns unchanged. Gates green. PR opened.

## Do NOT

- Do NOT change match patterns or mappings (behavior must be identical).
- Do NOT edit `README.md` (a different session owns the README alias table) or the per-module
  function docstrings (avoids collisions with other in-flight sessions) — confine docs to
  `src/lib.rs`.
- Do NOT add new aliases. Do NOT add dependencies.

## Effort: **high**
