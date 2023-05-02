import pytest

from src.PyTechnicalIndicators.Single.trend import personalised_aroon_down, personalised_aroon_up, personalised_aroon_oscillator, parabolic_sar


def test_aroon_up():
    aroon_up = personalised_aroon_up(10, 5)
    assert aroon_up == 50


def test_aroon_excpetion():
    with pytest.raises(Exception) as e:
        personalised_aroon_up(10, 50)
    assert str(e.value) == 'period_since_high (50) needs to be less than input period (10)'


def test_aroon_down():
    aroon_down = personalised_aroon_down(10, 8)
    assert aroon_down == 20


def test_aroon_down_excpetion():
    with pytest.raises(Exception) as e:
        personalised_aroon_down(10, 80)
    assert str(e.value) == 'period_since_low (80) needs to be less than input period (10)'


def test_aroon_oscillator():
    aroon_oscillator = personalised_aroon_oscillator(10, 5, 8)
    assert aroon_oscillator == 30


def test_parabolic_sar_rising():
    highs = [109, 111, 112, 110, 111]
    lows = [90, 94, 98, 100, 96]
    close = [100, 103, 109, 108, 110]
    rpsar = parabolic_sar(highs, lows, close)
    assert rpsar == 90.44


def test_parabolic_sar_falling():
    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [110, 108, 109, 103, 100]
    rpsar = parabolic_sar(highs, lows, close)
    assert rpsar == 111.56


def test_parabolic_sar_neutral():
    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104, 100]
    rpsar = parabolic_sar(highs, lows, close)
    assert rpsar == 100.02


def test_parabolic_sar_length_exception():
    highs = [111, 110, 112, 111]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94]
    close = [100, 103, 107, 104, 100]
    with pytest.raises(Exception) as e:
        parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'

    highs = [111, 110, 112, 111, 109]
    lows = [96, 100, 98, 94, 90]
    close = [100, 103, 107, 104]
    with pytest.raises(Exception) as e:
        parabolic_sar(highs, lows, close)
    assert str(e.value) == f'Length of lists need to match, high ({len(highs)}), low ({len(lows)}), close ({len(close)})'