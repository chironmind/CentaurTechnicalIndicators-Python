

def aroon_up(highs: list[float], period: int = 25) -> float:
    """
    A personalised version of the aroon_up function. Allows for the period to be chosen rather than set to 25.
    :param highs: List of high prices
    :param period: Periods
    :return: Returns the Aroon up as a float
    """
    length = len(highs)
    if length < period + 1:
        raise Exception(f'Length of highs ({length}) needs to be greater or equal to period +1 ({period} +1)')
    local_max = max(highs)
    period_since_high = 0
    for i in range(length - 1, -1, -1):
        if highs[i] == local_max:
            period_since_high = period - i
            break
    return 100 * ((period - period_since_high) / period)


def aroon_down(lows: list[float], period: int = 25) -> float:
    """
    A personalised verion of the Aroon down. Allows for the period to be chosen rather than set to 25.
    :param lows: List of low prices
    :param period: Periods
    :return: Returns the Aroon down as a float
    """
    length = len(lows)
    if length < period + 1:
        raise Exception(f'Length of lows ({length}) needs to be greater or equal to period +1 ({period} +1)')
    local_low = min(lows)
    period_since_low = 0
    for i in range(length - 1, -1, -1):
        if lows[i] == local_low:
            period_since_low = period - i
            break
    return 100 * ((period - period_since_low) / period)


def aroon_oscillator(highs: list[float], lows: list[float], period: int = 25) -> float:
    """
    The Aroon oscillator uses the Aroon up and the Aroon down to provide signals on changes in trend. Should be used in
    conjunction with the Aroon up and down.
    :param highs: List of high prices
    :param lows: List of low prices
    :param period: Period
    :return: Returns the Aroon oscillator as a float
    """
    return aroon_up(highs, period) - aroon_down(lows, period)


def parabolic_sar(high: list[float], low: list[float], close: list[float], previous_psar: float = 0, acceleration_factor: float = 0.02, extreme: float = 0, state: str = 'netural') -> tuple[float, float, float, str]:
    """
    Calculates the Parabolic Stop and Reverse and returns it as a float
    :param high: List of price highs
    :param low: List of price lows
    :param close: List of closes
    :param previous_psar: (Optional) Previous Parabolic SAR if one is available. Defaults to 0, and if defaulted will
     be calculated by in function
    :param acceleration_factor: (Optional) Acceleration factor. Defaults to 0.02. Assumption is that if a previous_psar
     is provided then an acceleration_factor will be provided.
    :param extreme: (Optional) Previous extreme point. Defaults to 0, and if defaulted will be calculated
     in function. Assumption is that if a previous_psar is provided then a previous_extreme_point will be provided.
    :param state: (Optional) Previous state. Should be one of the following 'rising', 'falling', or 'neutral'.
     Defaults to 'neutral', and if defaulted will be calculated and returned for use in next call.
    :return: Returns the parabolic SAR as a float, the acceleration factor, the extreme point, and the state.
    """
    length = len(high)
    if length != len(low) or length != len(close):
        raise Exception(f'Length of lists need to match, high ({length}), low ({len(low)}), close ({len(close)})')

    if previous_psar == 0:
        if close[0] > close[-1]:
            previous_psar = max(high)
            if extreme == 0:
                extreme = min(low)
            psar = previous_psar - (acceleration_factor * (previous_psar - extreme))
            state = 'falling'
        elif close[0] < close[-1]:
            previous_psar = min(low)
            if extreme == 0:
                extreme = max(high)
            psar = previous_psar + (acceleration_factor * (extreme - previous_psar))
            state = 'rising'
        else:
            previous_psar = close[-1]
            if extreme == 0:
                extreme = (max(high) + min(low)) / 2
            rpsar = previous_psar + (acceleration_factor * (extreme - previous_psar))
            fpsar = previous_psar - (acceleration_factor * (previous_psar - extreme))
            psar = (rpsar + fpsar) / 2
            state = 'neutral'
    else:
        if close[-1] < previous_psar:
            new_extreme = min(low)
            if state == 'falling':
                if new_extreme < extreme:
                    extreme = new_extreme
                    if acceleration_factor <= 0.18:
                        acceleration_factor += 0.02
            else:
                extreme = new_extreme
            state = 'falling'
            psar = previous_psar - (acceleration_factor * (previous_psar - extreme))
        elif close[-1] > previous_psar:
            new_extreme = max(high)
            if state == 'rising':
                if new_extreme > extreme:
                    extreme = new_extreme
                    if acceleration_factor <= 0.18:
                        acceleration_factor += 0.02
            else:
                extreme = new_extreme
            state = 'rising'
            psar = previous_psar + (acceleration_factor * (extreme - previous_psar))
        else:
            state = 'neutral'
            rpsar = previous_psar + (acceleration_factor * (extreme - previous_psar))
            fpsar = previous_psar - (acceleration_factor * (previous_psar - extreme))
            psar = (rpsar + fpsar) / 2
    return psar, acceleration_factor, extreme, state
