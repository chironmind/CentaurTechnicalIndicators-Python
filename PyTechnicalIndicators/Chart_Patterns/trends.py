import statistics
import math

from .peaks import get_peaks
from .pits import get_pits


def get_trend(p):
    print(p)
    p_diff = []
    for p_index in range(len(p)):
        if p_index != len(p)-1:
            p_diff.append(p[p_index+1][0]-p[p_index][0])

    trend = statistics.mean(p_diff)
    return trend


def get_peak_trend(prices):
    print(prices)
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
    peaks_list = get_peaks(typical_prices)
    pits_list = get_pits(typical_prices)

    for price_index in range(min_period, len(typical_prices)):
        # TODO: go through each, one after the other to detrmine the trend between a and b, if the trend between c and b
        #  deviates by x amount then it is a new trend otherwise carry one until it changes.
        #  to graph see draw a line from the last peak/pit based on the trend, so if trend is 1.5 then for each one away
        #  from the peak/pit add 1.5 to get the limit, add +- 2 stddev to see how far it could go
        #  taking into account the diff between peaks, and pits will allow to stop false positives
        #  this will need to be graphed to see how applicable it is...


# TODO: figure out the trendline that connects the most peaks/pits so that breakouts can be highlighted
#  figure out how to break down trends into different areas to slow up/down/flat
# todo: fibonacci retractment, get a peak and pit, and then do the retractement based on that
# todo: take into accout volume to determine support and resistance???

# for notebok get general industry direction and general overall market direction