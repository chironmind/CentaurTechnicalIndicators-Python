import statistics
from .moving_averages import moving_average, smoothed_moving_average, exponential_moving_average


def bollinger_bands(typical_prices: list[float]) -> tuple[float, float]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple for the upper and lower band
    :param typical_prices: list[float] - list of typical prices
    :return: Returns a tuple the first item is the lower Bollinger Band and the second item is the upper Bollinger Band
    """
    if len(typical_prices) != 20:
        raise Exception('Submitted price needs to be at least 20 periods long')

    ma = moving_average(typical_prices)
    stddev = statistics.stdev(typical_prices)

    upper_band = ma + (2 * stddev)
    lower_band = ma - (2 * stddev)

    return lower_band, upper_band


def ichimoku_cloud(highs: list[float], lows: list[float]) -> tuple[float, float]:
    """
    Calculates Ichimoku cloud from a list of highs and lows and returns a tuple with Senkou Span A and Span B as lists
    :param highs: list[floats] - list of highs
    :param lows: list[floats]- list of lows
    :return: Returns a tuple with the Senkou Span A as the first itme and the Senkou Span B as the second item
    """
    if len(highs) != 52:
        raise Exception('Submitted price needs to be at least 52 periods long')

    # TODO: this doesn't work, needs to be looped or something
    conversion_line = (max(highs) + min(lows)) / 2
    base_line = (max(highs) + min(lows)) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (max(highs) + min(lows)) / 2

    return leading_span_a, leading_span_b


def personalised_bollinger_bands(typical_prices: list[float], ma_model: str = 'ma', stddev_multiplier: int = 2) -> tuple[float, float]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple with for the upper and lower band

    The Personalised Bollinger Bands allows you to choose the model, period, and multiplier to calculate the Bollinger Bands.
    The default model that the traditional Bollinger Bands use is a simple moving average, but someone may want to change
    the model to fit their trading strategy. The same goes with the period, Bollinger Bands use a period of 20 to represent
    the moving average of a month, however this makes the assumption that you're looking at daily data, but someone may
    be looking at hourly data, or at a market that is traded 7 days a week (crypto) as opposed to 5 days a week. The same goes
    with the multiplier, the default is that the bands should be put at a distance of 2x the standard deviation away from
    the moving average line, but someone may want a tighter or looser band.
    :param typical_prices: list[float] - list of typical prices
    :param ma_model: str - the name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :param stddev_multiplier: int - How much to multiply the standard deviation by to get the upper or lower band. Defaults to 2.
    :return: Returns a tuple where the first item is the upper Bollinger Band and the second item is the lower Bollinger Band
    """

    if len(typical_prices) < 1:
        raise Exception(f'There needs to be a price to do a bollinger band')

    ma = ['ma', 'moving average', 'moving_average']
    sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
    ema = ['ema', 'exponential moving average', 'exponential_moving_average']

    if ma_model in ma:
        ma = moving_average(typical_prices)
    elif ma_model in sma:
        ma = smoothed_moving_average(typical_prices)
    elif ma_model in ema:
        ma = exponential_moving_average(typical_prices)
    else:
        ma = moving_average(typical_prices)

    stddev = statistics.stdev(typical_prices)

    upper_band = ma + (stddev_multiplier*stddev)
    lower_band = ma - (stddev_multiplier*stddev)

    return upper_band, lower_band


def personalised_ichimoku_cloud(highs: list[float], lows: list[float], conversion_period: int, base_period: int, span_b_period: int) -> tuple[float, float]:
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
    :return: Returns the Senkou Span A and Span B as a tuple with a list of floats for each
    """
    # TODO: needs defaults
    highest_period = max(conversion_period, base_period, span_b_period)
    if len(highs) < highest_period:
        raise Exception('Submitted price shorter than submitted periods')

    # TODO: this doesn't work, needs to be looped or something
    conversion_line = (max(highs[-conversion_period:]) + min(lows[-conversion_period:])) / 2
    base_line = (max(highs[-base_period:]) + min(lows[-base_period:])) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (max(highs[-span_b_period:]) + min(lows[-span_b_period:])) / 2

    return leading_span_a, leading_span_b
