import statistics
from .moving_averages import moving_average, smoothed_moving_average, exponential_moving_average


def bollinger_bands(typical_prices):
    if len(typical_prices) != 20:
        raise Exception('Submitted price needs to be at least 20 periods long')

    ma = moving_average(typical_prices)
    stddev = statistics.stdev(typical_prices)

    upper_band = ma + 2 * stddev
    lower_band = ma - 2 * stddev

    return upper_band, lower_band


def ichimoku_cloud(highs, lows):
    if len(highs) != 52:
        raise Exception('Submitted price needs to be at least 52 periods long')

    # TODO: this doesn't work, needs to be looped or something
    conversion_line = (max(highs) + min(lows)) / 2
    base_line = (max(highs) + min(lows)) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (max(highs) + min(lows)) / 2

    return leading_span_a, leading_span_b


def personalised_bollinger_bands(typical_price, ma_model='ma', stddev_multiplier=2):
    if len(typical_price) < 1:
        raise Exception(f'There needs to be a price to do a bollinger band')

    ma = ['ma', 'moving average', 'moving_average']
    sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
    ema = ['ema', 'exponential moving average', 'exponential_moving_average']

    if ma_model in ma:
        ma = moving_average(typical_price)
    elif ma_model in sma:
        ma = smoothed_moving_average(typical_price)
    elif ma_model in ema:
        ma = exponential_moving_average(typical_price)
    else:
        ma = moving_average(typical_price)

    stddev = statistics.stdev(typical_price)

    upper_band = ma + (stddev_multiplier*stddev)
    lower_band = ma - (stddev_multiplier*stddev)

    return upper_band, lower_band


def personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period):
    highest_period = max(conversion_period, base_period, span_b_period)
    if len(highs) < highest_period:
        raise Exception('Submitted price shorter than submitted periods')

    # TODO: this doesn't work, needs to be looped or something
    conversion_line = (max(highs[-conversion_period:]) + min(lows[-conversion_period:])) / 2
    base_line = (max(highs[-base_period:]) + min(lows[-base_period:])) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (max(highs[-span_b_period:]) + min(lows[-span_b_period:])) / 2

    return leading_span_a, leading_span_b
