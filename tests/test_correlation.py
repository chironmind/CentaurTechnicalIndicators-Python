import pytest

from src.PyTechnicalIndicators.Single import correlation as single_correlation
from src.PyTechnicalIndicators.Bulk import correlation as bulk_correlation


# TODO: Test perfectly correlated, opposing...
def test_single_correlate_asset_prices():
    asset_a_price = [120, 110, 105, 112, 114]
    asset_b_price = [150, 155, 162, 165, 159]
    correlation = single_correlation.correlate_asset_prices(asset_a_price, asset_b_price)
    assert correlation == -0.65025528597848


def test_single_correlate_asset_prices_perfect_positive():
    asset_a_price = [120, 110, 105, 112, 114]
    asset_b_price = [120, 110, 105, 112, 114]
    correlation = single_correlation.correlate_asset_prices(asset_a_price, asset_b_price)
    assert correlation == 1.0


def test_single_correlate_asset_prices_perfect_negatively():
    asset_a_price = [100, 105, 100, 95, 100]
    asset_b_price = [100, 95, 100, 105, 100]
    correlation = single_correlation.correlate_asset_prices(asset_a_price, asset_b_price)
    assert correlation == -0.9999999999999999


def test_single_correlate_asset_prices_exception():
    asset_a_price = [120, 110, 105, 98]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        single_correlation.correlate_asset_prices(asset_a_price, asset_b_price)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'

    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165]
    with pytest.raises(Exception) as e:
        single_correlation.correlate_asset_prices(asset_a_price, asset_b_price)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'


def test_bulk_correlate_asset_prices():
    asset_a_price = [120, 110, 105, 112, 114, 116]
    asset_b_price = [150, 155, 162, 165, 159, 154]
    corr = bulk_correlation.correlate_asset_prices(asset_a_price, asset_b_price, 5)
    assert corr == [-0.65025528597848, -0.4217205045478597]


def test_bulk_correlate_asset_prices_mismatch_length_exception():
    asset_a_price = [120, 110, 105, 98]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        bulk_correlation.correlate_asset_prices(asset_a_price, asset_b_price, 3)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'

    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165]
    with pytest.raises(Exception) as e:
        bulk_correlation.correlate_asset_prices(asset_a_price, asset_b_price, 3)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) needs to equal length of price_b ({len(asset_b_price)})'


def test_bulk_correlate_asset_prices_period_exception():
    asset_a_price = [120, 110, 105, 98, 114]
    asset_b_price = [150, 155, 162, 165, 170]
    with pytest.raises(Exception) as e:
        bulk_correlation.correlate_asset_prices(asset_a_price, asset_b_price, 10)
    assert str(e.value) == f'length of price_a ({len(asset_a_price)}) and length of price_b ({len(asset_b_price)}) needs to be greater than period (10)'