from src.PyTechnicalIndicators.Single import strength_indicators


def relative_strength_index(prices: list[float]) -> list[float]:
    """
    Calculates the RSI from a list of prices
    :param prices: List of prices
    :return: Returns the RSI as a list
    """
    if len(prices) < 14:
        raise Exception(f'14 periods are needed to calculate RSI {len(prices)} have been provided')
    return personalised_rsi(prices, 14)


# TODO: allow pma using kwargs
def personalised_rsi(prices: list[float], period: int, ma_model: str = 'sma') -> list[float]:
    """
    Calculates a personalised RSI

    The default RSI uses a period of 14 and a Smoothed Moving Average model to calculate the RSI. This functions allows
    any period of MA model to be used to calculate the RSI
    :param prices: List of prices
    :param period: Number of periods for which the moving average should be calculated for
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'sma'
    :return: Returns a list of personalised RSI
    """
    if len(prices) < period:
        raise Exception(f'Submitted prices needs to be greater than submitted period of {period}')
    rsi = []
    for i in range(period, len(prices) + 1):
        rsi.append(strength_indicators.personalised_rsi(prices[i-period:i], ma_model))
    return rsi


def accumulation_distribution_indicator(high: list[float], low: list[float], close: list[float], volume: list[int]) -> list[float]:
    if len(high) != len(low) or len(high) != len(close) or len(high) != len(volume):
        raise Exception(f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}')

    adi_list = []
    for i in range(len(high)):
        if adi_list:
            adi_list.append(strength_indicators.accumulation_distribution_indicator(high[i], low[i], close[i], volume[i], adi_list[-1]))
        else:
            adi_list.append(strength_indicators.accumulation_distribution_indicator(high[i], low[i], close[i], volume[i], 0))

    return adi_list


def directional_indicator(high: list[float], low: list[float], previous_close: list[float], period: int) -> list[tuple[float, float, float]]:
    """
    Calculates the directional indicator for a list of highs, lows, previous close for a given period
    :param high: List of highs
    :param low: List of lows
    :param previous_close: List of previous closes
    :param period: Period to calculate the period
    :return: Returns the positive, negative directional indicator, and the true range a list of tuples of floats
    """
    length = len(high)
    if length != len(low) or length != len(previous_close):
        raise Exception(f'lengths of high ({len(high)}), low ({len(low)}), and previous_close ({len(previous_close)}) need to match')
    if period > length:
        raise Exception(f'Period ({period}) needs to be at least equal to the length of lists ({length})')

    initial_di = strength_indicators.period_directional_indicator(high[:period], low[:period], previous_close[:period])
    di = [(initial_di[0], initial_di[1], initial_di[2])]
    positive_dm = initial_di[3]
    negative_dm = initial_di[4]
    for i in range(period, length):
        loop_di = strength_indicators.period_directional_indicator_known_previous(high[i], high[i-1], low[i], low[i-1], previous_close[i], di[-1][2], positive_dm, negative_dm, period)
        di.append((loop_di[0], loop_di[1], loop_di[2]))
        positive_dm = loop_di[3]
        negative_dm = loop_di[4]
    return di


def directional_index(positive_directional_indicator: list[float], negative_directional_indicator: list[float]) -> list[float]:
    """
    Calculates the directional index for a list of positive and negative directional indicators
    :param positive_directional_indicator: List of positive directional indicators
    :param negative_directional_indicator: List of negative directional indicators
    :return: Returns a list of directional indexes
    """
    length = len(positive_directional_indicator)
    if len(negative_directional_indicator) != length:
        raise Exception(f'Length of positive_directional_indicator ({length}) and negative_directional_indicator ({len(negative_directional_indicator)}) need to match')
    dx = []
    for i in range(length):
        dx.append(strength_indicators.directional_index(positive_directional_indicator[i], negative_directional_indicator[i]))
    return dx


def average_directional_index(directional_index: list[float], period: int, moving_average_model: str = 'ma') -> list[float]:
    """
    Calculates the average directional index from a list of directional indexes
    :param directional_index: List of directional indexes
    :param moving_average_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'sma'
    :return: Returns a list of average directional indexes
    """
    length = len(directional_index)
    if length < period:
        raise Exception(f'Length of ({directional_index}) needs to be at least equal to period ({period})')
    adx = []
    for i in range(length - period + 1):
        adx.append(strength_indicators.average_directional_index(directional_index[i:i+period], moving_average_model))
    return adx


def average_directional_index_rating(average_directional_index: list[float], period: int) -> list[float]:
    """
    Calculates the average directional index rating for a list of average directional indexes. The period is used to
    determine which past index to use to calculate the rating, Welles suggest 14 days.
    :param average_directional_index: List of average directional indexes
    :param period: Period to use
    :return: Returns a list of average directional index ratings as floats
    """
    length = len(average_directional_index)
    if length < period:
        raise Exception(f'Length of ({average_directional_index}) needs to be at least equal to period ({period})')
    adxr = []
    for i in range(period, length + 1):
        adxr.append(strength_indicators.average_directional_index_rating(average_directional_index[i-1], average_directional_index[i-period]))
    return adxr