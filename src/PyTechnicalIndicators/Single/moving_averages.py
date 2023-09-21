ma = ['ma', 'moving average', 'moving_average']
sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
ema = ['ema', 'exponential moving average', 'exponential_moving_average']


def moving_average(prices: list[float]) -> float:
    """
    Calculates the moving average
    :param prices: List of prices
    :return: Returns the moving average as a float
    """
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to do a moving average')
    return sum(prices) / len(prices)


# TODO: these could just call the personalised MA
def exponential_moving_average(prices: list[float]) -> float:
    """
    Calculates the exponential moving average
    :param prices: List of prices
    :return: Returns the EMA as a float
    """
    length_prices = len(prices)
    if length_prices <= 1:
        raise Exception('There needs to be prices to be able to do an exponential moving average')
    alpha = 2 / (length_prices + 1)
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, -1, -1):
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


def smoothed_moving_average(prices: list[float]) -> float:
    """
    Calculates the smoothed moving average
    :param prices: List of prices
    :return: Returns the SMA as a float
    """
    # SmoothedMA is same as EMA but alpha = 1 / len(prices)
    length_prices = len(prices)
    if length_prices <= 1:
        raise Exception('There needs to be prices to be able to do an smoothed moving average')

    alpha = 1 / length_prices
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, -1, -1):
        # the most recent value would need to have a 0 pow and it would get the highest
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


# TODO: have exp and smoothed call this with their hardcoded params once it passes tests
def personalised_moving_average(prices: list[float], alpha_nominator: int, alpha_denominator: int) -> float:
    """

    :param prices:
    :param alpha_nominator:
    :param alpha_denominator:
    :return:
    """
    length_prices = len(prices)
    if length_prices == 0:
        raise Exception('There needs to be prices to be able to do personalised moving average')

    if length_prices + alpha_denominator == 0:
        raise Exception('The length of prices and the value of the alpha denominator add up to 0, and division by 0 isn\'t possible')

    alpha = alpha_nominator / (length_prices + alpha_denominator)
    price_sum = 0
    denominator_sum = 0

    for i in range(length_prices - 1, -1, -1):
        power = length_prices - i
        denominator_sum += pow(1 - alpha, power)
        price_sum += prices[i] * pow(1 - alpha, power)

    return price_sum / denominator_sum


# TODO: MACD should probably be one function that gets called and returns everything (macd, signal, diff)
#  and rename below to macd line
def moving_average_convergence_divergence(prices: list[float]) -> float:
    """
    Calculates the MACD line
    :param prices: List of prices
    :return: Returns the MACD as a float
    """
    prices_length = len(prices)
    if prices_length < 26:
        raise Exception("Submitted prices is too short to calculate MACD")

    ema_12_periods = exponential_moving_average(prices[prices_length - 12:])
    ema_26_periods = exponential_moving_average(prices[prices_length - 26:])
    macd = ema_12_periods - ema_26_periods

    return macd


def signal_line(macd: list[float]) -> float:
    """
    Calculates the signal line
    :param macd: list of MACDs
    :return: Returns the signal line as a float
    """
    if len(macd) != 9:
        raise Exception("Submitted MACD array needs to be 9 lags long")

    return exponential_moving_average(macd)

# TODO: PMA
def personalised_macd(prices: list[float], short_period: int, long_period: int, ma_model: str = 'ema') -> float:
    """
    Calculates the personalised MACD

    The default MACD uses a short period of 12, a long period of 26, and uses an Exponential Moving Average model to calculate
    the MACD. This function allows for the MACD to match any markets that may trade on a different time frame
    :param prices: list of prices
    :param short_period: Number for the short period
    :param long_period: Number for the long period
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :return: Returns the MACD as a float
    """
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

# TODO: Support PMA
def personalised_signal_line(macd: list[float], ma_model: str = 'ema') -> float:
    """
    Calculates a personalised version of the signal line
    :param macd: List of MACDs
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :return: Returns the Signal line as a float
    """
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

# TODO: moving median


# TODO: Not convinced about what to do when there is no previous dynamic
def mcginley_dynamic(price: float, period: int, previous_mcginley_dynamic: float = 0) -> float:
    """
    The McGinley Dynamic offers an alternative to the moving average, the idea is that it should be more resilient to
    shocks than moving average models
    :param price: Current price
    :param period: The period works in a similar manner to the period for moving average models, the higher the period,
    the smoother the line
    :param previous_mcginley_dynamic: (Optional) The previous value of the McGinley Dynamic
    :return: Returns the McGinley dynamic as a float
    """
    if previous_mcginley_dynamic == 0:
        return price
    base = price / previous_mcginley_dynamic
    return previous_mcginley_dynamic + ((price - previous_mcginley_dynamic) / (period * pow(base, 4)))


def moving_average_envelopes(prices: list[float], ma_model: str = 'ma', difference: int = 3) -> tuple[float, float, float]:
    """
    Calculates the moving average envelope for a list of prices.
    The period used for the moving average will be the length of the price list.
    :param prices: List of prices
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :param difference: (Optional) The percent difference for the envelope from the calculated.
        The default of 3 means +- 3% from the calculated MA from the list of prices
    :return: Returns a tuple with the upper envelope, moving average, and lower envelope
    """
    if ma_model in ma:
        m_average = moving_average(prices)
    elif ma_model in sma:
        m_average = smoothed_moving_average(prices)
    elif ma_model in ema:
        m_average = exponential_moving_average(prices)
    else:
        raise Exception(f'{ma_model} is not an accepted model, accepted models are: {ma}, {sma}, {ema}')

    upper_envelope = m_average * (1 + (difference/100))
    lower_envelope = m_average * (1 - (difference/100))
    return upper_envelope, m_average, lower_envelope
