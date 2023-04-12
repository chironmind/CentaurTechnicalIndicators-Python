

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
