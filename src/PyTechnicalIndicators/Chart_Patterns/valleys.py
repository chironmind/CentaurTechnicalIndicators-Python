

def get_valleys(prices: list[float], period: int = 5) -> list[tuple[float, int]]:
    """
    Gets a list of pits (low) prices for a given period

    Calculates the pits for a list of prices and a period. Returns a list of tuples, with the first item is the pit
    price, and the second item is the index at which the price was found.

    For example, for the list of prices [100, 102, 101] would return [(100, 0)]
    :param prices: List of prices
    :param period: (Optional) Period in which the pit should be searched for (defaults to 5)
    :return: Returns a list of tuples, where the first item is the pit price, and the second item is the index
    """
    valleys = []
    for price_index in range(period, len(prices)+1):
        index = price_index - period
        sub_prices = prices[index:price_index]
        valley = min(sub_prices)
        for i in range(len(sub_prices)):
            if sub_prices[i] == valley:
                peak_tuple = (valley, index+i)
                if peak_tuple not in valleys:
                    valleys.append(peak_tuple)
    return valleys
