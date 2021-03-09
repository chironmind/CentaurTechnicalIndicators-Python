

def get_peaks(prices, period=5):
    # TODO: make periods a total not something you add before or after, makes it confusing
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


def get_highest_peak(prices):
    # Would this even be used
    return max(get_peaks(prices))
