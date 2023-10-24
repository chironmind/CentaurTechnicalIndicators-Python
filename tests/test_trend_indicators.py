import pytest

from src.PyTechnicalIndicators.Single import trend_indicators as trend_single
from src.PyTechnicalIndicators.Bulk import trend_indicators as trend_bulk


def test_single_aroon_up():
    aroon_up = trend_single.aroon_up(5, 10)
    assert aroon_up == 50


def test_single_aroon_excpetion():
    with pytest.raises(Exception) as e:
        trend_single.aroon_up(50, 10)
    assert str(e.value) == 'period_since_high (50) needs to be less than input period (10)'


def test_single_aroon_down():
    aroon_down = trend_single.aroon_down(8, 10)
    assert aroon_down == 20


def test_single_aroon_down_excpetion():
    with pytest.raises(Exception) as e:
        trend_single.aroon_down(80, 10)
    assert str(e.value) == 'period_since_low (80) needs to be less than input period (10)'


def test_single_aroon_oscillator():
    aroon_oscillator = trend_single.aroon_oscillator(5, 8, 10)
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
    period_from_high = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
    aroon_up = trend_bulk.aroon_up(period_from_high, 10)
    assert aroon_up == [0.0, 100.0, 90.0, 100.0, 100.0]


def test_bulk_aroon_down():
    period_from_low = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
    aroon_down = trend_bulk.aroon_down(period_from_low, 10)
    assert aroon_down == [100.0, 90.0, 80.0, 70.0, 100.0]


def test_bulk_aroon_oscillator():
    period_from_high = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
    period_from_low = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
    aroon_oscillator = trend_bulk.aroon_oscillator(period_from_high, period_from_low, 10)
    assert aroon_oscillator == [-100.0, 10.0, 10.0, 30.0, 0.0]


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
