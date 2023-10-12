from typing import Tuple


# TODO: Bulk for the below
def fibonacci_retracement(price: float) -> tuple[float, float, float, float, float, float, float]:
    """
    Calculates the Fibonacci retracement for a given price
    :param price: Price to calculate the Fibonacci retracement
    :return: Returns a tuple of floats that represent the following Fibonacci retracements
    (0%, 23.6%, 38.2%, 50%, 61.8%, 76.4%, 100%)
    """
    return price, price * 1.236, price * 1.382, price * 1.5, price * 1.618, price * 1.764, price * 2


def pivot_points(high: float, low: float, close: float) -> tuple[float, float, float, float, float]:
    """
    Calculates the pivot point, primary and secondary support and resistance levels
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :return: Returns a tuple of floats in the following order pivot point, primary support, primary resistance,
     secondary support, secondary resistance
    """
    pivot = (high + low + close) / 3
    support_1 = (2 * pivot) - high
    resistance_1 = (2 * pivot) - low
    support_2 = pivot - (resistance_1 - support_1)
    resistance_2 = (pivot - support_1) + resistance_1
    return pivot, support_1, resistance_1, support_2, resistance_2
