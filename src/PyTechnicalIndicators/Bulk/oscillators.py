from src.PyTechnicalIndicators.Single.oscillators import personalised_money_flow_index as mfi, personalised_chaikin_oscillator as co


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
    :return:
    """
    len_typical_prices = len(typical_prices)

    if len_typical_prices < period or len(volume) < period:
        raise Exception(f'typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be at least {period} periods in length')

    if len_typical_prices != len(volume):
        raise Exception(f"typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be of same length")

    money_flow_index_list = []

    for i in range(len_typical_prices - period + 1):
        money_flow_index_list.append(mfi(typical_prices[i:i+period], volume[i:i+period]))

    return money_flow_index_list


def chaikin_oscillator(high: list[float], low: list[float], close: list[float], volume: list[float]) -> list[float]:
    pass


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
        chaikin_oscillator_list.append(co(high[i:j], low[i:j], close[i:j], volume[i:j], short_period, moving_average))
    return chaikin_oscillator_list
