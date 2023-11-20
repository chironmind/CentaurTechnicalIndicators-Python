

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
