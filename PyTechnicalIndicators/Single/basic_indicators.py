import math
import statistics


def log(price):
    # Use math.log instead
    if not price:
        raise Exception('There needs to be a price to log')
    return math.log(price)


def log_diff(current_price, previous_price):
    # Use math.log instead
    if not current_price or not previous_price:
        raise Exception('There needs to be two prices to be able to do a diff')

    return math.log(current_price) - math.log(previous_price)


def stddev(prices):
    # Use statistics.stdev instead
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to calculate a stddev')

    return statistics.stdev(prices)


def mean(prices):
    # Use statistics.mean instead
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to calculate a mean')

    return statistics.mean(prices)


def median(prices):
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to calculate a median')

    return statistics.median(prices)


def variance(prices):
    # Use statistics.variance instead
    if len(prices) == 0:
        raise Exception('There needs to be prices to be able to calculate a variance')

    return statistics.variance(prices)
