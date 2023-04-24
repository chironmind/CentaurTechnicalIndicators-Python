from typing import Tuple


def fibonacci_retracement(price: float) -> tuple[float, float, float, float, float, float, float]:
    """
    Calculates the Fibonacci retracement for a given price
    :param price: Price to calculate the Fibonacci retracement
    :return: Returns a tuple of floats that represent the following Fibonacci retracements
    (0%, 23.6%, 38.2%, 50%, 61.8%, 76.4%, 100%)
    """
    return price, price * 1.236, price * 1.382, price * 1.5, price * 1.618, price * 1.764, price * 2
