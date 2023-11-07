from ..Single import correlation_indicators


def correlate_asset_prices(asset_a_prices: list[float], asset_b_prices: list[float], period: int) -> list[float]:
    """
    Calculate the correlation of two assets or a period of time
    :param asset_a_prices: Prices for asset a
    :param asset_b_prices: Prices for asset b
    :param period: Period for which to calculate the correlation
    :return: Returns a list of correlations
    """
    if period > len(asset_a_prices) or period > len(asset_b_prices):
        raise Exception(f'length of price_a ({len(asset_a_prices)}) and length of price_b ({len(asset_b_prices)}) needs to be greater than period ({period})')
    if len(asset_a_prices) != len(asset_b_prices):
        raise Exception(f'length of price_a ({len(asset_a_prices)}) needs to equal length of price_b ({len(asset_b_prices)})')
    correlation_list = []
    for i in range(len(asset_a_prices)-period+1):
        correlation_list.append(correlation_indicators.correlate_asset_prices(asset_a_prices[i:i+period], asset_b_prices[i:i+period]))
    return correlation_list
