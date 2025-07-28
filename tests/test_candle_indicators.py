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

def test_single_moving_constant_envelopes():
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3.0) == (97.97, 101.0, 104.03)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3.0) == (97.79178962398858, 100.81627796287482, 103.84076630176106)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3.0) == (97.59303317535547, 100.61137440758296, 103.62971563981044)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3.0) == (97.11660060318827, 100.1202068074106, 103.12381301163292)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3.0) == (97.97, 101.0, 104.03)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3.0) == (97.97, 101.0, 104.03)

def test_bulk_moving_constant_envelopes():
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 3.0, 3) == [(98.61666666666667, 101.66666666666667, 104.71666666666667), (98.94, 102.0, 105.06), (97.97, 101.0, 104.03)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 3.0, 3) == [(98.99105263157895, 102.05263157894737, 105.11421052631579), (98.78684210526316, 101.8421052631579, 104.89736842105265), (97.45947368421054, 100.47368421052633, 103.48789473684212)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 3.0, 3) == [(99.21714285714286, 102.28571428571429, 105.35428571428572), (98.66285714285713, 101.71428571428571, 104.76571428571428), (97.13857142857142, 100.14285714285714, 103.14714285714285)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 3.0, 3) == [(99.53358208955224, 102.61194029850746, 105.69029850746269), (98.43328358208956, 101.47761194029852, 104.52194029850747), (96.66701492537312, 99.65671641791045, 102.64641791044777)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 3.0, 3) == [(98.94, 102.0, 105.06), (98.94, 102.0, 105.06), (97.97, 101.0, 104.03)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_envelopes(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 3.0, 3) == [(98.61666666666667, 101.66666666666667, 104.71666666666667), (98.94, 102.0, 105.06), (97.97, 101.0, 104.03)]

def test_single_mcginley_dynamic_envelopes():
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_envelopes(prices, 3.0, 0.0) == (96.03, 99.0, 101.97)

def test_bulk_mcginley_dynamic_envelopes():
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_envelopes(prices, 3.0, 0.0, 3) == [(99.91, 103.0, 106.09), (99.21057060757755, 102.2789387706985, 105.34730693381945), (98.00279053187003, 101.03380467203097, 104.0648188121919)]

def test_single_moving_constant_bands():
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0) == (96.75735931288071, 101.0, 105.24264068711929)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 3.0) == (97.21627796287483, 100.81627796287482, 104.41627796287482)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 3.0) == (97.01137440758296, 100.61137440758296, 104.21137440758295)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 3.0) == (96.5202068074106, 100.1202068074106, 103.72020680741059)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.DeviationModel.UlcerIndex(), 3.0) == (95.1747572815534, 101.0, 106.8252427184466)
    assert PyTechnicalIndicators.candle_indicators.single.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0) == (96.75735931288071, 101.0, 105.24264068711929)

def test_bulk_moving_constant_bands():
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0, 3) == [(97.92500927989273, 101.66666666666667, 105.40832405344061), (99.55051025721683, 102.0, 104.44948974278317), (96.10102051443364, 101.0, 105.89897948556636)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 3.0, 3) == [(98.71929824561404, 102.05263157894737, 105.3859649122807), (99.8421052631579, 101.8421052631579, 103.8421052631579), (96.47368421052633, 100.47368421052633, 104.47368421052633)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 3.0, 3) == [(99.28571428571429, 102.28571428571429, 105.28571428571429), (99.71428571428571, 101.71428571428571, 103.71428571428571), (96.14285714285714, 100.14285714285714, 104.14285714285714)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 3.0, 3) == [(99.27860696517413, 102.61194029850746, 105.94527363184079), (99.47761194029852, 101.47761194029852, 103.47761194029852), (95.65671641791045, 99.65671641791045, 103.65671641791045)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.DeviationModel.UlcerIndex(), 3.0, 3) == [(102.0, 102.0, 102.0), (98.63679454840995, 102.0, 105.36320545159005), (93.47964398794676, 101.0, 108.52035601205324)]
    assert PyTechnicalIndicators.candle_indicators.bulk.moving_constant_bands(prices, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0, 3) == [(97.92500927989273, 101.66666666666667, 105.40832405344061), (99.55051025721683, 102.0, 104.44948974278317), (96.10102051443364, 101.0, 105.89897948556636)]

def test_single_mcginley_dynamic_bands():
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0, 0.0) == (94.75735931288071, 99.0, 103.24264068711929)
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 3.0, 0.0) == (95.4, 99.0, 102.6)
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 3.0, 0.0) == (95.4, 99.0, 102.6)
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 3.0, 0.0) == (95.4, 99.0, 102.6)
    assert PyTechnicalIndicators.candle_indicators.single.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.UlcerIndex(), 3.0, 0.0) == (93.1747572815534, 99.0, 104.8252427184466)

def test_bulk_mcginley_dynamic_bands():
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.StandardDeviation(), 3.0, 0.0, 3) == [(99.25834261322606, 103.0, 106.74165738677394), (99.82944902791533, 102.2789387706985, 104.72842851348167), (96.13482518646461, 101.03380467203097, 105.93278415759733)]
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.MeanAbsoluteDeviation(), 3.0, 0.0, 3) == [(99.66666666666667, 103.0, 106.33333333333333), (100.2789387706985, 102.2789387706985, 104.2789387706985), (97.03380467203097, 101.03380467203097, 105.03380467203097)]
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.MedianAbsoluteDeviation(), 3.0, 0.0, 3) == [(100.0, 103.0, 106.0), (100.2789387706985, 102.2789387706985, 104.2789387706985), (97.03380467203097, 101.03380467203097, 105.03380467203097)]
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.ModeAbsoluteDeviation(), 3.0, 0.0, 3) == [(99.66666666666667, 103.0, 106.33333333333333), (100.2789387706985, 102.2789387706985, 104.2789387706985), (97.03380467203097, 101.03380467203097, 105.03380467203097)]
    assert PyTechnicalIndicators.candle_indicators.bulk.mcginley_dynamic_bands(prices, PyTechnicalIndicators.DeviationModel.UlcerIndex(), 3.0, 0.0, 3) == [(103.0, 103.0, 103.0), (98.91573331910845, 102.2789387706985, 105.64214422228855), (93.51344865997773, 101.03380467203097, 108.55416068408421)]

def test_single_ichimoku_cloud():
    assert PyTechnicalIndicators.candle_indicators.single.ichimoku_cloud(high, low, close, 3, 4, 5) == (190.75, 192.0, 192.0, 189.5, 200.0)

def test_bulk_ichimoku_cloud():
    assert PyTechnicalIndicators.candle_indicators.bulk.ichimoku_cloud(high, low, close, 3, 4, 5) == [(190.75, 192.0, 192.0, 189.5, 200.0)]

def test_single_donchian_channels():
    assert PyTechnicalIndicators.candle_indicators.single.donchian_channels(high, low) == (174.0, 192.0, 210.0)

def test_bulk_donchian_channels():
    assert PyTechnicalIndicators.candle_indicators.bulk.donchian_channels(high, low, 3) == [(175.0, 192.5, 210.0), (174.0, 192.0, 210.0), (174.0, 189.5, 205.0)]

def test_single_keltner_channel():
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 2.0) == (162.66666666666666, 191.86666666666665, 221.06666666666663)
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 2.0) == (164.04600983658574, 190.49531968903696, 216.94462954148818)
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 2.0) == (164.56872037914695, 189.26066350710906, 213.95260663507116)
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 2.0) == (164.64024127531232, 186.86393795777678, 209.08763464024125)
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 2.0) == (157.0, 189.0, 221.0)
    assert PyTechnicalIndicators.candle_indicators.single.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 2.0) == (154.8, 184.0, 213.2)

def test_bulk_keltner_channel():
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 2.0, 3) == [(165.2222222222222, 197.2222222222222, 229.2222222222222), (169.44444444444443, 195.44444444444443, 221.44444444444443), (169.88888888888889, 189.88888888888889, 209.88888888888889)]
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 2.0, 3) == [(172.21052631578948, 198.84210526315792, 225.47368421052636), (167.14035087719301, 193.03508771929828, 218.92982456140354), (166.94736842105266, 187.6842105263158, 208.42105263157896)]
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 2.0, 3) == [(176.61904761904762, 199.76190476190476, 222.9047619047619), (165.04761904761904, 191.33333333333331, 217.6190476190476), (165.6190476190476, 186.47619047619045, 207.33333333333331)]
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 2.0, 3) == [(183.12437810945272, 200.9452736318408, 218.76616915422886), (160.87064676616913, 188.51243781094524, 216.15422885572136), (164.55721393034827, 185.00497512437812, 205.45273631840797)]
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 2.0, 3) == [(164.66666666666666, 200.66666666666666, 236.66666666666666), (168.66666666666666, 200.66666666666666, 232.66666666666666), (166.0, 184.0, 202.0)]
    assert PyTechnicalIndicators.candle_indicators.bulk.keltner_channel(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 2.0, 3) == [(165.33333333333334, 197.33333333333334, 229.33333333333334), (169.66666666666666, 195.66666666666666, 221.66666666666666), (164.0, 184.0, 204.0)]

def test_single_supertrend():
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 2.0) == 221.2
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 2.0) == 218.44930985245122
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 2.0) == 216.69194312796208
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 2.0) == 214.22369668246446
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 2.0) == 224.0
    assert PyTechnicalIndicators.candle_indicators.single.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 2.0) == 221.2

def test_bulk_supertrend():
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingAverage(), 2.0, 3) == [224.5, 218.0, 209.5] 
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SmoothedMovingAverage(), 2.0, 3) == [219.13157894736844, 217.89473684210526, 210.23684210526315]
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.ExponentialMovingAverage(), 2.0, 3) == [215.64285714285714, 218.28571428571428, 210.35714285714286]
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.PersonalisedMovingAverage(5, 4), 2.0, 3) == [210.32089552238807, 219.6417910447761, 209.94776119402985]
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMedian(), 2.0, 3) == [228.5, 224.0, 207.5]
    assert PyTechnicalIndicators.candle_indicators.bulk.supertrend(high, low, close, PyTechnicalIndicators.ConstantModelType.SimpleMovingMode(), 2.0, 3) == [224.5, 218.0, 209.5]

