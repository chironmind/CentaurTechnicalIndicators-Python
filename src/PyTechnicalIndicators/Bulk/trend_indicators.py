from ..Single import trend_indicators


def aroon_up(highs: list[float], period: int = 25) -> list[float]:
    """
    A personalised version of the aroon_up function. Allows for the period to be chosen rather than set to 25.
    :param highs: List of high prices
    :param period: Time period
    :return: Returns a list of Aroon ups
    """
    # Insanely the calculation is done on the previous x periods + the current period, others the oscillator would only
    #  fluctuate between 0 and 90, and the most recent period would be t-1 aka period 1 so
    #  100 * ( (period - 1) / period ) = 90 to get to 100 you would need to have a period 0, so the default period
    #  actually looks at a total of 26 periods... so the period needs to be increased by 1
    actual_period = period + 1
    length = len(highs)
    if length < actual_period:
        raise Exception(f'Length of prices ({length}) needs to be at least equal to period ({period} + 1)')
    periods_since_high = []
    for i in range(actual_period, length+1):
        sub_high = highs[i-actual_period:i]
        local_max = max(sub_high)
    #   list.index(x) returns first occurrence in the list, for two identical highs we want most recent
        for j in range(len(sub_high)-1, -1, -1):
            if sub_high[j] == local_max:
                periods_since_high.append(period-j)
                break
    aroon_up_list = []
    for p in periods_since_high:
        aroon_up_list.append(trend_indicators.aroon_up(p, period))
    return aroon_up_list


def aroon_down(lows: list[float], period: int = 25) -> list[float]:
    """
    A personalised verion of the Aroon down. Allows for the period to be chosen rather than set to 25.
    :param lows: List of lows
    :param period: Time period
    :return: Returns a list of Aroon downs
    """
    # see explanation in aroon up for actual period
    actual_period = period + 1
    length = len(lows)
    if length < period:
        raise Exception(f'Length of prices ({length}) needs to be at least equal to period ({period}+1)')
    period_since_low = []
    for i in range(actual_period, length+1):
        sub_low = lows[i-actual_period:i]
        local_min = min(sub_low)
    #   list.index(x) returns first occurrence in the list, for two identical highs we want most recent
        for j in range(len(sub_low)-1, -1, -1):
            if sub_low[j] == local_min:
                period_since_low.append(period-j)
                break
    aroon_down_list = []
    for p in period_since_low:
        aroon_down_list.append(trend_indicators.aroon_down(p, period))
    return aroon_down_list


def aroon_oscillator(highs: list[float], lows: list[float], period: int = 25) -> list[float]:
    """
    A personalised version of the Aroon oscillator. Should be used in conjunction with the Aroon up and down.
    :param highs: List of high prices
    :param lows: List of low prices
    :param period: Period to study
    :return: Returns the Aroon oscillator as a list of floats
    """
    au = aroon_up(highs, period)
    ad = aroon_down(lows, period)
    aroon_oscillator_list = []
    for i in range(len(au)):
        aroon_oscillator_list.append(au[i] - ad[i])
    return aroon_oscillator_list


# TODO: This could use the Chart pattern functions to determine highs and low
def parabolic_sar(high: list[float], low: list[float], close: list[float], period: int) -> list[float]:
    """
    Calculates the Parabolic Stop and Reverse and returns it as a float
    :param high: List of price highs
    :param low: List of price lows
    :param close: List of closing prices
    :param period: The period for which to calculate the parabolic sar
    :return: Returns a list of parabolic SARs
    """
    if len(high) != len(low) or len(high) != len(close):
        raise Exception(f'Length of lists need to match, high ({len(high)}), low ({len(low)}), close ({len(close)})')

    if period > len(high):
        raise Exception(f'Length of lists ({len(high)}) needs to be greater or equal to period ({period})')

    psar_list = [trend_indicators.parabolic_sar(high[:period], low[:period], close[:period])]
    acceleration_factor = 0.02
    if close[0] > close[period + 1]:
        previous_extreme = min(low[:period])
        previous_state = 'falling'
    elif close[0] < close[period + 1]:
        previous_extreme = max(high[:period])
        previous_state = 'rising'
    else:
        previous_extreme = (max(high[:period - 1]) + min(low[:period - 1])) / 2
        previous_state = 'neutral'

    for i in range(1, len(high) - period + 1):
        j = period + i - 1
        if close[j] < psar_list[-1]:
            new_extreme = min(low[i-1:j])
            if previous_state == 'falling':
                if new_extreme < previous_extreme:
                    previous_extreme = new_extreme
                    if acceleration_factor <= 0.18:
                        acceleration_factor += 0.02
            else:
                previous_extreme = new_extreme
            previous_state = 'falling'
        elif close[j] > psar_list[-1]:
            new_extreme = max(high[i-1:j])
            if previous_state == 'rising':
                if new_extreme > previous_extreme:
                    previous_extreme = new_extreme
                    if acceleration_factor <= 0.18:
                        acceleration_factor += 0.02
            else:
                previous_extreme = new_extreme
            previous_state = 'rising'
        psar_list.append(trend_indicators.parabolic_sar(high[i:j], low[i:j], close[i:j], psar_list[-1], acceleration_factor, previous_extreme))
    return psar_list
