import statistics

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
