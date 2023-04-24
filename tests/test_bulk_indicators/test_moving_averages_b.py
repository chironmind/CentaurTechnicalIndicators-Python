import pytest

from src.PyTechnicalIndicators.Bulk import moving_averages


def test_mcginley_dynamic():
    prices = [100, 110, 112, 115, 113, 111]
    md = moving_averages.mcginley_dynamic(prices, 10)
    assert md == [100, 100.68301345536507, 101.42207997889615, 102.24351258209249, 102.96445361554517, 103.55939307450244]


def test_moving_average_envelope():
    prices = [202, 205, 208, 204, 201, 198, 202]
    mae = moving_averages.moving_average_envelopes(prices, 5)
    assert mae == [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]


def test_moving_average_envelope_with_options():
    prices = [202, 205, 208, 204, 201, 198, 202]
    mae = moving_averages.moving_average_envelopes(prices, 5, 'ma', 3)
    assert mae == [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]


def test_moving_average_period_exception():
    prices = [202, 205, 208, 204, 201, 198, 202]
    with pytest.raises(Exception) as e:
        moving_averages.moving_average_envelopes(prices, 50)
    assert str(e.value) == f'Period (50) cannot be longer than length of prices ({len(prices)})'