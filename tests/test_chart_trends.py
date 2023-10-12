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
    prices = [(100, 0), (103, 1), (95, 2), (90, 3), (81, 4), (99, 5), (113, 6), (99, 7), (113, 8), (95, 9), (87, 10), (92, 11), (86, 12), (94, 13), (86, 14), (82, 15), (97, 16), (77, 17), (90, 18), (107, 19)]
    overall_trend = chart_trends.get_overall_trend(prices)
    assert overall_trend == (-0.48270676691729325, 98.88571428571429)


def test_break_down_trends():
    prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
    trend_breakdown = chart_trends.break_down_trends(prices, 1)
    assert trend_breakdown == [(0, 1, 3.0, 100.0), (2, 4, -7.0, 109.66666666666667), (5, 6, 14.0, 29.0), (7, 8, 14.0, 1.0), (9, 10, -8.0, 167.0), (11, 12, -6.0, 158.0), (13, 15, -6.0, 171.33333333333334), (16, 17, -20.0, 417.0), (18, 19, 17.0, -216.0)]

