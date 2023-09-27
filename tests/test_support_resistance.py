from src.PyTechnicalIndicators.Chart_Patterns import support_resistance


def test_fibonacci_retracement():
    fr = support_resistance.fibonacci_retracement(100)
    assert fr == (100, 123.6, 138.2, 150, 161.8, 176.4, 200)


def test_pivot_points():
    pivot = support_resistance.pivot_points(125, 118, 120)
    assert pivot == (121, 117, 124, 114, 128)
