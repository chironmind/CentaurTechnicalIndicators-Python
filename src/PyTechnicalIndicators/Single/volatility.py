import math

from src.PyTechnicalIndicators.Single.other import true_range


def average_true_range_initial(high: list[float], low: list[float], previous_close: list[float]) -> float:
    """
    Calculates the initial average true range from a list of highs, lows, and closing prices. This function is used when no
    previous average true range value exists. If the previous average true range is known use average_true_range
    :param high: List of high prices
    :param low: List of low prices
    :param previous_close: List of closing prices
    :return: Returns the average true range as a float
    """
    length = len(high)
    if length != len(low) or length != len(previous_close):
        raise Exception(f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(previous_close)}')
    sum_true_range = 0
    for i in range(1, length):
        sum_true_range += true_range(high[i], low[i], previous_close[i - 1])
    return sum_true_range / length


def average_true_range(high: float, low: float, previous_close: float, previous_average_true_range: float, period: int) -> float:
    """
    Calculates the average true range when the previous average true range is known. If it is not known use average_true_range_initial
    :param high: List of high prices
    :param low: List of low prices
    :param previous_close: List of closing prices
    :param previous_average_true_range: Previous average true range
    :param period: The period for which the true range is being observed
    :return: Returns the average true range as a float
    """
    current_true_range = true_range(high, low, previous_close)
    return ((previous_average_true_range * (period - 1)) + current_true_range) / period


def ulcer_index(close_prices: list[float]) -> float:
    """
    Calculates the ulcer index based on a list of close prices.

    The period and max price get determined based on the list of prices
    :param close_prices: List of closing prices
    :return: Returns the Ulcer Index as a float
    """
    squared_percentage_drawdown = [0]
    for i in range(1, len(close_prices)):
        period_high = max(close_prices[:i+1])
        percentage_drawdown = ((close_prices[i] - period_high) / period_high) * 100
        squared_percentage_drawdown.append(pow(percentage_drawdown, 2))
    squared_average = sum(squared_percentage_drawdown) / len(close_prices)
    return math.sqrt(squared_average)


def volatility_index(high: float, low: float, close: float, period: int, previous_volatility_index: float) -> float:
    """
    Calculates the volatility index
    :param high: Current high price
    :param low: Current low price
    :param close: Previous closing price
    :param period: Period observed
    :param previous_volatility_index: Previous volatility index value
    :return: Returns the volatility index as a float
    """
    tr = true_range(high, low, close)
    vi = (((period - 1) * previous_volatility_index) + tr) / period
    return vi
