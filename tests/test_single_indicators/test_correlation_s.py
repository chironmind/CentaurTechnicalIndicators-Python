import pytest

from src.PyTechnicalIndicators.Single.correlation import correlate_asset_prices

# Test perfectly correlated, opposing...
def test_correlate_asset_prices():
    asset_a_price = [120, 110, 105, 112, 114]
    asset_b_price = [150, 155, 162, 165, 159]
    correlation = correlate_asset_prices(asset_a_price, asset_b_price)
    assert correlation == -6.2383852361787784e-30


def test_correlate_asset_prices_exception():
    asset_a_price = [120, 110, 105, 98]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        correlate_asset_prices(asset_a_price, asset_b_price)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'

    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165]
    with pytest.raises(Exception) as e:
        correlate_asset_prices(asset_a_price, asset_b_price)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'
