import math
import statistics

from src.PyTechnicalIndicators.Single import basic_indicators


def log(prices: list[float]) -> list[float]:
    """
    Calculates the log of a list of prices
    :param prices: -- list of floats
    :return: list of logs (floats)
    """
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    logs = []
    for i in range(len(prices)):
        logs.append(math.log(prices[i]))

    return logs


def log_diff(prices: list[float]) -> list[float]:
    """
    Calculates the difference between the log a price and the log of the previous price
    :param prices: list of prices as floats
    :return: Returns a list of log differences (floats) the length of the list will be one shorter than the input prices list
    """
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    logdiffs = []
    for i in range(len(prices)):
        if i == 0:
            logdiffs.append(0)
            continue

        logdiffs.append(math.log(prices[i]) - math.log(prices[i - 1]))

    return logdiffs


def stddev(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the standard deviation of a list of prices
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the standard deviation needs to be calculated for. For example period=20 would calculate the standard deviation for 20 periods
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list (floats) of standard deviations
    """
    # period is the timeframe that you want it calculate it for throughout time
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    stddevs = []
    if fill_empty:
        for i in range(period):
            stddevs.append(fill_value)
    for i in range(period, len(prices)+1):
        stddevs.append(statistics.stdev(prices[i - period:i]))
    return stddevs


def mean(prices: list[float], period: int, fill_empty: bool = False, fill_value: str = None) -> list[float]:
    """
    Calculates the mean, or average, of a list of prices over a certain period and returns a list of means
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the mean needs to be calculated for. For example period=20 would calculate the mean for 20 periods
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list (floats) of means
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    means = []
    if fill_empty:
        for i in range(period):
            means.append(fill_value)
    for i in range(period, len(prices)+1):
        means.append(statistics.mean(prices[i - period:i]))
    return means


def median(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the median for a list of prices over a certain period and returns them as a list

    Setting the period will determine timeframe for which the median gets calculated for. For example when calculating the
    median for a period of 20 it will iterate through the list of prices and return a list of medians for 20 periods
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the median needs to be calculated for. For example period=20 would calculate the median for 20 periods
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list (floats) of medians
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    medians = []
    if fill_empty:
        for i in range(period):
            medians.append(fill_value)
    for i in range(period, len(prices)+1):
        p = prices[i - period:i]
        medians.append(basic_indicators.median(prices[i - period:i]))
    return medians


def variance(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the variance for a list of prices for a certain period of time and returns a list of variances

    When calculating the variance you can choose the number of periods that you want the variance that you want to be
    calculated for.
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the variance needs to be calculated for. For example period=20 would calculate the variance for 20 periods
    :param fill_empty: bool - (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: any - (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list (floats) of variances
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    vars = []
    if fill_empty:
        for i in range(period):
            vars.append(fill_value)
    for i in range(period, len(prices)+1):
        vars.append(statistics.variance(prices[i - period:i]))

    return vars


# TODO: Mean, medain and mode absolute deviations missing
def mean_absolute_deviation(prices: list[float], period: int) -> list[float]:
    """
    Calculates the mean absolute deviation for a list of prices
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the mean needs to be calculated for. For example period=20 would calculate the mean for 20 periods
    :return: Returns a list (floats) of mean absolute deviations
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    means = []
    for i in range(period, len(prices)+1):
        means.append(basic_indicators.mean_absolute_deviation(prices[i - period:i]))
    return means


def median_absolute_deviation(prices: list[float], period: int) -> list[float]:
    """
    Calculates the median absolute deviation for a list of prices
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the mean needs to be calculated for. For example period=20 would calculate the mean for 20 periods
    :return: Returns a list (floats) of median absolute deviations
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    medians = []
    for i in range(period, len(prices)+1):
        medians.append(basic_indicators.median_absolute_deviation(prices[i - period:i]))
    return medians


def mode_absolute_deviation(prices: list[float], period: int) -> list[float]:
    """
    Calculates the mode absolute deviation for a list of prices
    :param prices: list[float] - list of prices
    :param period: int - timeframe for which the mean needs to be calculated for. For example period=20 would calculate the mean for 20 periods
    :return: Returns a list (floats) of mode absolute deviations
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    modes = []
    for i in range(period, len(prices)+1):
        modes.append(basic_indicators.mode_absolute_deviation(prices[i - period:i]))
    return modes
