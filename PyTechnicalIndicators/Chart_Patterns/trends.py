import statistics
import math

from .peaks import get_peaks
from .pits import get_pits


def get_trend(p):
    p_diff = []
    for p_index in range(len(p)):
        if p_index != len(p)-1:
            p_diff.append(p[p_index+1][0]-p[p_index][0])

    trend = statistics.mean(p_diff)
    return trend


def get_peak_trend(prices):
    peaks_list = get_peaks(prices)
    return get_trend(peaks_list)


def get_pit_trend(prices):
    pits_list = get_pits(prices)
    return get_trend(pits_list)


def get_overall_trend(prices):
    peaks_trend = get_peak_trend(prices)
    pits_trend = get_pit_trend(prices)

    return (peaks_trend + pits_trend) / 2


def get_trend_angle(price_a, index_a, price_b, index_b):
    adjacent = index_b - index_a
    opposite = price_b - price_a
    unknown_side = math.sqrt(math.pow(adjacent, 2) + math.pow(opposite, 2))

    angle = math.acos((math.pow(adjacent, 2) + math.pow(unknown_side, 2) - math.pow(opposite, 2))/(2*(unknown_side*adjacent)))

    return math.degrees(angle)


def break_down_trend(outlier_list, typical_prices):
    trends = []

    previous_tuple = outlier_list[1]
    trend_start = outlier_list[0]
    period_trends = []

    for position in range(2, len(outlier_list)):
        current_price = outlier_list[position][0]
        current_index = outlier_list[position][1]
        previous_price = previous_tuple[0]
        previous_index = previous_tuple[1]
        current_period_length = current_index - previous_index

        previous_trend = (previous_price - trend_start[0]) / (previous_index - trend_start[1])
        expected_price = previous_price + (current_period_length * previous_trend)
        current_trend = (current_price - trend_start[0]) / (current_index - trend_start[1])
        micro_period_trend = (current_price - previous_price) / (current_index - previous_index)

        if current_period_length <= 3:
            continue

        period_trends.append(previous_trend)

        std_dev_multiplier = 2
        if len(period_trends) > 1:
            trend_std_dev = statistics.stdev(period_trends)

            upper_trend_band = previous_trend + trend_std_dev
            lower_trend_band = previous_trend - trend_std_dev
            if current_trend > upper_trend_band or current_trend < lower_trend_band:
                std_dev_multiplier = 1
            elif micro_period_trend > upper_trend_band or micro_period_trend < lower_trend_band:
                std_dev_multiplier = 1

        period_std_dev = statistics.stdev(typical_prices[trend_start[1]:current_index+1])
        upper_trend_limit = expected_price + (std_dev_multiplier * period_std_dev)
        lower_trend_limit = expected_price - (std_dev_multiplier * period_std_dev)

        if current_price > upper_trend_limit or current_price < lower_trend_limit:
            trends.append((trend_start[1], previous_index, previous_trend))
            # Trend started at t-1 as t is current outlier
            trend_start = previous_tuple
            period_trends = []

        previous_tuple = outlier_list[position]

    return trends


def break_down_trends(prices, min_period=2, peaks_only=False, pits_only=False):
    peaks_list = get_peaks(prices, min_period)
    pits_list = get_pits(prices, min_period)

    if not pits_only:
        peak_trends = break_down_trend(peaks_list, prices)
    if not peaks_only:
        pit_trends = break_down_trend(pits_list, prices)

    if peaks_only:
        return peak_trends
    if pits_only:
        return pit_trends

    return peak_trends, pit_trends


def merge_trends(typical_prices, min_period=2):
    peaks_list = get_peaks(typical_prices, min_period)
    pits_list = get_pits(typical_prices, min_period)
    outlier_list = peaks_list
    last_index = 0
    for pit in pits_list:
        for outlier_index in range(last_index, len(outlier_list)):
            if pit[1] < outlier_list[outlier_index][1]:
                outlier_list.insert(outlier_index, pit)
                last_index = outlier_index
                break

            if outlier_index == len(outlier_list):
                outlier_list.append(pit)
                last_index = len(outlier_list)

    return break_down_trend(outlier_list, typical_prices)

# todo: create bands for the stddev to graph

# todo: fibonacci retractment, get a peak and pit, and then do the retractement based on that
# todo: take into account volume to determine support and resistance, volume will need to be transformed into a series,
#   use the first value as 100, and change accordingly
