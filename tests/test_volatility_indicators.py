from PyTechnicalIndicators import volatility_indicators, ConstantModelType

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

def test_single_ulcer_index():
    assert volatility_indicators.single.ulcer_index(prices) == 1.9417475728155338

def test_bulk_ulcer_index():
    assert volatility_indicators.bulk.ulcer_index(prices, 5) == [1.9417475728155338]

def test_bulk_volatility_system():
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.SimpleMovingAverage()) == [169.0, 175.0, 181.0]
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.SmoothedMovingAverage()) == [174.36842105263156, 175.10526315789474, 180.26315789473685]
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.ExponentialMovingAverage()) == [177.85714285714286, 174.71428571428572, 180.14285714285714]
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.PersonalisedMovingAverage(5, 4)) == [183.17910447761193, 173.3582089552239, 180.55223880597015]
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.SimpleMovingMedian()) == [165.0, 169.0, 183.0]
    assert volatility_indicators.bulk.volatility_system(high, low, close, 3, 2.0, ConstantModelType.SimpleMovingMode()) == [169.0, 175.0, 181.0]
