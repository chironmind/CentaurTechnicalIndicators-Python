from src.PyTechnicalIndicators.Single.oscillators import personalised_money_flow_index as mfi


def money_flow_index(typical_prices: list[float], volume: list[int]) -> list[float]:
    """
    Calculates the money flow index from the typical price and volume, it uses a period of 14 to make the calculations.
    To choose a different period use the personalised_money_flow_index function
    :param typical_prices: list of typical prices
    :param volume: list of volumes
    :return: Returns a list of money flow index
    """
    return personalised_money_flow_index(typical_prices, volume, 14)


def personalised_money_flow_index(typical_prices: list[float], volume: list[int], period: int) -> list[float]:
    """
    Calculates the money flow index from the typical price and volume for a given period.
    :param typical_prices: List of typical prices
    :param volume: List of volumes
    :param period: Period of time
    :return:
    """
    len_typical_prices = len(typical_prices)

    if len_typical_prices < period or len(volume) < period:
        raise Exception(f'typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be at least {period} periods in length')

    if len_typical_prices != len(volume):
        raise Exception(f"typical_prices ({len_typical_prices}) and volume ({len(volume)}) need to be of same length")

    money_flow_index_list = []

    for i in range(len_typical_prices - period + 1):
        money_flow_index_list.append(mfi(typical_prices[i:i+period], volume[i:i+period]))

    return money_flow_index_list

