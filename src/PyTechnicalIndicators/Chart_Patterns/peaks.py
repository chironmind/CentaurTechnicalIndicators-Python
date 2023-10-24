

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
    length = len(prices)
    if length < period:
        raise Exception(f'Length of prices ({length}) needs to be at least equal to period ({period})')
    peaks = []
    for price_index in range(period, length+1):
        index = price_index - period
        sub_prices = prices[index:price_index]
        peak = max(sub_prices)
        for i in range(len(sub_prices)):
            if sub_prices[i] == peak:
                peak_tuple = (peak, index+i)
                if peak_tuple not in peaks:
                    peaks.append(peak_tuple)
    return peaks
