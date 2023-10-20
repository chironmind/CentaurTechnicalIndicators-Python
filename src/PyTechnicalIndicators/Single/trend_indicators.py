

def aroon_up(period_since_high: int) -> float:
    """
    The aroon up provides an indicator to measure the time since the last high. The Aroon calculations assumes a maximum period of 25.
    :param period_since_high: Number of periods since the last high
    :return: Returns the Aroon up as a float
    """
    if period_since_high > 25:
        raise Exception(f'period_since_high ({period_since_high}) has to be under 25')
    return personalised_aroon_up(25, period_since_high)


def personalised_aroon_up(period: int, period_since_high: int) -> float:
    """
    A personalised version of the aroon_up function. Allows for the period to be chosen rather than set to 25.
    :param period: Maximum number of periods to study
    :param period_since_high: Number of periods since the last high
    :return: Returns the Aroon up as a float
    """
    if period_since_high > period:
        raise Exception(f'period_since_high ({period_since_high}) needs to be less than input period ({period})')
    return 100 * ((period - period_since_high) / period)


def aroon_down(period_since_low: int) -> float:
    """
    The Aroon down provides an indicator that measure the time since the last low. The Aroon calculations assumes a maximum period of 25.
    :param period_since_low: Number of periods since the last low
    :return: Returns the Aroon down as a float
    """
    if period_since_low > 25:
        raise Exception(f'period_since_low ({period_since_low}) needs to smaller than 25')
    return personalised_aroon_down(25, period_since_low)


def personalised_aroon_down(period: int, period_since_low: int) -> float:
    """
    A personalised verion of the Aroon down. Allows for the period to be chosen rather than set to 25.
    :param period: Maximum number of periods to study
    :param period_since_low: Number of periods since the last low
    :return: Returns the Aroon down as a float
    """
    if period_since_low > period:
        raise Exception(f'period_since_low ({period_since_low}) needs to be less than input period ({period})')
    return 100 * ((period - period_since_low) / period)


def aroon_oscillator(period_since_high: int, period_since_low: int) -> float:
    """
    The Aroon oscillator uses the Aroon up and the Aroon down to provide signals on changes in trend. Should be used in
    conjunction with the Aroon up and down.
    :param period_since_high: Number of periods since the last high
    :param period_since_low: Number of periods since the last low
    :return: Returns the Aroon oscillator as a float
    """
    return aroon_up(period_since_high) - aroon_down(period_since_low)


def personalised_aroon_oscillator(period: int, period_since_high: int, period_since_low: int) -> float:
    """
    A personalised version of the Aroon oscillator. Should be used in conjunction with the Aroon up and down.
    :param period: Maximum number of periods to study
    :param period_since_high: Number of periods since the last high
    :param period_since_low: Number of periods since the last low
    :return: Returns the Aroon oscillator as a float
    """
    return personalised_aroon_up(period, period_since_high) - personalised_aroon_down(period, period_since_low)


def parabolic_sar(high: list[float], low: list[float], close: list[float], previous_psar: float = 0, acceleration_factor: float = 0.02, previous_extreme_point: float = 0) -> float:
    """
    Calculates the Parabolic Stop and Reverse and returns it as a float
    :param high: List of price highs
    :param low: List of price lows
    :param close: List of closes
    :param previous_psar: (Optional) Previous Parabolic SAR if one is available. Defaults to 0, and if defaulted will
     be calculated by in function
    :param acceleration_factor: (Optional) Acceleration factor. Defaults to 0.02. Assumption is that if a previous_psar
     is provided then a acceleration_factor will be provided.
    :param previous_extreme_point: (Optional) Previous extreme point. Defaults to 0, and if defaulted will be calculated
     in function. Assumption is that if a previous_psar is provided then a previous_extreme_point will be provided.
    :return: Returns the parabolic SAR as a float
    """
    if len(high) != len(low) or len(high) != len(close):
        raise Exception(f'Length of lists need to match, high ({len(high)}), low ({len(low)}), close ({len(close)})')
    if previous_psar == 0:
        if close[0] > close[-1]:
            if previous_psar == 0:
                previous_psar = max(high)
            if previous_extreme_point == 0:
                previous_extreme_point = min(low)
            return previous_psar - (acceleration_factor * (previous_psar - previous_extreme_point))
        elif close[0] < close[-1]:
            if previous_psar == 0:
                previous_psar = min(low)
            if previous_extreme_point == 0:
                previous_extreme_point = max(high)
            return previous_psar + (acceleration_factor * (previous_extreme_point - previous_psar))
        else:
            if previous_psar == 0:
                previous_psar = close[-1]
            if previous_extreme_point == 0:
                previous_extreme_point = (max(high) + min(low)) / 2
            rpsar = previous_psar + (acceleration_factor * (previous_extreme_point - previous_psar))
            fpsar = previous_psar - (acceleration_factor * (previous_psar - previous_extreme_point))
            return (rpsar + fpsar) / 2
    else:
        if close[-1] > previous_psar:
            return previous_psar + (acceleration_factor * (previous_extreme_point - previous_psar))
        elif close[-1] < previous_psar:
            return previous_psar - (acceleration_factor * (previous_psar - previous_extreme_point))
        else:
            rpsar = previous_psar + (acceleration_factor * (previous_extreme_point - previous_psar))
            fpsar = previous_psar - (acceleration_factor * (previous_psar - previous_extreme_point))
            return (rpsar + fpsar) / 2
