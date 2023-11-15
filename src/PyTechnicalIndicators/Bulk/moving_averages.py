from ..Single import moving_averages


def moving_average(prices: list[float], period: int) -> list[float]:
    """
    Calculates the moving average for a list of prices and a certain period, returns a list of moving averages.
    :param prices: List of prices
    :param period: Period for which the moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of moving averages
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < period:
        raise Exception(f'Length of prices ({prices}) needs to or equal to period ({period})')
    mas = []
    for i in range(period, len(prices)+1):
        price_set = prices[i - period:i]
        mas.append(moving_averages.moving_average(price_set))
    return mas


def exponential_moving_average(prices: list[float], period: int) -> list[float]:
    """
    Calculates the exponential moving average for a list of prices and a certain period, returns a list of exponential moving averages.
    :param prices: List of prices
    :param period: Period for which the exponential moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of exponential moving averages
    """
    return personalised_moving_average(prices, period, 2, 1)


def smoothed_moving_average(prices: list[float], period: int) -> list[float]:
    """
    Calculates the smoothed moving average for a list of prices and a certain period, returns a list of smoothed moving averages.
    :param prices: List of prices
    :param period: Period for which the smoothed moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of smoothed moving averages
    """
    return personalised_moving_average(prices, period, 1, 0)


def personalised_moving_average(prices: list[float], period: int, alpha_nominator: int, alpha_denominator: int) -> list[float]:
    """
    Calculates the personalised moving average for a list of prices and a certain period, returns a list of personalised moving averages.

    Moving averages are calculated using an alpha nominator and an alpha denominator. For example when calculating the
    exponential moving average the alpha nominator is 2 and the denominator is 1. For the smoothed moving average the
    nominator is 1 and the denominator is 0.
    :param prices: List of prices
    :param period: Period for which the smoothed moving average should be calculated for
    :param alpha_nominator: Nominator used when calculating the alpha
    :param alpha_denominator: Denominator used when calculating the alpha
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of smoothed moving averages
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < period:
        raise Exception(f'Length of prices ({prices}) needs to or equal to period ({period})')
    pma = []
    for i in range(period, len(prices)+1):
        price_set = prices[i - period: i]
        single_pma = moving_averages.personalised_moving_average(price_set, alpha_nominator, alpha_denominator)
        pma.append(single_pma)
    return pma


# TODO: Allow for PMA and McGinley
def moving_average_convergence_divergence(prices: list[float], macd_short_period: int = 12, macd_long_period: int = 26, signal_period: int = 9, ma_model: str = 'ema') -> list[tuple[float, float, float]]:
    """
    Calculates the MACD, signal line, and difference between them.
    :param prices:  List of prices
    :param macd_short_period: Short period for the MACD. Defaults to 12
    :param macd_long_period: Long period for the MACD. Defaults to 26.
    :param signal_period: Period for the Signal line. Defaults to 9.
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :return: Returns the MACD line, signal line, and the difference between the two as a list of floats.
    """
    macd = macd_line(prices, macd_short_period, macd_long_period, ma_model)
    signal = signal_line(macd, signal_period, ma_model)
    length_diff = len(macd) - len(signal)
    r = []
    for i in range(len(signal)):
        r.append((macd[i+length_diff], signal[i], macd[i+length_diff] - signal[i]))
    return r


# TODO: Allow for PMA and McGinley
def macd_line(prices: list[float], short_period: int = 12, long_period: int = 26, ma_model: str = 'ema') -> list[float]:
    """
    Calculates the MACD.
    The default MACD uses a short period of 12, a long period of 26, and uses an Exponential Moving Average model to calculate
    the MACD. This function allows for the MACD to match any markets that may trade on a different time frame.
    :param prices: List of prices
    :param short_period: A number for the short period, must be greater than 0 and greater than the long period
    :param long_period: A number for the long period, must be greater than 0
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :return: Returns a list of MACD points
    """
    length = len(prices)
    if length < long_period:
        raise Exception(f'Prices ({length}) needs to be equal or greater than long_period ({long_period})')
    macd = []
    for i in range(long_period, length+1):
        price_set = prices[i - long_period: i]
        single_macd = moving_averages.macd_line(price_set, short_period, long_period, ma_model)
        macd.append(single_macd)
    return macd


# TODO: Support PMA  and McGinley
def signal_line(macd: list[float], period: int = 9, ma_model: str = 'ema'):
    """
    Calculates the Signal line
    The default signal line calculation uses a period of 9 and an Exponential Moving Average model. The caller of the
    function can decide the values if needed.
    :param macd: List of MACDs
    :param period: Number of periods for which the moving average should be calculated for
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of Signal line points
    """
    macd_len = len(macd)
    if macd_len < period:
        raise Exception(f"Length of MACD ({macd_len}) needs to be equal or greater tjan period ({period})")
    signal_lines = []
    for i in range(period, macd_len+1):
        macd_set = macd[i-period: i]
        signal_line = moving_averages.signal_line(macd_set, ma_model)
        signal_lines.append(signal_line)
    return signal_lines

# TODO: Moving Median and McGinley

def mcginley_dynamic(prices: list[float], period: int) -> list[float]:
    """
    The McGinley Dynamic offers an alternative to the moving average, the idea is that it should be more resilient to
    shocks than moving average models
    :param prices: List of prices
    :param period: The period works in a similar manner to the period for moving average models, the higher the period,
    the smoother the line
    :return: Returns a list of McGinley Dynamics
    """
    initial_mcginley_dynamic = moving_averages.mcginley_dynamic(prices[0], period)
    mcginley_dynamic_list = [initial_mcginley_dynamic]
    for price in prices[1:]:
        mcginley_dynamic_list.append(moving_averages.mcginley_dynamic(price, period, mcginley_dynamic_list[-1]))
    return mcginley_dynamic_list


def moving_average_envelopes(prices: list[float], period: int, ma_model: str = 'ma', difference: int = 3) -> list[tuple[float, float, float]]:
    """
    Calculates the moving average envelopes for a list of prices
    :param prices: List of prices
    :param period: Moving Average period
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :param difference: (Optional) The percent difference for the envelope from the calculated.
        The default of 3 means +- 3% from the calculated MA from the list of prices
    :return: Returns a list of tuples with the upper envelope, moving average, and lower envelope
    """
    if period > len(prices):
        raise Exception(f'Period ({period}) cannot be longer than length of prices ({len(prices)})')
    ma_envelope_list = []
    for i in range(len(prices) - period + 1):
        ma_envelope_list.append(moving_averages.moving_average_envelopes(prices[i:i+period], ma_model, difference))
    return ma_envelope_list
