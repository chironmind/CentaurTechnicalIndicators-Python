import pytest

from pytechnicalindicators import momentum_indicators

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

def test_single_relative_strength_index():
    assert momentum_indicators.single.relative_strength_index(prices, "simple") == 42.857142857142854
    assert momentum_indicators.single.relative_strength_index(prices, "smoothed") == 39.99999999999999
    assert momentum_indicators.single.relative_strength_index(prices, "exponential") == 38.46153846153846
    assert momentum_indicators.single.relative_strength_index(prices, "median") == 42.857142857142854
    assert momentum_indicators.single.relative_strength_index(prices, "mode") == 42.857142857142854
    with pytest.raises(ValueError):
        momentum_indicators.single.relative_strength_index(prices, "")


def test_bulk_relative_strength_index():
    assert momentum_indicators.bulk.relative_strength_index(prices, "simple", 3) == [100.0, 33.33333333333333, 0.0]
    assert momentum_indicators.bulk.relative_strength_index(prices, "smoothed", 3) == [100.0, 33.33333333333333, 0.0]
    assert momentum_indicators.bulk.relative_strength_index(prices, "exponential", 3) == [100.0, 33.33333333333333, 0.0]
    assert momentum_indicators.bulk.relative_strength_index(prices, "median", 3) == [100.0, 33.33333333333333, 0.0]
    assert momentum_indicators.bulk.relative_strength_index(prices, "mode", 3) == [100.0, 33.33333333333333, 0.0]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.relative_strength_index(prices, "", 3)

def test_single_stochastic_oscillator():
    assert momentum_indicators.single.stochastic_oscillator(prices) == 0.0

def test_bulk_stochastic_oscillator():
    assert momentum_indicators.bulk.stochastic_oscillator(prices, 3) == [100.0, 0.0, 0.0]

stochastic_oscillators = [0.0, 25.0, 50.0, 33.0, 73.0]

def test_single_slow_stochastic():
    assert momentum_indicators.single.slow_stochastic(stochastic_oscillators, "simple") == 36.2
    assert momentum_indicators.single.slow_stochastic(stochastic_oscillators, "smoothed") == 42.89623988576868
    assert momentum_indicators.single.slow_stochastic(stochastic_oscillators, "exponential") == 47.8436018957346
    assert momentum_indicators.single.slow_stochastic(stochastic_oscillators, "median") == 33.0
    assert momentum_indicators.single.slow_stochastic(stochastic_oscillators, "mode") == 36.2
    with pytest.raises(ValueError):
        momentum_indicators.single.slow_stochastic(stochastic_oscillators, "")

def test_bulk_slow_stochastic():
    assert momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "simple", 3) == [25.0, 36.0, 52.0]
    assert momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "smoothed", 3) == [31.578947368421055, 36.684210526315795, 55.526315789473685]
    assert momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "exponential", 3) == [35.714285714285715, 36.714285714285715, 58.285714285714285]
    assert momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "median", 3) == [25.0, 33.0, 50.0]
    assert momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "mode", 3) == [25.0, 36.0, 52.0]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, "", 3)

slow_stochastics = [75.0, 60.0, 73.0, 58.0]

def test_single_slowest_stochastic():
    assert momentum_indicators.single.slowest_stochastic(slow_stochastics, "simple") == 66.5
    assert momentum_indicators.single.slowest_stochastic(slow_stochastics, "smoothed") == 65.14857142857143
    assert momentum_indicators.single.slowest_stochastic(slow_stochastics, "exponential") == 64.15441176470587
    assert momentum_indicators.single.slowest_stochastic(slow_stochastics, "median") == 66.5
    assert momentum_indicators.single.slowest_stochastic(slow_stochastics, "mode") == 66.5
    with pytest.raises(ValueError):
        momentum_indicators.single.slowest_stochastic(slow_stochastics, "")

def test_bulk_slowest_stochastic():
    assert momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "simple", 3) == [69.33333333333333, 63.666666666666664]
    assert momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "smoothed", 3) == [69.31578947368422, 63.15789473684211]
    assert momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "exponential", 3) == [69.57142857142857, 62.57142857142857]
    assert momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "median", 3) == [73.0, 60.0]
    assert momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "mode", 3) == [69.33333333333333, 63.666666666666664]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.slowest_stochastic(slow_stochastics, "", 3)

def test_single_williams_percent_r():
    assert momentum_indicators.single.williams_percent_r(high, low, close[-1]) == -61.111111111111114

def test_bulk_williams_percent_r():
    assert momentum_indicators.bulk.williams_percent_r(high, low, close, 3) == [-25.71428571428571, -63.888888888888886, -54.83870967741935]

def test_single_money_flow_index():
    assert momentum_indicators.single.money_flow_index(prices, volume) == 56.771463119709786

def test_bulk_money_flow_index():
    assert momentum_indicators.bulk.money_flow_index(prices, volume, 3) == [55.314533622559644, 0.0, 58.60655737704918]

def test_single_rate_of_change():
    assert momentum_indicators.single.rate_of_change(prices[-1], prices[-2]) == -1.9801980198019802

def test_bulk_rate_of_change():
    assert momentum_indicators.bulk.rate_of_change(prices) == [2.0, 0.9803921568627451, -1.9417475728155338, -1.9801980198019802]

def test_single_on_balance_volume():
    assert momentum_indicators.single.on_balance_volume(prices[-1], prices[-2], volume[-1], 0.0) == -1300.0

def test_bulk_on_balance_volume():
    assert momentum_indicators.bulk.on_balance_volume(prices, volume, 0.0) == [1500.0, 2700.0, 1800.0, 500.0]

def test_single_commodity_channel_index():
    assert momentum_indicators.single.commodity_channel_index(prices, "simple", "standard", 0.015) == -94.28090415820633
    assert momentum_indicators.single.commodity_channel_index(prices, "smoothed", "mean", 0.015) == -100.9043312708234
    assert momentum_indicators.single.commodity_channel_index(prices, "exponential", "median", 0.015) == -89.52080042127541
    assert momentum_indicators.single.commodity_channel_index(prices, "median", "ulcer", 0.015) == -68.66666666666667
    assert momentum_indicators.single.commodity_channel_index(prices, "mode", "mode", 0.015) == -111.11111111111111
    with pytest.raises(ValueError):
        momentum_indicators.single.commodity_channel_index(prices, "", "mode", 0.015)
    with pytest.raises(ValueError):
        momentum_indicators.single.commodity_channel_index(prices, "mode", "", 0.015)

def test_bulk_commodity_channel_index():
    assert momentum_indicators.bulk.commodity_channel_index(prices, "simple", "standard", 0.015, 3) == [71.26966450997959, -81.64965809277261, -81.64965809277261]
    assert momentum_indicators.bulk.commodity_channel_index(prices, "smoothed", "mean", 0.015, 3) == [56.84210526315789, -84.21052631579046, -73.68421052631648]
    assert momentum_indicators.bulk.commodity_channel_index(prices, "exponential", "median", 0.015, 3) == [47.619047619047215, -71.42857142857083, -57.14285714285695]
    assert momentum_indicators.bulk.commodity_channel_index(prices, "median", "ulcer", 0.015, 3) == [0.0, -59.467077726531464, -53.1889712879152]
    assert momentum_indicators.bulk.commodity_channel_index(prices, "mode", "mode", 0.015, 3) == [79.99999999999983, -100.00000000000001, -100.00000000000001]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.commodity_channel_index(prices, "", "mode", 0.015, 3)
    with pytest.raises(ValueError):
        momentum_indicators.bulk.commodity_channel_index(prices, "mode", "", 0.015, 3)

def test_single_mcginley_dynamic_commodity_channel_index():
    assert momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "standard", 0.015) == (0.0, 99.0)
    assert momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "mean", 0.015) == (0.0, 99.0)
    assert momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "median", 0.015) == (0.0, 99.0)
    assert momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "mode", 0.015) == (0.0, 99.0)
    assert momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "ulcer", 0.015) == (0.0, 99.0)
    with pytest.raises(ValueError):
        momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, "", 0.015)

def test_bulk_mcginley_dynamic_commodity_channel_index():
    assert momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "standard", 0.015, 3) == [(0.0, 103.0), (-104.42491334912364, 102.2789387706985), (-83.02972804940603, 101.03380467203097)]
    assert momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "mean", 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "median", 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "mode", 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "ulcer", 0.015, 3) == [(0.0, 103.0), (-76.05475128460245, 102.2789387706985), (-54.08798915294147, 101.03380467203097)]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, "", 0.015, 3)

def test_single_macd_line():
    assert momentum_indicators.single.macd_line(prices, 3, "simple", "simple") == 0.0
    assert momentum_indicators.single.macd_line(prices, 3, "smoothed", "smoothed") == -0.3425937523484919
    assert momentum_indicators.single.macd_line(prices, 3, "exponential", "exponential") == -0.46851726472581845
    assert momentum_indicators.single.macd_line(prices, 3, "median", "median") == 0.0
    assert momentum_indicators.single.macd_line(prices, 3, "mode", "mode") == 0.0
    with pytest.raises(ValueError):
        momentum_indicators.single.macd_line(prices, 3, "", "mode")
    with pytest.raises(ValueError):
        momentum_indicators.single.macd_line(prices, 3, "mode", "")

def test_bulk_macd_line():
    assert momentum_indicators.bulk.macd_line(prices, 2, "simple", 4, "simple") == [0.5, -1.25]
    assert momentum_indicators.bulk.macd_line(prices, 2, "smoothed", 4, "smoothed") == [0.06666666666667709, -1.1676190476190413]
    assert momentum_indicators.bulk.macd_line(prices, 2, "exponential", 4, "exponential") == [-0.11764705882352189, -1.01102941176471]
    assert momentum_indicators.bulk.macd_line(prices, 2, "median", 4, "median") == [0.5, -1.5]
    assert momentum_indicators.bulk.macd_line(prices, 2, "mode", 4, "mode") == [0.5, -1.25]
    with pytest.raises(ValueError):
         momentum_indicators.bulk.macd_line(prices, 2, "", 4, "mode")
    with pytest.raises(ValueError):
        momentum_indicators.bulk.macd_line(prices, 2, "mode", 4, "")

macds = [-0.3, -1.7, -0.8, 0.2, 1.6]

def test_single_signal_line():
    assert momentum_indicators.single.signal_line(macds, "simple") == -0.1999999999999999
    assert momentum_indicators.single.signal_line(macds, "smoothed") == 0.07577344121846738
    assert momentum_indicators.single.signal_line(macds, "exponential") == 0.31279620853080564
    assert momentum_indicators.single.signal_line(macds, "median") == -0.3
    assert momentum_indicators.single.signal_line(macds, "mode") == 0.0
    with pytest.raises(ValueError):
        momentum_indicators.single.signal_line(macds, "")

def test_bulk_signal_line():
    assert momentum_indicators.bulk.signal_line(macds, "simple", 3) == [-0.9333333333333332, -0.7666666666666666, 0.3333333333333333]
    assert momentum_indicators.bulk.signal_line(macds, "smoothed", 3) == [-0.9789473684210527, -0.5157894736842106, 0.6526315789473685]
    assert momentum_indicators.bulk.signal_line(macds, "exponential", 3) == [-0.9857142857142857, -0.35714285714285715, 0.8571428571428573]
    assert momentum_indicators.bulk.signal_line(macds, "median", 3) == [-0.8, -0.8, 0.2]
    assert momentum_indicators.bulk.signal_line(macds, "mode", 3) == [-1.0, -1.0, 0.3333333333333333]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.signal_line(macds, "", 3)

def test_single_mcginley_dynamic_macd_line():
    assert momentum_indicators.single.mcginley_dynamic_macd_line(prices, 3, 0.0, 0.0) == (0.0, 99.0, 99.0)

def test_bulk_mcginley_dynamic_macd_line():
    assert momentum_indicators.bulk.mcginley_dynamic_macd_line(prices, 2, 0.0, 4, 0.0) == [(0.0, 101.0, 101.0), (-0.541644978308824, 99.91671004338234, 100.45835502169116)]

def test_single_chaikin_oscillator():
    assert momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "simple", "simple") == (175.33333333333326, 2635.8333333333335)
    assert momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "smoothed", "smoothed") == (383.32130898402636, 2635.8333333333335)
    assert momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "exponential", "exponential") == (460.72839088241915, 2635.8333333333335)
    assert momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "median", "median") == (-157.49999999999997, 2635.8333333333335)
    assert momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "mode", "mode") == (175.39999999999998, 2635.8333333333335)
    with pytest.raises(ValueError):
        momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "", "mode")
    with pytest.raises(ValueError):
        momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, "mode", "")

def test_bulk_chaikin_oscillator():
    assert momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "simple", "simple") == [(-261.04166666666663, 35.83333333333337), (751.25, 2311.666666666667)]
    assert momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "smoothed", "smoothed") == [(-115.6285714285714, 35.83333333333337), (873.8904761904763, 2311.666666666667)]
    assert momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "exponential", "exponential") == [(-43.759191176470615, 35.83333333333337), (832.5735294117644, 2311.666666666667)]
    assert momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "median", "median") == [(-360.0, 35.83333333333337), (1221.25, 2311.666666666667)]
    assert momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "mode", "mode") == [(-261.0, 35.83333333333337), (751.5, 2311.666666666667)]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "", "mode")
    with pytest.raises(ValueError):
        momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, "mode", "")

def test_single_percentage_price_oscillator():
    assert momentum_indicators.single.percentage_price_oscillator(prices, 3, "simple") == 0.0
    assert momentum_indicators.single.percentage_price_oscillator(prices, 3, "smoothed") == -0.339819877574384
    assert momentum_indicators.single.percentage_price_oscillator(prices, 3, "exponential") == -0.4656702758356384
    assert momentum_indicators.single.percentage_price_oscillator(prices, 3, "median") == 0.0
    assert momentum_indicators.single.percentage_price_oscillator(prices, 3, "mode") == 0.0
    with pytest.raises(ValueError):
        momentum_indicators.single.percentage_price_oscillator(prices, 3, "")


def test_bulk_percentage_price_oscillator():
    assert momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "simple") == [0.0]
    assert momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "smoothed") == [-0.339819877574384]
    assert momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "exponential") == [-0.4656702758356384]
    assert momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "median") == [0.0]
    assert momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "mode") == [0.0]
    with pytest.raises(ValueError):
        momentum_indicators.bulk.percentage_price_oscillator(prices, 3, 5, "")

def test_single_chande_momentum_oscillator():
    assert momentum_indicators.single.chande_momentum_oscillator(prices) == -14.285714285714285

def test_bulk_chande_momentum_oscillator():
    assert momentum_indicators.bulk.chande_momentum_oscillator(prices, 3) == [100.0, -33.33333333333333, -100.0]

