from ..Single import candle_indicators


def bollinger_bands(typical_price: list[float], period: int = 20, ma_model: str = 'ma', stddev_multiplier: int = 2, fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple with a list for the upper and lower band

    The function allows you to choose the model, period, and multiplier to calculate the Bollinger Bands.
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
    length = len(typical_price)
    if length < period:
        raise Exception(f'Prices ({length}) needs to be equal or greater than ({period})')
    bbands = []
    if fill_empty:
        for i in range(period):
            bbands.append((fill_value, fill_value))

    for i in range(period, len(typical_price)+1):
        bbands.append(candle_indicators.bollinger_bands(typical_price[i-period:i], ma_model, stddev_multiplier))
    return bbands


def ichimoku_cloud(highs: list[float], lows: list[float], close: list[float], conversion_period: int = 9, base_period: int = 26, span_b_period: int = 52, fill_empty: bool = False, fill_value: any = None) -> list[tuple[float, float]]:
    """
    Calculates Ichimoku cloud from a list of highs and lows and returns a tuple with Senkou Span A and Span B as lists

    The function allows for fine-tuning of ichimoku cloud but change the conversion period, based period and span b period.
    The default conversion period is 9, the default base period is 26, the default Span B period is 52, adjusting these
    to fit the current market will yield a more precise cloud
    :param highs: List of highs
    :param lows: List of lows
    :param close: List of closing prices
    :param conversion_period: int -
    :param base_period:
    :param span_b_period:
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list with Senkou Span A and Span B as a tuple
    """
    highest_period = max(conversion_period, base_period, span_b_period)
    length = len(highs)
    if length != len(lows) or length != len(close):
        raise Exception(f'Length of highs ({length}), lows ({len(lows)}), and close ({len(close)}) need to match')
    if length < highest_period:
        raise Exception(f'Prices ({length}) needs to be equal or greater that the highest period ({highest_period})')
    senkou_span = []
    if fill_empty:
        for i in range(highest_period):
            senkou_span.append((fill_value, fill_value))

    for i in range(highest_period, length+1):
        senkou_span.append(candle_indicators.ichimoku_cloud(highs[i-highest_period:i], lows[i-highest_period:i], close[i-highest_period:i], conversion_period, base_period, span_b_period))
    return senkou_span
