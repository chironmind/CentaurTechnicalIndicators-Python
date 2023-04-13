import statistics


# TODO: Check this, results seem odd, does it need to be done on a point by point basis?
def correlate_asset_prices(price_asset_a: list[float], price_asset_b: list[float]) -> float:
    """
    Calculate the correlation between two prices for a given period. Period is determined by the length of the list of prices
    :param price_asset_a: List of prices of the first asset
    :param price_asset_b: List of prices of the second asset
    :return: Returns the correlation between two assets as a float
    """
    if len(price_asset_a) != len(price_asset_b):
        raise Exception(f'length of price_a ({len(price_asset_a)}) needs to equal length of price_b ({len(price_asset_b)})')

    asset_a_avg_price = statistics.mean(price_asset_a)
    print(asset_a_avg_price)
    asset_b_avg_price = statistics.mean(price_asset_b)
    print(asset_b_avg_price)

    asset_a_avg_return = 0
    for price in price_asset_a:
        asset_a_avg_return += price - asset_a_avg_price

    asset_b_avg_return = 0
    for price in price_asset_b:
        asset_b_avg_return += price - asset_b_avg_price

    covariance = (asset_a_avg_return * asset_b_avg_return) / (len(price_asset_a) - 1)
    asset_a_std_dev = statistics.stdev(price_asset_a)
    asset_b_std_dev = statistics.stdev(price_asset_b)

    return covariance / (asset_a_std_dev * asset_b_std_dev)


#  TODO: Other versions of the correlation https://en.wikipedia.org/wiki/Correlation