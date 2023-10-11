import pytest

from src.PyTechnicalIndicators.Chart_Patterns import valleys


def test_get_valleys():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    vly = valleys.get_valleys(prices, 10)
    assert vly == [(81, 4), (86, 12), (86, 14), (82, 15), (77, 17)]
