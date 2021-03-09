ma = ['ma', 'moving average', 'moving_average']
sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
ema = ['ema', 'exponential moving average', 'exponential_moving_average']

def moving_average(prices):
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to do a moving average')
    return sum(prices) / len(prices)


def exponential_moving_average(prices):
    length_prices = len(prices)
    if length_prices <= 1:
        raise Exception('There needs to be prices to be able to do an exponential moving average')
    alpha = 2 / (length_prices + 1)
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, 0, -1):
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


def smoothed_moving_average(prices):
    # SmoothedMA is same as EMA but alpha = 1 / len(prices)
    length_prices = len(prices)
    if length_prices <= 1:
        raise Exception('There needs to be prices to be able to do an smoothed moving average')

    alpha = 1 / length_prices
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, 0, -1):
        # the most recent value would need to have a 0 pow and it would get the highest
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


def personalised_moving_average(prices, alpha_nominator, alpha_denominator):
    length_prices = len(prices)
    if length_prices == 0:
        raise Exception('There needs to be prices to be able to do personalised moving average')

    if length_prices + alpha_denominator == 0:
        raise Exception('The length of prices and the value of the alpha denominator add up to 0, and division by 0 isn\'t possible')

    alpha = alpha_nominator / (length_prices + alpha_denominator)
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, 0, -1):
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


def moving_average_divergence_convergence(prices):
    prices_length = len(prices)
    if prices_length < 26:
        raise Exception("Submitted prices is too short to calculate MACD")

    ema_12_periods = exponential_moving_average(prices[prices_length - 12:])
    ema_26_periods = exponential_moving_average(prices[prices_length - 26:])
    macd = ema_12_periods - ema_26_periods

    return macd


def signal_line(macd):
    if len(macd) != 9:
        raise Exception("Submitted MACD array needs to be 9 lags long")

    return exponential_moving_average(macd)


def personalised_macd(prices, short_period, long_period, ma_model='ema'):
    if short_period <= 0 or long_period <= short_period:
        raise Exception('Period needs to be at least 1')

    prices_length = len(prices)
    if prices_length < long_period:
        raise Exception(f"Submitted prices is too short to calculate MACD needs to be greater than {long_period}")

    if ma_model in ma:
        ma_short_period = moving_average(prices[prices_length - short_period:])
        ma_long_period = moving_average(prices[prices_length - long_period:])
    elif ma_model in sma:
        ma_short_period = smoothed_moving_average(prices[prices_length - short_period:])
        ma_long_period = smoothed_moving_average(prices[prices_length - long_period:])
    elif ma_model in ema:
        ma_short_period = exponential_moving_average(prices[prices_length - short_period:])
        ma_long_period = exponential_moving_average(prices[prices_length - long_period:])
    else:
        ma_short_period = exponential_moving_average(prices[prices_length - short_period:])
        ma_long_period = exponential_moving_average(prices[prices_length - long_period:])

    macd = ma_short_period - ma_long_period

    return macd


def personalised_signal_line(macd, ma_model='ema'):
    if len(macd) == 1:
        raise Exception("Submitted MACD array is too short needs to be greater than 1")

    if ma_model in ma:
        return moving_average(macd)
    elif ma_model in sma:
        return smoothed_moving_average(macd)
    elif ma_model in ema:
        return exponential_moving_average(macd)
    else:
        return exponential_moving_average(macd)
