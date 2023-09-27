import pytest

from src.PyTechnicalIndicators.Single import volatility as volatility_single
from src.PyTechnicalIndicators.Bulk import volatility as volatility_bulk


def test_single_average_true_range():
    atr = volatility_single.average_true_range(123, 116, 120, 11, 3)
    assert atr == 9.666666666666666


def test_single_average_true_range_initial():
    high = [120, 125, 123]
    low = [90, 110, 116]
    close = [100, 115, 120]
    atr = volatility_single.average_true_range_initial(high, low, close)
    assert atr == 11


def test_single_average_true_range_length_exception():
    high = [120, 125]
    low = [90, 110, 116]
    close = [100, 115, 120]
    with pytest.raises(Exception) as e:
        volatility_single.average_true_range_initial(high, low, close)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    high = [120, 125, 123]
    low = [90, 110]
    with pytest.raises(Exception) as e:
        volatility_single.average_true_range_initial(high, low, close)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    low = [90, 110, 116]
    close = [100, 115]
    with pytest.raises(Exception) as e:
        volatility_single.average_true_range_initial(high, low, close)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'


def test_single_ulcer_index():
    close_prices = [103, 105, 106, 104, 101]
    ui = volatility_single.ulcer_index(close_prices)
    assert ui == 2.2719989771306217


def test_single_volatility_index_no_previous():
    vi = volatility_single.volatility_index(190, 120, 130, 14, 0)
    assert vi == 5


def test_single_volatility_index():
    vi = volatility_single.volatility_index(190, 120, 130, 14, 5)
    assert vi == 9.642857142857142


def test_bulk_average_true_range():
    high = [124, 136, 140, 138, 135, 142]
    low = [111, 115, 105, 123, 128, 130]
    close = [115, 122, 127, 128, 130, 132]

    atr = volatility_bulk.average_true_range(high, low, close, 3)

    assert len(atr) == 4
    assert atr == [18.666666666666668, 17.444444444444446, 13.962962962962964, 13.30864197530864]


def test_bulk_ulcer_index():
    close_prices = [103, 105, 106, 104, 101, 99, 93]
    ui = volatility_bulk.ulcer_index(close_prices, 5)
    assert ui == [2.2719989771306217, 3.7261165392700946, 6.630672977662482]


def test_bulk_volatility_index():
    high = [190, 190, 150]
    low = [120, 150, 120]
    close = [150, 120, 190]
    vi = volatility_bulk.volatility_index(high, low, close, 14)
    assert vi == [5.0, 9.642857142857142, 13.95408163265306]
