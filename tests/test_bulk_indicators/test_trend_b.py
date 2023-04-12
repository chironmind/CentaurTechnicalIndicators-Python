from src.PyTechnicalIndicators.Bulk.trend import personalised_aroon_oscillator, personalised_aroon_down, personalised_aroon_up


def test_aroon_up():
    period_from_high = [5, 6, 0, 1, 2]
    aroon_up = personalised_aroon_up(10, period_from_high)
    assert aroon_up == [50, 40, 100, 90, 80]


def test_aroon_down():
    period_from_low = [8, 9, 10, 10, 0]
    aroon_down = personalised_aroon_down(10, period_from_low)
    assert aroon_down == [20, 10, 0, 0, 100]


def test_aroon_oscillator():
    period_from_high = [5, 6, 0, 1, 2]
    period_from_low = [8, 9, 10, 10, 0]
    aroon_oscillator = personalised_aroon_oscillator(10, period_from_high, period_from_low)
    assert aroon_oscillator == [30, 30, 100, 90, -20]
