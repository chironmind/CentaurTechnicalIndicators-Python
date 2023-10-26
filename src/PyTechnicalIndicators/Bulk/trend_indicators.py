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
    aroon_up_list = []
    for i in range(actual_period, length+1):
        aroon_up_list.append(trend_indicators.aroon_up(highs[i-actual_period:i], period))
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
    aroon_down_list = []
    for i in range(actual_period, length+1):
        aroon_down_list.append(trend_indicators.aroon_down(lows[i-actual_period:i], period))
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


def parabolic_sar(high: list[float], low: list[float], close: list[float], period: int) -> list[tuple[float, float, float, str]]:
    """
    Calculates the Parabolic Stop and Reverse and returns it as a float
    :param high: List of price highs
    :param low: List of price lows
    :param close: List of closing prices
    :param period: The period for which to calculate the parabolic sar
    :return: Returns a list of parabolic SARs, the acceleration factor, the extreme point, and the state
    """
    length = len(high)
    if length != len(low) or length != len(close):
        raise Exception(f'Length of lists need to match, high ({length}), low ({len(low)}), close ({len(close)})')
    if period > length:
        raise Exception(f'Length of lists ({length}) needs to be greater or equal to period ({period})')
    psar_list = [trend_indicators.parabolic_sar(high[:period], low[:period], close[:period])]
    for i in range(period+1, length+1):
        psar_list.append(trend_indicators.parabolic_sar(high[i-period:i], low[i-period:i], close[i-period:i], psar_list[-1][0], psar_list[-1][1], psar_list[-1][2], psar_list[-1][3]))
    return psar_list
