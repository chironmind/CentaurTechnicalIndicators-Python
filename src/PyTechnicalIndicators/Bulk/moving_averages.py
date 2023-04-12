from ..Single import moving_averages as MAs

ma = ['ma', 'moving average', 'moving_average']
sma = ['sma', 'smoothed moving average', 'smoothed_moving_average']
ema = ['ema', 'exponential moving average', 'exponential_moving_average']


def moving_average(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the moving average for a list of prices and a certain period, returns a list of moving averages.
    :param prices: List of prices
    :param period: Period for which the moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of moving averages
    """
    # MA gives an idea of the trend and whether it's going to switch bull/bear
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    moving_averages = []
    if fill_empty:
        for i in range(period):
            moving_averages.append(fill_value)
    for i in range(period, len(prices)):
        price_set = prices[i - period:i]
        moving_averages.append(MAs.moving_average(price_set))
    return moving_averages


def exponential_moving_average(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the exponential moving average for a list of prices and a certain period, returns a list of exponential moving averages.
    :param prices: List of prices
    :param period: Period for which the exponential moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of exponential moving averages
    """
    return personalised_moving_average(prices, period, 2, 1, fill_empty, fill_value)


def smoothed_moving_average(prices: list[float], period: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the smoothed moving average for a list of prices and a certain period, returns a list of smoothed moving averages.
    :param prices: List of prices
    :param period: Period for which the smoothed moving average should be calculated for
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of smoothed moving averages
    """
    return personalised_moving_average(prices, period, 1, 0, fill_empty, fill_value)


def personalised_moving_average(prices: list[float], period: int, alpha_nominator: int, alpha_denominator: int, fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the personalised moving average for a list of prices and a certain period, returns a list of personalised moving averages.

    Moving averages are calculated using an alpha nominator and an alpha denominator. For example when calculating the
    exponential moving average the alpha nominator is 2 and the denominator is 1. For the smoothed moving average the
    nominator is 1 and the denominator is 0.
    :param prices: List of prices
    :param period: Period for which the smoothed moving average should be calculated for
    :param alpha_nominator: Nominator used when calculating the alpha
    :param alpha_denominator: Denominator used when calculating the alpha
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of smoothed moving averages
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < 0:
        raise Exception('Length of prices needs to be greater than 0')

    pma = []
    if fill_empty:
        for i in range(period):
            pma.append(fill_value)
    for i in range(period, len(prices)):
        price_set = prices[i - period: i]
        single_pma = MAs.personalised_moving_average(price_set, alpha_nominator, alpha_denominator)
        pma.append(single_pma)
    return pma


def moving_average_convergence_divergence(prices: list[float], fill_empty: bool = False, fill_value: any = None) -> list[float]:
    """
    Calculates the MACD line

    :param prices: list of prices
    :param fill_empty: Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of MACD points
    """
    if len(prices) < 26:
        raise Exception('The minimum length of prices needs to be 26 to calculate the MACD')
    return personalised_macd(prices, 12, 26, 'ema', fill_empty, fill_value)


def signal_line(macd: list[float], fill_empty: bool = False, fill_value: any = None):
    """
    Calculates the Signal line for the MACD

    :param macd: List of MACD points
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of Signal line points
    """
    if len(macd) < 9:
        raise Exception("Submitted MACD needs to be greater 9 lags long")
    return personalised_signal_line(macd, 9, 'ema', fill_empty, fill_value)

# TODO: Allow for PMA
def personalised_macd(prices: list[float], short_period: int, long_period: int, ma_model: str = 'ema', fill_empty: bool = False, fill_value: bool = None):
    """
    Calculates a personalised MACD.

    The default MACD uses a short period of 12, a long period of 26, and uses an Exponential Moving Average model to calculate
    the MACD. This function allows for the MACD to match any markets that may trade on a different time frame.
    :param prices: List of prices
    :param short_period: A number for the short period, must be greater than 0 and greater than the long period
    :param long_period: A number for the long period, must be greater than 0
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of MACD points
    """
    if short_period <= 0 or long_period <= 0:
        raise Exception('Period needs to be at least 1')

    if len(prices) < long_period:
        raise Exception(f'The minimum length of prices needs to be {long_period} to calculate the MACD')

    macd = []
    if fill_empty:
        for i in range(long_period):
            macd.append(fill_value)
    for i in range(long_period, len(prices)):
        price_set = prices[i - long_period: i]
        single_macd = MAs.personalised_macd( price_set, short_period, long_period, ma_model)
        macd.append( single_macd )
    return macd

# TODO: Support PMA
def personalised_signal_line(macd: list[float], period: int, ma_model: str = 'ema', fill_empty: bool = False, fill_value: any = None):
    """
    Calculates a personalised Signal line

    The default signal line calculation uses a period of 9 and an Exponential Moving Average model. This function allows
    the signal line calculation to be more in line with the market.
    :param macd: List of MACDs
    :param period: Number of periods for which the moving average should be calculated for
    :param ma_model: Name of the moving average that should be used. Supported models are:
        'ma', 'moving average', 'moving_average', 'sma', 'smoothed moving average', 'smoothed_moving_average', 'ema', 'exponential moving average', 'exponential_moving_average'
        Defaults to 'ema'
    :param fill_empty: (Optional) Whether empty values should be filled with the fill_value (default False)
    :param fill_value: (Optional) The fill value to fill empty values with if fill_empty is True (default None)
    :return: Returns a list of Signal line points
    """
    if period <= 0:
        raise Exception('Period needs to be at least 1')

    macd_len = len(macd)
    if macd_len == 0:
        raise Exception("Submitted MACD array is too short to calculate singal line")

    signal_lines = []
    if fill_empty:
        for i in range(period):
            signal_lines.append(fill_value)
    for i in range(period, macd_len):
        macd_set = macd[i-period: i]
        signal_line = MAs.personalised_signal_line(macd_set, ma_model)
        signal_lines.append(signal_line)
    return signal_lines

# TODO: Moving Median


def mcginley_dynamic(prices: list[float], period: int) -> list[float]:
    """
    The McGinley Dynamic offers an alternative to the moving average, the idea is that it should be more resilient to
    shocks than moving average models
    :param prices: List of prices
    :param period: The period works in a similar manner to the period for moving average models, the higher the period,
    the smoother the line
    :return: Returns a list of McGinley Dynamics
    """
    initial_mcginley_dynamic = MAs.mcginley_dynamic(prices[0], period)
    mcginley_dynamic_list = [initial_mcginley_dynamic]
    for price in prices[1:]:
        mcginley_dynamic_list.append(MAs.mcginley_dynamic(price, period, mcginley_dynamic_list[-1]))
    return mcginley_dynamic_list