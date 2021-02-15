
import pandas
# import matplotlib.pyplot as plt
from PyTechnicalIndicators.Bulk import basic_indicators, moving_averages, strength_indicators
import random

# TODO: at the end of each of these add one to show the use of single

data = pandas.read_csv("orcl.csv", sep=',', index_col=0, parse_dates=True)
data.index.name = 'Date'
data['Typical Price'] = (data['High'] + data['Low'] + data['Close']) / 3

# Log
log_df = pandas.DataFrame(index=data.index)
log_df['log'] = basic_indicators.log(data['Typical Price'])

log_diff_df = pandas.DataFrame(index=data.index)
log_diff_df['log diff'] = basic_indicators.log_diff(data['Typical Price'])

# TODO: want to grph them and probably have them as separate time series
print(log_df)
print(log_diff_df)

# median
median_5_period = basic_indicators.median(data['Typical Price'], 5)
median_10_period = basic_indicators.median(data['Typical Price'], 10)
median_30_period = basic_indicators.median(data['Typical Price'], 30)

# TODO: have last 5 in a table
print(median_5_period[-5:])
print(median_10_period[-5:])
print(median_30_period[-5:])

# mean
mean_5_period = basic_indicators.mean(data['Typical Price'], 5)
mean_10_period = basic_indicators.mean(data['Typical Price'], 10)
mean_30_period = basic_indicators.mean(data['Typical Price'], 30)

# TODO: have last 5 in a table
print(mean_5_period[-5:])
print(mean_10_period[-5:])
print(mean_30_period[-5:])

# stddev
stddev_5_period = basic_indicators.stddev(data['Typical Price'], 5)
stddev_10_period = basic_indicators.stddev(data['Typical Price'], 10)
stddev_30_period = basic_indicators.stddev(data['Typical Price'], 30)

# TODO: have last 5 in a table
print(stddev_5_period[-5:])
print(stddev_10_period[-5:])
print(stddev_30_period[-5:])

# Variance
variance_5_period = basic_indicators.variance(data['Typical Price'], 5)
variance_10_period = basic_indicators.variance(data['Typical Price'], 10)
variance_30_period = basic_indicators.variance(data['Typical Price'], 30)

# TODO: have last 5 in a table
print(variance_5_period[-5:])
print(variance_10_period[-5:])
print(variance_30_period[-5:])

# Moving Average
# TODO: explain while fill empty == true
moving_averages_df = pandas.DataFrame(data=data, index=data.index, copy=True)
moving_averages_df['5 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 5, True)
moving_averages_df['10 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 10, True)
moving_averages_df['30 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 30, True)

# TODO: graph
print(moving_averages_df)

# Smoothed Moving Average
smoothed_moving_averages_df = pandas.DataFrame(data=data, index=data.index, copy=True)
smoothed_moving_averages_df['5 day SMA'] = moving_averages.smoothed_moving_average(
    smoothed_moving_averages_df['Typical Price'],
    5,
    True
)
smoothed_moving_averages_df['10 day SMA'] = moving_averages.smoothed_moving_average(
    smoothed_moving_averages_df['Typical Price'],
    10,
    True
)
smoothed_moving_averages_df['30 day SMA'] = moving_averages.smoothed_moving_average(
    smoothed_moving_averages_df['Typical Price'],
    30,
    True
)

# TODO: graph
print(smoothed_moving_averages_df)

# Exponential Moving Average
exponential_moving_averages_df = pandas.DataFrame(data=data, index=data.index, copy=True)
exponential_moving_averages_df['5 day EMA'] = moving_averages.exponential_moving_average(
    exponential_moving_averages_df['Typical Price'],
    5,
    True
)
exponential_moving_averages_df['10 day EMA'] = moving_averages.exponential_moving_average(
    exponential_moving_averages_df['Typical Price'],
    10,
    True
)
exponential_moving_averages_df['30 day EMA'] = moving_averages.exponential_moving_average(
    exponential_moving_averages_df['Typical Price'],
    30,
    True
)

# TODO: graph
print(exponential_moving_averages_df)

# Personalised Moving Average
# TODO: explain random alpha nomitaor and denominator
random_alpha_nominator = random.uniform(0, 2)
print(f'random_alpha_nominator: {random_alpha_nominator}')
random_alpha_denominator = random.random()
print(f'random_alpha_denominator: {random_alpha_denominator}')

personalised_moving_averages_df = pandas.DataFrame(data=data, index=data.index, copy=True)
personalised_moving_averages_df['5 day PMA'] = moving_averages.personalised_moving_average(
    personalised_moving_averages_df['Typical Price'],
    5,
    random_alpha_nominator,
    random_alpha_denominator,
    True
)
personalised_moving_averages_df['10 day PMA'] = moving_averages.personalised_moving_average(
    personalised_moving_averages_df['Typical Price'],
    10,
    random_alpha_nominator,
    random_alpha_denominator,
    True)
personalised_moving_averages_df['30 day PMA'] = moving_averages.personalised_moving_average(
    personalised_moving_averages_df['Typical Price'],
    30,
    random_alpha_nominator,
    random_alpha_denominator,
    True)

# TODO: graph
print(personalised_moving_averages_df)

# MACD
macd = moving_averages.moving_average_convergence_divergence(data['Typical Price'])
signal_line = moving_averages.signal_line(macd)
macd_diff = [macd[i] - signal_line[i-25] for i in range(len(macd[25:]))]

# TODO: graph all three together
print(macd)
print(signal_line)
print(macd_diff)

# Personalised MACD
# TODO: Explain why there's a personalised and how to use
personalised_macd = moving_averages.personalised_macd(data['Typical Price'], 5, 30)
personalised_signal_line = moving_averages.personalised_signal_line(personalised_macd, 5)
personalised_macd_diff = [personalised_macd[i] - personalised_signal_line[i-25] for i in range(len(personalised_macd[25:]))]

# TODO: graph all three together
print(personalised_macd)
print(personalised_signal_line)
print(personalised_macd_diff)

# RSI
rsi = strength_indicators.relative_strength_index(data['Typical Price'])
# TODO: Graph
print(rsi)

# Personalised RSI
# TODO: Explain options
personalised_rsi = strength_indicators.personalised_rsi(data['Typical Price'], 10, 'ema')
# TODO: graph
print(personalised_rsi)

# SO
stochastic_oscillator = strength_indicators.stochastic_oscillator(data['Typical Price'])
# TODO: Graph
print(stochastic_oscillator)

# Personalised SO
personalised_stochastic_oscillator = strength_indicators.personalised_stochastic_oscillator(data['Typical Price'], 10)
# TODO: Graph
print(personalised_stochastic_oscillator)
