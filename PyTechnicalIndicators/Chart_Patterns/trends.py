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


def break_down_trends(typical_prices, min_period=2):
    peaks_list = get_peaks(typical_prices, min_period)
    pits_list = get_pits(typical_prices, min_period)

    peak_trends = []
    pit_trends = []

    # TODO: take into account the index diff between last two and apply trend to figure out what the actual stddev diff is

    # TODO: could export into a diff function and call it with the different peak/pit values
    previous_peak_trend = None
    peak_start = ()
    for peak_position in range(len(peaks_list)-1):
        current_trend = peaks_list[peak_position+1] - peaks_list[peak_position]

        if previous_peak_trend is None:
            previous_peak_trend = current_trend
            peak_start = peaks_list[peak_position]
            continue

        stddev_diff = 2*(statistics.stdev(previous_peak_trend))

        if current_trend >= previous_peak_trend+stddev_diff or current_trend <= previous_peak_trend-stddev_diff:
            period_trend = peaks_list[peak_position][0] - peak_start[0]
            peak_trends.append((peak_start[1], peaks_list[peak_position][1], period_trend))
            peak_start = peaks_list[peak_position]

        previous_peak_trend = current_trend

    previous_pit_trend = None
    pit_start = ()
    for pit_position in range(len(pits_list)-1):
        current_trend = pits_list[pit_position+1] - pits_list[pit_position]

        if previous_pit_trend is None:
            previous_pit_trend = current_trend
            pit_start = pits_list[pit_position]
            continue

        stddev_diff = 2*(statistics.stdev(previous_pit_trend))

        if current_trend >= previous_pit_trend+stddev_diff or current_trend <= previous_pit_trend-stddev_diff:
            period_trend = pits_list[pit_position][0] - pit_start[0]
            pit_trends.append((peak_start[1], peaks_list[pit_position][1], period_trend))
            pit_start = pits_list[pit_position]

        previous_pit_trend = current_trend


    # TODO: figure out how to merge...
    #  take into account the diff between peaks, and pits will allow to stop false positives
    #  this will need to be graphed to see how applicable it is...


# TODO: figure out the trendline that connects the most peaks/pits so that breakouts can be highlighted
#  figure out how to break down trends into different areas to slow up/down/flat
# todo: fibonacci retractment, get a peak and pit, and then do the retractement based on that
# todo: take into accout volume to determine support and resistance???

# for notebok get general industry direction and general overall market direction