from src.PyTechnicalIndicators.Single.momentum_indicators import rate_of_change as roc
from src.PyTechnicalIndicators.Single.momentum_indicators import on_balance_volume as obv
from src.PyTechnicalIndicators.Single.momentum_indicators import personalised_commodity_channel_index as cci

def rate_of_change(closing_prices: list[float], period: int) -> list[float]:
    """
    Calculates and returns the rate of change of a list of closing prices for a provided period

    This function will calculate the rate of change based on the following formula:
        rate_of_change = ((closing_prices[t] - closing_prices[t-n]) / closing_prices[t-period]) * 100
    The period will determine where the function will fetch the previous close price from. For example if you provide the
    following list:
        closing_prices = [ 100, 110, 105, 120, 120, 130 ]
    and provide a period of 2, the rates of change that will be calculated will be for the following pairs:
        * 100 and 105
        * 110 and 120
        * 105 and 120
        * 120 and 130
    This function assumes that the older prices are at the beginning of the list and the more recent ones at the end
    :param closing_prices: List of closing prices
    :param period: Period for which the rate of change needs to be calculated for
    :return: Returns a list of rates of change
    """
    len_closing = len(closing_prices)

    if period > len_closing:
        raise Exception('Period has to be greater or equal to the length of closing prices')

    rates_of_change = []
    for i in range(len_closing - period):
        rates_of_change.append(roc(current_close_price=closing_prices[i+period], previous_close_price=closing_prices[i]))

    return rates_of_change


def on_balance_volume(closing_prices: list[float], volume: list[int]) -> list[float]:
    if len(closing_prices) != len(volume):
        raise Exception(f'Length closing_prices ({len(closing_prices)}) has to equal length volume ({len(volume)})')

    obv_list = [volume[0]]
    for i in range(1, len(closing_prices)):
        obv_list.append(obv(closing_prices[i], closing_prices[i-1], volume[i], obv_list[-1]))

    return obv_list


def personalised_commodity_channel_index(typical_prices: list[float], period: int, ma_model: str = 'ma', absolute_deviation_model: str = 'mean') -> list[float]:
    """

    :param typical_prices:
    :param period:
    :param ma_model:
    :param absolute_deviation_model:
    :return:
    """
    if len(typical_prices) < period:
        raise Exception(f'typical_prices ({len(typical_prices)}) needs to be greater or equal to the period ({period})')
    cci_list = []
    for i in range(len(typical_prices)-period+1):
        cci_list.append(cci(typical_prices[i:i+period], ma_model, absolute_deviation_model))
    return cci_list
