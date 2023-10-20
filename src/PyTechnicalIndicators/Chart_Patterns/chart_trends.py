import statistics
import math

from src.PyTechnicalIndicators.Chart_Patterns import peaks, valleys


def get_trend_line(p: list[tuple[float, int]]) -> tuple[float, float]:
    """
    Gets the trend line of a list of prices and their indexes

    It is intended for internal use for the functions in trend_indicators.py
    :param p: list of tuples with price and index
    :return: Returns the slope and intercept as a tuple of floats
    """
    length = len(p)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sq = 0
    for i in p:
        # y is the first item, x is the second item
        sum_x += i[1]
        sum_y += i[0]
        sum_xy += i[0] * i[1]
        sum_x_sq += pow(i[1], 2)
    slope = ((length * sum_xy)-(sum_x * sum_y)) / ((length * sum_x_sq) - (pow(sum_x, 2)))
    intercept = (sum_y - (slope * sum_x)) / length
    return slope, intercept


def get_peak_trend(prices: list[float], period: int = 5) -> tuple[float, float]:
    """
    Get the trend of peaks (highs) from a list of prices
    :param prices: list of prices
    :param period: period used to calculate the peaks. Defaults to 5
    :return: Returns the slope and intercept as a tuple of floats
    """
    peaks_list = peaks.get_peaks(prices, period)
    return get_trend_line(peaks_list)


def get_valley_trend(prices: list[float], period: int = 5) -> tuple[float, float]:
    """
    Get the trend of valleys (lows) from a list of prices
    :param prices: list of prices
    :param period: period used to calculate the peaks. Defaults to 5
    :return: Returns the slope and intercept as a tuple of floats
    """
    valley_list = valleys.get_valleys(prices, period)
    return get_trend_line(valley_list)


def get_overall_trend(prices: list[tuple[float, int]]) -> tuple[float, float]:
    """
    Get the overall trend from a list of prices
    :param prices: List of prices and their indexes
    :return: Returns the slope and intercept as a tuple of floats
    """
    return get_trend_line(prices)


def break_down_trends(prices: list[float], standard_deviation_multiplier: int = 2) -> list[tuple[int, int, float, float]]:
    """
    Calculates and splits the different trends in a list of prices, and returns the positions of the trends
    :param prices: List of peaks or valleys
    :param standard_deviation_multiplier: The maximum a trend between two periods can differ before being determined
        to be a new trend
    :return: Returns the index of the start of the trend, the index of the end of the trend, the slope of the trend,
        and the intercept as a tuple
    """
    trends = []
    previous_slope = 0
    previous_intercept = 0
    previous_trend_points = [(prices[0], 0)]
    for i in range(1, len(prices)):
        current_trend_points = previous_trend_points + [(prices[i], i)]
        current_trend = get_trend_line(current_trend_points)
        if len(previous_trend_points) > 1:
            current_point_based_on_current_trend = (current_trend[0] * i) + current_trend[1]
            previous_trend_line = [(previous_slope * j[1]) + previous_intercept for j in previous_trend_points]
            previous_trend_line.append((previous_slope * i) + previous_intercept)
            previous_trend_line_stddev = statistics.stdev(previous_trend_line)
            upper_limit = previous_trend_line[-1] + (standard_deviation_multiplier * previous_trend_line_stddev)
            lower_limit = previous_trend_line[-1] - (standard_deviation_multiplier * previous_trend_line_stddev)
            if current_point_based_on_current_trend < lower_limit or current_point_based_on_current_trend > upper_limit:
                trends.append((previous_trend_points[0][1], previous_trend_points[-1][1], previous_slope, previous_intercept))
                previous_slope = 0
                previous_intercept = 0
                previous_trend_points = [(prices[i], i)]
                continue
        previous_trend_points.append((prices[i], i))
        previous_slope = current_trend[0]
        previous_intercept = current_trend[1]
    trends.append((previous_trend_points[0][1], previous_trend_points[-1][1], previous_slope, previous_intercept))
    return trends

# TODO: take into account volume to determine support and resistance, volume will need to be transformed into a series,
#   use the first value as 100, and change accordingly
