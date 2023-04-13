import math


def average_true_range(high: list[float], low: list[float], close: list[float], previous_atr: float = 0) -> float:
    """
    Calculates the average true range from a list of highs, lows, and closing prices. If the previous average true range
    is provided it will use it when doing the calculation, otherwise it will use a simpler formula
    :param high: List of high prices
    :param low: List of low prices
    :param close: List of closing prices
    :param previous_atr: Previous average true range
    :return: Returns the average true range as a float
    """

    if len(high) != len(low) or len(high) != len(close):
        raise Exception(f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}')

    if previous_atr == 0:
        sum_true_range = 0
        for i in range(1, len(high)):
            tr_high_low = high[i] - low[i]
            tr_high_close = high[i] - close[i - 1]
            tr_low_close = low[i] - close[i - 1]

            if tr_high_low > tr_high_close and tr_high_low > tr_low_close:
                sum_true_range += tr_high_low
            elif tr_high_close > tr_low_close:
                sum_true_range += tr_high_close
            else:
                sum_true_range += tr_low_close

        return (1/len(high)) * sum_true_range

    true_range_high_low = high[-1] - low[-1]
    true_range_high_close = high[-1] - close[-2]
    true_range_low_close = low[-1] - close[-2]

    if true_range_high_low > true_range_high_close and true_range_high_low > true_range_low_close:
        true_range = true_range_high_low
    elif true_range_high_close > true_range_low_close:
        true_range = true_range_high_close
    else:
        true_range = true_range_low_close

    return ((previous_atr * (len(high) - 1)) + true_range) / len(high)


def ulcer_index(close_prices: list[float]) -> float:
    """
    Calculates the ulcer index based on a list of close prices.

    The period and max price get determined based on the list of prices
    :param close_prices: List of closing prices
    :return: Returns the Ulcer Index as a float
    """
    squared_percentage_drawdown = [0]
    for i in range(1, len(close_prices)):
        period_high = max(close_prices[:i+1])
        percentage_drawdown = ((close_prices[i] - period_high) / period_high) * 100
        squared_percentage_drawdown.append(pow(percentage_drawdown, 2))
    squared_average = sum(squared_percentage_drawdown) / len(close_prices)
    return math.sqrt(squared_average)
