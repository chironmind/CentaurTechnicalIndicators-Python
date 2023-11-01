# PyTechnicalIndicators

A simple, lightweight package used to calculate Technical Indicators in Python.

This package only uses Python built in types, and the Python standard library.

## Installation

Install using pip

```shell
pip install PyTechnicalIndicators
```

## Usage

To see this package in use and explanations go to the [PyTechnicalIndicators Example Repo](www.github.com/0100101001010000/PyTechnicalIndicators_Examples),
this README is specific to calling functions in the package.

The PyTechnicalIndicators package is split into three directories.

`Bulk` is used to calculate multiple Technical Indicators for a large list of prices.

`Single` is used to calculate a singe Technical Indicator for a price.

`Chart Patterns` is used to calculate chart patterns to be displayed on OHLC charts.

### Bulk
The `Bulk` directory has 11 files used to calculate different Technical Indicator areas.

#### Basic Indicators
`basic_indicators` has functions native to the Python standard library that get calculated for a list of asset prices and
returns a list of technical indicators.

##### Log
Calculates the log for a list of prices
```python
from PyTechnicalIndicators.Bulk.basic_indicators import log
prices = [100, 102, 105, 103, 108]
bulk_log = log(prices)
print(bulk_log)
# will print [4.605170185988092, 4.624972813284271, 4.653960350157523, 4.634728988229636, 4.68213122712422]
```

##### Log Differnce
Calculates difference in log between a price at t and t-1
```python
from PyTechnicalIndicators.Bulk.basic_indicators import log_diff
prices = [100, 102, 105, 103, 108]
bulk_log_diff = log_diff(prices)
print(bulk_log_diff)
# will print [0, 0.019802627296178876, 0.028987536873252395, -0.019231361927887214, 0.04740223889458406]
```
The first value will always be 0 because there is no other value to do the difference against.

##### Standard Deviation
Calculates the standard deviation of a list of prices over a period. Period parameter that needs to be 
determined by the caller
```python
from PyTechnicalIndicators.Bulk.basic_indicators import standard_deviation
prices = [100, 102, 105, 103, 108]
bulk_stddev = standard_deviation(prices, 3)
print(bulk_stddev)
# will print [2.516611478423583, 1.5275252316519468, 2.516611478423583]
```

##### Mean
Calculates price average over a period. Period needs to be determined by the caller. 
```python
from PyTechnicalIndicators.Bulk.basic_indicators import mean
prices = [100, 102, 105, 103, 108]
bulk_mean = mean(prices, 3)
print(bulk_mean)
# will print [102.333333333333333, 103.3333333333333333, 105.333333333333333]
```

##### Median
Calculates the price median over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.basic_indicators import median
prices = [100, 102, 105, 103, 108]
bulk_median = median(prices, 3)
print(bulk_median)
# will print [102, 103, 105]
```

##### Variance
Calculates price variance over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.basic_indicators import variance
prices = [100, 102, 105, 103, 108]
bulk_variance = variance(prices, 3)
print(bulk_variance)
# will print [6.33333333333333333, 2.3333333333333333, 6.333333333333333]
```

##### Mean Absolute Deviation
Calculates the prices absolute deviation from the mean over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.basic_indicators import mean_absolute_deviation
prices = [100, 102, 105, 103, 108]
bulk_mean_absolute_deviation = mean_absolute_deviation(prices, 3)
print(bulk_mean_absolute_deviation)
# will print [1.7777777777777761, 1.1111111111111096, 1.7777777777777761]
```

##### Median Absolute Deviation
Calculates the prices absolute deviation from the median over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.basic_indicators import median_absolute_deviation
prices = [100, 102, 105, 103, 108]
bulk_median_absolute_deviation = median_absolute_deviation(prices, 3)
print(bulk_median_absolute_deviation)
# will print [1.6666666666666667, 1.0, 1.6666666666666667]
```

##### Mode Absolute Deviation
Calculates the prices absolute deviation from the median over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.basic_indicators import mode_absolute_deviation
prices = [100, 102, 105, 103, 108]
bulk_mode_absolute_deviation = mode_absolute_deviation(prices, 3)
print(bulk_mode_absolute_deviation)
# will print [2.3333333333333335, 1.3333333333333333, 1.6666666666666667]
```

#### Candle Indicators
`candle_indicators` has technical indicators intended to be used on OHLC charts.

##### Bollinger Bands
Calculates the Bollinger Bands for typical prices. The period defaults to 20, moving average model defaults to 'ma' 
(moving average), and the standard deviation multiplier defaults to 2. These can be changed by the caller.

The first item in the tuple is the lower band, the second item is the upper band.
```python
from PyTechnicalIndicators.Bulk.candle_indicators import bollinger_bands
# Default Bollinger Bands
prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 110, 108]
bbands = bollinger_bands(prices)
print(bbands)
# will print [(96.36499833879442, 119.33500166120557), (96.91237286601877, 119.48762713398123), (97.16213062944371, 119.53786937055628)]

# Personalised Bollinger Bands
prices = [110, 107, 108, 105, 103, 106, 107, 110, 108]
personalised_bbands = bollinger_bands(prices, period=7, ma_model='ema', stddev_multiplier=3)
print(personalised_bbands) 
# will print [(99.46018315489414, 112.81255052123461), (100.42609144537805, 113.77845881171852), (100.49915238054767, 114.23128362705957)]
```

##### Ichimoku Cloud
Calculates the Ichimoku Cloud from high, low, and closing prices. The conversion period defaults to 9, the base period
defaults to 26, and the span B period defaults to 52. These can be changed by the caller.

Returns the leading span A, leading span B, baseline, conversion line, and lagged close based on the base period, in that order.
```python
from PyTechnicalIndicators.Bulk.candle_indicators import ichimoku_cloud
# Default Ichimoku Cloud
highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120, 104, 111, 113, 114, 107, 102, 103, 111, 108, 107, 118,
         106, 109, 118, 114, 108, 120, 103, 119, 119, 110, 100, 118, 111, 101, 105, 113, 112, 103, 117, 107, 115,
         114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 113, 119]
lows = [114, 111, 103, 100, 103, 96, 100, 101, 91, 115, 93, 98, 107, 95, 104, 99, 95, 94, 96, 92, 114, 97, 108, 106,
        107, 106, 97, 101, 92, 107, 110, 91, 101, 104, 93, 97, 92, 106, 102, 96, 100, 102, 109, 113, 109, 108, 95,
        95, 98, 94, 104, 98, 99, 103]
close = [114, 116, 108, 100, 103, 102, 106, 101, 103, 118, 102, 106, 112, 101, 107, 99, 101, 111, 103, 106, 116,
         106, 108, 106, 113, 106, 109, 103, 106, 118, 110, 94, 109, 107, 93, 101, 103, 110, 102, 102, 102, 112, 111,
         115, 110, 108, 103, 98, 98, 95, 113, 112, 109, 114]
icloud = ichimoku_cloud(highs, lows, close)
print(icloud) 
# will print [(105.25, 105.5, 105.5, 105, 109), (105.0, 105.5, 105, 105, 103), (105.75, 105.5, 105, 106.5, 106)]

# Personalised Ichimoku Cloud
highs = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
lows = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
close = [99, 103, 108, 113, 115, 110, 108, 96, 95, 99, 99, 109, 108, 113, 116]
icloud = ichimoku_cloud(highs, lows, close, conversion_period=5, base_period=3, span_b_period=13)
print(icloud) 
# will print [(105.0, 105.5, 105, 105, 99), (106.25, 106.0, 106.5, 106, 109), (106.5, 106.5, 106.5, 106.5, 108)]
```

#### Correlation Indicators
`correlation_indicators` are indicators that calculate the correlation between two assets.

##### Correlate Asset Prices
Calculates the price correlation between two asset prices over a given period. Period needs to be determined by caller.
```python
from PyTechnicalIndicators.Bulk.correlation_indicators import correlate_asset_prices
asset_a_price = [120, 110, 105, 112, 114, 116]
asset_b_price = [150, 155, 162, 165, 159, 154]
correlation = correlate_asset_prices(asset_a_price, asset_b_price, 5)
print(correlation) 
# will print [-0.65025528597848, -0.4217205045478597]
```

#### Momentum Indicators
`momentum_indicators` are indicators that calculate price momentum of an asset.

##### Rate of Change
Calculates the rate of change of an asset over a period. Period needs to be determined by caller.
```python
from PyTechnicalIndicators.Bulk.momentum_indicators import rate_of_change
closing_prices = [100, 101, 105, 103, 99, 80, 85, 100, 90, 85]
roc = rate_of_change(closing_prices, 3)
print(roc) 
# will print [3.0, -1.9801980198019802, -23.809523809523807, -17.475728155339805, 1.0101010101010102, 12.5, 0]
```

##### On Balance Volume
Calculates the on balance volume from asset prices and volume.
```python
from PyTechnicalIndicators.Bulk.momentum_indicators import on_balance_volume
closing_prices = [100, 105, 111, 107, 108]
volume = [1200, 1800, 1600, 1700, 1500]
obv = on_balance_volume(closing_prices, volume)
print(obv) 
# will print [1200, 3000, 4600, 2900, 4400]
```

##### Commodity Channel Index
Calculates the commodity channel index from typical prices over a given period. Period needs to be determined by caller.
Moving average model defaults to 'ma' (moving average) and absolute deviation model default to 'mean'. These can be
changed by caller.

```python
from PyTechnicalIndicators.Bulk.momentum_indicators import commodity_channel_index
# Default Commodity Channel Index
prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
cci = commodity_channel_index(prices, 7)
print(cci) 
# [-119.7640117994101, -86.35170603674531, -94.51476793248943]

prices = [103, 106, 111, 113, 111, 102, 98, 99, 95]
personalised_cci = commodity_channel_index(prices, period=7, ma_model='ema', absolute_deviation_model='median')
print(cci) 
```

#### Moving Averages
`moving_averages` has indicators related to calculating and using moving averages.

##### Moving Average
Calculates the moving average of an asset over a given period. Period needs to be determined by caller.
```python
from PyTechnicalIndicators.Bulk.moving_averages import moving_average
prices = [110, 107, 108, 105, 103, 106, 107]
mas = moving_average(prices, 5)
print(mas) 
# [106.6, 105.8, 105.8]
```

##### Exponential Moving Average
Calculates the exponential moving average of an asset over a given period. Period needs to be determined by caller.
```python
from PyTechnicalIndicators.Bulk.moving_averages import exponential_moving_average
prices = [110, 107, 108, 105, 103, 106, 107]
emas = exponential_moving_average(prices, 5)
print(emas) 
# [105.35071090047394, 105.36492890995261, 105.9099526066351]
```

##### Smoothed Moving Average
Calculates the smoothed moving average of an asset over a given period. Period needs to be determined by caller.
```python
from PyTechnicalIndicators.Bulk.moving_averages import smoothed_moving_average
prices = [110, 107, 108, 105, 103, 106, 107]
smas = smoothed_moving_average(prices, 5)
print(smas) 
# [105.89005235602093, 105.52213231794384, 105.81770585435507]
```

##### Personalised Moving Average
The `personalised_moving_average` is an internal function used by the smoothed (nominator=1, denominator=0), and the
exponential (nominator=2, denominator=1) moving average functions as the underlying logic is indentical with changes in
the nominator and denominator of the alpha variables for each. This function is exposed in the event that the caller 
knows what they're doing, or feel lucky, and wants to tweak the alpha when calculating the moving average.
```python
from PyTechnicalIndicators.Bulk.moving_averages import personalised_moving_average
prices = [110, 107, 108, 105, 103, 106, 107]
pmas = personalised_moving_average(prices, period=5, alpha_nominator=5, alpha_denominator=3)
print(pmas)
```

##### Moving Average Convergence Divergence
Calculates the Moving Average Convergence Divergence (MACD). This is a high level function that calls `macd_line`, 
`signal_line`, and does the difference of the two to allow a histogram to be charted. It returns the three in that 
order.

The `macd_line` and `signal_line` can be called independently and are covered below.
```python
from PyTechnicalIndicators.Bulk.moving_averages import moving_average_convergence_divergence
# Default MACD
prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101,
              99, 103, 106, 104, 102, 109, 116]
macd = moving_average_convergence_divergence(prices)
print(macd)

# Personalised MACD
personalised_macd = moving_average_convergence_divergence(prices, macd_short_period=3, macd_long_period=9, signal_period=3, ma_model='ma')
print(personalised_macd)
```

##### MACD Line
Calculate the MACD line for `moving_average_convergence_divergence`. The short period defaults to 12, the long period
defaults to 26, and the moving average model defaults to 'ema' (exponential moving average).
```python
from PyTechnicalIndicators.Bulk.moving_averages import macd_line
# Default MACD Line
prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101,
              99, 103, 106, 104, 102, 109, 116]
macd = macd_line(prices)
print(macd)
# [-2.164962379494412, -1.597159438916961, -0.4970353844502142]

# Personalised MACD Line
prices = [110, 107, 108, 105, 103, 106, 107]
pers_macd = macd_line(prices, short_period=3, long_period=5, ma_model='ma')
print(pers_macd) 
# [-1.2666666666666657, -1.1333333333333258, -0.46666666666666856]
```

##### Signal Line
Calculates the signal line for `moving_average_convergence_divergence`. The period defaults to 9, nd the moving average
model defaults to 'ema' (exponential moving average).
```python
from PyTechnicalIndicators.Bulk.moving_averages import signal_line
# Default Signal Line
macds = [-2, -1.8, -1, -0.3, 0.1, 0.6, 1.2, 2.4, 1.9, 1.8, 1.2]
signal = signal_line(macds)
print(signal)
# [0.8922983167758831, 1.1916575053179188, 1.2863408873310813]

# Personalised Signal Line
macds = [0.1, 0.6, 1.2, 2.4, 1.9]
signal = signal_line(macds, period=3, ma_model='ma')
print(signal)
# [0.6333333333333333, 1.3999999999999997, 1.8333333333333333]
```

##### McGinley Dynamic
Calculates the McGinely dynamic of an asset over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.moving_averages import mcginley_dynamic
prices = [100, 110, 112, 115, 113, 111]
md = mcginley_dynamic(prices, 10)
print(md) 
# [100, 100.68301345536507, 101.42207997889615, 102.24351258209249, 102.96445361554517, 103.55939307450244]
```

##### Moving Average Envelopes
Calculates upper and lower envelopes for a list of prices over a given period. Moving average model defaults to 'ma'
(moving average), the difference between the bands and the moving average defaults to 3%. These can be updated by the
caller.
```python
from PyTechnicalIndicators.Bulk.moving_averages import moving_average_envelopes
# Default MA Envelopes
prices = [202, 205, 208, 204, 201, 198, 202]
mae = moving_average_envelopes(prices, 5)
print(mae) 
# [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]

# Personalied MA Envelopes
prices = [202, 205, 208, 204, 201, 198, 202]
pers_mae = moving_average_envelopes(prices, 5, 'ma', 3)
print(pers_mae) 
# [(210.12, 204, 197.88), (209.296, 203.2, 197.10399999999998), (208.678, 202.6, 196.522)]
```

#### Oscillators
Technical Indicators that oscillate

##### Money Flow Index
Calculates the money flow index for an asset. Period defaults to 14 but can be updated by caller.
```python
from PyTechnicalIndicators.Bulk.oscillators import money_flow_index
# Default MFI
typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]
mfi = money_flow_index(typical_prices, volume)
print(mfi)
# [39.58136997172759, 33.33167997619165, 33.54593097992682]

# Personalised MFI
pers_mfi = money_flow_index(typical_prices, volume, 3)
print(pers_mfi) 
# [99.00990099009901, 51.75879396984925, 57.608695652173914, 52.6381129733085, 57.681641708264, 51.92211682476285, 0, 0, 0, 0, 57.465091299677766, 51.958562641631595, 0, 52.7027027027027]
```

##### Chaikin Oscillator
Calculates the Chaikin ocillator for an asset. The short period defaults to 3, the long period to 10, the moving average
model to 'ema' (exponential moving average).
```python
from PyTechnicalIndicators.Bulk.oscillators import chaikin_oscillator
# Default Chaikin Oscillator
high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
co = chaikin_oscillator(high, low, close, volume)
print(co)

# Personalised Chaikin Oscillator
pers_co = chaikin_oscillator(high, low, close, volume, 5, 20, 'ma')
print(pers_co)
```


## License

## Contributing