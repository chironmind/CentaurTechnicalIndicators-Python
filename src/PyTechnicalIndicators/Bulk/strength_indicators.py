from ..Single.moving_averages import moving_average, smoothed_moving_average, exponential_moving_average

# TODO: Call single RSI to avoid dup lines of code
def relative_strength_index(prices: list[float], fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the RSI from a list of prices
    :param prices: List of prices
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns the RSI as a list
    """
    if len(prices) < 14:
        raise Exception(f'14 periods are needed to calculate RSI {len(prices)} have been provided')

    rsi = []
    if fill_empty:
        for i in range(14):
            rsi.append(fill_value)
    for i in range(14, len(prices)):

        previous_gains = []
        previous_loss = []

        for j in range(i, i-14, -1):
            # More recent value at the end of the list so you'll want to reverse loop
            # If current price is greater than previous then we're going up
            if j == 0:
                continue

            if prices[j] > prices[j-1]:
                previous_gains.append(prices[j] - prices[j-1])
            elif prices[j] < prices[j-1]:
                previous_loss.append(prices[j-1] - prices[j])

        if previous_gains:
            if len(previous_gains) == 1:
                previous_average_gains = previous_gains[0]
            else:
                previous_average_gains = smoothed_moving_average(previous_gains)
        else:
            previous_average_gains = 0
        if previous_loss:
            if len(previous_loss) == 1:
                previous_average_loss = previous_loss[0]
            else:
                previous_average_loss = smoothed_moving_average(previous_loss)
        else:
            previous_average_loss = 0

        if previous_average_loss == 0:
            rsi.append(100)
            continue

        relative_strength = previous_average_gains / previous_average_loss

        rsi.append(100 - (100 / (1 + relative_strength)))

    return rsi


def stochastic_oscillator(close_prices: list[float], fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the SO from a list of closing prices
    :param close_prices: List of closing prices
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of SO
    """
    if len(close_prices) < 14:
        raise Exception(f'14 periods are needed to calculate RSI {len(close_prices)} have been provided')

    so = []
    if fill_empty:
        for i in range(14):
            so.append(fill_value)
    for i in range(14, len(close_prices)):
        lowest_closing = min(close_prices[i-14:i])
        highest_closing = max(close_prices[i-14:i])
        previous_close = close_prices[i-1]

        so.append(((previous_close - lowest_closing) / (highest_closing - lowest_closing))*100)

    return so


# TODO: allow pma using kwargs
def personalised_rsi(prices: list[float], period: int, ma_model: str = 'sma', fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates a personalised RSI

    The default RSI uses a period of 14 and a Smoothed Moving Average model to calculate the RSI. This functions allows
    any period of MA model to be used to calculate the RSI
    :param prices: List of prices
    :param period: Number of periods for which the moving average should be calculated for
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'sma'
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of personalised RSI
    """
    if len(prices) < period:
        raise Exception(f'Submitted prices needs to be greater than submitted period of {period}')

    rsi = []
    if fill_empty:
        for i in range(period):
            rsi.append(fill_value)
    ma = ['ma', 'moving average', 'moving_average']
    sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
    ema = ['ema', 'exponential moving average', 'exponential_moving_average']

    for i in range(period, len(prices)):

        previous_gains = []
        previous_loss = []

        for j in range(i, i-period, -1):
            # More recent value at the end of the list so you'll want to reverse loop
            # If current price is greater than previous then we're going up
            if j == 0:
                continue

            if prices[j] > prices[j-1]:
                previous_gains.append(prices[j] - prices[j-1])
            elif prices[j] < prices[j-1]:
                previous_loss.append(prices[j-1] - prices[j])

        if ma_model in ma:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains[0]
                else:
                    previous_average_gains = moving_average(previous_gains)
            else:
                previous_average_gains = 0
            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss[0]
                else:
                    previous_average_loss = moving_average(previous_loss)
            else:
                previous_average_loss = 0
        elif ma_model in sma:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains[0]
                else:
                    previous_average_gains = smoothed_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss[0]
                else:
                    previous_average_loss = smoothed_moving_average(previous_loss)
            else:
                previous_average_loss = 0

        elif ma_model in ema:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains[0]
                else:
                    previous_average_gains = exponential_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss[0]
                else:
                    previous_average_loss = exponential_moving_average(previous_loss)
            else:
                previous_average_loss = 0

        else:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains[0]
                else:
                    previous_average_gains = smoothed_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss[0]
                else:
                    previous_average_loss = smoothed_moving_average(previous_loss)
            else:
                previous_average_loss = 0

        if previous_average_loss == 0:
            rsi.append(100)
            continue

        relative_strength = previous_average_gains / previous_average_loss

        rsi.append(100 - (100 / (1 + relative_strength)))

    return rsi


def personalised_stochastic_oscillator(close_prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates a personalised SO

    The normal period that the SO uses is 14 periods, this functions allows for any period to be used
    :param close_prices: list of close prices
    :param period: Number of periods for which the moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of personalised SO
    """
    if len(close_prices) < period:
        raise Exception(f'Submitted prices needs to be greater than submitted period of {period}')

    so = []
    if fill_empty:
        for i in range(period):
            so.append(fill_value)
    for i in range(period, len(close_prices)):
        lowest_closing = min(close_prices[i-period:i])
        highest_closing = max(close_prices[i-period:i])
        previous_close = close_prices[i-1]

        so.append(((previous_close - lowest_closing) / (highest_closing - lowest_closing))*100)

    return so
