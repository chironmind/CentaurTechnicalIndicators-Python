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


def break_down_trend(price_list):
    trends = []

    previous_trend = None
    previous_tuple = ()
    trend_start = ()

    for position in range(len(price_list)-1):
        current_trend = price_list[position+1][0] - price_list[position][0]

        if previous_trend is None:
            previous_trend = current_trend
            previous_tuple = price_list[position]
            trend_start = price_list[position]
            continue

        current_price = price_list[position][0]
        print(current_price)
        current_index = price_list[position][1]
        print(current_index)
        previous_price = previous_tuple[0]
        print(previous_price)
        previous_index = previous_tuple[1]
        print(previous_index)
        time_passed = current_index - previous_index
        print(time_passed)
        trended_price = previous_price + (previous_trend * time_passed)
        print(trended_price)

        stddev_diff = 2*(statistics.stdev(trended_price))
        print(stddev_diff)
        upper_trend_limit = trended_price + stddev_diff
        lower_trend_limit = trended_price - stddev_diff

        if current_trend > upper_trend_limit or current_trend < lower_trend_limit:
            period_trend = current_price - trend_start[0]
            trends.append((trend_start[1], current_index, period_trend))
            trend_start = price_list[position]

        previous_tuple = price_list[position]
        previous_trend = current_trend

    return trends


def break_down_trends(typical_prices, min_period=2):
    peaks_list = get_peaks(typical_prices, min_period)
    pits_list = get_pits(typical_prices, min_period)

    peak_trends = break_down_trend(peaks_list)
    pit_trends = break_down_trend(pits_list)

    return peak_trends, pit_trends

    # TODO: figure out how to merge...
    #  take into account the diff between peaks, and pits will allow to stop false positives
    #  this will need to be graphed to see how applicable it is...


# TODO: figure out the trendline that connects the most peaks/pits so that breakouts can be highlighted
#  figure out how to break down trends into different areas to slow up/down/flat
# todo: fibonacci retractment, get a peak and pit, and then do the retractement based on that
# todo: take into accout volume to determine support and resistance???

# for notebok get general industry direction and general overall market direction