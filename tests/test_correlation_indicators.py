from PyTechnicalIndicators import correlation_indicators, ConstantModelType, DeviationModel

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

prices_a = [100.0, 102.0, 103.0, 101.0, 99.0]
prices_b = [192.0, 200.0, 201.0, 187.0, 188.0]

def test_single_correlation():
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingAverage(), DeviationModel.StandardDeviation()) == 0.8169678632647616
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SmoothedMovingAverage(), DeviationModel.MeanAbsoluteDeviation()) == 1.0556339082935264
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.ExponentialMovingAverage(), DeviationModel.MedianAbsoluteDeviation()) == 1.2124140206954974
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.PersonalisedMovingAverage(5, 4), DeviationModel.ModeAbsoluteDeviation()) == 1.5200776889081322
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingMedian(), DeviationModel.UlcerIndex()) == 0.8238549759365069
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingMode(), DeviationModel.StandardDeviation()) == 0.8169678632647616

def test_bulk_correlation():
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingAverage(), DeviationModel.StandardDeviation(), 3) == [0.9732227014483793, 0.8962581595302719, 0.8322397195638238]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SmoothedMovingAverage(), DeviationModel.MeanAbsoluteDeviation(), 3) == [1.2679485090435099, 1.239381348107105, 1.18721144967682]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.ExponentialMovingAverage(), DeviationModel.MedianAbsoluteDeviation(), 3) == [1.9931972789115662, 1.7886297376093352, 1.7274052478134112]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.PersonalisedMovingAverage(5, 4), DeviationModel.ModeAbsoluteDeviation(), 3) == [1.7473064877543827, 1.8586359248533328, 1.6597423331105674]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingMedian(), DeviationModel.UlcerIndex(), 3) == [float('inf'), 1.03515, 0.6300067463043878]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, ConstantModelType.SimpleMovingMode(), DeviationModel.StandardDeviation(), 3) == [0.9732227014483793, 0.8962581595302719, 0.8322397195638238]

