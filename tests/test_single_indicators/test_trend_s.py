import pytest

from src.PyTechnicalIndicators.Single.trend import personalised_aroon_down, personalised_aroon_up, personalised_aroon_oscillator


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
