import pytest

from src.PyTechnicalIndicators.Bulk.oscillators import personalised_money_flow_index, personalised_chaikin_oscillator, fast_stochastic, slow_stochastic, williams_percent_r


def test_standard_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = personalised_money_flow_index(typical_prices, volume, 14)

    assert len(mfi) == 3
    assert mfi == [39.58136997172759, 33.33167997619165,33.54593097992682]


def test_personalised_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = personalised_money_flow_index(typical_prices, volume, 3)

    assert len(mfi) == 14
    assert mfi == [99.00990099009901, 51.75879396984925, 57.608695652173914, 52.6381129733085, 57.681641708264, 51.92211682476285, 0, 0, 0, 0, 57.465091299677766, 51.958562641631595, 0, 52.7027027027027]


def test_money_flow_index_incorrect_size():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        personalised_money_flow_index(typical_prices, volume, 20)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be at least 20 periods in length"


def test_money_flow_index_mismatch_list_error():
    typical_prices = [100, 105, 103, 104, 106, 109]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        personalised_money_flow_index(typical_prices, volume, 3)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be of same length"


def test_chaikin_oscillator():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
    co = personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert co == [697.480158730159, 542.0138888888889, 95.15151515151518]


def test_chaikin_oscillator_mismatch_list_length():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'


def test_chaikin_oscillator_short_period_exception():
    high = [150, 157, 163]
    low = [132, 143, 153]
    close = [148, 155, 157]
    volume = [1500, 1600, 1800]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == str(f'short_period (3) needs to be smaller than the length of lists ({len(high)})')


def test_chaikin_oscillator_long_period_exception():
    high = [150, 157, 163]
    low = [132, 143, 153]
    close = [148, 155, 157]
    volume = [1500, 1600, 1800]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 1, 10, 'ma')
    assert str(e.value) == str(f'long_period (10) needs to be less or equal to length of lists ({len(high)})')


def test_chaikin_oscillator_short_greater_long_exception():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
    with pytest.raises(Exception) as e:
        personalised_chaikin_oscillator(high, low, close, volume, 11, 10, 'ma')
    assert str(e.value) == str(f'long_period (10) needs to be longer than short_period (11)')


def test_fast_stochastic():
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    fs = fast_stochastic(close, 3, 3, 'ma')
    assert fs == (
        [100.0, 0.0, 0.0, 100.0, 70.0, 0.0, 23.076923076923077, 0.0, 37.5, 33.33333333333333],
        [33.333333333333336, 33.333333333333336, 56.666666666666664, 56.666666666666664, 31.025641025641026, 7.6923076923076925, 20.192307692307693, 23.61111111111111]
    )


def test_slow_stochastic():
    fast_stochastics = [33.333333333333336, 33.333333333333336, 56.666666666666664, 56.666666666666664, 31.025641025641026, 7.6923076923076925, 20.192307692307693, 23.61111111111111]
    ss = slow_stochastic(fast_stochastics, 3, 3, 'ma')
    assert ss == ([41.111111111111114, 48.888888888888886, 48.11965811965812, 31.794871794871796, 19.636752136752136, 17.165242165242166], [46.039886039886035, 42.93447293447293, 33.18376068376068, 22.865622032288698])


def test_williams_percent_r():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]

    wr = williams_percent_r(high, low, close, 3)
    assert wr == [-19.35483870967742, -65.0, -83.33333333333333, -13.333333333333334, -27.77777777777778, -81.81818181818181, -50.0, -76.19047619047619, -50.0, -53.84615384615385]