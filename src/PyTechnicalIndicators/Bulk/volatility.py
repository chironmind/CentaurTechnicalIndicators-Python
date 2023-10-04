from src.PyTechnicalIndicators.Single import volatility


def average_true_range(high: list[float], low: list[float], close: list[float], period: int) -> list[float]:
    """
    Calculates the average true range from a list of highs, lows, and closing prices for a given period
    :param high: List of highs
    :param low: List of lows
    :param close: List of closing prices
    :param period: Period to calculate the average true range
    :return: Returns the average true range as a float
    """
    length = len(high)
    if length != len(low) or length != len(close):
        raise Exception(f'lengths needs to match, high: {length}, low: {len(low)}, close {len(close)}')
    if length < period:
        raise Exception(f'period {period} needs to match list length, high: {length}, low: {len(low)}, close {len(close)}')

    atr_list = []
    for i in range(length - period + 1):
        if not atr_list:
            atr_list.append(volatility.average_true_range_initial(high[i:i + period], low[i:i + period], close[i:i + period]))
        else:
            atr_list.append(volatility.average_true_range(high[i + period - 1], low[i + period - 1], close[i + period - 1], atr_list[-1], period))
    return atr_list


def ulcer_index(close_prices: list[float], period: int) -> list[float]:
    """
    Calculates the ulcer index from a list of closing prices. The period determines how many period to calculate each
    ulcer index for
    :param close_prices: List of closing prices
    :param period: ow many period to calculate each ulcer index for
    :return: Returns a list of ulcer index
    """
    if period > len(close_prices):
        raise Exception(f'length of close_prices ({close_prices}) needs to be greater or equal to the period ({period})')
    ulcer_index_list = []
    for i in range(len(close_prices)-period+1):
        ulcer_index_list.append(volatility.ulcer_index(close_prices[i:i+period]))
    return ulcer_index_list


# From https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
def volatility_index(high: list[float], low: list[float], close: list[float], period: int) -> list[float]:
    """
    Calculates the volatility index
    :param high: List of highs
    :param low: List of lows
    :param close: List of previous closing prices
    :param period: Period observed
    :return: Returns a list of volatility index
    """
    length = len(high)
    if length != len(low) or length != len(close):
        raise Exception(f'lengths needs to match, high: {length}, low: {len(low)}, close {len(close)}')
    vi = []
    for i in range(length):
        if not vi:
            vi.append(volatility.volatility_index(high[i], low[i], close[i], period, 0))
        else:
            vi.append(volatility.volatility_index(high[i], low[i], close[i], period, vi[-1]))
    return vi


# Doesn't make sense to have a single version of this, it should just have the functions called individually
def volatility_system(high: list[float], low: list[float], close: list[float], period: int = 7, average_true_range_constant: float = 3.0) -> list[tuple[float, float, float, float]]:
    """
    Calculates the Welles volatility system from here https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of previous closing prices, these need to have happened t-1 the input highs and lows
    :param period: period to be observed
    :return: Returns a list of the significant close, average range constant, stop and reverse point, and average true range as a tuple
    """
    length = len(high)
    if length != len(low) and length != len(close):
        raise Exception(f'Lengths of high ({length}), low ({len(low)}) and close ({len(close)}) need to match')
    if length < period + 1:
        raise Exception(
            f'The period ({period}) needs to be one longer than the lengths of high ({length}), low ({len(low)}) and close ({len(close)})')

    vs = []
    for i in range(length-period):
        if not vs:
            vs.append(volatility.volatility_system(high[i:i+period+1], low[i:i+period+1], close[i:i+period+1], period, average_true_range_constant))
        else:
            vs.append(volatility.volatility_system(high[i+1:i+period+1], low[i+1:i+period+1], close[i+1:i+period+1], period, average_true_range_constant, vs[-1]))
    return vs
