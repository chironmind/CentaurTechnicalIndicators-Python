import pytest

from pytechnicalindicators import correlation_indicators

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
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "standard") == 0.8169678632647616
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "smoothed", "mean") == 1.0556339082935264
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "exponential", "median") == 1.5130926978279808
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "median", "ulcer") == 0.8238549759365069
    assert correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "mode", "mode") == 0.6974358974358974
    with pytest.raises(ValueError):
        correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "", "mode")
    with pytest.raises(ValueError):
        correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "mode", "")

def test_bulk_correlation():
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "simple", "standard", 3) == [0.9732227014483793, 0.8962581595302719, 0.8322397195638238]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "smoothed", "mean", 3) == [1.2679485090435099, 1.239381348107105, 1.18721144967682]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "exponential", "median", 3) == [5.9795918367346985, 5.564625850340154, 5.374149659863946]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "median", "ulcer", 3) == [float('inf'), 1.03515, 0.6300067463043878]
    assert correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "mode", "mode", 3) == [1.3333333333333333, 0.7777777777777778, 0.7222222222222222]

def test_new_deviation_models_correlation():
    """Test new probability distribution deviation models added in rust_ti 2.2.0"""
    # Test log standard deviation
    result = correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "log")
    assert isinstance(result, float)
    
    # Test Laplace distribution
    result = correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "exponential", "laplace")
    assert isinstance(result, float)
    
    # Test Cauchy distribution
    result = correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "smoothed", "cauchy")
    assert isinstance(result, float)
    
    # Test Student-t distribution with degrees of freedom
    result = correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "student_t:7.5")
    assert isinstance(result, float)
    
    # Test Empirical Quantile Range
    result = correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "empirical_quantile_range:0.1:0.9:0.01")
    assert isinstance(result, float)
    
    # Test bulk operations with new models
    result = correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "exponential", "log", 3)
    assert isinstance(result, list) and len(result) == 3
    
    result = correlation_indicators.bulk.correlate_asset_prices(prices_a, prices_b, "simple", "empirical:0.2:0.8:0.05", 3)
    assert isinstance(result, list) and len(result) == 3
    
    # Test error handling for invalid student_t parameter
    with pytest.raises(ValueError):
        correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "student_t:not_a_number")
    
    with pytest.raises(ValueError):
        correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "student_t:-1")
    
    # Test error handling for invalid empirical quantile range
    with pytest.raises(ValueError):
        correlation_indicators.single.correlate_asset_prices(prices_a, prices_b, "simple", "eqr:1.0:1.5:0.01")

