from ..Single.moving_averages import exponential_moving_average as single_ema


def moving_average(prices, period):
    # MA gives an idea of the trend and whether it's going to switch bull/bear
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    moving_averages = []
    for i in range(period, len(prices)):
        moving_averages.append(sum(prices[i - period:i]) / period)

    return moving_averages


def exponential_moving_average(prices, period):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    ema = []
    for i in range(period, len(prices)):
        alpha = 2 / (period + 1)
        price_sum = 0
        denominator_sum = 0

        for j in range(i, i - period, -1):
            power = i - j
            denominator_sum += pow(1 - alpha, power)
            price_sum += prices[j] * pow(1 - alpha, power)

        ema.append(price_sum / denominator_sum)

    return ema


def smoothed_moving_average(prices, period):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    sma = []
    for i in range(period, len(prices)):
        alpha = 1 / len(prices)
        price_sum = 0
        denominator_sum = 0

        for j in range(i, i - period, -1):
            # the most recent value would need to have a 0 pow and it would get the highest
            power = i - j
            denominator_sum += pow(1 - alpha, power)
            price_sum += prices[j] * pow(1 - alpha, power)

    return sma


def personalised_moving_average(prices, period, alpha_nominator, alpha_denominator):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    pma = []
    for i in range(period, len(prices)):
        alpha = alpha_nominator / (len(prices) + alpha_denominator)
        price_sum = 0
        denominator_sum = 0

        for j in range(i, i - period, -1):
            # the most recent value would need to have a 0 pow and it would get the highest
            power = i - j
            denominator_sum += pow(1 - alpha, power)
            price_sum += prices[j] * pow(1 - alpha, power)

    return pma


def moving_average_convergence_divergence(prices):
    if len(prices) < 26:
        raise Exception('The minimum length of prices needs to be 24 to calculate the MACD')

    macd = []
    for i in range(25, len(prices)):
        ema_12_periods = single_ema(prices[i-12:i])
        ema_26_periods = single_ema(prices[i-26:i])
        macd.append(ema_12_periods - ema_26_periods)

    return macd


def signal_line(macd):
    if len(macd) != 9:
        raise Exception("Submitted MACD needs to be 9 lags long")

    signal_lines = []
    for i in range(9, len(macd)):
        signal_lines.append(single_ema(macd[i-9: i]))

    return signal_lines


def personalised_macd(prices, short_period, long_period):
    if short_period <= 0 or long_period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < long_period:
        raise Exception(f'The minimum length of prices needs to be {long_period} to calculate the MACD')

    macd = []
    for i in range(long_period, len(prices)):
        ema_short_period = single_ema(prices[i-short_period:i])
        ema_long_period = single_ema(prices[i-long_period:i])
        macd.append(ema_short_period - ema_long_period)

    return macd


def personalised_signal_line(macd, period):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(macd) == 0:
        raise Exception("Submitted MACD array is too short to calculate singal line")

    signal_lines = []
    for i in range(period, len(macd)):
        signal_lines.append(single_ema(macd[i-period: i]))

    return signal_lines
