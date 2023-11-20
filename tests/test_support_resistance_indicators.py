from src.PyTechnicalIndicators.Bulk import support_resistance_indicators as bulk_support_resistance_indicators
from src.PyTechnicalIndicators.Single import support_resistance_indicators as single_support_resistance_indicators


def test_single_pivot_points():
    pivot = single_support_resistance_indicators.pivot_points(125, 118, 120)
    assert pivot == (121, 117, 124, 114, 128)


def test_bulk_pivot_points():
    high = [115, 119, 125, 118, 116]
    low = [99, 96, 110, 105, 108]
    close = [108, 113, 120, 115, 110]
    pivot = bulk_support_resistance_indicators.pivot_points(high, low, close)
    assert pivot == [
        (107.33333333333333, 99.66666666666666, 115.66666666666666, 91.33333333333333, 123.33333333333333),
        (109.33333333333333, 99.66666666666666, 122.66666666666666, 86.33333333333333, 132.33333333333331),
        (118.33333333333333, 111.66666666666666, 126.66666666666666, 103.333333333333333, 133.33333333333331),
        (112.66666666666667, 107.33333333333334, 120.33333333333334, 99.66666666666667, 125.66666666666667),
        (111.33333333333333, 106.66666666666666, 114.66666666666666, 103.33333333333333, 119.33333333333333)
    ]
