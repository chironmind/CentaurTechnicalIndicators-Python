import statistics
import math

from peaks import get_peaks
from pits import get_pits


def get_trend(p):
    p_diff = []
    for p_index in range(len(p)):
        if p_index != len(p)-1:
            p_diff.append(p[p_index+1]-p[p_index])

    trend = statistics.mean(p_diff)
    return trend


def get_peak_trend(prices):
    peaks = get_peaks(prices)
    return get_trend(peaks)


def get_pit_trend(prices):
    pits = get_pits(prices)
    return get_trend(pits)


def get_overall_trend(prices):
    peaks_trend = get_peaks(prices)
    pits_trend = get_pits(prices)

    return (peaks_trend + pits_trend) / 2


def get_trend_angle(price_a, index_a, price_b, index_b):
    adjacent = index_b - index_a
    opposite = price_b - price_a

    angle = math.tan(opposite/adjacent)

    return angle




# TODO: figure out the trendline that connects the most peaks/pits so that breakouts can be highlighted
# todo: implement measure rule p26
#  figure out how to break down trends into different areas to slow up/down/flat
#   figure out what logarithmic price is for trends
# todo: support and resistance
#   include round number support (10, 15, 20...), but include some kind of rounding of fuzzy logic
# todo: fibonacci retractment, get a peak and pit, and then do the retractement based on that
# todo: horizontal consolidation region, figur out where the price is pretty much flat
# todo: channels, like hcr^ but not flat, pretty much diagonal support and resistance
# take into accout volume to determine support and resistance???
# todo: implement buy / sell signals, see each in the book to see if it implementable based on trends
#   and add targets to them

# for notebok get general industry direction and general overall market direction