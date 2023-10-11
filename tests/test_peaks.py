import pytest

from src.PyTechnicalIndicators.Chart_Patterns import peaks


def test_get_peaks():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    pks = peaks.get_peaks(prices, 10)
    assert pks == [(113, 6), (113, 8), (97, 16), (107, 19)]
