import pytest

from src.PyTechnicalIndicators.Single import basic_indicators as single_basic_indicators
from src.PyTechnicalIndicators.Bulk import basic_indicators as bulk_basic_indicators

prices = [100, 102, 105, 103, 108]


def test_bulk_log():
    # Python log function uses natural logarithm
    log = bulk_basic_indicators.log(prices)
    assert log == [4.605170185988092, 4.624972813284271, 4.653960350157523, 4.634728988229636, 4.68213122712422]


def test_bulk_log_diff():
    log_diff = bulk_basic_indicators.log_diff(prices)
    assert log_diff == [0, 0.019802627296178876, 0.028987536873252395, -0.019231361927887214, 0.04740223889458406]


def test_bulk_stddev():
    stddev = bulk_basic_indicators.standard_deviation(prices, 3)
    assert stddev == [2.516611478423583, 1.5275252316519468, 2.516611478423583]


def test_bulk_mean():
    mean = bulk_basic_indicators.mean(prices, 3)
    assert mean == [102.333333333333333, 103.3333333333333333, 105.333333333333333]


def test_bulk_median():
    mean = bulk_basic_indicators.median(prices, 3)
    assert mean == [102, 103, 105]


def test_bulk_variance():
    variance = bulk_basic_indicators.variance(prices, 3)
    assert variance == [6.33333333333333333, 2.3333333333333333, 6.333333333333333]


def test_bulk_mean_deviation():
    prices = [100, 102, 105, 103, 108]
    mean_deviation = bulk_basic_indicators.mean_absolute_deviation(prices, 3)
    assert mean_deviation == [1.7777777777777761, 1.1111111111111096, 1.7777777777777761]


def test_bulk_median_deviation():
    median_deviation = bulk_basic_indicators.median_absolute_deviation(prices, 3)
    assert median_deviation == [1.6666666666666667, 1.0, 1.6666666666666667]


def test_bulk_mode_deviation():
    mode_deviation = bulk_basic_indicators.mode_absolute_deviation(prices, 3)
    assert mode_deviation == [2.3333333333333335, 1.3333333333333333, 1.6666666666666667]

