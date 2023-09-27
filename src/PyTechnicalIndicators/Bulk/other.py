from src.PyTechnicalIndicators.Single import other


def value_added_personalised_index(prices: list[float], starting_investment: int = 1000) -> list[float]:
    """
    Calculates and returns a personalised version of the VAMI where the period is determined by the called

    If the caller wants to start with an initial investment other than $1000, the caller should use the starting_investment
    variable
    :param prices: list of prices, these should be the start prices for each period. An assumption here is made that the
    start price for period t is the end price for period t+1.
    :param starting_investment: (Optional) Use if the starting investment should be different that $1000
    :return: Returns a list of Value Added Personalised Index
    """
    vapi_list = [other.value_added_personalised_index(prices[0], prices[1], starting_investment)]
    for i in range(1, len(prices)-1):
        vapi_list.append(other.value_added_personalised_index(prices[i], prices[i+1], vapi_list[-1]))
    return vapi_list


def true_range(high: list[float], low: list[float], close: list[float]) -> list[float]:
    """
    Calculates the true range which is the greatest distance between current high and low, or previous close and high, or previous close and low
    :param high: List of highs
    :param low: List of lows
    :param close: List of closing prices
    :return: Returns a list of true ranges
    """
    length = len(high)
    if length != len(low) and length != len(close):
        raise Exception(f'Lengths of high ({length}), low ({len(low)}) and close ({len(close)}) need to match')
    tr = []
    for i in range(length):
        tr.append(other.true_range(high[i], low[i], close[i]))
    return tr


def significant_close(close: list[float], period: int):
    """
    Returns the significant closes from a list of closes over a period of time
    :param close: Closing prices
    :param period: Observed period
    :return: Returns a list of significant closes
    """
    if len(close) < period:
        raise Exception(f'Length of close prices ({len(close)}) needs to be greater than the period ({period})')
    sc = []
    for i in range(len(close) - period + 1):
        sc.append(other.significant_close(close[i:i+period]))
    return sc


def average_range_constant(average_true_range: list[float], constant: float = 3.0) -> list[float]:
    """
    Calculates the average range constant
    :param average_true_range: List of average true range
    :param period: Period observed
    :param constant: Constant to multiply it by
    :return: Returns a list of average range constants
    """
    arc = []
    for atr in average_true_range:
        arc.append(atr * constant)
    return arc


# TODO: For stop and reverse points, have it be calculated as a single point from a list of points, based on the various functions
