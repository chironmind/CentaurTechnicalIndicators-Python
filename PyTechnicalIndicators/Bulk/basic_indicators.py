import math
import statistics


def log(prices):
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    logs = []
    for i in range(len(prices)):
        logs.append(math.log(prices[i]))

    return logs


def log_diff(prices):
    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    logdiffs = []
    for i in range(len(prices)):
        if i == 0:
            logdiffs.append(0)
            continue

        logdiffs.append(math.log(prices[i]) - math.log(prices[i - 1]))

    return logdiffs


def stddev(prices, period, fill_empty=False, fill_value=None):
    # period is the the timeframe that you want it calculate it for throughout time
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    stddevs = []
    if fill_empty:
        for i in range(period):
            stddevs.append(fill_value)
    for i in range(period, len(prices)):
        stddevs.append(statistics.stdev(prices[i - period:i]))

    return stddevs


def mean(prices, period, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    means = []
    if fill_empty:
        for i in range(period):
            means.append(fill_value)
    for i in range(period, len(prices)):
        means.append(statistics.mean(prices[i - period:i]))

    return means


def median(prices, period, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    medians = []
    if fill_empty:
        for i in range(period):
            medians.append(fill_value)
    for i in range(period, len(prices)):
        medians.append(statistics.median(prices[i - period:i]))

    return medians


def variance(prices, period, fill_empty=False, fill_value=None):
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    vars = []
    if fill_empty:
        for i in range(period):
            vars.append(fill_value)
    for i in range(period, len(prices)):
        vars.append(statistics.variance(prices[i - period:i]))

    return vars
