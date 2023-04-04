from src.PyTechnicalIndicators.Single.volatility import average_true_range as atr


def average_true_range(high: list[float], low: list[float], close: list[float], period: int) -> list[float]:
    """
    Calculates the average true range from a list of highs, lows, and closing prices for a given period
    :param high: List of highs
    :param low: List of lows
    :param close: List of closing prices
    :param period: Period to calculate the average true range
    :return: Returns the average true range as a float
    """

    if len(high) != len(low) or len(high) != len(close):
        raise Exception(f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}')

    if len(high) < period:
        raise Exception(f'period {period} needs to match list length, high: {len(high)}, low: {len(low)}, close {len(close)}')

    atr_list = []

    for i in range(len(high) - period + 1):
        if atr_list:
            atr_list.append(atr(high[i:i+period], low[i:i+period], close[i:i+period], atr_list[-1]))
        else:
            atr_list.append(atr(high[i:i + period], low[i:i + period], close[i:i + period], 0))

    return atr_list

