from .strength_indicators import accumulation_distribution_indicator
from . import moving_averages as mam


def money_flow_index(typical_prices: list[float], volume: list[int]) -> float:
    """
    Calculates the money flow index from the typical price and volume

    The length of typical prices and volume has to be 14 periods in length, if a custom period is wanted,
    personalised_money_flow_index should be used
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :return: Returns the money flow index as a float
    """

    if len(typical_prices) != 14 or len(volume) != 14:
        raise Exception(f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be 14 periods in length")
    return personalised_money_flow_index(typical_prices, volume)


def personalised_money_flow_index(typical_prices: list[float], volume: list[int]) -> float:
    """
    Calculates the money flow index from the typical price and volume

    There are no limitation on the period, the period that will be choosen will be that of the length of the lists
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :return: Returns the money flow index as a float
    """
    typical_price_len = len(typical_prices)

    if typical_price_len != len(volume):
        raise Exception(f"typical_prices ({typical_price_len}) and volume({len(volume)})  need to be of same length")

    raw_money_flow = []

    for i in range(typical_price_len):
        raw_money_flow.append(typical_prices[i] * volume[i])

    positive_money_flow = 0
    negative_money_flow = 0

    for j in range(1, len(raw_money_flow)):
        if raw_money_flow[j] > raw_money_flow[j-1]:
            positive_money_flow += raw_money_flow[j]
        elif raw_money_flow[j] < raw_money_flow[j-1]:
            negative_money_flow += raw_money_flow[j]
        else:
            # TODO: Check if this is correct behaviour
            continue

    if negative_money_flow == 0:
        money_flow_ratio = 100
    else:
        money_flow_ratio = positive_money_flow / negative_money_flow
    mfi = 100 - (100 / (1 + money_flow_ratio))

    return mfi


def chaikin_oscillator(high: list[float], low: list[float], close: list[float], volume: list[float]) -> float:
    """
    Calculates the Chaikin Oscillator
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param volume: List of traded volume
    :return: Returns the Chaikin Oscillator as a float
    """
    if len(high) != 10:
        raise Exception('The Chaikin Oscillator expects there to be a maximum of 10 periods, , for a personalised version use personalised_chaikin_oscillator')
    return personalised_chaikin_oscillator(high, low, close, volume, 3)


# TODO: Add PMA and McGinley to accepted MA models
def personalised_chaikin_oscillator(high: list[float], low: list[float], close: list[float], volume: list[float], short_period: int, ma_model: str = 'ma') -> float:
    """
    A personalised verion of the Chaikin Oscillator, allows the caller to choose the long and short period, rather than
    having it set to 3 and 10 periods. The long period will be assumed to be the length of the lists provided. The function
    also allows for the caller to choose the moving average model
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param volume: List of traded volume
    :param short_period: Number of periods for the short period
    :param ma_model: (Optional)  Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the Chaikin Oscillator as a float
    """
    length = len(high)
    if length != len(low) or length != len(close) or length != len(volume):
        raise Exception(f'length of lists need to match. high ({length}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})')
    if short_period >= length:
        raise Exception(f'short_period ({short_period}) needs to be smaller than the length of lists ({length})')

    accumulation_distribution = accumulation_distribution_indicator(high[0], low[0], close[0], volume[0])
    short_period_accumulation_distribution = []
    long_period_accumulation_distribution = [accumulation_distribution]

    for i in range(1, length):
        accumulation_distribution = accumulation_distribution_indicator(high[i], low[i], close[i], volume[i], long_period_accumulation_distribution[-1])
        long_period_accumulation_distribution.append(accumulation_distribution)
        if i >= length - short_period:
            short_period_accumulation_distribution.append(accumulation_distribution)

    if ma_model in mam.ma:
        short_period_ma = mam.moving_average(short_period_accumulation_distribution)
        long_period_ma = mam.moving_average(long_period_accumulation_distribution)
    elif ma_model in mam.sma:
        short_period_ma = mam.smoothed_moving_average(short_period_accumulation_distribution)
        long_period_ma = mam.smoothed_moving_average(long_period_accumulation_distribution)
    elif ma_model in mam.ema:
        short_period_ma = mam.exponential_moving_average(short_period_accumulation_distribution)
        long_period_ma = mam.exponential_moving_average(long_period_accumulation_distribution)
    else:
        raise Exception(f'{ma_model} is not an accepted MA model, please use either {mam.ma}, {mam.sma}, or {mam.ema}')

    return short_period_ma - long_period_ma


def stochastic_oscillator(close_prices: list[float]) -> float:
    """
    Calculates the SO for a list of closing prices
    :param close_prices: list of closing prices
    :return: Returns the SO as a float
    """
    if len(close_prices) != 14:
        raise Exception(f'14 periods are needed to calculate SO, {len(close_prices)} have been provided')
    return personalised_stochastic_oscillator(close_prices)


def personalised_stochastic_oscillator(close_prices: list[float]) -> float:
    """
    Calculates a personalised version of the SO

    Main difference is that in normal SO the length of the input list has to be 14, however this function accepts anything
    :param close_prices: list of close prices
    :return: Returns the SO as a float
    """
    if len(close_prices) < 1:
        raise Exception(f'Submitted prices needs to be greater than 0')
    lowest_closing = min(close_prices)
    highest_closing = max(close_prices)
    return ((close_prices[-1] - lowest_closing) / (highest_closing - lowest_closing)) * 100


def fast_stochastic(stochastic_oscillators: list[float], ma_model: str = 'ma') -> float:
    """
    Calculates the fast stochastic from the stochastic oscillator, the length of the list will determine the period.
    :param stochastic_oscillators: List of stochastic oscillators
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the fast stochastic as a float
    """
    if ma_model in mam.ma:
        return mam.moving_average(stochastic_oscillators)
    elif ma_model in mam.sma:
        return mam.smoothed_moving_average(stochastic_oscillators)
    elif ma_model in mam.ema:
        return mam.exponential_moving_average(stochastic_oscillators)
    else:
        raise Exception(f'{ma_model} is not an accepted MA model, please use either {mam.ma}, {mam.sma}, or {mam.ema}')


def slow_stochastic(fast_stochastic: list[float], ma_model: str = 'ma') -> float:
    """
    Calculates the %D-Slow for the slow stochastic
    :param fast_stochastic: List of fast stochastic %D
    :param ma_model: (Optional) Name of the moving average model that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the %D-Slow as a float
    """
    if ma_model in mam.ma:
        return mam.moving_average(fast_stochastic)
    elif ma_model in mam.sma:
        return mam.smoothed_moving_average(fast_stochastic)
    elif ma_model in mam.ema:
        return mam.exponential_moving_average(fast_stochastic)
    else:
        raise Exception(f'{ma_model} is not an accepted MA model, please use either {mam.ma}, {mam.sma}, or {mam.ema}')


def slow_stochastic_ds(slow_stochastic: list[float], ma_model: str = 'ma') -> float:
    """
    Calculates the %DS-Slow for the slow stochastic
    :param slow_stochastic: List of %D-Slow
    :param ma_model: (Optional) Name of the moving average model that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the %DS-Slow as a float
    """
    if ma_model in mam.ma:
        return mam.moving_average(slow_stochastic)
    elif ma_model in mam.sma:
        return mam.smoothed_moving_average(slow_stochastic)
    elif ma_model in mam.ema:
        return mam.exponential_moving_average(slow_stochastic)
    else:
        raise Exception(f'{ma_model} is not an accepted MA model, please use either {mam.ma}, {mam.sma}, or {mam.ema}')


def williams_percent_r(high: float, low: float, close: float) -> float:
    """
    Calculate the Williams %R for a maximum high, minimum low, and closing price
    :param high: Highest high for the period studied
    :param low: Lowest low for the period studied
    :param close: Closing price for the period
    :return: Returns the Williams %R as a float.
    """
    return ((high - close) * -100) / (high - low)
