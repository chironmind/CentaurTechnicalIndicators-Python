import statistics


def mean_absolute_deviation(prices: list[float]) -> float:
    """
    Calculates the mean absolute deviation for a list of prices
    :param prices: List of prices
    :return: Returns the mean absolute deviation as a float
    """
    mean = statistics.mean(prices)
    absolute_deviation = 0
    for price in prices:
        absolute_deviation += abs(price - mean)
    return absolute_deviation / len(prices)


def median_absolute_deviation(prices: list[float]) -> float:
    """
    Calculates the median absolute deviation for a list of prices
    :param prices: List of prices
    :return: Returns the median absolute deviation as a float
    """
    median = statistics.median(prices)
    absolute_deviation = 0
    for price in prices:
        absolute_deviation += abs(price - median)
    return absolute_deviation / len(prices)


def mode_absolute_deviation(prices: list[float]) -> float:
    """
    Calculates the mode absolute deviation for a list of prices
    :param prices: List of prices
    :return: Returns the mode absolute deviation as a float
    """
    mode = statistics.mode(prices)
    absolute_deviation = 0
    for price in prices:
        absolute_deviation += abs(price - mode)
    return absolute_deviation / len(prices)
