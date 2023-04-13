import pytest

from src.PyTechnicalIndicators.Bulk.correlation import correlate_asset_prices


def test_correlate_asset_prices():
    asset_a_price = [120, 110, 105, 112, 114, 116]
    asset_b_price = [150, 155, 162, 165, 159, 154]
    corr = correlate_asset_prices(asset_a_price, asset_b_price, 5)
    assert corr == [-6.2383852361787784e-30, 0]


def test_correlate_asset_prices_mismatch_length_exception():
    asset_a_price = [120, 110, 105, 98]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        correlate_asset_prices(asset_a_price, asset_b_price, 3)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'

    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165]
    with pytest.raises(Exception) as e:
        correlate_asset_prices(asset_a_price, asset_b_price, 3)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'


def test_correlate_asset_prices_period_exception():
    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        correlate_asset_prices(asset_a_price, asset_b_price, 10)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) and length of price_b ({len(asset_b_price)}) needs to be greater than period (10)'