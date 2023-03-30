

# TODO: make periods a total not something you add before or after, makes it confusing
def get_peaks(prices: list[float], period: int = 5) -> list[tuple[float, int]]:
    """
    Gets a list of peaks (high) prices for a given period

    Calculates the peaks for a list of prices and a period. Returns a list of tuples, with the first item is the peak
    price, and the second item is the index at which the price was found.

    For example, for the list of prices [100, 102, 101] would return [(102, 1)]

    second
    :param prices: List of prices
    :param period: (Optional) Period in which the peak should be searched for (defaults to 5)
    :return: Returns a list of tuples, where the first item is the peak price, and the second item is the index
    """
    peaks = []
    for price_index in range(len(prices)):
        if price_index < period:
            sub_prices = prices[:price_index+period]
        elif price_index > len(prices) - period:
            sub_prices = prices[price_index-period:]
        else:
            sub_prices = prices[price_index-period:price_index+period]

        peak = max(sub_prices)
        if prices[price_index] == peak and sub_prices.count(peak) == 1:
            peaks.append((prices[price_index], price_index))

    return peaks
