import pytest

from src.PyTechnicalIndicators.Single import moving_averages as single_moving_averages
from src.PyTechnicalIndicators.Bulk import moving_averages as bulk_moving_averages


# TODO check errors
def test_single_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    ma = single_moving_averages.moving_average(prices)
    assert ma == 106.57142857142857


def test_single_exponential_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    ema = single_moving_averages.exponential_moving_average(prices)
    assert ema == 106.13636683806438


def test_single_smoothed_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    sma = single_moving_averages.smoothed_moving_average(prices)
    assert sma == 106.2801969069567


def test_single_personalised_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    pma = single_moving_averages.personalised_moving_average(prices, 3, 5)
    assert pma == 106.13636683806438


def test_single_macd():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101, 99, 103, 106, 104, 102]
    macd = single_moving_averages.moving_average_convergence_divergence(prices)
    assert macd == -2.164962379494412


def test_single_signal_line():
    macds = [-2, -1.8, -1, -0.3, 0.1, 0.6, 1.2, 2.4, 1.9]
    signal = single_moving_averages.signal_line(macds)
    assert signal == 0.8922983167758831


def test_single_personalised_macd():
    prices = [110, 107, 108, 105, 103, 106, 107]
    macd = single_moving_averages.personalised_macd(prices, 3, 7, 'ma')
    assert macd == -1.2380952380952408


def test_single_personalised_signal():
    macds = [0.1, 0.6, 1.2, 2.4, 1.9]
    signal = single_moving_averages.personalised_signal_line(macds, 'ma')
    assert signal == 1.2399999999999998


def test_single_mcginley_dynamic_no_previous():
    md = single_moving_averages.mcginley_dynamic(100, 10)
    assert md == 100


def test_single_mcginley_dynamic_previous():
    md = single_moving_averages.mcginley_dynamic(110, 10, 100)
    assert md == 100.68301345536507


def test_single_moving_average_envelope():
    prices = [202, 205, 208, 204, 201]
    mae = single_moving_averages.moving_average_envelopes(prices)
    assert mae == (210.12, 204, 197.88)


def test_single_moving_average_envelope_with_options():
    prices = [202, 205, 208, 204, 201]
    mae = single_moving_averages.moving_average_envelopes(prices, 'ma', 3)
    assert mae == (210.12, 204, 197.88)


def test_single_moving_average_envelope_model_exception():
    prices = [202, 205, 208, 204, 201]
    with pytest.raises(Exception) as e:
        single_moving_averages.moving_average_envelopes(prices, 'zzz', 3)
    assert str(e.value) == f'zzz is not an accepted model, accepted models are: {single_moving_averages.ma}, {single_moving_averages.sma}, {single_moving_averages.ema}'


def test_bulk_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    mas = bulk_moving_averages.moving_average(prices, 5)
    assert mas == [106.6, 105.8, 105.8]


def test_bulk_mcginley_dynamic():
    prices = [100, 110, 112, 115, 113, 111]
    md = bulk_moving_averages.mcginley_dynamic(prices, 10)
    assert md == [100, 100.68301345536507, 101.42207997889615, 102.24351258209249, 102.96445361554517, 103.55939307450244]


def test_bulk_moving_average_envelope():
    prices = [202, 205, 208, 204, 201, 198, 202]
    mae = bulk_moving_averages.moving_average_envelopes(prices, 5)
    assert mae == [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]


def test_bulk_moving_average_envelope_with_options():
    prices = [202, 205, 208, 204, 201, 198, 202]
    mae = bulk_moving_averages.moving_average_envelopes(prices, 5, 'ma', 3)
    assert mae == [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]


def test_bulk_moving_average_period_exception():
    prices = [202, 205, 208, 204, 201, 198, 202]
    with pytest.raises(Exception) as e:
        bulk_moving_averages.moving_average_envelopes(prices, 50)
    assert str(e.value) == f'Period (50) cannot be longer than length of prices ({len(prices)})'
