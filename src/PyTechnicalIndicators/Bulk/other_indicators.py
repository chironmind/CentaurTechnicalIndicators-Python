from ..Single import other_indicators


def return_on_investment(prices: list[float], starting_investment: int = 1000) -> list[tuple[float, float]]:
    """
    Calculates the return on investment and returns the value of the investment at the end of the period, as well as the
    percentage change

    If the caller wants to start with an initial investment other than $1000, the caller should input the value they
    want in starting_investment instead of leaving it to default to 1000
    :param prices: list of prices, these should be the start prices for each period. An assumption here is made that the
    start price for period t is the end price for period t+1.
    :param starting_investment: (Optional) Use if the starting investment should be different that $1000
    :return: Returns a list of return on investment and the percentage return
    """
    roi_list = [other_indicators.return_on_investment(prices[0], prices[1], starting_investment)]
    for i in range(1, len(prices)-1):
        roi_list.append(other_indicators.return_on_investment(prices[i], prices[i+1], roi_list[-1][0]))
    return roi_list


def true_range(high: list[float], low: list[float], previous_close: list[float]) -> list[float]:
    """
    Calculates the true range which is the greatest distance between current high and low, or previous close and high, or previous close and low
    :param high: List of highs
    :param low: List of lows
    :param previous_close: List of previous closing prices
    :return: Returns a list of true ranges
    """
    length = len(high)
    if length != len(low) and length != len(previous_close):
        raise Exception(f'Lengths of high ({length}), low ({len(low)}) and close ({len(previous_close)}) need to match')
    tr = []
    for i in range(length):
        tr.append(other_indicators.true_range(high[i], low[i], previous_close[i]))
    return tr


def average_range_constant(average_true_range: list[float], constant: float = 3.0) -> list[float]:
    """
    Calculates the average range constant
    :param average_true_range: List of average true range
    :param constant: Constant to multiply it by
    :return: Returns a list of average range constants
    """
    arc = []
    for atr in average_true_range:
        arc.append(atr * constant)
    return arc


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
        sc.append(other_indicators.significant_close(close[i:i+period]))
    return sc
