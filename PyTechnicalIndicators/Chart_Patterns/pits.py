

def get_pits(prices, scope=5):
    pits = []
    for price_index in range(len(prices)):
        if price_index < scope:
            sub_prices = prices[:price_index + scope]
        elif price_index > len(prices) - scope:
            sub_prices = prices[price_index - scope:]
        else:
            sub_prices = prices[price_index - scope:price_index + scope]

        pit = min(sub_prices)
        if prices[price_index] == pit and sub_prices.count(pit) == 1:
            pits.append((prices[price_index], price_index))

    return pits


def get_lowest_pit(prices):
    # Would this even be used
    return min(get_pits(prices))
