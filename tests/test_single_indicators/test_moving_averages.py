import pytest

from src.PyTechnicalIndicators.Single.moving_averages import mcginley_dynamic, moving_average_envelopes, ma, ema, sma


def test_mcginley_dynamic_no_previous():
    md = mcginley_dynamic(100, 10)
    assert md == 100


def test_mcginley_dynamic_previous():
    md = mcginley_dynamic(110, 10, 100)
    assert md == 100.68301345536507


def test_moving_average_envelope():
    prices = [202, 205, 208, 204, 201]
    mae = moving_average_envelopes(prices)
    assert mae == (210.12, 204, 197.88)


def test_moving_average_envelope_with_options():
    prices = [202, 205, 208, 204, 201]
    mae = moving_average_envelopes(prices, 'ma', 3)
    assert mae == (210.12, 204, 197.88)


def test_moving_average_envelope_model_exception():
    prices = [202, 205, 208, 204, 201]
    with pytest.raises(Exception) as e:
        moving_average_envelopes(prices, 'zzz', 3)
    assert str(e.value) == f'zzz is not an accepted model, accepted models are: {ma}, {sma}, {ema}'
