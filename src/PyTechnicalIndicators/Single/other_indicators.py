

def return_on_investment(start_price: float, end_price: float, previous_roi: float = 1000) -> tuple[float, float]:
    """
    Calculates the return on investment and returns the value of the investment at the end of the period, as well as the
    percentage change

    If the caller wants to start with an initial investment other than $1000, the caller should input the value they
    want as the first previous_roi instead of leaving it to default to 1000
    :param start_price: The price at the start of the period
    :param end_price: The price at the end of the period
    :param previous_roi: (Optional) The previous return on investment (Default = 1000)
    :return: Returns the return on investment and the percentage return as a tuple of floats
    """
    initial_investment = previous_roi / start_price
    final_investment_worth = end_price * initial_investment
    percent_return_on_investment = ((final_investment_worth - previous_roi) / previous_roi) * 100
    return final_investment_worth, percent_return_on_investment


def true_range(high: float, low: float, previous_close: float) -> float:
    """
    Calculates the true range which is the greatest distance between current high and low, or previous close and high, or previous close and low
    :param high: Current high
    :param low: Current low
    :param previous_close: Previous close
    :return: Returns the true range as a float
    """
    high_low = high - low
    high_close = high - previous_close
    close_low = previous_close - low

    if high_low >= high_close and high_low >= close_low:
        return high_low
    elif high_close >= close_low:
        return high_close
    else:
        return close_low


def average_range_constant(average_true_range: float, constant: float = 3.0) -> float:
    """
    Calculates the average range constant for an average true range
    :param average_true_range: the average true range
    :param constant: The constant to multiply it by. Defaults to 3
    :return: Returns the average range constant
    """
    return average_true_range * constant


def significant_close(close: list[float]) -> float:
    """
    Returns the most significant close for a list of prices
    :param close: List of closing prices
    :return: Returns the most significant close
    """
    return max(close)


def stop_and_reverse(close: float, significant_close: float, average_range_constant: float, previous_stop_and_reverse: float = 0) -> float:
    """
    Calculates Welles stop and reverse point
    :param close: current close price
    :param significant_close: the significant close of the observed period
    :param average_range_constant: the average range constant
    :return: Returns the stop and reverse point
    """
    if close < previous_stop_and_reverse:
        return close + average_range_constant
    return significant_close - average_range_constant

