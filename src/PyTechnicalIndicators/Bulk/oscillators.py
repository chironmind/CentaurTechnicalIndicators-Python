from ..Single import oscillators


def money_flow_index(typical_prices: list[float], volume: list[int]) -> list[float]:
    """
    Calculates the money flow index from the typical price and volume, it uses a period of 14 to make the calculations.
    To choose a different period use the personalised_money_flow_index function
    :param typical_prices: list of typical prices
    :param volume: list of volumes
    :return: Returns a list of money flow index
    """
    return personalised_money_flow_index(typical_prices, volume, 14)


def personalised_money_flow_index(typical_prices: list[float], volume: list[int], period: int) -> list[float]:
    """
    Calculates the money flow index from the typical price and volume for a given period.
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :param period: Period of time
    :return: Returns a list of money flow index
    """
    len_typical_prices = len(typical_prices)
    if len_typical_prices < period or len(volume) < period:
        raise Exception(f'typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be at least {period} periods in length')
    if len_typical_prices != len(volume):
        raise Exception(f"typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be of same length")

    money_flow_index_list = []
    for i in range(len_typical_prices - period + 1):
        money_flow_index_list.append(oscillators.personalised_money_flow_index(typical_prices[i:i+period], volume[i:i+period]))
    return money_flow_index_list


def chaikin_oscillator(high: list[float], low: list[float], close: list[float], volume: list[float]) -> list[float]:
    """
    Calculates the Chaikin Oscillator
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param volume: List of traded volume
    :return: Returns the Chaikin Oscillators as a list of floats
    """
    length = len(high)
    if length != len(low) or length != len(close) or length != len(volume):
        raise Exception(
            f'length of lists need to match. high ({length}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})')
    if length < 10:
        raise Exception('The Chaikin Oscillator expects there to be a maximum of 10 periods, for a personalised version use personalised_chaikin_oscillator')
    return personalised_chaikin_oscillator(high, low, close, volume, 3, 10)


def personalised_chaikin_oscillator(high: list[float], low: list[float], close: list[float], volume: list[float], short_period: int, long_period: int, moving_average: str = 'ma') -> list[float]:
    """
    A personalised verion of the Chaikin Oscillator, allows the caller to choose the long and short period, rather than
    having it set to 3 and 10 periods. The long period will be assumed to be the length of the lists provided. The function
    also allows for the caller to choose the moving average model
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param volume: List of traded volume
    :param short_period: Number of periods for the short period
    :param long_period: Number of period for the long period
    :param moving_average: (Optional)  Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the Chaikin Oscillators as a list of float
    """
    length = len(high)
    if length != len(low) or length != len(close) or length != len(volume):
        raise Exception(
            f'length of lists need to match. high ({length}), low ({len(low)}), close ({len(close)}), volume ({len(volume)})')
    if short_period >= length:
        raise Exception(f'short_period ({short_period}) needs to be smaller than the length of lists ({length})')
    if long_period > length:
        raise Exception(f'long_period ({long_period}) needs to be less or equal to length of lists ({length})')
    if short_period >= long_period:
        raise Exception(f'long_period ({long_period}) needs to be longer than short_period ({short_period})')
    chaikin_oscillator_list = []
    for i in range(length-long_period+1):
        j = i+long_period
        chaikin_oscillator_list.append(oscillators.personalised_chaikin_oscillator(high[i:j], low[i:j], close[i:j], volume[i:j], short_period, moving_average))
    return chaikin_oscillator_list


def stochastic_oscillator(close_prices: list[float]) -> list[float]:
    """
    Calculates the SO from a list of closing prices
    :param close_prices: List of closing prices
    :return: Returns a list of SO
    """
    if len(close_prices) < 14:
        raise Exception(f'14 periods are needed to calculate RSI {len(close_prices)} have been provided')
    for i in range(14, len(close_prices)):
        return personalised_stochastic_oscillator(close_prices, 14)


def personalised_stochastic_oscillator(close_prices: list[float], period: int) -> list[float]:
    """
    Calculates a personalised SO

    The normal period that the SO uses is 14 periods, this functions allows for any period to be used
    :param close_prices: list of close prices
    :param period: Number of periods for which the moving average should be calculated for
    :return: Returns a list of personalised SO
    """
    if len(close_prices) < period:
        raise Exception(f'Submitted prices needs to be greater than submitted period of {period}')
    so = []
    for i in range(period, len(close_prices)+1):
        so.append(oscillators.personalised_stochastic_oscillator(close_prices[i-period:i]))
    return so


def fast_stochastic(stochastic_oscillators: list[float], period: int, ma_model: str = 'ma') -> list[float]:
    """
    Calculates the fast stochastics from a list of stochastic oscillators for a given period
    :param stochastic_oscillators: List of closing prices
    :param period: Period to calculate the fast stochastic
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the fast stochastic as a tuple of floats
    """
    length = len(stochastic_oscillators)
    if length < period:
        raise Exception(f'Period ({period}) needs to be at least equal to length of stochastic_oscillators ({length})')
    fast_stochastics = []
    for i in range(period, length+1):
        fast_stochastics.append(oscillators.fast_stochastic(stochastic_oscillators[i - period:i], ma_model))
    return fast_stochastics


def slow_stochastic(fast_stochastic: list[float], period: int, ma_model: str = 'ma') -> list[float]:
    """
    Calculates the slow stochastics from a list of fast stochastics for a given period
    :param fast_stochastic: List of fast stochastics (%D)
    :param period: Period used to calculate the MA of the fast stochastic
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the fast stochastic as a tuple of floats
    """
    length = len(fast_stochastic)
    if length < period:
        raise Exception(f'Period ({period}) needs to be at least equal to length of stochastic_oscillators ({length})')
    slow_stochastics = []
    for i in range(period, length+1):
        slow_stochastics.append(oscillators.slow_stochastic(fast_stochastic[i - period:i], ma_model))
    return slow_stochastics


def slow_stochastic_ds(slow_stochastic: list[float], period: int, ma_model: str = 'ma') -> list[float]:
    """
    Calculates the %DS-Slow for the slow stochastic for a given period
    :param slow_stochastic: List of slow stochastics (%D-Slow)
    :param period: Period used to calculate the MA of the %DS-Slow
    :param ma_model: (Optional) Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :return: Returns the fast stochastic as a tuple of floats
    """
    length = len(slow_stochastic)
    if length < period:
        raise Exception(f'Period ({period}) needs to be at least equal to length of stochastic_oscillators ({length})')
    slow_stochastics_ds = []
    for i in range(period, length+1):
        slow_stochastics_ds.append(oscillators.slow_stochastic_ds(slow_stochastic[i - period:i], ma_model))
    return slow_stochastics_ds


def williams_percent_r(high: list[float], low: list[float], close: list[float], period: int) -> list[float]:
    """
    Calculate the Williams %R from a list of highs, lows, and closing prices.
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param period: Period used to calculate Williams %R
    :return: Returns the Williams %R as a list of floats
    """
    length = len(high)
    if length != len(low) or length != len(close):
        raise Exception(f'length of lists need to match. high ({length}), low ({len(low)}), close ({len(close)})')
    if length < period:
        raise Exception(f'length of lists ({length}) needs to be smaller or equal to the period ({period})')

    williams_r = []
    for i in range(len(close)-period+1):
        j = i + period
        williams_r.append(oscillators.williams_percent_r(max(high[i:j]), min(low[i:j]), close[j-1]))
    return williams_r
