import pytest

from pytechnicalindicators import trend_indicators

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
high = [200.0, 210.0, 205.0, 190.0, 185.0]
low = [175.0, 192.0, 200.0, 174.0, 179.0]
close = [192.0, 200.0, 201.0, 187.0, 188.0]
volume = [1000.0, 1500.0, 1200.0, 900.0, 1300.0]

def test_single_aroon_up():
    assert trend_indicators.single.aroon_up(high) == 25.0

def test_bulk_aroon_up():
    assert trend_indicators.bulk.aroon_up(high, 3) == [50.0, 0.0, 0.0]

def test_single_aroon_down():
    assert trend_indicators.single.aroon_down(low) == 75.0

def test_bulk_aroon_down():
    assert trend_indicators.bulk.aroon_down(low, 3) == [0.0, 100.0, 50.0]

def test_single_aroon_oscillator():
    assert trend_indicators.single.aroon_oscillator(25.0, 25.0) == 0.0

def test_bulk_aroon_oscillator():
    assert trend_indicators.bulk.aroon_oscillator([25.0, 50.0, 75.0], [25.0, 10.0, 100.0]) == [0.0, 40.0, -25.0]

def test_single_aroon_indicator():
    assert trend_indicators.single.aroon_indicator(high, low) == (25.0, 75.0, -50.0)

def test_bulk_aroon_indicator():
    assert trend_indicators.bulk.aroon_indicator(high, low, 3) == [(50.0, 0.0, 50.0), (0.0, 100.0, -100.0), (0.0, 50.0, -50.0)]

def test_single_short_parabolic_time_price_system():
    assert trend_indicators.single.short_parabolic_time_price_system(high[-1], min(low), 0.02, max(high[-2:])) == 190.0

def test_single_long_parabolic_time_price_system():
    assert trend_indicators.single.long_parabolic_time_price_system(low[-1], max(high), 0.02, min(low[-2:])) == 174.0

def test_bulk_parabolic_time_price_system():
    assert trend_indicators.bulk.parabolic_time_price_system(high, low, 0.0, 0.02, 0.2, 'long', 0.0) == [175.0, 175.0, 182.0, 210.0, 210.0]
    with pytest.raises(ValueError):
        trend_indicators.bulk.parabolic_time_price_system(high, low, 0.0, 0.02, 0.2, '', 0.0)

extended_high = high + [180.0, 195.0, 205.0, 210.0, 225.0]
extended_low = low + [160.0, 150.0, 170.0, 190.0, 185.0]
extended_close = close + [175.0, 160.0, 180.0, 200.0, 205.0]

def test_bulk_directional_movement_system():
    assert trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "simple") == [(25.0, 19.0, 41.80035650623886, 61.64091899386017), (30.0, 0.0, 41.800356506238856, 56.19429590017825), (31.57894736842105, 0.0, 71.2121212121212, 56.50623885918003)]
    assert trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "smoothed") == [(25.0, 19.0, 31.22713200112581, 59.76561278418864), (30.0, 0.0, 54.15142133408387, 56.17787784970447), (31.57894736842105, 0.0, 81.81818181818183, 56.52265690965382)]
    assert trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "exponential") == [(25.0, 19.0, 25.439266615737203, 58.75137933961463), (30.0, 0.0, 62.7196333078686, 56.14973262032085), (31.57894736842105, 0.0, 87.66233766233766, 56.55080213903743)]
    assert trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "median") == [(25.0, 19.0, 13.636363636363635, 56.81818181818182), (30.0, 0.0, 13.636363636363635, 56.81818181818182), (31.57894736842105, 0.0, 100.0, 56.81818181818182)]
    assert trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "mode") == [(25.0, 19.0, 42.0, 71.0), (30.0, 0.0, 42.0, 71.0), (31.57894736842105, 0.0, 100.0, 71.0)]
    with pytest.raises(ValueError):
        trend_indicators.bulk.directional_movement_system(extended_high, extended_low, extended_close, 3, "")

def test_single_volume_price_trend():
    assert trend_indicators.single.volume_price_trend(prices[-1], prices[-2], volume[-1], 0.0) == -25.742574257425744

def test_bulk_volume_price_trend():
    assert trend_indicators.bulk.volume_price_trend(prices, volume[:-1], 0.0) == [20.0, 34.705882352941174, 11.40491147915477, -6.416870699063054]

def test_single_true_strength_index():
    assert trend_indicators.single.true_strength_index(prices, 3, "simple", "simple") == -0.2
    assert trend_indicators.single.true_strength_index(prices, 3, "smoothed", "smoothed") == -0.5599999999999999
    assert trend_indicators.single.true_strength_index(prices, 3, "exponential", "exponential") == -0.7254901960784312
    assert trend_indicators.single.true_strength_index(prices, 3, "median", "median") == -0.25
    assert trend_indicators.single.true_strength_index(prices, 3, "mode", "mode") == -0.5
    with pytest.raises(ValueError):
        trend_indicators.single.true_strength_index(prices, 3, "", "mode")
    with pytest.raises(ValueError):
        trend_indicators.single.true_strength_index(prices, 3, "mode", "")

def test_bulk_true_strength_index():
    assert trend_indicators.bulk.true_strength_index(prices, "simple", 2, "simple", 3) == [-0.19999999999999998]
    assert trend_indicators.bulk.true_strength_index(prices, "smoothed", 2, "smoothed", 3) == [-0.56]
    assert trend_indicators.bulk.true_strength_index(prices, "exponential", 2, "exponential", 3) == [-0.7254901960784313]
    assert trend_indicators.bulk.true_strength_index(prices, "median", 2, "median", 3) == [-0.3333333333333333]
    assert trend_indicators.bulk.true_strength_index(prices, "mode", 2, "mode", 3) == [-0.16666666666666666]
    with pytest.raises(ValueError):
        trend_indicators.bulk.true_strength_index(prices, "", 2, "mode", 3)
    with pytest.raises(ValueError):
        trend_indicators.bulk.true_strength_index(prices, "mode", 2, "", 3)

