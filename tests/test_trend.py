import pytest

from src.PyTechnicalIndicators.Single import trend_indicators as trend_single
from src.PyTechnicalIndicators.Bulk import trend_indicators as trend_bulk


def test_single_aroon_up():
    aroon_up = trend_single.personalised_aroon_up(10, 5)
    assert aroon_up == 50


def test_single_aroon_excpetion():
    with pytest.raises(Exception) as e:
        trend_single.personalised_aroon_up(10, 50)
    assert str(e.value) == 'period_since_high (50) needs to be less than input period (10)'


def test_single_aroon_down():
    aroon_down = trend_single.personalised_aroon_down(10, 8)
    assert aroon_down == 20


def test_single_aroon_down_excpetion():
    with pytest.raises(Exception) as e:
        trend_single.personalised_aroon_down(10, 80)
    assert str(e.value) == 'period_since_low (80) needs to be less than input period (10)'


def test_single_aroon_oscillator():
    aroon_oscillator = trend_single.personalised_aroon_oscillator(10, 5, 8)
    assert aroon_oscillator == 30


def test_single_parabolic_sar_rising():
    highs = [109, 111, 112, 110, 111]
    lows = [90, 94, 98, 100, 96]
    close = [100, 103, 109, 108, 110]
    rpsar = trend_single.parabolic_sar(highs, lows, close)
    assert rpsar == 90.44


def test_single_parabolic_sar_falling():
    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [110, 108, 109, 103, 100]
    rpsar = trend_single.parabolic_sar(highs, lows, close)
    assert rpsar == 111.56


def test_single_parabolic_sar_neutral():
    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104, 100]
    rpsar = trend_single.parabolic_sar(highs, lows, close)
    assert rpsar == 100.02


def test_single_parabolic_sar_length_exception():
    highs = [111, 110, 112, 111]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        trend_single.parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        trend_single.parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104]
    with pytest.raises(Exception) as e:
        trend_single.parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'


def test_bulk_aroon_up():
    period_from_high = [5, 6, 0, 1, 2]
    aroon_up = trend_bulk.personalised_aroon_up(10, period_from_high)
    assert aroon_up == [50, 40, 100, 90, 80]


def test_bulk_aroon_down():
    period_from_low = [8, 9, 10, 10, 0]
    aroon_down = trend_bulk.personalised_aroon_down(10, period_from_low)
    assert aroon_down == [20, 10, 0, 0, 100]


def test_bulk_aroon_oscillator():
    period_from_high = [5, 6, 0, 1, 2]
    period_from_low = [8, 9, 10, 10, 0]
    aroon_oscillator = trend_bulk.personalised_aroon_oscillator(10, period_from_high, period_from_low)
    assert aroon_oscillator == [30, 30, 100, 90, -20]


def test_bulk_parabolic_sar_rising():
    highs = [109, 111, 112, 110, 111, 113, 109, 107]
    lows = [90, 94, 98, 100, 96, 89, 95, 93]
    close = [100, 103, 109, 108, 110, 111, 108, 106]
    psar = trend_bulk.parabolic_sar(highs, lows, close, 5)
    assert psar == [90.44, 90.8712, 91.756352, 92.60609792000001]


def test_bulk_parabolic_sar_falling():
    highs = [111, 110, 112, 111, 109, 110, 107, 105]
    lows = [96, 100, 98, 94, 90, 89, 92, 90]
    close = [110, 108, 109, 103, 100, 102, 103, 99]
    psar = trend_bulk.parabolic_sar(highs, lows, close, 5)
    assert psar == [111.56, 111.1288, 110.243648, 109.39390207999999]


def test_bulk_parabolic_sar_length_exception():
    highs = [111, 110, 112, 111]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        trend_bulk.parabolic_sar(highs, lows, close, 3)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        trend_bulk.parabolic_sar(highs, lows, close, 3)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104]
    with pytest.raises(Exception) as e:
        trend_bulk.parabolic_sar(highs, lows, close, 3)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'


def test_bulk_parabolic_sar_period_exception():
    highs = [109, 111, 112, 110, 111, 113, 109, 107]
    lows = [90, 94, 98, 100, 96, 89, 95, 93]
    close = [100, 103, 109, 108, 110, 111, 108, 106]
    with pytest.raises(Exception) as e:
        trend_bulk.parabolic_sar(highs, lows, close, 50)
    assert str(e.value) == f'Length of lists ({len(highs)}) needs to be greater or equal to period (50)'
