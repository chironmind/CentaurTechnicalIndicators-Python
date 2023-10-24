import statistics

from . import moving_averages


# TODO: PMA and McGinley dynamic
def bollinger_bands(typical_prices: list[float], ma_model: str = 'ma', stddev_multiplier: int = 2) -> tuple[float, float]:
    """
    Calculates the Bollinger bands from a list of typical prices and returns a tuple with for the upper and lower band

    The function allows you to choose the model, period, and multiplier to calculate the Bollinger Bands.
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
    :return: Returns a tuple where the first item is the lower Bollinger Band and the second item is the upper Bollinger Band
    """

    if len(typical_prices) < 1:
        raise Exception(f'There needs to be a price to do a bollinger band')
    if ma_model in moving_averages.ma:
        ma = moving_averages.moving_average(typical_prices)
    elif ma_model in moving_averages.sma:
        ma = moving_averages.smoothed_moving_average(typical_prices)
    elif ma_model in moving_averages.ema:
        ma = moving_averages.exponential_moving_average(typical_prices)
    else:
        ma = moving_averages.moving_average(typical_prices)
    stddev = statistics.stdev(typical_prices)
    upper_band = ma + (stddev_multiplier*stddev)
    lower_band = ma - (stddev_multiplier*stddev)
    return lower_band, upper_band


def ichimoku_cloud(highs: list[float], lows: list[float], close: list[float], conversion_period: int = 9, base_period: int = 26, span_b_period: int = 52) -> tuple[float, float, float, float, float]:
    """
    Calculates Ichimoku cloud from a list of highs and lows and returns a tuple with Senkou Span A and Span B as lists

    The personalised ichimoku cloud allows for fine tuning of ichimoku cloud but change the conversion period, based period and span b period.
    The default conversion period is 9, the default base period is 26, the default Span B period is 52, adjusting these
    to fit the current market will yield a more precise cloud
    :param highs: List of highs
    :param lows: List of lows
    :param close: List of closing prices
    :param conversion_period:
    :param base_period:
    :param span_b_period:
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns the Senkou Span A and Span B, Base Line, Conversion Line, and the Lagged close price as a tuple with a list of floats for each
    """
    highest_period = max(conversion_period, base_period, span_b_period)
    if len(highs) < highest_period:
        raise Exception('Submitted price shorter than submitted periods')
    conversion_line = (max(highs[-conversion_period:]) + min(lows[-conversion_period:])) / 2
    base_line = (max(highs[-base_period:]) + min(lows[-base_period:])) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (max(highs[-span_b_period:]) + min(lows[-span_b_period:])) / 2
    return leading_span_a, leading_span_b, base_line, conversion_line, close[-base_period]
