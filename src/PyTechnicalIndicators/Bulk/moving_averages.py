from ..Single import moving_averages as MAs

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
        price_set = prices[i - period:i]
        moving_averages.append( MAs.moving_average( price_set ))
    return moving_averages


def exponential_moving_average(prices, period, fill_empty=False, fill_value=None):
    return personalised_moving_average(prices, period, 2, 1, fill_empty, fill_value)


def smoothed_moving_average(prices, period, fill_empty=False, fill_value=None):
    return personalised_moving_average(prices, period, 1, 0, fill_empty, fill_value)


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
        price_set = prices[i - period: i]
        single_pma = MAs.personalised_moving_average(price_set, alpha_nominator, alpha_denominator)
        pma.append(single_pma)
    return pma


def moving_average_convergence_divergence(prices, fill_empty=False, fill_value=None):
    if len(prices) < 26:
        raise Exception('The minimum length of prices needs to be 26 to calculate the MACD')
    return personalised_macd(prices, 12, 26, fill_empty, fill_value)


def signal_line(macd, fill_empty=False, fill_value=None):
    if len(macd) < 9:
        raise Exception("Submitted MACD needs to be greater 9 lags long")
    return personalised_signal_line(macd, 9, 'ema', fill_empty, fill_value)


def personalised_macd(prices, short_period, long_period, ma_model='ema', fill_empty=False, fill_value=None):
    if short_period <= 0 or long_period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < long_period:
        raise Exception(f'The minimum length of prices needs to be {long_period} to calculate the MACD')

    macd = []
    if fill_empty:
        for i in range(long_period):
            macd.append(fill_value)
    for i in range(long_period, len(prices)):
        price_set = prices[i - long_period: i]
        single_macd = MAs.personalised_macd( price_set, short_period, long_period, ma_model, fill_empty, fill_value )
        macd.append( single_macd )
    return macd


def personalised_signal_line(macd, period, ma_model='ema', fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    macd_len = len(macd)
    if macd_len == 0:
        raise Exception("Submitted MACD array is too short to calculate singal line")

    signal_lines = []
    if fill_empty:
        for i in range(period):
            signal_lines.append(fill_value)
    for i in range(period, macd_len):
        macd_set = macd[i-period: i]
        signal_line = MAs.personalised_signal_line( macd_set, ma_model )
        signal_lines.append( signal_line )
    return signal_lines
