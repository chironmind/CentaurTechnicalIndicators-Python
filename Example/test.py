
import pandas
# import matplotlib.pyplot as plt
from PyTechnicalIndicators.Bulk import basic_indicators, moving_averages

# TODO: at the end of each of these add one to show the use of single

data = pandas.read_csv("orcl.csv", sep=',', index_col=0, parse_dates=True)
data.index.name = 'Date'

data['Typical Price'] = (data['High'] + data['Low'] + data['Close']) / 3

# log
log_df = pandas.DataFrame(data=data['Date'])
log_df['log'] = basic_indicators.log(data['Typical Price'])

log_diff_df = pandas.DataFrame(data=data['Date'])
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

# variance
variance_5_period = basic_indicators.variance(data['Typical Price'], 5)
variance_10_period = basic_indicators.variance(data['Typical Price'], 10)
variance_30_period = basic_indicators.variance(data['Typical Price'], 30)

# TODO: have last 5 in a table
print(variance_5_period[-5:])
print(variance_10_period[-5:])
print(variance_30_period[-5:])

# Moving Average
moving_averages_df = pandas.DataFrame(data=data)
moving_averages_df['5 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 5)
moving_averages_df['10 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 10)
moving_averages_df['30 day MA'] = moving_averages.moving_average(moving_averages_df['Typical Price'], 30)

# TODO: graph
print(moving_averages_df)

# Smoothed Moving Average
smoothed_moving_averages_df = pandas.DataFrame(data=data)
smoothed_moving_averages_df['5 day MA'] = moving_averages.smoothed_moving_average(smoothed_moving_averages_df['Typical Price'], 5)
smoothed_moving_averages_df['10 day MA'] = moving_averages.smoothed_moving_average(smoothed_moving_averages_df['Typical Price'], 10)
smoothed_moving_averages_df['30 day MA'] = moving_averages.smoothed_moving_average(smoothed_moving_averages_df['Typical Price'], 30)

# TODO: graph
print(smoothed_moving_averages_df)


# Exponential Moving Average
exponential_moving_averages_df = pandas.DataFrame(data=data)
exponential_moving_averages_df['5 day MA'] = moving_averages.exponential_moving_average(exponential_moving_averages_df['Typical Price'], 5)
exponential_moving_averages_df['10 day MA'] = moving_averages.exponential_moving_average(exponential_moving_averages_df['Typical Price'], 10)
exponential_moving_averages_df['30 day MA'] = moving_averages.exponential_moving_average(exponential_moving_averages_df['Typical Price'], 30)

# TODO: graph
print(exponential_moving_averages_df)
