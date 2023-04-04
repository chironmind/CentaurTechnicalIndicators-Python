

def rate_of_change(current_close_price: float, previous_close_price: float) -> float:
    """
    Calculates and returns the rate of change from the current price at t and previous close price at t-n

    This function will calculate the rate of change based on the following formula:
        rate_of_change = ((current_close_price - previous_close_price) / previous_close_price) * 100
    The period between the close price at t and t-n is decided by the caller of the function. A shorter period will react
    more quickly to changes in prices but will can also raise false signals
    :param current_close_price: close price at t
    :param previous_close_price: close price at t-n
    :return: Returns the rate of change as a float
    """
    if current_close_price == previous_close_price:
        return 0

    return ((current_close_price - previous_close_price) / previous_close_price) * 100


def on_balance_volume(current_close: float, previous_close: float, current_volume: float, previous_obv: float) -> float:
    if current_close > previous_close:
        volume = current_volume
    elif current_close == previous_close:
        volume = 0
    else:
        volume = -current_volume

    return previous_obv + volume
