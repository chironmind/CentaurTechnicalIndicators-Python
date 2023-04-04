import pytest

from src.PyTechnicalIndicators.Single.volatility import average_true_range


def test_average_true_range():
    high = [120, 125, 123]
    low = [90, 110, 116]
    close = [100, 115, 120]
    atr = average_true_range(high, low, close, 15)
    assert atr == 12.666666666666666


def test_average_true_range_no_previous():
    high = [120, 125, 123]
    low = [90, 110, 116]
    close = [100, 115, 120]
    atr = average_true_range(high, low, close, 0)
    assert atr == 11


def test_average_true_range_length_exception():
    high = [120, 125]
    low = [90, 110, 116]
    close = [100, 115, 120]
    with pytest.raises(Exception) as e:
        average_true_range(high, low, close, 0)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    high = [120, 125, 123]
    low = [90, 110]
    with pytest.raises(Exception) as e:
        average_true_range(high, low, close, 0)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    low = [90, 110, 116]
    close = [100, 115]
    with pytest.raises(Exception) as e:
        average_true_range(high, low, close, 0)
    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'
