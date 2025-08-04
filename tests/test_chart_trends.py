from pytechnicalindicators import chart_trends

"""The purpose of these tests are just to confirm that the bindings work.

These tests are not meant to be in depth, nor to test all edge cases, those should be
done in [RustTI](https://github.com/chironmind/RustTI). These tests exist to confirm whether an update in the bindings, or
RustTI has broken functionality.

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
        soft_r_squared_minimum=0.75,
        soft_r_squared_maximum=1.0,
        hard_r_squared_minimum=0.5,
        hard_r_squared_maximum=1.5,
        soft_standard_error_multiplier=2.0,
        hard_standard_error_multiplier=3.0,
        soft_reduced_chi_squared_multiplier=2.0,
        hard_reduced_chi_squared_multiplier=3.0
    )
   
    assert trends == [(0, 2, 1.5, 100.16666666666667), (2, 4, -2.0, 107.0)]

