from ..Single.moving_averages import moving_average, smoothed_moving_average, exponential_moving_average


def relative_strength_index(prices, fill_empty=False, fill_value=None):
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
                previous_average_gains = previous_gains
            else:
                previous_average_gains = smoothed_moving_average(previous_gains)
        else:
            previous_average_gains = 0
        if previous_loss:
            if len(previous_loss) == 1:
                previous_average_loss = previous_gains
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


def stochastic_oscillator(close_prices, fill_empty=False, fill_value=None):
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


def personalised_rsi(prices, period, ma_model='sma', fill_empty=False, fill_value=None):
    # TODO: allow pma
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
                    previous_average_gains = previous_gains
                else:
                    previous_average_gains = moving_average(previous_gains)
            else:
                previous_average_gains = 0
            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss
                else:
                    previous_average_loss = moving_average(previous_loss)
            else:
                previous_average_loss = 0
        elif ma_model in sma:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains
                else:
                    previous_average_gains = smoothed_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss
                else:
                    previous_average_loss = smoothed_moving_average(previous_loss)
            else:
                previous_average_loss = 0

        elif ma_model in ema:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains
                else:
                    previous_average_gains = exponential_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss
                else:
                    previous_average_loss = exponential_moving_average(previous_loss)
            else:
                previous_average_loss = 0

        else:
            if previous_gains:
                if len(previous_gains) == 1:
                    previous_average_gains = previous_gains
                else:
                    previous_average_gains = smoothed_moving_average(previous_gains)
            else:
                previous_average_gains = 0

            if previous_loss:
                if len(previous_loss) == 1:
                    previous_average_loss = previous_loss
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


def personalised_stochastic_oscillator(close_prices, period, fill_empty=False, fill_value=None):
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
