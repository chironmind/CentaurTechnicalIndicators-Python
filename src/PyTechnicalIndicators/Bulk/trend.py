from src.PyTechnicalIndicators.Single.trend import personalised_aroon_up as pau, personalised_aroon_down as pad, personalised_aroon_oscillator as pao


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
