import PyTechnicalIndicators

"""The purpose of these tests are just to confirm that the bindings work.

These tests are not meant to be in depth, nor to test all edge cases, those should be 
done in [RustTI](). These tests exist to confirm whether an update in the bindings, or
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
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 42.857142857142854
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == 39.99999999999999
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 38.46153846153846
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 36.363636363636374
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 42.857142857142854
    assert PyTechnicalIndicators.momentum_indicators.single.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 42.857142857142854

def test_bulk_relative_strength_index():
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3) == [100.0, 33.33333333333333, 0.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3) == [100.0, 33.33333333333333, 0.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3) == [100.0, 33.33333333333333, 0.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3) == [100.0, 33.33333333333333, 0.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3) == [100.0, 33.33333333333333, 0.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.relative_strength_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3) == [100.0, 33.33333333333333, 0.0]

def test_single_stochastic_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.single.stochastic_oscillator(prices) == 0.0

def test_bulk_stochastic_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.bulk.stochastic_oscillator(prices, 3) == [100.0, 0.0, 0.0]

stochastic_oscillators = [0.0, 25.0, 50.0, 33.0, 73.0]

def test_single_slow_stochastic():
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 36.2
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == 42.89623988576868
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 47.8436018957346
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 56.38785006462732
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 33.0
    assert PyTechnicalIndicators.momentum_indicators.single.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 36.2

def test_bulk_slow_stochastic():
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3) == [25.0, 36.0, 52.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3) == [31.578947368421055, 36.684210526315795, 55.526315789473685]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3) == [35.714285714285715, 36.714285714285715, 58.285714285714285]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3) == [41.7910447761194, 36.07462686567164, 63.26865671641791]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3) == [25.0, 33.0, 50.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slow_stochastic(stochastic_oscillators, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3) == [25.0, 36.0, 52.0]

slow_stochastics = [75.0, 60.0, 73.0, 58.0]

def test_single_slowest_stochastic():
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 66.5
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == 65.14857142857143
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 64.15441176470587
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 62.33748443337485
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 66.5
    assert PyTechnicalIndicators.momentum_indicators.single.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 66.5

def test_bulk_slowest_stochastic():
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3) == [69.33333333333333, 63.666666666666664]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3) == [69.31578947368422, 63.15789473684211]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3) == [69.57142857142857, 62.57142857142857]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3) == [70.40298507462687, 61.25373134328358]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3) == [73.0, 60.0]
    assert PyTechnicalIndicators.momentum_indicators.bulk.slowest_stochastic(slow_stochastics, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3) == [69.33333333333333, 63.666666666666664]

def test_single_williams_percent_r():
    assert PyTechnicalIndicators.momentum_indicators.single.williams_percent_r(high, low, close[-1]) == -63.888888888888886

def test_bulk_williams_percent_r():
    assert PyTechnicalIndicators.momentum_indicators.bulk.williams_percent_r(high, low, close, 3) == [-25.71428571428571, -63.888888888888886]

def test_single_money_flow_index():
    assert PyTechnicalIndicators.momentum_indicators.single.money_flow_index(prices, volume) == 56.771463119709786

def test_bulk_money_flow_index():
    assert PyTechnicalIndicators.momentum_indicators.bulk.money_flow_index(prices, volume, 3) == [55.314533622559644, 0.0, 58.60655737704918]

def test_single_rate_of_change():
    assert PyTechnicalIndicators.momentum_indicators.single.rate_of_change(prices[-1], prices[-2]) == -1.9801980198019802

def test_bulk_rate_of_change():
    assert PyTechnicalIndicators.momentum_indicators.bulk.rate_of_change(prices) == [2.0, 0.9803921568627451, -1.9417475728155338, -1.9801980198019802]

def test_single_on_balance_volume():
    assert PyTechnicalIndicators.momentum_indicators.single.on_balance_volume(prices[-1], prices[-2], volume[-1], 0.0) == -1300.0

def test_bulk_on_balance_volume():
    assert PyTechnicalIndicators.momentum_indicators.bulk.on_balance_volume(prices, volume, 0.0) == [1500.0, 2700.0, 1800.0, 500.0]

def test_single_commodity_channel_index():
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015) == -94.28090415820633
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 0.015) == -100.9043312708234
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 0.015) == -89.52080042127541
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 0.015) == -62.23371152281093
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.DeviationModel.UlcerIndex(), 0.015) == -68.66666666666667
    assert PyTechnicalIndicators.momentum_indicators.single.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015) == -94.28090415820633

def test_bulk_commodity_channel_index():
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015, 3) == [71.26966450997959, -81.64965809277261, -81.64965809277261]
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 0.015, 3) == [56.84210526315789, -84.21052631579046, -73.68421052631648]
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 0.015, 3) == [47.619047619047215, -71.42857142857083, -57.14285714285695]
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 0.015, 3) == [23.28358208955226, -47.7611940298516, -32.83582089552227]
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.DeviationModel.UlcerIndex(), 0.015, 3) == [0.0, -59.467077726531464, -53.1889712879152]
    assert PyTechnicalIndicators.momentum_indicators.bulk.commodity_channel_index(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015, 3) == [71.26966450997959, -81.64965809277261, -81.64965809277261]

def test_single_mcginley_dynamic_commodity_channel_index():
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015) == (0.0, 99.0)
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 0.015) == (0.0, 99.0)
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 0.015) == (0.0, 99.0)
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 0.015) == (0.0, 99.0)
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.UlcerIndex(), 0.015) == (0.0, 99.0)

def test_bulk_mcginley_dynamic_commodity_channel_index():
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.StandardDeviation(), 0.015, 3) == [(0.0, 103.0), (-104.42491334912364, 102.2789387706985), (-83.02972804940603, 101.03380467203097)]
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 0.015, 3) == [(0.0, 103.0), (-127.89387706985026, 102.2789387706985), (-101.6902336015484, 101.03380467203097)]
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index(prices, 0.0, PyTechnicalIndicators.DeviationModel.UlcerIndex(), 0.015, 3) == [(0.0, 103.0), (-76.05475128460245, 102.2789387706985), (-54.08798915294147, 101.03380467203097)]

def test_single_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == -0.3425937523484919
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == -0.46851726472581845
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == -0.4634903895001514
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.macd_line(prices, 3, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 0.0

def test_bulk_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 4, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == [0.5, -1.25]
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 4, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == [0.06666666666667709, -1.1676190476190413]
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 4, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == [-0.11764705882352189, -1.01102941176471]
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 4, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == [-0.24853228962817298, -0.6520192136630385]
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 4, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == [0.5, -1.5]
    assert PyTechnicalIndicators.momentum_indicators.bulk.macd_line(prices, 2, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 4, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == [0.5, -1.25]

macds = [-0.3, -1.7, -0.8, 0.2, 1.6]

def test_single_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == -0.1999999999999999
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage()) == 0.07577344121846738
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 0.31279620853080564
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 0.7744937526928048
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == -0.3
    assert PyTechnicalIndicators.momentum_indicators.single.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 0.0

def test_bulk_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3) == [-0.9333333333333332, -0.7666666666666666, 0.3333333333333333]
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3) == [-0.9789473684210527, -0.5157894736842106, 0.6526315789473685]
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3) == [-0.9857142857142857, -0.35714285714285715, 0.8571428571428573]
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3) == [-0.9582089552238806, -0.12238805970149252, 1.1641791044776122]
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3) == [-0.8, -0.8, 0.2]
    assert PyTechnicalIndicators.momentum_indicators.bulk.signal_line(macds, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3) == [-1.0, -1.0, 0.3333333333333333]

def test_single_mcginley_dynamic_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.single.mcginley_dynamic_macd_line(prices, 3, 0.0, 0.0) == (0.0, 99.0, 99.0)

def test_bulk_mcginley_dynamic_macd_line():
    assert PyTechnicalIndicators.momentum_indicators.bulk.mcginley_dynamic_macd_line(prices, 2, 0.0, 4, 0.0) == [(0.0, 101.0, 101.0), (-0.541644978308824, 99.91671004338234, 100.45835502169116)]

def test_single_chaikin_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.single.chaikin_oscillator(high, low, close, volume, 3, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 0.0

def test_bulk_chaikin_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4)) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian()) == 0.0
    assert PyTechnicalIndicators.momentum_indicators.bulk.chaikin_oscillator(high, low, close, volume, 2, 4, 0.0, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMode()) == 0.0

# TODO: PPO

def test_single_chande_momentum_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.single.chande_momentum_oscillator(prices) == -14.285714285714285

def test_bulk_chande_momentum_oscillator():
    assert PyTechnicalIndicators.momentum_indicators.bulk.chande_momentum_oscillator(prices, 3) == [100.0, -33.33333333333333, -100.0]

















