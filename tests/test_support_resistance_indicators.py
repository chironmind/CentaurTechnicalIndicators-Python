from src.PyTechnicalIndicators.Bulk import support_resistance_indicators as bulk_support_resistance_indicators
from src.PyTechnicalIndicators.Single import support_resistance_indicators as single_support_resistance_indicators


def test_single_fibonacci_retracement():
    fr = single_support_resistance_indicators.fibonacci_retracement(100)
    assert fr == (100, 123.6, 138.2, 150, 161.8, 176.4, 200)


def test_single_pivot_points():
    pivot = single_support_resistance_indicators.pivot_points(125, 118, 120)
    assert pivot == (121, 117, 124, 114, 128)


def test_bulk_fibonacci_retracement():
    fr = bulk_support_resistance_indicators.fibonacci_retracement([100, 103, 106, 102, 96])
    assert fr == [
        (100, 123.6, 138.2, 150, 161.8, 176.4, 200),
        (103, 127.30799999999999, 142.34599999999998, 154.5, 166.65400000000002, 181.692, 206),
        (106, 131.016, 146.492, 159, 171.508, 186.984, 212),
        (102, 126.072, 140.964, 153, 165.036, 179.928, 204),
        (96, 118.656, 132.672, 144, 155.328, 169.344, 192)
    ]


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
