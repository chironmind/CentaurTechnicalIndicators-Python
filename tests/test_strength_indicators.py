import pytest

from pytechnicalindicators import strength_indicators

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
high = [200.0, 210.0, 205.0, 190.0, 195.0]
low = [175.0, 192.0, 200.0, 174.0, 179.0]
close = [192.0, 200.0, 201.0, 187.0, 188.0]
open_prices = [180.0, 190.0, 200.0, 190.0, 180.0]
volume = [1000.0, 1500.0, 1200.0, 900.0, 1300.0]

def test_single_accumulation_distribution():
    assert strength_indicators.single.accumulation_distribution(high[-1], low[-1], close[-1], volume[-1], 0.0) == 162.5

def test_bulk_accumulation_distribution_no_previous():
    assert strength_indicators.bulk.accumulation_distribution(high, low, close, volume, 0.0) == [360.0, 193.33333333333334, -526.6666666666666, 35.83333333333337, 198.33333333333337]

def test_single_volume_index():
    assert strength_indicators.single.volume_index(close[-1], close[-2], 0.0) == 0.005376190340015442

def test_bulk_positive_volume_index():
    assert strength_indicators.bulk.positive_volume_index(close, volume, 0.0) == [0.043402777777777776, 0.043402777777777776, 0.043402777777777776, 0.04363487819370172]

def test_bulk_negative_volume_index_no_previous():
    assert strength_indicators.bulk.negative_volume_index(close, volume, 0.0) == [0.0, 0.005025, 0.004675, 0.004675]

def test_single_relative_vigor_index():
    assert strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "simple") == 0.27607361963190186
    assert strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "smoothed") == 0.2468619246861925
    assert strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "exponential") == 0.2317460317460318
    assert strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "median") == 0.27607361963190186
    assert strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "mode") == 0.25
    with pytest.raises(ValueError):
        strength_indicators.single.relative_vigor_index(open_prices, high, low, close, "")

def test_bulk_relative_vigor_index():
     assert strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "simple", 4) == [0.3563218390804598, 0.1842105263157895]
     assert strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "smoothed", 4) == [0.3563218390804598, 0.1842105263157895]
     assert strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "exponential", 4) == [0.3563218390804598, 0.1842105263157895]
     assert strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "median", 4) == [0.3563218390804598, 0.1842105263157895]
     assert strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "mode", 4) == [0.3333333333333333, 0.15384615384615385]
     with pytest.raises(ValueError):
         strength_indicators.bulk.relative_vigor_index(open_prices, high, low, close, "", 4)

