from ..Single.moving_averages import exponential_moving_average as single_ema
from ..Single.moving_averages import moving_average as single_ma
from ..Single.moving_averages import smoothed_moving_average as single_sma

ma = ['ma', 'moving average', 'moving_average']
sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
ema = ['ema', 'exponential moving average', 'exponential_moving_average']


def moving_average(prices, period, fill_empty=False, fill_value=None):
    # MA gives an idea of the trend and whether it's going to switch bull/bear
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    moving_averages = []
    if fill_empty:
        for i in range(period):
            moving_averages.append(fill_value)
    for i in range(period, len(prices)):
        moving_averages.append(sum(prices[i - period:i]) / period)

    return moving_averages


def exponential_moving_average(prices, period, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    ema = []
    if fill_empty:
        for i in range(period):
            ema.append(fill_value)
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


def smoothed_moving_average(prices, period, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    sma = []
    if fill_empty:
        for i in range(period):
            sma.append(fill_value)
    for i in range(period, len(prices)):
        alpha = 1 / len(prices)
        price_sum = 0
        denominator_sum = 0

        for j in range(i, i - period, -1):
            # the most recent value would need to have a 0 pow and it would get the highest
            power = i - j
            denominator_sum += pow(1 - alpha, power)
            price_sum += prices[j] * pow(1 - alpha, power)

        sma.append(price_sum / denominator_sum)

    return sma


def personalised_moving_average(prices, period, alpha_nominator, alpha_denominator, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    pma = []
    if fill_empty:
        for i in range(period):
            pma.append(fill_value)
    for i in range(period, len(prices)):
        alpha = alpha_nominator / (len(prices) + alpha_denominator)
        price_sum = 0
        denominator_sum = 0

        for j in range(i, i - period, -1):
            # the most recent value would need to have a 0 pow and it would get the highest
            power = i - j
            denominator_sum += pow(1 - alpha, power)
            price_sum += prices[j] * pow(1 - alpha, power)

        pma.append(price_sum / denominator_sum)

    return pma


def moving_average_convergence_divergence(prices):
    if len(prices) < 26:
        raise Exception('The minimum length of prices needs to be 24 to calculate the MACD')

    macd = []
    for i in range(25, len(prices)):
        ema_12_periods = single_ema(prices[i-12:i])
        ema_26_periods = single_ema(prices[i-25:i])
        macd.append(ema_12_periods - ema_26_periods)

    return macd


def signal_line(macd):
    if len(macd) < 9:
        raise Exception("Submitted MACD needs to be greater 9 lags long")

    signal_lines = []
    for i in range(9, len(macd)):
        signal_lines.append(single_ema(macd[i-9: i]))

    return signal_lines


def personalised_macd(prices, short_period, long_period, ma_model='ema'):
    if short_period <= 0 or long_period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < long_period:
        raise Exception(f'The minimum length of prices needs to be {long_period} to calculate the MACD')

    macd = []
    for i in range(long_period, len(prices)):
        if ma_model in ma:
            ma_short_period = single_ma(prices[i - short_period:i])
            ma_long_period = single_ma(prices[i - short_period:i])
        elif ma_model in sma:
            ma_short_period = single_sma(prices[i - short_period:i])
            ma_long_period = single_sma(prices[i - short_period:i])
        elif ma_model in ema:
            ma_short_period = single_ema(prices[i-short_period:i])
            ma_long_period = single_ema(prices[i-short_period:i])
        else:
            ma_short_period = single_ema(prices[i-short_period:i])
            ma_long_period = single_ema(prices[i-short_period:i])

        macd.append(ma_short_period - ma_long_period)

    return macd


def personalised_signal_line(macd, period, ma_model='ema'):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(macd) == 0:
        raise Exception("Submitted MACD array is too short to calculate singal line")

    signal_lines = []
    for i in range(period, len(macd)):
        if ma_model in ma:
            signal_lines.append(single_ma(macd[i-period: i]))
        elif ma_model in sma:
            signal_lines.append(single_sma(macd[i-period: i]))
        elif ma_model in ema:
            signal_lines.append(single_ema(macd[i-period: i]))
        else:
            signal_lines.append(single_ema(macd[i-period: i]))

        signal_lines.append(single_ema(macd[i-period: i]))

    return signal_lines
