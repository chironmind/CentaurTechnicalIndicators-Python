import statistics
from ..Single.moving_averages import moving_average, smoothed_moving_average, exponential_moving_average


def bollinger_bands(typical_price, fill_empty=False, fill_value=None):
    if len(typical_price) < 20:
        raise Exception('Submitted price is too short, needs to be at least 20 periods long')

    upper_band = []
    lower_band = []

    if fill_empty:
        for i in range(20):
            upper_band.append(fill_value)
            lower_band.append(fill_value)

    for i in range(20, len(typical_price)):
        ma = moving_average(typical_price[i-20:i])
        stddev = statistics.stdev(typical_price[i-20:i])

        upper_band.append(ma + 2*stddev)
        lower_band.append(ma - 2*stddev)

    return upper_band, lower_band


def ichimoku_cloud(highs, lows, fill_empty=False, fill_value=None):
    if len(highs) < 52:
        raise Exception('Submitted price is too short, needs to be at least 52 periods long')

    senkou_span_a = []
    senkou_span_b = []

    if fill_empty:
        for i in range(52):
            senkou_span_a.append(fill_value)
            senkou_span_b.append(fill_value)

    for i in range(52, len(highs)):
        # TODO: this doesn't work, needs to be looped or something
        conversion_line = (max(highs[i-9:i]) + min(lows[i-9:i])) / 2
        base_line = (max(highs[i-26:i]) + min(lows[i-26:i])) / 2
        leading_span_a = (conversion_line + base_line) / 2
        leading_span_b = (max(highs[i-52:i]) + min(lows[i-52:i])) / 2
        senkou_span_a.append(leading_span_a)
        senkou_span_b.append(leading_span_b)

    return senkou_span_a, senkou_span_b


def personalised_bollinger_bands(typical_price, period, ma_model='ma', stddev_multiplier=2, fill_empty=False, fill_value=None):
    if len(typical_price) < period:
        raise Exception(f'Submitted price is shorter than submitted period of {period}')

    upper_band = []
    lower_band = []

    ma = ['ma', 'moving average', 'moving_average']
    sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
    ema = ['ema', 'exponential moving average', 'exponential_moving_average']

    if fill_empty:
        for i in range(period):
            upper_band.append(fill_value)
            lower_band.append(fill_value)

    for i in range(period, len(typical_price)):
        if ma_model in ma:
            selected_ma = moving_average(typical_price[i-period:i])
        elif ma_model in sma:
            selected_ma = smoothed_moving_average(typical_price[i - period:i])
        elif ma_model in ema:
            selected_ma = exponential_moving_average(typical_price[i - period:i])
        else:
            selected_ma = moving_average(typical_price[i - period:i])

        stddev = statistics.stdev(typical_price[i-period:i])

        upper_band.append(selected_ma + (stddev_multiplier*stddev))
        lower_band.append(selected_ma - (stddev_multiplier*stddev))

    return upper_band, lower_band


def personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period, fill_empty=False, fill_value=None):
    highest_period = max(conversion_period, base_period, span_b_period)
    if len(highs) < highest_period:
        raise Exception('Submitted price shorter than submitted periods')

    senkou_span_a = []
    senkou_span_b = []

    if fill_empty:
        for i in range(highest_period):
            senkou_span_a.append(fill_value)
            senkou_span_b.append(fill_value)

    for i in range(highest_period, len(highs)):
        # TODO: this doesn't work, needs to be looped or something
        conversion_line = (max(highs[i-conversion_period:i]) + min(lows[i-conversion_period:i])) / 2
        base_line = (max(highs[i-base_period:i]) + min(lows[i-base_period:i])) / 2
        leading_span_a = (conversion_line + base_line) / 2
        leading_span_b = (max(highs[i-span_b_period:i]) + min(lows[i-span_b_period:i])) / 2
        senkou_span_a.append(leading_span_a)
        senkou_span_b.append(leading_span_b)

    return senkou_span_a, senkou_span_b
