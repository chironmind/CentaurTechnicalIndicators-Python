

def get_pits(prices, period=5):
    # TODO: make periods a total not something you add before or after, makes it confusing
    pits = []
    for price_index in range(len(prices)):
        if price_index < period:
            sub_prices = prices[:price_index + period]
        elif price_index > len(prices) - period:
            sub_prices = prices[price_index - period:]
        else:
            sub_prices = prices[price_index - period:price_index + period]

        pit = min(sub_prices)
        if prices[price_index] == pit and sub_prices.count(pit) == 1:
            pits.append((prices[price_index], price_index))

    return pits


def get_lowest_pit(prices):
    # Would this even be used
    return min(get_pits(prices))
