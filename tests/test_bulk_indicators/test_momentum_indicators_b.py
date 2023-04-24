import pytest

from src.PyTechnicalIndicators.Bulk.momentum_indicators import rate_of_change, on_balance_volume, personalised_commodity_channel_index


def test_rate_of_change():
    closing_prices = [100, 101, 105, 103, 99, 80, 85, 100, 90, 85]
    roc = rate_of_change(closing_prices=closing_prices, period=3)
    # This should calculate the roc for the following pairs (current, previous):
    #   (103, 100), (99, 101), (80, 105), (85, 103), (100, 99), (90, 80), (85, 85)
    assert roc == [3.0, -1.9801980198019802, -23.809523809523807, -17.475728155339805, 1.0101010101010102, 12.5, 0]


def test_rate_of_change_exception():
    closing_prices = [100, 101, 105]
    with pytest.raises(Exception) as e:
        rate_of_change(closing_prices=closing_prices, period=4)

    assert str(e.value) == "Period has to be greater or equal to the length of closing prices"


def test_on_balance_volume():
    closing_prices = [100, 105, 111, 107, 108]
    volume = [1200, 1800, 1600, 1700, 1500]
    obv = on_balance_volume(closing_prices, volume)
    assert len(obv) == 5
    assert obv == [1200, 3000, 4600, 2900, 4400]


def test_on_balance_volume_length_exception():
    closing_prices = [100, 105, 111]
    volume = [1200, 1800, 1600, 1700, 1500]

    with pytest.raises(Exception) as e:
        on_balance_volume(closing_prices, volume)

    assert str(e.value) == f'Length closing_prices ({len(closing_prices)}) has to equal length volume ({len(volume)})'


def test_commodity_channel_index():
    prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
    cci = personalised_commodity_channel_index(prices, 7)
    assert cci == [-119.7640117994101, -86.35170603674531, -94.51476793248943]


def test_commodity_channel_index_size_exception():
    prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
    with pytest.raises(Exception) as e:
        personalised_commodity_channel_index(prices, 11)
    assert str(e.value) == f'typical_prices ({len(prices)}) needs to be greater or equal to the period (11)'
