from .moving_averages import moving_average, smoothed_moving_average, exponential_moving_average
from src.PyTechnicalIndicators.Single.volatility import average_true_range

def relative_strength_index(prices: list[float]) -> float:
    """
    Calculate the RSI for a list of prices
    :param prices: list of prices
    :return: Returns the RSI as a float
    """
    prices_length = len(prices)
    if prices_length != 14:
        raise Exception(f'14 periods are needed to calculate RSI, {prices_length} have been provided')

    previous_gains = []
    previous_loss = []

    for i in range(prices_length - 1, 0, -1):
        if i == 0:
            continue

        if prices[i] > prices[i - 1]:
            previous_gains.append(prices[i] - prices[i - 1])
        elif prices[i] < prices[i - 1]:
            previous_loss.append(prices[i - 1] - prices[i])

    # TODO: deal with no loss scenario
    previous_average_gains = smoothed_moving_average(previous_gains)
    previous_average_loss = smoothed_moving_average(previous_loss)

    if previous_average_loss == 0:
        return 100

    relative_strength = previous_average_gains / previous_average_loss

    rsi = (100 - (100 / (1 + relative_strength)))
    return rsi


def stochastic_oscillator(close_prices: list[float]) -> float:
    """
    Calculates the SO for a list of closing prices
    :param close_prices: list of closing prices
    :return: Returns the SO as a float
    """
    if len(close_prices) != 14:
        raise Exception(f'14 periods are needed to calculate SO, {len(close_prices)} have been provided')

    lowest_closing = min(close_prices)
    highest_closing = max(close_prices)
    previous_close = close_prices[-1]

    so = ((previous_close - lowest_closing) / (highest_closing - lowest_closing)) * 100
    return so


def personalised_rsi(prices: list[float], ma_model: str = 'sma') -> float:
    """
    Calculates a personalised RSI based on the price and a chose MA model
    :param prices: list of prices
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'sma'
    :return: Returns the RSI as a float
    """
    # Let used input own length
    prices_length = len(prices)
    if prices_length < 1:
        raise Exception('Submitted prices needs to be greater than 0')

    previous_gains = []
    previous_loss = []

    for i in range(prices_length - 1, 0, -1):
        if i == 0:
            continue

        if prices[i] > prices[i - 1]:
            previous_gains.append(prices[i] - prices[i - 1])
        elif prices[i] < prices[i - 1]:
            previous_loss.append(prices[i - 1] - prices[i])

    ma = ['ma', 'moving average', 'moving_average']
    sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
    ema = ['ema', 'exponential moving average', 'exponential_moving_average']

    if ma_model in ma:
        previous_average_gains = moving_average(previous_gains)
        previous_average_loss = moving_average(previous_loss)
    elif ma_model in sma:
        previous_average_gains = smoothed_moving_average(previous_gains)
        previous_average_loss = smoothed_moving_average(previous_loss)
    elif ma_model in ema:
        previous_average_gains = exponential_moving_average(previous_gains)
        previous_average_loss = exponential_moving_average(previous_loss)
    else:
        previous_average_gains = smoothed_moving_average(previous_gains)
        previous_average_loss = smoothed_moving_average(previous_loss)

    if previous_average_loss == 0:
        return 100

    relative_strength = previous_average_gains / previous_average_loss

    rsi = (100 - (100 / (1 + relative_strength)))
    return rsi


def personalised_stochastic_oscillator(close_prices: list[float]) -> float:
    """
    Calculates a personalised version of the SO

    Main difference is that in normal SO the length of the input list has to be 14, however this function accepts anything
    :param close_prices: list of close prices
    :return: Returns the SO as a float
    """
    # Let used input own length
    if len(close_prices) < 1:
        raise Exception(f'Submitted prices needs to be greater than 0')

    lowest_closing = min(close_prices)
    highest_closing = max(close_prices)
    previous_close = close_prices[-1]

    so = ((previous_close - lowest_closing) / (highest_closing - lowest_closing)) * 100
    return so


def accumulation_distribution_indicator(high: float, low: float, close: float, volume: float, previous_adi: float) -> float:
    """
    Calculates the accumulation distribution indicator

    :param high: High price
    :param low: Low price
    :param close: Closing price
    :param volume: Volume
    :param previous_adi: Previous accumulation distribution indicator
    :return: Returns the accumulation distribution indicator as a float
    """
    money_flow_multiplier = ((close - low) - (high - close)) / (high - low)
    money_flow_volume = money_flow_multiplier * volume
    return previous_adi + money_flow_volume


def average_directional_index(current_high: float, previous_high: float, current_low: float, previous_low: float) -> float:
    """

    :param current_high:
    :param previous_high:
    :param current_low:
    :param previous_low:
    :return:
    """
    pass


# TODO: Check math by hand
def personalised_average_directional_index(high: list[float], low: list[float], close: list[float], previous_adi: float, period: int) -> float:
    """
    Calculates the average directional index and returns it as a float

    Calculated according to "New concepts in technical trading systems" (1978) - Wilder, J. Welles https://archive.org/details/newconceptsintec00wild/page/43/mode/2up
    The personalised version allows for any period to be used
    :param high:
    :param low:
    :param close:
    :param previous_adi:
    :param period:
    :return:
    """
    length = len(high)
    if length != len(low) or len(high) != len(close):
        raise Exception(f'Lengths needs to match, high: {length}, low: {len(low)}, close {len(close)}')

    if period > length:
        raise Exception(f'Period ({period}) needs to be smaller or equal length of lists ({length})')

    if previous_adi != 0:
        dmi = directional_movement_index(high[-period:], low[-period:], close[-period:])
        return ((previous_adi * period - 1) + dmi) / period
    else:
        
        dmi_list = []
        for i in range(length - period):
            dmi_list.append(directional_movement_index(high[i:i+period], low[i:i+period], close[i:i+period]))
        return sum(dmi_list) / len(dmi_list)


def directional_movement_index(high: list[float], low: list[float], close: list[float]) -> float:
    """

    :param high:
    :param low:
    :param close:
    :return:
    """
    positive_directional_movement = high[-1] - high[-2]
    negative_directional_movement = low[-2] - low[-1]

    if positive_directional_movement > negative_directional_movement:
        negative_directional_movement = 0
    else:
        positive_directional_movement = 0
    sum_positive_directional_movement = 0

    for i in range(1, len(high)):
        sum_positive_directional_movement += high[i] - high[i - 1]
    positive_directional_movement_average = sum_positive_directional_movement / len(high)
    smoothed_positive_directional_movement = (sum_positive_directional_movement - positive_directional_movement_average) + positive_directional_movement
    sum_negative_directional_movement = 0

    for i in range(1, len(low)):
        sum_negative_directional_movement += low[i - 1] - low[i]
    negative_directional_movement_average = sum_negative_directional_movement / len(low)
    smoothed_negative_directional_movement = (sum_negative_directional_movement - negative_directional_movement_average) + negative_directional_movement

    atr = average_true_range(high, low, close, 0)
    positive_directional_index = (smoothed_positive_directional_movement / atr) * 100
    negative_directional_index = (smoothed_negative_directional_movement / atr) * 100
    return (abs(positive_directional_index - negative_directional_index) / abs(positive_directional_index + negative_directional_index)) * 100
