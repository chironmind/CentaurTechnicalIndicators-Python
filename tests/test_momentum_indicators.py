import pytest

from src.PyTechnicalIndicators.Single import momentum_indicators as single_momentum_indicators
from src.PyTechnicalIndicators.Bulk import momentum_indicators as bulk_momentum_indicators
from src.PyTechnicalIndicators.Single.moving_averages import ema, sma, ma


def test_single_rate_of_change_increase():
    # Where current > previous
    current_close = 110
    previous_close = 100
    roc = single_momentum_indicators.rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == 10


def test_single_rate_of_change_decrease():
    # Where current < previous
    current_close = 120
    previous_close = 150
    roc = single_momentum_indicators.rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == -20


def test_single_rate_of_change_equal():
    # Where current = previous
    current_close = 100
    previous_close = 100
    roc = single_momentum_indicators.rate_of_change(current_close_price=current_close, previous_close_price=previous_close)
    assert roc == 0


def test_single_on_balance_volume_current_price_greater():
    obv = single_momentum_indicators.on_balance_volume(110, 100, 1000, 1500)
    assert obv == 2500


def test_single_on_balance_volume_prices_equal():
    obv = single_momentum_indicators.on_balance_volume(100, 100, 1000, 1500)
    assert obv == 1500


def test_single_on_balance_volume_previous_price_greater():
    obv = single_momentum_indicators.on_balance_volume(100, 110, 1000, 1500)
    assert obv == 500


def test_single_commodity_channel_index():
    prices = [103, 106, 111, 113, 111, 102, 98]
    cci = single_momentum_indicators.commodity_channel_index(prices)
    assert cci == -119.7640117994101


def test_single_commodity_channel_index_ma_model_exception():
    prices = [103, 106, 111, 113, 111, 102, 98]
    with pytest.raises(Exception) as e:
        single_momentum_indicators.commodity_channel_index(prices, ma_model='zzz')
    assert str(e.value) == f'zzz is not an accepted MA model, please use either {ma}, {sma}, or {ema}'


def test_single_commodity_channel_index_ad_model_exception():
    prices = [103, 106, 111, 113, 111, 102, 98]
    with pytest.raises(Exception) as e:
        single_momentum_indicators.commodity_channel_index(prices, absolute_deviation_model='zzz')
    assert str(e.value) == f'zzz is not an accepted absolute deviation model'


def test_bulk_rate_of_change():
    closing_prices = [100, 101, 105, 103, 99, 80, 85, 100, 90, 85]
    roc = bulk_momentum_indicators.rate_of_change(closing_prices=closing_prices, period=3)
    assert roc == [3.0, -1.9801980198019802, -23.809523809523807, -17.475728155339805, 1.0101010101010102, 12.5, 0]


def test_bulk_rate_of_change_exception():
    closing_prices = [100, 101, 105]
    with pytest.raises(Exception) as e:
        bulk_momentum_indicators.rate_of_change(closing_prices=closing_prices, period=4)

    assert str(e.value) == "Period has to be greater or equal to the length of closing prices"


def test_bulk_on_balance_volume():
    closing_prices = [100, 105, 111, 107, 108]
    volume = [1200, 1800, 1600, 1700, 1500]
    obv = bulk_momentum_indicators.on_balance_volume(closing_prices, volume)
    assert obv == [1200, 3000, 4600, 2900, 4400]


def test_bulk_on_balance_volume_length_exception():
    closing_prices = [100, 105, 111]
    volume = [1200, 1800, 1600, 1700, 1500]

    with pytest.raises(Exception) as e:
        bulk_momentum_indicators.on_balance_volume(closing_prices, volume)

    assert str(e.value) == f'Length closing_prices ({len(closing_prices)}) has to equal length volume ({len(volume)})'


def test_bulk_commodity_channel_index():
    prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
    cci = bulk_momentum_indicators.commodity_channel_index(prices, 7)
    assert cci == [-119.7640117994101, -86.35170603674531, -94.51476793248943]


def test_bulk_commodity_channel_index_size_exception():
    prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
    with pytest.raises(Exception) as e:
        bulk_momentum_indicators.commodity_channel_index(prices, 11)
    assert str(e.value) == f'typical_prices ({len(prices)}) needs to be greater or equal to the period (11)'
