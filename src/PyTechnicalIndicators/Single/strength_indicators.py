from .moving_averages import moving_average, smoothed_moving_average, exponential_moving_average


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
