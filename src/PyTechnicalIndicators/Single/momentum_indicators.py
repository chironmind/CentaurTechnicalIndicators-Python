from src.PyTechnicalIndicators.Single import moving_averages as mam
from src.PyTechnicalIndicators.Single import basic_indicators as bi


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


def commodity_channel_index(typical_prices: list[float]):
    return personalised_commodity_channel_index(typical_prices)


def personalised_commodity_channel_index(typical_prices: list[float], ma_model: str = 'ma', absolute_deviation_model: str = 'mean') -> float:
    """
    A personalised version of the Commodity Channel Index
    :param typical_prices: List of typical prices
    :param ma_model: (Optional) Name of the moving average model that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ma'
    :param absolute_deviation_model: (Optional) Name of the absolute deviation model that should be used. Supported models are:
        'mean_absolute_difference', 'mean absolute difference', 'mean', 'median_absolute_difference', 'median absolute difference', 'median'
        'mode_absolute_difference', 'mode absolute difference', 'mode'
    :return:
    """
    if ma_model in mam.ma:
        moving_average = mam.moving_average(typical_prices)
    elif ma_model in mam.sma:
        moving_average = mam.smoothed_moving_average(typical_prices)
    elif ma_model in mam.ema:
        moving_average = mam.exponential_moving_average(typical_prices)
    else:
        raise Exception(f'{ma_model} is not an accepted MA model, please use either {mam.ma}, {mam.sma}, or {mam.ema}')

    if absolute_deviation_model in ['mean_absolute_difference', 'mean absolute difference', 'mean']:
        absolute_deviation = bi.mean_absolute_deviation(typical_prices)
    elif absolute_deviation_model in ['median_absolute_difference', 'median absolute difference', 'median']:
        absolute_deviation = bi.median_absolute_deviation(typical_prices)
    elif absolute_deviation_model in ['mode_absolute_difference', 'mode absolute difference', 'mode']:
        absolute_deviation = bi.mode_absolute_deviation(typical_prices)
    else:
        raise Exception(f'{absolute_deviation_model} is not an accepted absolute deviation model')

    return (typical_prices[-1] - moving_average) / (0.015 * absolute_deviation)
