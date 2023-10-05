from src.PyTechnicalIndicators.Single import moving_averages
from src.PyTechnicalIndicators.Single import other


# TODO: just call personalised with hardcoded values
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

    previous_average_gains = moving_averages.smoothed_moving_average(previous_gains)
    previous_average_loss = moving_averages.smoothed_moving_average(previous_loss)

    if previous_average_loss == 0:
        return 100

    relative_strength = previous_average_gains / previous_average_loss

    rsi = (100 - (100 / (1 + relative_strength)))
    return rsi


# TODO: support pma
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

    if ma_model in moving_averages.ma:
        previous_average_gains = moving_averages.moving_average(previous_gains)
        previous_average_loss = moving_averages.moving_average(previous_loss)
    elif ma_model in moving_averages.sma:
        previous_average_gains = moving_averages.smoothed_moving_average(previous_gains)
        previous_average_loss = moving_averages.smoothed_moving_average(previous_loss)
    elif ma_model in moving_averages.ema:
        previous_average_gains = moving_averages.exponential_moving_average(previous_gains)
        previous_average_loss = moving_averages.exponential_moving_average(previous_loss)
    else:
        # TODO: raise exception
        previous_average_gains = moving_averages.smoothed_moving_average(previous_gains)
        previous_average_loss = moving_averages.smoothed_moving_average(previous_loss)

    if previous_average_loss == 0:
        return 100

    relative_strength = previous_average_gains / previous_average_loss

    rsi = (100 - (100 / (1 + relative_strength)))
    return rsi


def accumulation_distribution_indicator(high: float, low: float, close: float, volume: float, previous_adi: float = 0) -> float:
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


def period_directional_indicator(high: list[float], low: list[float], previous_close: list[float]) -> tuple[float, float, float, float, float]:
    """
    Calculates the positive and negative directional index for the length of the submitted lists
    :param high: List of high prices
    :param low: List of low prices
    :param previous_close: List of previous closing prices
    :return: Returns the positive, negative directional indicators, true range, positive, and negative directional movement as a tuple of floats
    """
    length = len(high)
    if length != len(low) or len(previous_close) != length:
        raise Exception(f'Length of high ({length}), low ({len(low)}), and previous_close ({len(previous_close)}), need to match')

    positive_dm_sum = 0
    negative_dm_sum = 0
    tr = other.true_range(high[0], low[0], previous_close[0])
    for i in range(1, length):
        dm = directional_movement(high[i], high[i-1], low[i], low[i-1])
        if dm[1] == 'positive':
            positive_dm_sum += dm[0]
        elif dm[1] == 'negative':
            negative_dm_sum += dm[0]
        tr += other.true_range(high[i], low[i], previous_close[i])
    positive_di = (positive_dm_sum / tr) * 100
    negative_di = (negative_dm_sum / tr) * 100
    return positive_di, negative_di, tr, positive_dm_sum, negative_dm_sum


def period_directional_indicator_known_previous(current_high: float, previous_high: float, current_low: float, previous_low: float, previous_close: float, previous_true_range: float, previous_positive_dm: float, previous_negative_dm: float, period: int) -> tuple[float, float, float, float, float]:
    """
    Calculates the directional indicator for a period when the previous directional indicators are known
    :param current_high: Current high
    :param previous_high: Previous high
    :param current_low: Current low
    :param previous_low: Previous low
    :param previous_close: Previous close
    :param previous_directional_movement: Tuple of the previous positive, negative directional indicators, and true range
    :param period: Period directional indicator is being calculated for
    :return: Returns the positive, negative directional indicator, and true range as a tuple of floats
    """
    current_tr = other.true_range(current_high, current_low, previous_close)
    current_dm = directional_movement(current_high, previous_high, current_low, previous_low)
    if current_dm[1] == 'positive':
        current_positive_dm = known_previous_directional_movement(current_dm[0], previous_positive_dm, period)
        current_negative_dm = known_previous_directional_movement(0, previous_negative_dm, period)
    elif current_dm[1] == 'negative':
        current_positive_dm = known_previous_directional_movement(0, previous_positive_dm, period)
        current_negative_dm = known_previous_directional_movement(current_dm[0], previous_negative_dm, period)
    elif current_dm[1] == 'none':
        current_positive_dm = known_previous_directional_movement(0, previous_positive_dm, period)
        current_negative_dm = known_previous_directional_movement(0, previous_negative_dm, period)
    else:
        raise Exception(f'Unknown directional movement {current_dm[1]}')
    tr = known_previous_directional_movement(current_tr, previous_true_range, period)
    positive_di = (current_positive_dm/tr) * 100
    negative_di = (current_negative_dm/tr) * 100
    return positive_di, negative_di, tr, current_positive_dm, current_negative_dm


def known_previous_directional_movement(current_value: float, previous_value: float, period: int) -> float:
    """
    Used to calculate the directional indicator (or true range) when the previous value is known
    :param current_value: Current directional movement or true range
    :param previous_value: Previous directional indicator or true range
    :param period: The period that the directional indicator is being calculated for
    :return: Returns the directional indicator (or true range) as a float
    """
    return previous_value - (previous_value/period) + current_value


def directional_indicator(current_high: float, previous_high: float, current_low: float, previous_low: float, previous_close: float) -> tuple[float, str]:
    """
    Calculates the directional indicator according to Welles https://archive.org/details/newconceptsintec00wild/page/35/mode/2up
    :param current_high: Current high
    :param previous_high: Previous high
    :param current_low: Current low
    :param previous_low: Previous low
    :param previous_close: Previous close
    :return: Returns the directional indicator as a float with a string to note if it is "positive", "negative", or "none"
    """
    dm = directional_movement(current_high, previous_high, current_low, previous_low)
    tr = other.true_range(current_high, current_low, previous_close)
    return dm[0]/tr, dm[1]


def directional_movement(current_high: float, previous_high: float, current_low: float, previous_low: float) -> tuple[float, str]:
    """
    Calculates the directional movement according to Welles https://archive.org/details/newconceptsintec00wild/page/35/mode/2up
    :param current_high: Current high
    :param previous_high: Previous high
    :param current_low: Current low
    :param previous_low: Previous low
    :return: Returns the directional movement as a float with a string to note if it is "positive", "negative", or "none"
    """
    positive_directional_movement = current_high - previous_high
    negative_directional_movement = previous_low - current_low

    if positive_directional_movement > negative_directional_movement and positive_directional_movement > 0:
        return positive_directional_movement, 'positive'
    elif negative_directional_movement > positive_directional_movement and negative_directional_movement > 0:
        return negative_directional_movement, 'negative'
    else:
        return 0, 'none'


def directional_index(positive_directional_indicator: float, negative_directional_indicator: float) -> float:
    """
    Calculates the directional index according to Welles https://archive.org/details/newconceptsintec00wild/page/43/mode/2up
    :param positive_directional_indicator: Positive directional index
    :param negative_directional_indicator: Negative directional index
    :return:
    """
    if positive_directional_indicator >= negative_directional_indicator:
        nominator = positive_directional_indicator - negative_directional_indicator
    else:
        nominator = negative_directional_indicator - positive_directional_indicator
    denominator = positive_directional_indicator + negative_directional_indicator
    return nominator / denominator


# TODO: support pma
def average_directional_index(directional_index: list[float], moving_average_model: str = 'ma') -> float:
    """
    Calculates the average directional index for a list of directional indices
    :param directional_index: List of directional index
    :param moving_average_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'sma'
    :return:
    """

    if moving_average_model in moving_averages.ma:
        return moving_averages.moving_average(directional_index)
    elif moving_average_model in moving_averages.sma:
        return moving_averages.smoothed_moving_average(directional_index)
    elif moving_average_model in moving_averages.ema:
        return moving_averages.exponential_moving_average(directional_index)
    else:
        raise Exception(f'moving_average_model: {moving_average_model} is not an accepted moving average model')


def average_directional_index_rating(current_average_directional_index: float, previous_average_directional_index: float) -> float:
    """
    Calculates the average directoinal index rating according to Welles https://archive.org/details/newconceptsintec00wild/page/43/mode/2up
    :param current_average_directional_index: The current average directional index
    :param previous_average_directional_index: The average directional index from a predetermined period ago, normally 14
    :return: Returns the average directional index rating as a float
    """
    return (current_average_directional_index + previous_average_directional_index) / 2
