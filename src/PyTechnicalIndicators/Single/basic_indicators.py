import statistics


def median(prices: list[float], even_rule: str = 'average') -> float:
    """
    The median function from the Python standard library orders the numbers before doing the median, which is not
    helpful when looking at financial data. This function gets the middle value of an unsorted list of prices
    :param prices: List of prices
    :param even_rule: Determines what to do if the list of prices if even. Options are 'average' which takes the average
    of the two number in the middle. 'low' which takes the first of the two numbers. 'high' which takes the second of the
    two numbers. Defaults to 'high
    :return: Returns the median as a float
    """
    length = len(prices)
    if (length % 2) == 0:
        middle = int(length / 2)
        median_list = prices[middle-1:middle+1]
        if even_rule == 'average':
            return statistics.mean(median_list)
        elif even_rule == 'low':
            return median_list[0]
        elif even_rule == 'high':
            return median_list[1]
        else:
            raise Exception(f'{even_rule} is not a supported even_rule')
    else:
        middle = int(length / 2)
        return prices[middle]


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
    price_median = median(prices)
    absolute_deviation = 0
    for price in prices:
        absolute_deviation += abs(price - price_median)
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
