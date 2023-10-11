import pytest

from src.PyTechnicalIndicators.Bulk import oscillators as oscillators_bulk
from src.PyTechnicalIndicators.Single import oscillators as single_oscillators
from src.PyTechnicalIndicators.Single.moving_averages import ma, sma, ema


def test_single_money_flow_index():
    typical_prices = [101, 100, 102, 103, 105, 106, 107, 110, 108, 109, 107, 106, 105, 108]
    volume = [1250, 1000, 800, 900, 1100, 1500, 1600, 1800, 2000, 1750, 1800, 1500, 1000, 1100]
    mfi = single_oscillators.money_flow_index(typical_prices=typical_prices, volume=volume)
    print(mfi)
    assert mfi == 66.51053864168618


def test_single_money_flow_index_all_positive():
    # Unlikely for daily, but this could happen for tick
    typical_prices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
    volume = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
    mfi = single_oscillators.money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 99.00990099009901


def test_single_money_flow_index_all_negative():
    # Unlikely for daily, but this could happen for tick
    typical_prices = [114, 113, 112, 110, 111, 109, 108, 107, 106, 105, 104, 103, 102, 101]
    volume = [2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700]
    mfi = single_oscillators.money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 0


def test_single_money_flow_index_exception():
    typical_prices = [100, 101, 102]
    volume = [1000, 1100, 1200]
    with pytest.raises(Exception) as e:
        single_oscillators.money_flow_index(typical_prices=typical_prices, volume=volume)
    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be 14 periods in length"


def test_single_personalised_money_flow_index():
    typical_prices = [100, 101, 100, 90, 103]
    volume = [1000, 1100, 1200, 1050, 1100]
    mfi = single_oscillators.personalised_money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 78.4688995215311


def test_single_personalised_money_flow_index_exception():
    typical_prices = [100, 101, 100, 90, 103]
    volume = [1000, 1100, 1200, 1050]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_money_flow_index(typical_prices=typical_prices, volume=volume)
    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume({len(volume)})  need to be of same length"


def test_single_chaikin_oscillator():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    co = single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert co == 697.480158730159


def test_single_chaikin_oscillator_mismatch_list_length():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert str(e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'


def test_single_chaikin_oscillator_short_period_exception():
    high = [150, 157, 163]
    low = [132, 143, 153]
    close = [148, 155, 157]
    volume = [1500, 1600, 1800]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'ma')
    assert str(f'short_period (3) needs to be smaller than the length of lists ({len(high)})')


def test_single_chaikin_oscillator_wrong_model():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        single_oscillators.personalised_chaikin_oscillator(high, low, close, volume, 3, 'zzz')
    assert str(e.value) == str(f'zzz is not an accepted MA model, please use either {ma}, {sma}, or {ema}')


def test_single_stochastic_oscillator():
    close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89]
    so = single_oscillators.stochastic_oscillator(close)
    assert so == 65.625


def test_single_personalised_stochastic_oscillator():
    close = [84, 83, 89, 95, 89]
    so = single_oscillators.personalised_stochastic_oscillator(close)
    assert so == 50


def test_single_fast_stochastic():
    stochastic_oscillators = [65.625, 100, 100]
    fs = single_oscillators.fast_stochastic(stochastic_oscillators)
    assert fs == 88.54166666666667


def test_single_slow_stochastic():
    fast_stochastics = [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]
    ss = single_oscillators.slow_stochastic(fast_stochastics)
    assert ss == 82.23425863236291


def test_single_slow_stochastic_ds():
    slow_stochastics = [89.69128533244347, 87.43902556418001]
    ssds = single_oscillators.slow_stochastic_ds(slow_stochastics)
    assert ssds == 88.56515544831174


def test_single_williams_percent_r():
    wr = single_oscillators.williams_percent_r(143, 132, 138)
    assert wr == -45.45454545454545


def test_bulk_standard_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = oscillators_bulk.money_flow_index(typical_prices, volume)

    assert len(mfi) == 3
    assert mfi == [39.58136997172759, 33.33167997619165,33.54593097992682]


def test_bulk_personalised_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = oscillators_bulk.personalised_money_flow_index(typical_prices, volume, 3)

    assert len(mfi) == 14
    assert mfi == [99.00990099009901, 51.75879396984925, 57.608695652173914, 52.6381129733085, 57.681641708264, 51.92211682476285, 0, 0, 0, 0, 57.465091299677766, 51.958562641631595, 0, 52.7027027027027]


def test_bulk_money_flow_index_incorrect_size():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_money_flow_index(typical_prices, volume, 20)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be at least 20 periods in length"


def test_bulk_money_flow_index_mismatch_list_error():
    typical_prices = [100, 105, 103, 104, 106, 109]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_money_flow_index(typical_prices, volume, 3)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be of same length"


def test_bulk_chaikin_oscillator():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
    co = oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert co == [697.480158730159, 542.0138888888889, 95.15151515151518]


def test_bulk_chaikin_oscillator_mismatch_list_length():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(
        e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'

    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == f'length of lists need to match. high ({len(high)}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})'


def test_bulk_chaikin_oscillator_short_period_exception():
    high = [150, 157, 163]
    low = [132, 143, 153]
    close = [148, 155, 157]
    volume = [1500, 1600, 1800]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 3, 10, 'ma')
    assert str(e.value) == str(f'short_period (3) needs to be smaller than the length of lists ({len(high)})')


def test_bulk_chaikin_oscillator_long_period_exception():
    high = [150, 157, 163]
    low = [132, 143, 153]
    close = [148, 155, 157]
    volume = [1500, 1600, 1800]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 1, 10, 'ma')
    assert str(e.value) == str(f'long_period (10) needs to be less or equal to length of lists ({len(high)})')


def test_bulk_chaikin_oscillator_short_greater_long_exception():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
    with pytest.raises(Exception) as e:
        oscillators_bulk.personalised_chaikin_oscillator(high, low, close, volume, 11, 10, 'ma')
    assert str(e.value) == str(f'long_period (10) needs to be longer than short_period (11)')


def test_bulk_stochastic_oscillator():
    close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89, 97, 104]
    so = oscillators_bulk.stochastic_oscillator(close)
    assert so == [65.625, 100, 100]


def test_bulk_personalised_stochastic_oscillator():
    close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89]
    so = oscillators_bulk.personalised_stochastic_oscillator(close, 5)
    assert so == [0.0, 0.0, 30.0, 57.14285714285714, 100.0, 100.0, 90.0, 100.0, 100.0, 50.0]


def test_bulk_fast_stochastic():
    stochastic_oscillators = [0.0, 0.0, 30.0, 57.14285714285714, 100.0, 100.0, 90.0, 100.0, 100.0, 50.0]
    fs = oscillators_bulk.fast_stochastic(stochastic_oscillators, 5, 'ema')
    assert fs == [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]


def test_bulk_slow_stochastic():
    fast_stochastics = [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]
    ss = oscillators_bulk.slow_stochastic(fast_stochastics, 5, 'ema')
    assert ss == [89.69128533244347, 87.43902556418001]


def test_bulk_slow_stochastic_ds():
    slow_stochastics = [89, 87, 88, 83, 82]
    ssds = oscillators_bulk.slow_stochastic_ds(slow_stochastics, 3, 'ma')
    assert ssds == [88, 86, 84.33333333333333]


def test_bulk_williams_percent_r():
    high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
    low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
    close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
    wr = oscillators_bulk.williams_percent_r(high, low, close, 3)
    assert wr == [-19.35483870967742, -65.0, -83.33333333333333, -13.333333333333334, -27.77777777777778, -81.81818181818181, -50.0, -76.19047619047619, -50.0, -53.84615384615385]
