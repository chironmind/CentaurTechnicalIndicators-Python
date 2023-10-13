from ..Single import candle_indicators


def bollinger_bands(typical_price: list[float], fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple with a list for the upper and lower band
    :param typical_price: list[float] - list of typical prices
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of tuples, where the first instance in the tuple is the lower band and the second instance is the upper band
    """
    if len(typical_price) < 20:
        raise Exception('Submitted price is too short, needs to be at least 20 periods long')

    bbands = []

    # TODO: Figure out if the fill empty is really needed
    if fill_empty:
        for i in range(20):
            bbands.append((fill_value, fill_value))

    for i in range(20, len(typical_price)+1):
        bbands.append(candle_indicators.bollinger_bands(typical_price[i-20:i]))
    return bbands


def ichimoku_cloud(highs: list[float], lows: list[float], fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates Ichimoku cloud from a list of highs and lows and returns a tuple with Senkou Span A and Span B as lists
    :param highs: list[floats] - list of highs
    :param lows: list[floats]- list of lows
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns the Senkou Span A and Span B as a list of tuples
    """
    if len(highs) < 52 or len(lows) < 52:
        raise Exception('Submitted price is too short, needs to be at least 52 periods long')

    icloud = []

    if fill_empty:
        for i in range(52):
            icloud.append((fill_value, fill_value))

    for i in range(52, len(highs)+1):
        icloud.append(candle_indicators.ichimoku_cloud(highs[i-52:i], lows[i-52:i]))
    return icloud


# TODO: Refactor to use single
def personalised_bollinger_bands(typical_price: list[float], period: int = 20, ma_model: str = 'ma', stddev_multiplier: int = 2, fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple with a list for the upper and lower band

    The Personalised Bollinger Bands allows you to choose the model, period, and multiplier to calculate the Bollinger Bands.
    The default model that the traditional Bollinger Bands use is a simple moving average, but someone may want to change
    the model to fit their trading strategy. The same goes with the period, Bollinger Bands use a period of 20 to represent
    the moving average of a month, however this makes the assumption that you're looking at daily data, but someone may
    be looking at hourly data, or at a market that is traded 7 days a week (crypto) as opposed to 5 days a week. The same goes
    with the multiplier, the default is that the bands should be put at a distance of 2x the standard deviation away from
    the moving average line, but someone may want a tighter or looser band.
    :param typical_price: list[float] - list of typical prices
    :param period: int - timeframe for which the variance needs to be calculated for. For example period=20 would calculate the variance for 20 periods (default 20)
    :param ma_model: str - the name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :param stddev_multiplier: int - How much to multiply the standard deviation by to get the upper or lower band. Defaults to 2.
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of tuples, the first one for the lower Bollinger Band and the second for the upper Bollinger Band
    """

    if len(typical_price) < period:
        raise Exception(f'Submitted price is shorter than submitted period of {period}')

    bbands = []

    if fill_empty:
        for i in range(period):
            bbands.append((fill_value, fill_value))

    for i in range(period, len(typical_price)+1):
        bbands.append(candle_indicators.personalised_bollinger_bands(typical_price[i-period:i], ma_model, stddev_multiplier))
    return bbands


def personalised_ichimoku_cloud(highs: list[float], lows: list[float], conversion_period: int = 9, base_period: int = 26, span_b_period: int = 52, fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates Ichimoku cloud from a list of highs and lows and returns a tuple with Senkou Span A and Span B as lists

    The personalised ichimoku cloud allows for fine tuning of ichimoku cloud but change the conversion period, based period and span b period.
    The default conversion period is 9, the default base period is 26, the default Span B period is 52, adjusting these
    to fit the current market will yield a more precise cloud
    :param highs: list[float] - list of highs
    :param lows: list[float] - list of lows
    :param conversion_period: int -
    :param base_period:
    :param span_b_period:
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list with Senkou Span A and Span B as a tuple
    """

    highest_period = max(conversion_period, base_period, span_b_period)
    if len(highs) < highest_period:
        raise Exception('Submitted price shorter than submitted periods')

    senkou_span = []

    if fill_empty:
        for i in range(highest_period):
            senkou_span.append((fill_value, fill_value))

    for i in range(highest_period, len(highs)+1):
        senkou_span.append(candle_indicators.personalised_ichimoku_cloud(highs[i-highest_period:i], lows[i-highest_period:i], conversion_period, base_period, span_b_period))
    return senkou_span
