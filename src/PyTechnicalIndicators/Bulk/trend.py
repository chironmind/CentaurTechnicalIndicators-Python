from src.PyTechnicalIndicators.Single.trend import personalised_aroon_up as pau, personalised_aroon_down as pad, personalised_aroon_oscillator as pao, parabolic_sar as psar


def personalised_aroon_up(period: int, period_since_high: list[int]) -> list[float]:
    """
    A personalised version of the aroon_up function. Allows for the period to be chosen rather than set to 25.
    :param period: Maximum number of periods to study
    :param period_since_high: Number of periods since the last high
    :return: Returns a list of Aroon ups
    """
    aroon_up_list = []
    for p in period_since_high:
        aroon_up_list.append(pau(period, p))
    return aroon_up_list


def aroon_up(period_since_high: list[int]) -> list[float]:
    """
    The aroon up provides an indicator to measure the time since the last high. The Aroon calculations assumes a maximum period of 25.
    :param period_since_high: Number of periods since the last high
    :return: Returns a list of Aroon ups
    """
    return personalised_aroon_up(25, period_since_high)


def personalised_aroon_down(period: int, period_since_low: list[int]) -> list[float]:
    """
    A personalised verion of the Aroon down. Allows for the period to be chosen rather than set to 25.
    :param period: Maximum number of periods to study
    :param period_since_low: Number of periods since the last low
    :return: Returns a list of Aroon downs
    """
    aroon_down_list = []
    for p in period_since_low:
        aroon_down_list.append(pad(period, p))
    return aroon_down_list


def aroon_down(period_since_low: list[int]) -> list[float]:
    """
    The Aroon down provides an indicator that measure the time since the last low. The Aroon calculations assumes a maximum period of 25.
    :param period_since_low: Number of periods since the last low
    :return: Returns a list of Aroon downs
    """
    return personalised_aroon_down(25, period_since_low)


def personalised_aroon_oscillator(period: int, period_since_high: list[int], period_since_low: list[int]) -> list[float]:
    """
    A personalised version of the Aroon oscillator. Should be used in conjunction with the Aroon up and down.
    :param period: Maximum number of periods to study
    :param period_since_high: Number of periods since the last high
    :param period_since_low: Number of periods since the last low
    :return: Returns a list of Aroon oscillators
    """
    au = personalised_aroon_up(period, period_since_high)
    ad = personalised_aroon_down(period, period_since_low)
    aroon_oscillator_list = []
    for i in range(len(au)):
        aroon_oscillator_list.append(au[i] - ad[i])
    return aroon_oscillator_list


def aroon_oscillator(period_since_high: list[int], period_since_low: list[int]) -> list[float]:
    """
    The Aroon oscillator uses the Aroon up and the Aroon down to provide signals on changes in trend. Should be used in
    conjunction with the Aroon up and down.
    :param period_since_high: Number of periods since the last high
    :param period_since_low: Number of periods since the last low
    :return: Returns a list of Aroon oscillators
    """
    return personalised_aroon_oscillator(25, period_since_high, period_since_low)

# TODO: A function that gets prices a determines the highs and lows instead of having to pass them in?


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

    psar_list = [psar(high[:period], low[:period], close[:period])]
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
        psar_list.append(psar(high[i:j], low[i:j], close[i:j], psar_list[-1], acceleration_factor, previous_extreme))
    return psar_list
