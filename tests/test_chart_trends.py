import pytest

from src.PyTechnicalIndicators.Chart_Patterns import chart_trends


def test_get_trend():
    p = [(100, 2), (110, 5), (115, 7), (140, 18)]
    trend = chart_trends.get_trend_line(p)
    assert trend == (2.4315068493150687, 96.79794520547945)


def test_get_peak_trend():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    peak_trend = chart_trends.get_peak_trend(prices, 10)
    assert peak_trend == (-0.860813704496788, 118.04496788008565)


def test_get_valleys_trend():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    peak_trend = chart_trends.get_valley_trend(prices, 10)
    assert peak_trend == (-0.09683794466403162, 83.60079051383399)


def test_get_overall_trend():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    overall_trend = chart_trends.get_overall_trend(prices)
    assert overall_trend == (-0.48270676691729325, 98.88571428571429)


def test_break_down_trends():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    trend_breakdown = chart_trends.break_down_trends(prices)
    assert trend_breakdown == [(0, 1, 3.0, 100.0), (2, 4, -7.0, 109.66666666666667), (5, 7, 0.0, 103.66666666666667), (8, 15, -2.9404761904761907, 125.69047619047619), (16, 18, -3.5, 147.5), (19, 19, 0, 0)]
