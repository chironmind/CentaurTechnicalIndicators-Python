from ..Single import support_resistance_indicators


def fibonacci_retracement(prices: list[float]) -> list[tuple[float, float, float, float, float, float, float]]:
    """
    Calculates the Fibonacci retracement for a list of prices
    :param prices: List of prices
    :return:
    """
    fr = []
    for price in prices:
        fr.append(support_resistance_indicators.fibonacci_retracement(price))
    return fr


def pivot_points(highs: list[float], lows: list[float], close: list[float]) -> list[tuple[float, float, float, float, float]]:
    """
    Calculates the pivot point, primary and secondary support and resistance levels
    :param highs: List of high prices
    :param lows: List of low prices
    :param close: List of closing prices
    :return: Returns a list of tuple of floats in the following order pivot point, primary support, primary resistance,
     secondary support, secondary resistance
    """
    length = len(highs)
    if length != len(lows) or length != len(close):
        raise Exception(f'Length of highs ({length}), lows ({len(lows)}), and close ({len(close)}) do not match')
    pp = []
    for i in range(length):
        pp.append(support_resistance_indicators.pivot_points(highs[i], lows[i], close[i]))
    return pp
