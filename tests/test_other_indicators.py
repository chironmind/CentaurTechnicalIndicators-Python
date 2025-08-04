import pytest

from pytechnicalindicators import other_indicators

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

def test_single_return_on_investment():
    assert other_indicators.single.return_on_investment(prices[0], prices[-1], 1000) == (990.0, -1.0)

def test_bulk_return_on_investment():
    assert other_indicators.bulk.return_on_investment(prices, 1000) == [(1020.0, 2.0), (1030.0, 0.9803921568627451), (1010.0, -1.9417475728155338), (990.0, -1.9801980198019802)]

def test_single_true_range():
    assert other_indicators.single.true_range(close[-2], high[-1], low[-1]) == 16.0

def test_bulk_true_range():
    assert other_indicators.bulk.true_range(close, high, low) == [25.0, 18.0, 5.0, 16.0, 16.0]

def test_single_average_true_range():
    assert other_indicators.single.average_true_range(close, high, low, "simple") == 16.0
    assert other_indicators.single.average_true_range(close, high, low, "smoothed") == 15.30699666825321
    assert other_indicators.single.average_true_range(close, high, low, "exponential") == 15.033175355450236
    assert other_indicators.single.average_true_range(close, high, low, "median") == 16.0
    assert other_indicators.single.average_true_range(close, high, low, "mode") == 16.0
    with pytest.raises(ValueError):
        other_indicators.single.average_true_range(close, high, low, "")

def test_bulk_average_true_range():
    assert other_indicators.bulk.average_true_range(close, high, low, "simple", 3) == [16.0, 13.0, 12.333333333333334]
    assert other_indicators.bulk.average_true_range(close, high, low, "smoothed", 3) == [13.315789473684212, 12.947368421052632, 13.68421052631579]
    assert other_indicators.bulk.average_true_range(close, high, low, "exponential", 3) == [11.571428571428571, 13.142857142857142, 14.428571428571429]
    assert other_indicators.bulk.average_true_range(close, high, low, "median", 3) == [18.0, 16.0, 16.0]
    assert other_indicators.bulk.average_true_range(close, high, low, "mode", 3) == [16.0, 13.0, 16.0]
    with pytest.raises(ValueError):
        other_indicators.bulk.average_true_range(close, high, low, "", 3)

def test_single_internal_bar_strength():
    assert other_indicators.single.internal_bar_strength(high[-1], low[-1], close[-1]) == 0.5625

def test_bulk_internal_bar_strength():
    assert other_indicators.bulk.internal_bar_strength(high, low, close) == [0.68, 0.4444444444444444, 0.2, 0.8125, 0.5625]

def test_bulk_positivity_indicator():
    assert other_indicators.bulk.positivity_indicator(open_prices, close, 3, "simple") == [(-0.4975124378109453, -3.9158374792703152), (1.6042780748663104, -1.2977447876482116), (-4.25531914893617, -1.0495178372936016)]
    assert other_indicators.bulk.positivity_indicator(open_prices, close, 3, "smoothed") == [(-0.4975124378109453, -3.1304006284367643), (1.6042780748663104, -0.44981957647730964), (-4.25531914893617, -1.6138028232879709)] 
    assert other_indicators.bulk.positivity_indicator(open_prices, close, 3, "exponential") == [(-0.4975124378109453, -2.605721393034826), (1.6042780748663104, 0.060298203406193), (-4.25531914893617, -2.0443189834032864)]
    assert other_indicators.bulk.positivity_indicator(open_prices, close, 3, "median") == [(-0.4975124378109453, -5.0), (1.6042780748663104, -0.4975124378109453), (-4.25531914893617, -0.4975124378109453)]
    assert other_indicators.bulk.positivity_indicator(open_prices, close, 3, "mode") == [(-0.4975124378109453, -3.6666666666666665), (1.6042780748663104, -1.0), (-4.25531914893617, -0.6666666666666666)]
    with pytest.raises(ValueError):
        other_indicators.bulk.positivity_indicator(open_prices, close, 3, "")
