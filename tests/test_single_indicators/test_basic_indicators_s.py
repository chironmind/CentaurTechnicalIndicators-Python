from src.PyTechnicalIndicators.Single import basic_indicators as bi


def test_mean_absolute_deviation():
    prices = [103, 106, 111, 113, 111, 102, 98]
    mad = bi.mean_absolute_deviation(prices)
    assert mad == 4.612244897959185


def test_median_absolute_deviation():
    prices = [103, 106, 111, 113, 111, 102, 98]
    mad = bi.median_absolute_deviation(prices)
    assert mad == 4.571428571428571


def test_mode_absolute_deviation():
    prices = [103, 106, 111, 113, 111, 102, 98]
    mad = bi.mode_absolute_deviation(prices)
    assert mad == 5.285714285714286
