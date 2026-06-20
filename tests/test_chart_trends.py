import pytest

from centaur_technical_indicators import chart_trends

"""The purpose of these tests are just to confirm that the bindings work.

These tests are not meant to be in depth, nor to test all edge cases, those should be
done in [CentaurTechnicalIndicators-Rust](https://github.com/chironmind/CentaurTechnicalIndicators-Rust). These tests exist to confirm whether an update in the bindings, or
CentaurTechnicalIndicators-Rust has broken functionality.

To run the tests `maturin` needs to have built the egg. To do so run the following from
your CLI

```shell
$ source you_venv_location/bin/activate

$ pip3 install -r test_requirements.txt

$ maturin develop

$ pytest .
```
"""

prices = [100.0, 102.0, 103.0, 101.0, 99.0]


def test_peaks():
    assert chart_trends.peaks(prices, 5, 1) == [(103.0, 2)]

def test_valleys():
    assert chart_trends.valleys(prices, 5, 1) == [(99.0, 4)]

def test_peak_trend():
    peak_prices = prices + [102.0, 104.0, 100.0]
    assert chart_trends.peak_trend(peak_prices, 3) == (0.25, 102.5)

def test_valley_trend():
    assert chart_trends.valley_trend(prices, 3) == (-0.25, 100.0)

def test_overall_trend():
    assert chart_trends.overall_trend(prices) == (-0.3, 101.6)

def test_break_down_trends():
    trends = chart_trends.break_down_trends(
        prices,
        max_outliers=1,
        soft_adj_r_squared_minimum=0.25,
        hard_adj_r_squared_minimum=0.05,
        soft_rmse_multiplier=1.3,
        hard_rmse_multiplier=2.0,
        soft_durbin_watson_min=1.0,
        soft_durbin_watson_max=3.0,
        hard_durbin_watson_min=0.7,
        hard_durbin_watson_max=3.3
    )
   
    assert trends == [(0, 2, 1.5, 100.16666666666667), (2, 4, -2.0, 107.0)]


def test_peak_favorable_move():
    # Reference 107; forward window [104, 100, 102]; 107 - min(100) = 7.0
    assert chart_trends.peak_favorable_move([107.0, 104.0, 100.0, 102.0], 0, 3) == 7.0
    # Monotonic rise: price never drops below the reference, so the move is negative.
    assert chart_trends.peak_favorable_move([100.0, 101.0, 102.0, 103.0], 0, 3) == -1.0

def test_valley_favorable_move():
    # Reference 100; forward window [102, 107, 104]; max(107) - 100 = 7.0
    assert chart_trends.valley_favorable_move([100.0, 102.0, 107.0, 104.0], 0, 3) == 7.0
    # Monotonic fall: price never rises above the reference, so the move is negative.
    assert chart_trends.valley_favorable_move([105.0, 104.0, 103.0, 102.0], 0, 3) == -1.0

def test_peaks_keeps_valid_index_zero_peak():
    """Regression: index-0 extremum must not be dropped (Rust 1.3.0 fix)."""
    assert chart_trends.peaks([110., 109., 108., 107.], 2, 1) == [(110.0, 0)]


def test_peaks_does_not_drop_retained_peak_after_monotonic_run():
    """Regression: peak retained after a monotonic run must survive (Rust 1.3.0 fix)."""
    assert chart_trends.peaks([110., 109., 108., 120.], 2, 2) == [(110.0, 0), (120.0, 3)]


def test_favorable_move_invalid_input():
    # Empty prices -> EmptyData -> ValueError
    with pytest.raises(ValueError):
        chart_trends.peak_favorable_move([], 0, 3)
    # period == 0 -> InvalidPeriod -> ValueError
    with pytest.raises(ValueError):
        chart_trends.peak_favorable_move([100.0, 101.0, 102.0], 0, 0)
    # Forward window out of bounds (index + period >= len) -> InvalidPeriod -> ValueError
    with pytest.raises(ValueError):
        chart_trends.valley_favorable_move([100.0, 101.0, 102.0], 1, 3)


