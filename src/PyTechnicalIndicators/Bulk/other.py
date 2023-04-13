from src.PyTechnicalIndicators.Single.other import value_added_personalised_index as vapi


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
    vapi_list = [vapi(prices[0], prices[1], starting_investment)]
    for i in range(1, len(prices)-1):
        vapi_list.append(vapi(prices[i], prices[i+1], vapi_list[-1]))
    return vapi_list
