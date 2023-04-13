

def value_added_monthly_index(price_start_month: float, price_end_month: float, previous_vami: float = 1000) -> float:
    """
    Calculates the Value Added Monthly Index (VAMI) a.k.a the return on an $1000 investment over a month.

    :param price_start_month: The price at the start of the month
    :param price_end_month: The price at the end of the month
    :param previous_vami: (Optional) The previous Value Added Monthly Index (Default = 1000)
    :return: Returns the Value Added Monthly Index
    """
    return value_added_personalised_index(price_start_month, price_end_month, previous_vami)


def value_added_personalised_index(start_price: float, end_price: float, previous_vapi: float = 1000) -> float:
    """
    Calculates and returns a personalised version of the VAMI where the period is determined by the called

    If the caller wants to start with an initial investment other than $1000, the caller should input the value they
    want as the first previous_vapi instead of leaving it to default to 1000
    :param start_price: The price at the start of the period
    :param end_price: The price at the end of the period
    :param previous_vapi: (Optional) The previous Value Added Monthly Index (Default = 1000)
    :return: Returns the value add personalised index as a float
    """
    return previous_vapi * (1 + (end_price - start_price))
