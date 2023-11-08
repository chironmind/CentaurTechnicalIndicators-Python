import pytest

from src.PyTechnicalIndicators.Single import moving_averages as single_moving_averages
from src.PyTechnicalIndicators.Bulk import moving_averages as bulk_moving_averages


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


def test_single_personalised_moving_average_denominator_error():
    prices = [110, 107, 108, 105, 103, 106, 107]
    with pytest.raises(Exception) as e:
        single_moving_averages.personalised_moving_average(prices, 3, -7)
    assert str(e.value) == f'The length of prices 7 and the value of the alpha denominator -7 add up to 0, and division by 0 isn\'t possible'


def test_single_macd():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101, 99, 103, 106, 104, 102]
    macd = single_moving_averages.macd_line(prices)
    assert macd == -2.164962379494412


def test_single_signal_line():
    macds = [-2, -1.8, -1, -0.3, 0.1, 0.6, 1.2, 2.4, 1.9]
    signal = single_moving_averages.signal_line(macds)
    assert signal == 0.8922983167758831


def test_single_personalised_macd():
    prices = [110, 107, 108, 105, 103, 106, 107]
    macd = single_moving_averages.macd_line(prices, 3, 7, 'ma')
    assert macd == -1.2380952380952408


def test_single_personalised_signal():
    macds = [0.1, 0.6, 1.2, 2.4, 1.9]
    signal = single_moving_averages.signal_line(macds, 'ma')
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


def test_bulk_exponential_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    emas = bulk_moving_averages.exponential_moving_average(prices, 5)
    assert emas == [105.35071090047394, 105.36492890995261, 105.9099526066351]


def test_bulk_smoothed_moving_average():
    prices = [110, 107, 108, 105, 103, 106, 107]
    smas = bulk_moving_averages.smoothed_moving_average(prices, 5)
    assert smas == [105.89005235602093, 105.52213231794384, 105.81770585435507]


def test_bulk_moving_average_convergence_divergence():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101,
              99, 103, 106, 104, 102, 109, 116, 103, 105, 102, 107, 103, 111, 106]
    macd = bulk_moving_averages.moving_average_convergence_divergence(prices)
    assert macd == [(-0.1012853102636484, -0.743614115716126, -0.6423288054524776), (-0.05576254400048697, -0.5406481426783447, -0.48488559867785774)]


def test_bulk_macd():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101,
              99, 103, 106, 104, 102, 109, 116]
    macd = bulk_moving_averages.macd_line(prices)
    assert macd == [-2.164962379494412, -1.597159438916961, -0.4970353844502142]


def test_bulk_signal_line():
    macds = [-2, -1.8, -1, -0.3, 0.1, 0.6, 1.2, 2.4, 1.9, 1.8, 1.2]
    signal = bulk_moving_averages.signal_line(macds)
    assert signal == [0.8922983167758831, 1.1916575053179188, 1.2863408873310813]


def test_bulk_personalised_moving_average_convergence_divergence():
    prices = [110, 107, 108, 105, 103, 106, 107, 101, 99, 103, 106, 104, 102, 109, 116]
    macd = bulk_moving_averages.moving_average_convergence_divergence(prices, 3, 5, 3, 'ma')
    assert macd == [(-0.46666666666666856, -0.9555555555555534, -0.4888888888888848), (0.2666666666666657, -0.44444444444444287, -0.7111111111111086), (-0.8666666666666742, -0.355555555555559, 0.5111111111111153), (-2.200000000000003, -0.9333333333333371, 1.2666666666666657), (-0.5333333333333314, -1.2000000000000028, -0.6666666666666714), (1.7333333333333343, -0.3333333333333333, -2.0666666666666678), (1.2000000000000028, 0.8000000000000019, -0.4000000000000009), (0.20000000000000284, 1.0444444444444467, 0.8444444444444439), (1.5999999999999943, 1.0, -0.5999999999999943)]


def test_bulk_personalised_macd():
    prices = [110, 107, 108, 105, 103, 106, 107]
    macd = bulk_moving_averages.macd_line(prices, 3, 5, 'ma')
    assert macd == [-1.2666666666666657, -1.1333333333333258, -0.46666666666666856]


def test_bulk_personalised_signal():
    macds = [0.1, 0.6, 1.2, 2.4, 1.9]
    signal = bulk_moving_averages.signal_line(macds, 3, 'ma')
    assert signal == [0.6333333333333333, 1.3999999999999997, 1.8333333333333333]


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
