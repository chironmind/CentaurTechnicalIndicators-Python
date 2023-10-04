import math

from src.PyTechnicalIndicators.Single import other


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
    for i in range(length):
        sum_true_range += other.true_range(high[i], low[i], previous_close[i])
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
    current_true_range = other.true_range(high, low, previous_close)
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
    tr = other.true_range(high, low, close)
    vi = (((period - 1) * previous_volatility_index) + tr) / period
    return vi


# TODO: This needs kwargs
def volatility_system(high: list[float], low: list[float], close: list[float], period: int = 7, average_true_range_constant: float = 3.0, previous_volatility_system: tuple[float, float, float, float] = (0,0,0,0)) -> tuple[float, float, float, float]:
    """
    Calculates the Welles volatility system from here https://archive.org/details/newconceptsintec00wild/page/25/mode/2up
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of previous closing prices, these need to have happened t-1 the input highs and lows
    :param period: period to be observed
    :param average_true_range_constant: Constant to multiply the average true range
    :param previous_volatility_system: the previous volatility system. It is used to have more precise calculations for
        the next volatility system. If not provided it will default to ()
    :return: Returns the significant close, average range constant, and stop and reverse point as a tuple
    """
    length = len(high)
    if length != len(low) and length != len(close):
        raise Exception(f'Lengths of high ({length}), low ({len(low)}) and close ({len(close)}) need to match')

    previous_significant_close = previous_volatility_system[0]
    previous_average_true_constant = previous_volatility_system[1]
    previous_stop_and_reverse = previous_volatility_system[2]
    previous_average_true_range = previous_volatility_system[3]
    if not previous_average_true_range:
        if length < period + 1:
            raise Exception(f'The period ({period}) needs to be one longer than the lengths of high ({length}), low ({len(low)}) and close ({len(close)})')
        atr_initial = average_true_range_initial(high[-period-1:period], low[-period-1:period], close[-period-1:period])
        atr = average_true_range(high[-1], low[-1], close[-1], atr_initial, period)
    else:
        atr = average_true_range(high[-1], low[-1], close[-1], previous_average_true_range, period)
    arc = other.average_range_constant(atr, average_true_range_constant)
    sic = other.significant_close(close)
    if sic < previous_significant_close:
        sic = previous_significant_close
    if previous_stop_and_reverse and close[-1] < previous_stop_and_reverse:
        sar = close[-1] + arc
        sic = close[-1]
    else:
        sar = sic - arc
    return sic, arc, sar, atr
