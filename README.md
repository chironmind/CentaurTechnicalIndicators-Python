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
The `Bulk` directory has 11 files used to calculate different Technical Indicator categories.

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

##### Stochastic Oscillator
Calculates the stochastic oscillator for an asset. Period defaults to 14, can be changed by caller.
```python
from PyTechnicalIndicators.Bulk.oscillators import stochastic_oscillator
# Default Stochastic Oscillator
close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89, 97, 104]
so = stochastic_oscillator(close)
print(so) 
# [65.625, 100, 100]

# Personalised Stochastic Oscillator
close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89]
pso = stochastic_oscillator(close, 5)
print(pso) 
# [0.0, 0.0, 30.0, 57.14285714285714, 100.0, 100.0, 90.0, 100.0, 100.0, 50.0]
```

##### Fast Stochastic
Calculates the fast stochastic from a list of stochastic oscillators for a given period. Moving average model defaults
to 'ma' (moving average). Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.oscillators import fast_stochastic
# Default Fast Stochastic
stochastic_oscillators = [0.0, 0.0, 30.0, 57.14285714285714, 100.0, 100.0, 90.0, 100.0, 100.0, 50.0]
fs = fast_stochastic(stochastic_oscillators, 5)
print(fs) 

# Personalised Fast Stochastic
stochastic_oscillators = [0.0, 0.0, 30.0, 57.14285714285714, 100.0, 100.0, 90.0, 100.0, 100.0, 50.0]
pers_fs = fast_stochastic(stochastic_oscillators, 5, 'ema')
print(pers_fs) 
# [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]
```

##### Slow Stochastic
Calculates the slow stochastic from a list of fast stochastics over a given period. Moving average model defaults
to 'ma' (moving average). Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.oscillators import slow_stochastic
# Default Slow Stochastic
fast_stochastics = [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]
ss = slow_stochastic(fast_stochastics, 5)
print(ss)
    
# Personalised Slow Stochastic
fast_stochastics = [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926, 79.66824644549763]
pers_ss = slow_stochastic(fast_stochastics, 5, 'ema')
print(pers_ss) 
# [89.69128533244347, 87.43902556418001]
```

##### Slow Stochastic DS
Calculates the %DS-Slow from the slow stochastic over a given period. Moving average model defaults
to 'ma' (moving average). Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Bulk.oscillators import slow_stochastic_ds
# Default Slow Stochastic DS
slow_stochastics = [89, 87, 88, 83, 82]
ssds = slow_stochastic_ds(slow_stochastics, 3)
print(ssds)
# [88, 86, 84.33333333333333]

# Personalised Slow Stochastic DS
slow_stochastics = [89, 87, 88, 83, 82]
pers_ssds = slow_stochastic_ds(slow_stochastics, 3, 'ma')
print(pers_ssds)
# [88, 86, 84.33333333333333]
```

##### Williams %R
Calculates the Williams %R for an asset over a given period.
```python
from PyTechnicalIndicators.Bulk.oscillators import williams_percent_r
high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
wr = williams_percent_r(high, low, close, 3)
print(wr)
# [-19.35483870967742, -65.0, -83.33333333333333, -13.333333333333334, -27.77777777777778, -81.81818181818181, -50.0, -76.19047619047619, -50.0, -53.84615384615385]
```

#### Other Indicators
Indicators that don't really fall into other categories

##### Value Added Index
Calculates the value added index for an asset. Starting investment defaults to 1000 but can be changed by caller.
```python
from PyTechnicalIndicators.Bulk.other_indicators import return_on_investment
prices = [100, 210, 270, 250, 180, 220]

# Default Value Added Index
roi = return_on_investment(prices)
print(vai)
# [(2000, 100), (2500, 25), (2500, 0), (1000, -60)]

# Personalised Value Added Index
vai = return_on_investment(prices, 2000)
print(vai)
# [(4000, 100), (5000, 25), (5000, 0), (2000, -60)]
```

##### True Range
Calculates the true range for an asset. Primarily used internally.
```python
from PyTechnicalIndicators.Bulk.other_indicators import true_range
high = [190, 190, 150]
low = [120, 150, 120]
close = [150, 120, 190]
tr = true_range(high, low, close) 
print(tr)
# [70, 70, 70]
```

##### Average Range Constant
Calculates the average range constant for an asset. The constant defaults to 3 but can be updated by caller.
```python
from PyTechnicalIndicators.Bulk.other_indicators import average_range_constant
average_true_range = [10, 11]

# Default ARC
arc = average_range_constant(average_true_range) 
print(arc)
#[30, 33]
    
# Personalised ARC
pers_arc = average_range_constant(average_true_range, 2) 
print(pers_arc)
# [20, 22]
```

##### Significant Close
Calculates the significant close of an asset for a given period.
```python
from PyTechnicalIndicators.Bulk.other_indicators import significant_close
close = [100, 105, 109, 106, 107, 110]
sc = significant_close(close, 4) 
print(sc)
# [109, 109, 110]
```

#### Strength Indicators

##### Relative Strength Index
Calculates the RSI of an asset. Period defaults to 14m and moving average model defaults to 'sma' (smoothed moving 
average)
```python
from PyTechnicalIndicators.Bulk.strength_indicators import relative_strength_index
# Default RSI
prices = [100, 103, 110, 115, 123, 115, 116, 112, 110, 106, 116, 116, 126, 130, 118]
rsi = relative_strength_index(prices)
print(rsi) 
# [60.44650041420754, 49.98706804800788]

# Personal RSI
pers_rsi = relative_strength_index(prices, 13, 'ma')
print(pers_rsi)
# [58.27814569536424, 58.82352941176471, 51.35135135135135]
```

##### Accumulation Distribution Index
Calculate the ADI of an asset.
```python
from PyTechnicalIndicators.Bulk.strength_indicators import accumulation_distribution_indicator
high = [190, 220, 215]
low = [160, 180, 170]
close = [165, 200, 200]
volume = [1200, 1500, 1200]
adi = accumulation_distribution_indicator(high, low, close, volume)
print(adi) 
# [-800, -800, -400]
```

##### Directional Indicator
Calculate the directional indicator of an asset over a period. 

Returns positive and negative direction indicators, and true range to be used in `directional_index`.
```python
from PyTechnicalIndicators.Bulk.strength_indicators import directional_indicator
high = [127, 107, 130, 109, 120, 110, 125, 110, 105, 103]
low = [87, 97, 85, 81, 80, 75, 85, 70, 60, 50]
close = [115, 106, 124, 90, 88, 79, 90, 85, 83, 45]
di = directional_indicator(high, low, close, 5)
print(di)
# [
#     (20.858895705521473, 2.4539877300613497, 163),
#     (16.444981862152358, 4.9576783555018135, 165.4),
#     (21.332404828226554, 3.8068709377901575, 172.32),
#     (16.534724721122704, 11.384490824037423, 177.856),
#     (12.561830965460091, 13.988535108027989, 187.2848),
#     (9.056111058075762, 14.89632957740407, 207.82783999999998)
# ]
```

##### Directional Index
Calculates the directional index from directional indicator values (positive and negative indicators).
```python
from PyTechnicalIndicators.Bulk.strength_indicators import directional_index
positive_directional_indicator = [20.858895705521473, 16.444981862152358, 21.332404828226554, 16.534724721122704, 12.561830965460091, 9.056111058075762]
negative_directional_indicator = [2.4539877300613497, 4.9576783555018135, 3.8068709377901575, 11.384490824037423, 13.988535108027989, 14.89632957740407]
idx = directional_index(positive_directional_indicator, negative_directional_indicator)
print(idx)
# [0.7894736842105263, 0.536723163841808, 0.6971375807940905, 0.18446914773642656, 0.053735761632022705, 0.24382561293889254]
```

##### Average Direction Index
Calculates the average direction index over a given period from the directional index.
```python
from PyTechnicalIndicators.Bulk.strength_indicators import average_directional_index
idx = [0.7894736842105263, 0.536723163841808, 0.6971375807940905, 0.18446914773642656, 0.053735761632022705, 0.24382561293889254]
adx = average_directional_index(idx, 3, 'ma')
print(adx)
# [0.6744448096154749, 0.47277663079077503, 0.31178083005417995, 0.16067684076911393]
```

##### Average Directional Index Rating
Calculates the average directional index rating of the average directional index over a period.
```python
from PyTechnicalIndicators.Bulk.strength_indicators import average_directional_index_rating
adx = [0.6744448096154749, 0.47277663079077503, 0.31178083005417995, 0.16067684076911393]
adxr = average_directional_index_rating(adx, 3)
print(adxr)
# [0.49311281983482746, 0.3167267357799445]
```

#### Support and Resistance Indicators

##### Pivot points
Calculates the pivot points of an asset.
```python
from PyTechnicalIndicators.Bulk.support_resistance_indicators import pivot_points
high = [115, 119, 125, 118, 116]
low = [99, 96, 110, 105, 108]
close = [108, 113, 120, 115, 110]
pivot = pivot_points(high, low, close)
print(pivot) 
# [
#     (107.33333333333333, 99.66666666666666, 115.66666666666666, 91.33333333333333, 123.33333333333333),
#     (109.33333333333333, 99.66666666666666, 122.66666666666666, 86.33333333333333, 132.33333333333331),
#     (118.33333333333333, 111.66666666666666, 126.66666666666666, 103.333333333333333, 133.33333333333331),
#     (112.66666666666667, 107.33333333333334, 120.33333333333334, 99.66666666666667, 125.66666666666667),
#     (111.33333333333333, 106.66666666666666, 114.66666666666666, 103.33333333333333, 119.33333333333333)
# ]
```

#### Trend Indicators

##### Aroon Up
Calculates the Aroon up for an asset. Period defaults to 25.
```python
from PyTechnicalIndicators.Bulk.trend_indicators import aroon_up
period_from_high = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
aroon_up = aroon_up(period_from_high, 10)
print(aroon_up) 
# [0.0, 100.0, 90.0, 100.0, 100.0]
```

##### Aroon Down
Calculates the Aroon Down for an asset. Period defaults to 25.
```python
from PyTechnicalIndicators.Bulk.trend_indicators import aroon_down
period_from_low = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
aroon_down = aroon_down(period_from_low, 10)
print(aroon_down) 
# [100.0, 90.0, 80.0, 70.0, 100.0]
```

##### Aroon Oscillator
Calculates the Aroon oscillator of an asset.
```python
from PyTechnicalIndicators.Bulk.trend_indicators import aroon_oscillator
highs = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
lows = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
aroon_oscillator = aroon_oscillator(highs, lows, 10)
print(aroon_oscillator)
# [-100.0, 10.0, 10.0, 30.0, 0.0]
```

##### Parabolic Stop and Reverse
Calculates the parabolic SaR of an asset over a given period.
```python
from PyTechnicalIndicators.Bulk.trend_indicators import parabolic_sar
highs = [109, 111, 112, 110, 111, 113, 109, 107]
lows = [90, 94, 98, 100, 96, 89, 95, 93]
close = [100, 103, 109, 108, 110, 111, 108, 106]
psar = parabolic_sar(highs, lows, close, 5)
print(psar)
# [(90.44, 0.02, 112, 'rising'),  (91.3424, 0.04, 113, 'rising'), (92.208704, 0.04, 113, 'rising'), (93.04035584, 0.04, 113, 'rising')]
```

#### Volatility Indicators

##### Average True Range
Calculates the average true range of an asset over a given period.
```python
from PyTechnicalIndicators.Bulk.volatility_indicators import average_true_range
high = [120, 125, 123, 127, 121, 110]
low = [90, 110, 116, 113, 96, 79]
close = [100, 115, 120, 125, 110, 83]
atr = average_true_range(high, low, close, 3)
print(atr)
# [17.333333333333332, 16.22222222222222, 19.14814814814815, 23.09876543209877]
```

##### Ulcer Index
Calculates the Ulcer index of an asset over a given period.
```python
from PyTechnicalIndicators.Bulk.volatility_indicators import ulcer_index
close_prices = [103, 105, 106, 104, 101, 99, 93]
ui = ulcer_index(close_prices, 5)
print(ui)
# [2.2719989771306217, 3.7261165392700946, 6.630672977662482]
```

##### Volatility Index
Calculate the volatility index of an asset over a given period.
```python
from PyTechnicalIndicators.Bulk.volatility_indicators import volatility_index
high = [190, 190, 150]
low = [120, 150, 120]
close = [150, 120, 190]
vi = volatility_index(high, low, close, 14)
print(vi) 
# [5.0, 9.642857142857142, 13.95408163265306]
```

##### Volatility System
Calculates the volatility system of an asset. Period defaults to 7, average true range constant defaults to 3.
```python
from PyTechnicalIndicators.Bulk.volatility_indicators import volatility_system
high = [120, 125, 123, 127, 121, 110]
low = [90, 110, 116, 113, 96, 79]
close = [100, 115, 120, 125, 110, 83]
vs = volatility_system(high, low, close, 3, 2)
print(vs) 
# [(125, 32.44444444444444, 92.55555555555556, 16.22222222222222),
# (125, 38.2962962962963, 86.7037037037037, 19.14814814814815),
# (83, 46.19753086419754, 129.19753086419755, 23.09876543209877)]
```

### Single

Most of the `Single` functions are missing the period parameter as the length of the passed in prices is assumed to be 
the period.

#### Basic Indicators
Single `basic_indicators` is missing a number of functions that bulk has because they are native Python functions. There
was no need to have a wrapper function call the native function. Package user can just call the native function.

##### Mean Absolute Deviation
Calculates the prices absolute deviation from the mean.
```python
from PyTechnicalIndicators.Single.basic_indicators import mean_absolute_deviation
prices = [100, 102, 105]
single_mean_absolute_deviation = mean_absolute_deviation(prices)
print(single_mean_absolute_deviation)
# 1.7777777777777761
```

##### Median Absolute Deviation
Calculates the prices absolute deviation from the median.
```python
from PyTechnicalIndicators.Single.basic_indicators import median_absolute_deviation
prices = [100, 102, 105]
single_median_absolute_deviation = median_absolute_deviation(prices)
print(single_median_absolute_deviation)
# 1.6666666666666667
```

##### Mode Absolute Deviation
Calculates the prices absolute deviation from the median over a period. Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Single.basic_indicators import mode_absolute_deviation
prices = [100, 102, 105]
single_mode_absolute_deviation = mode_absolute_deviation(prices)
print(single_mode_absolute_deviation)
# 2.3333333333333335
```

#### Candle Indicators
`candle_indicators` has technical indicators intended to be used on OHLC charts.

##### Bollinger Bands
Calculates the Bollinger Bands for typical prices. The moving average model defaults to 'ma' 
(moving average), and the standard deviation multiplier defaults to 2.

The first item in the tuple is the lower band, the second item is the upper band.
```python
from PyTechnicalIndicators.Single.candle_indicators import bollinger_bands
# Default Bollinger Bands
prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107]
bbands = bollinger_bands(prices)
print(bbands)
# (96.36499833879442, 119.33500166120557)

# Personalised Bollinger Bands
prices = [110, 107, 108, 105, 103, 106, 107]
personalised_bbands = bollinger_bands(prices, ma_model='ema', stddev_multiplier=3)
print(personalised_bbands) 
# (99.46018315489414, 112.81255052123461)
```

##### Ichimoku Cloud
Calculates the Ichimoku Cloud from high, low, and closing prices. The conversion period defaults to 9, the base period
defaults to 26, and the span B period defaults to 52. These can be changed by the caller.

Returns the leading span A, leading span B, baseline, conversion line, and lagged close based on the base period, in that order.
```python
from PyTechnicalIndicators.Single.candle_indicators import ichimoku_cloud
# Default Ichimoku Cloud
highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120, 104, 111, 113, 114, 107, 102, 103, 111, 108, 107, 118,
         106, 109, 118, 114, 108, 120, 103, 119, 119, 110, 100, 118, 111, 101, 105, 113, 112, 103, 117, 107, 115,
         114, 116, 110, 108, 103, 100, 100, 100, 116, 115]
lows = [114, 111, 103, 100, 103, 96, 100, 101, 91, 115, 93, 98, 107, 95, 104, 99, 95, 94, 96, 92, 114, 97, 108, 106,
        107, 106, 97, 101, 92, 107, 110, 91, 101, 104, 93, 97, 92, 106, 102, 96, 100, 102, 109, 113, 109, 108, 95,
        95, 98, 94, 104, 98]
close = [114, 116, 108, 100, 103, 102, 106, 101, 103, 118, 102, 106, 112, 101, 107, 99, 101, 111, 103, 106, 116,
         106, 108, 106, 113, 106, 109, 103, 106, 118, 110, 94, 109, 107, 93, 101, 103, 110, 102, 102, 102, 112, 111,
         115, 110, 108, 103, 98, 98, 95, 113, 112]
icloud = ichimoku_cloud(highs, lows, close)
print(icloud) 
# (105.25, 105.5, 105.5, 105, 109)

# Personalised Ichimoku Cloud
highs = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115]
lows = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98]
close = [99, 103, 108, 113, 115, 110, 108, 96, 95, 99, 99, 109, 108]
icloud = ichimoku_cloud(highs, lows, close, conversion_period=5, base_period=3, span_b_period=13)
print(icloud) 
# (105.0, 105.5, 105, 105, 99)
```

#### Correlation Indicators
`correlation_indicators` are indicators that calculate the correlation between two assets.

##### Correlate Asset Prices
Calculates the price correlation between two asset prices.
```python
from PyTechnicalIndicators.Single.correlation_indicators import correlate_asset_prices
asset_a_price = [120, 110, 105, 112, 114]
asset_b_price = [150, 155, 162, 165, 159]
correlation = correlate_asset_prices(asset_a_price, asset_b_price)
print(correlation) 
# -0.65025528597848
```

#### Momentum Indicators
`momentum_indicators` are indicators that calculate price momentum of an asset.

##### Rate of Change
Calculates the rate of change of an asset. Unlike the Bulk function this function takes a current and previous closing 
price.
```python
from PyTechnicalIndicators.Single.momentum_indicators import rate_of_change
roc = rate_of_change(current_close_price=101, previous_close_price=100)
print(roc) 
# 3.0
```

##### On Balance Volume
Calculates the on balance volume from asset prices and volume. A previous observation parameter can be passed in to make
the calculation more precise.
```python
from PyTechnicalIndicators.Single.momentum_indicators import on_balance_volume
closing_prices = [100, 105, 111, 107, 108]
volume = [1200, 1800, 1600, 1700, 1500]
obv = on_balance_volume(current_close=105, previous_close=100, current_volume=1800)
print(obv) 
# 1200
next_obv = on_balance_volume(current_close=105, previous_close=100, current_volume=1800, previous_obv=1200)
# 3000
```

##### Commodity Channel Index
Calculates the commodity channel index of an asset.
Moving average model defaults to 'ma' (moving average) and absolute deviation model default to 'mean'.

```python
from PyTechnicalIndicators.Single.momentum_indicators import commodity_channel_index
# Default Commodity Channel Index
prices = [103, 106, 111, 113, 111, 102, 98]
cci = commodity_channel_index(prices)
print(cci) 
# -119.7640117994101

prices = [103, 106, 111, 113, 111, 102, 98]
personalised_cci = commodity_channel_index(prices, ma_model='ema', absolute_deviation_model='median')
print(cci) 
```

#### Moving Averages
`moving_averages` has indicators related to calculating and using moving averages.

##### Moving Average
Calculates the moving average of an asset.
```python
from PyTechnicalIndicators.Single.moving_averages import moving_average
prices = [110, 107, 108, 105, 103]
mas = moving_average(prices)
print(mas) 
# 106.6
```

##### Exponential Moving Average
Calculates the exponential moving average of an asset.
```python
from PyTechnicalIndicators.Single.moving_averages import exponential_moving_average
prices = [110, 107, 108, 105, 103]
emas = exponential_moving_average(prices)
print(emas) 
# 105.35071090047394
```

##### Smoothed Moving Average
Calculates the smoothed moving average of an asset.
```python
from PyTechnicalIndicators.Single.moving_averages import smoothed_moving_average
prices = [110, 107, 108, 105, 103]
smas = smoothed_moving_average(prices)
print(smas) 
# 105.89005235602093
```

##### Personalised Moving Average
The `personalised_moving_average` is an internal function used by the smoothed (nominator=1, denominator=0), and the
exponential (nominator=2, denominator=1) moving average functions as the underlying logic is indentical with changes in
the nominator and denominator of the alpha variables for each. This function is exposed in the event that the caller 
knows what they're doing, or feel lucky, and wants to tweak the alpha when calculating the moving average.
```python
from PyTechnicalIndicators.Single.moving_averages import personalised_moving_average
prices = [110, 107, 108, 105, 103]
pmas = personalised_moving_average(prices, alpha_nominator=5, alpha_denominator=3)
print(pmas)
```

##### MACD Line
Calculate the MACD line for `moving_average_convergence_divergence`. The short period defaults to 12, the long period
defaults to 26, and the moving average model defaults to 'ema' (exponential moving average).
```python
from PyTechnicalIndicators.Single.moving_averages import macd_line
# Default MACD Line
prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 101,
              99, 103, 106, 104, 102]
macd = macd_line(prices)
print(macd)
# -2.164962379494412

# Personalised MACD Line
prices = [110, 107, 108, 105, 103]
pers_macd = macd_line(prices, short_period=3, long_period=5, ma_model='ma')
print(pers_macd) 
# -1.2666666666666657
```

##### Signal Line
Calculates the signal line for `moving_average_convergence_divergence`. The moving average
model defaults to 'ema' (exponential moving average).
```python
from PyTechnicalIndicators.Single.moving_averages import signal_line
# Default Signal Line
macds = [-2, -1.8, -1, -0.3, 0.1, 0.6, 1.2, 2.4, 1.92]
signal = signal_line(macds)
print(signal)
# 0.8922983167758831

# Personalised Signal Line
macds = [0.1, 0.6, 1.2]
signal = signal_line(macds, ma_model='ma')
print(signal)
# 0.6333333333333333
```

##### McGinley Dynamic
Calculates the McGinely dynamic of an asset for a given period.
```python
from PyTechnicalIndicators.Single.moving_averages import mcginley_dynamic
md = mcginley_dynamic(100, period=10)
print(md) 
# 100
next_md = mcginley_dynamic(110, period=10, previous_mcginley_dynamic=md)
print(next_md)
# 100.68301345536507
```

##### Moving Average Envelopes
Calculates upper and lower envelopes for a list of prices. Moving average model defaults to 'ma'
(moving average), the difference between the bands and the moving average defaults to 3%.
```python
from PyTechnicalIndicators.Bulk.moving_averages import moving_average_envelopes
# Default MA Envelopes
prices = [202, 205, 208, 204, 201]
mae = moving_average_envelopes(prices, period=5)
print(mae) 
# (210.12, 204, 197.88)

# Personalised MA Envelopes
prices = [202, 205, 208, 204, 201]
pers_mae = moving_average_envelopes(prices, period=5, ma_model='ma', difference=3)
print(pers_mae) 
# (210.12, 204, 197.88)
```

#### Oscillators
Technical Indicators that oscillate

##### Money Flow Index
Calculates the money flow index for an asset.
```python
from PyTechnicalIndicators.Single.oscillators import money_flow_index
# Default MFI
typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107]
volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500]
mfi = money_flow_index(typical_prices, volume)
print(mfi)
# 39.58136997172759

# Personalised MFI
typical_prices = [100, 105, 103]
volume = [1200, 1200, 1300]
pers_mfi = money_flow_index(typical_prices, volume)
print(pers_mfi) 
# 99.00990099009901
```

##### Chaikin Oscillator
Calculates the Chaikin ocillator for an asset. The short period defaults to 3, the moving average
model to 'ema' (exponential moving average). The long period from the bulk model is assumed to be the length of the list.
```python
from PyTechnicalIndicators.Single.oscillators import chaikin_oscillator
# Default Chaikin Oscillator
high = [150, 157, 163, 152, 155, 160, 158, 153, 148, 144, 145, 143]
low = [132, 143, 153, 148, 145, 151, 142, 138, 132, 135, 137, 132]
close = [148, 155, 157, 150, 148, 158, 155, 142, 145, 137, 140, 138]
volume = [1500, 1600, 1800, 2200, 2000, 1900, 1750, 1800, 2100, 1800, 1700, 1500]
co = chaikin_oscillator(high, low, close, volume)
print(co)

# Personalised Chaikin Oscillator
pers_co = chaikin_oscillator(high, low, close, volume, 5, 'ma')
print(pers_co)
```

##### Stochastic Oscillator
Calculates the stochastic oscillator for an asset. 
```python
from PyTechnicalIndicators.Bulk.oscillators import stochastic_oscillator
close = [100, 92, 88, 82, 75, 68, 74, 76, 84, 84, 83, 89, 95, 89]
so = stochastic_oscillator(close)
print(so) 
# 65.625
```

##### Fast Stochastic
Calculates the fast stochastic from a list of stochastic oscillators. Moving average model defaults
to 'ma' (moving average). Period needs to be determined by the caller.
```python
from PyTechnicalIndicators.Single.oscillators import fast_stochastic
stochastic_oscillators = [0.0, 0.0, 30.0, 57.14285714285714]
fs = fast_stochastic(stochastic_oscillators, 'ema')
print(fs) 
# 58.13134732566012
```

##### Slow Stochastic
Calculates the slow stochastic from a list of fast stochastics. Moving average model defaults
to 'ma' (moving average). 
```python
from PyTechnicalIndicators.Single.oscillators import slow_stochastic
fast_stochastics = [58.13134732566012, 77.14285714285714, 85.9783344617468, 94.19092755585648, 98.29383886255926]
ss = slow_stochastic(fast_stochastics, 'ema')
print(ss) 
# 89.69128533244347
```

##### Slow Stochastic DS
Calculates the %DS-Slow from the slow stochastic. Moving average model defaults
to 'ma' (moving average).
```python
from PyTechnicalIndicators.Bulk.oscillators import slow_stochastic_ds

slow_stochastics = [89, 87, 88]
ssds = slow_stochastic_ds(slow_stochastics, 3, 'ma')
print(ssds)
# 88
```

##### Williams %R
Calculates the Williams %R for an asset over a given period.
```python
from PyTechnicalIndicators.Single.oscillators import williams_percent_r
high = 150
low = 132
close = 148
wr = williams_percent_r(high, low, close)
print(wr)
# -19.35483870967742
```

#### Other Indicators
Indicators that don't really fall into other categories

##### Return on Invesment
Calculates the value added index for an asset. Starting investment defaults to 1000 but can be changed by caller.
The `Single` function takes a start price and end price.
```python
from PyTechnicalIndicators.Single.other_indicators import return_on_investment
roi = return_on_investment(start_price=100, end_price=200)
print(roi)
# (2000, 100)
```

##### True Range
Calculates the true range for an asset. Primarily used internally.
```python
from PyTechnicalIndicators.Single.other_indicators import true_range
high = 190
low = 120
close = 150
tr = true_range(high, low, close) 
print(tr)
# 70
```

##### Average Range Constant
Calculates the average range constant for an asset. The constant defaults to 3 but can be updated by caller.
```python
from PyTechnicalIndicators.Single.other_indicators import average_range_constant
pers_arc = average_range_constant(10, 2) 
print(pers_arc)
# 20
```

##### Significant Close
Calculates the significant close of an asset.
```python
from PyTechnicalIndicators.Single.other_indicators import significant_close
close = [100, 105, 109, 106]
sc = significant_close(close) 
print(sc)
# 109
```

#### Strength Indicators

##### Relative Strength Index
Calculates the RSI of an asset. Moving average model defaults to 'sma' (smoothed moving 
average)
```python
from PyTechnicalIndicators.Single.strength_indicators import relative_strength_index
# Default RSI
prices = [100, 103, 110, 115, 123, 115, 116, 112, 110, 106, 116, 116, 126]
pers_rsi = relative_strength_index(prices, 'ma')
print(pers_rsi)
# 58.27814569536424
```

##### Accumulation Distribution Index
Calculate the ADI of an asset.
```python
from PyTechnicalIndicators.Single.strength_indicators import accumulation_distribution_indicator
high = 190
low = 160
close = 165
volume = 1200
adi = accumulation_distribution_indicator(high, low, close, volume)
print(adi) 
# -800
```

##### Directional Indicator
Calculate the directional indicator of an asset. 

Returns positive and negative direction indicators, and true range to be used in `directional_index`.
```python
from PyTechnicalIndicators.Single.strength_indicators import directional_indicator
high = [127, 107, 130, 109, 120]
low = [87, 97, 85, 81, 80]
close = [115, 106, 124, 90, 88]
di = directional_indicator(high, low, close)
print(di)
# (20.858895705521473, 2.4539877300613497, 163)
```

##### Directional Index
Calculates the directional index from directional indicator values (positive and negative indicators).
```python
from PyTechnicalIndicators.Single.strength_indicators import directional_index
positive_directional_indicator = 20.858895705521473
negative_directional_indicator = 2.4539877300613497
idx = directional_index(positive_directional_indicator, negative_directional_indicator)
print(idx)
# 0.7894736842105263
```

##### Average Direction Index
Calculates the average direction index from the directional index.
```python
from PyTechnicalIndicators.Single.strength_indicators import average_directional_index
idx = [0.7894736842105263, 0.536723163841808, 0.6971375807940905]
adx = average_directional_index(idx, 'ma')
print(adx)
# 0.6744448096154749
```

##### Average Directional Index Rating
Calculates the average directional index rating of the average directional index over a period. Unlike the `Bulk` 
version the `Single` version takes the current `average_directional_index` and the previous one.
```python
from PyTechnicalIndicators.Single.strength_indicators import average_directional_index_rating
adx = [0.6744448096154749, 0.47277663079077503, 0.31178083005417995, 0.16067684076911393]
adxr = average_directional_index_rating(current_average_directional_index=0.47277663079077503, previous_average_directional_index=0.6744448096154749)
print(adxr)
# 0.49311281983482746
```

#### Support and Resistance Indicators

##### Pivot points
Calculates the pivot points of an asset.
```python
from PyTechnicalIndicators.Single.support_resistance_indicators import pivot_points
high = 115
low = 99
close = 108
pivot = pivot_points(high, low, close)
print(pivot) 
# (107.33333333333333, 99.66666666666666, 115.66666666666666, 91.33333333333333, 123.33333333333333),
```

#### Trend Indicators

##### Aroon Up
Calculates the Aroon up for an asset.
```python
from PyTechnicalIndicators.Single.trend_indicators import aroon_up
period_from_high = [116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
aroon_up = aroon_up(period_from_high, 10)
print(aroon_up) 
# 100.0
```

##### Aroon Down
Calculates the Aroon Down for an asset.
```python
from PyTechnicalIndicators.Single.trend_indicators import aroon_down
period_from_low = [109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
aroon_down = aroon_down(period_from_low, 10)
print(aroon_down) 
# 100.0
```

##### Aroon Oscillator
Calculates the Aroon oscillator of an asset.
```python
from PyTechnicalIndicators.Single.trend_indicators import aroon_oscillator
highs = [110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
lows = [109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
aroon_oscillator = aroon_oscillator(highs, lows, 10)
print(aroon_oscillator)
# 0.0
```

##### Parabolic Stop and Reverse
The `Single` version of this function is intended for intended use.
```python
from PyTechnicalIndicators.Single.trend_indicators import parabolic_sar
highs = [110, 111, 113, 109, 107]
lows = [100, 96, 89, 95, 93]
close = [108, 110, 111, 108, 106]
psar = parabolic_sar(highs, lows, close, previous_psar=92.208704, acceleration_factor=0.04, extreme=113, state='rising')
print(psar)
# (93.04035584, 0.04, 113, 'rising')
```

#### Volatility Indicators

##### Average True Range
Calculates the average true range of an asset.  `Single` has two versions of this function the first when there isn't 
a previous ATR, the other when there is.
```python
from PyTechnicalIndicators.Single.volatility_indicators import average_true_range_initial, average_true_range
high = [120, 125, 123]
low = [90, 110, 116]
close = [100, 115, 120]
atr = average_true_range_initial(high, low, close)
print(atr)
# 17.333333333333332
next_atr = average_true_range(high=127, low=113, close=125, previous_average_true_range=atr, period=3)
print(next_atr)
# 16.22222222222222
```

##### Ulcer Index
Calculates the Ulcer index of an asset.
```python
from PyTechnicalIndicators.Single.volatility_indicators import ulcer_index
close_prices = [103, 105, 106, 104, 101]
ui = ulcer_index(close_prices)
print(ui)
# 2.2719989771306217
```

##### Volatility Index
Calculate the volatility index of an asset. Function takes an optional previous VI parameter if one has been calculated.
```python
from PyTechnicalIndicators.Single.volatility_indicators import volatility_index
vi = volatility_index(high=190, low=120, close=150, period=14)
print(vi) 
# 5.0
next_vi = volatility_index(high=190, low=150, close=120, period=14, previous_volatility_index=vi)
print(next_vi)
# 9.642857142857142
```

##### Volatility System
Calculates the volatility system of an asset. Period defaults to 7, average true range constant defaults to 3. Takes an
optional previous parameter is one is available.
```python
from PyTechnicalIndicators.Single.volatility_indicators import volatility_system
high = [120, 125, 123]
low = [90, 110, 116]
close = [100, 115, 120]
vs = volatility_system(high, low, close, period=3, average_true_range_constant=2)
print(vs) 
# (125, 32.44444444444444, 92.55555555555556, 16.22222222222222)
high = [125, 123, 127]
low = [110, 116, 113]
close = [115, 120, 125]
next_vs = volatility_system(high, low, close, period=3, average_true_range_constant=2, previous_volatility_system=vs)
# (125, 38.2962962962963, 86.7037037037037, 19.14814814814815)
```

### Chart Patterns

#### Chart Trends
A series of functions to help with OHLC analysis

##### Get Trend Line
Calculates the trend line for a series of points and locations. This function is primarily intended for internal use as the 
locations of each point is expected and calculated by other functions. Returns slope then intercept.
```python
from PyTechnicalIndicators.Chart_Patterns.chart_trends import get_trend_line
price_points = [(100, 2), (110, 5), (115, 7), (140, 18)]
trend = get_trend_line(price_points)
print(trend)
# (2.4315068493150687, 96.79794520547945)
```

##### Get Peak Trend
Calculates the trend line for all peaks. Function takes a period parameter to determine the highest point within 
period, defaults to 5. Returns slope then intercept.
```python
from PyTechnicalIndicators.Chart_Patterns.chart_trends import get_peak_trend
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
peak_trend = get_peak_trend(prices, 10)
print(peak_trend)
# (-0.860813704496788, 118.04496788008565)
```

##### Get Valley Trend
Calculates the trend line for all valleys. Function takes a period parameter to determine the lowest point within 
period, defaults to 5. Returns slope then intercept.
```python
from PyTechnicalIndicators.Chart_Patterns.chart_trends import get_valley_trend
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
peak_trend = get_valley_trend(prices, 10)
print(peak_trend)
# (-0.09683794466403162, 83.60079051383399)
```

##### Get Overall Trend
Calculates the overall trend line for all prices. Returns slope then intercept.
```python
from PyTechnicalIndicators.Chart_Patterns.chart_trends import get_overall_trend
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
overall_trend = get_overall_trend(prices)
print(overall_trend)
# (-0.48270676691729325, 98.88571428571429)
```

##### Breakdown Trends
Calculates new trend starts and ends for a list of prices. The standard deviation multiplier defaults to 2 but can be 
updated by caller, a higher multiplier is more forgiving in price changes before announcing a new trend. The sensitivity
denominator defaults to 2 and can be updated by caller, it decides how forgiving it should be when lists are small vs 
large lists.
```python
from PyTechnicalIndicators.Chart_Patterns.chart_trends import break_down_trends
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
trend_breakdown = break_down_trends(prices)
print(trend_breakdown)
# [(0, 1, 3.0, 100.0), (2, 4, -7.0, 109.66666666666667), (5, 7, 0.0, 103.66666666666667), (8, 15, -2.9404761904761907, 125.69047619047619), (16, 18, -3.5, 147.5), (19, 19, 0, 0)]
```

#### Peaks

##### Get Peaks
Intended use is to be used in combination with `get_peak_trends` so that peaks are highlight on chart with the trend
line. Optional period can be passed in to determine the highest point of the period. Defaults to 5.
```python
from PyTechnicalIndicators.Chart_Patterns.peaks import get_peaks
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
pks = get_peaks(prices, 10)
print(pks)
# [(113, 6), (113, 8), (97, 16), (107, 19)]
```

#### Valleys

##### Get Valleys
Intended use is to be used in combination with `get_valley_trends` so that peaks are highlight on chart with the trend
line. Optional period can be passed in to determine the lowest point of the period. Defaults to 5.
```python
from PyTechnicalIndicators.Chart_Patterns.valleys import get_valleys
prices = [100, 103, 95, 90, 81, 99, 113, 99, 113, 95, 87, 92, 86, 94, 86, 82, 97, 77, 90, 107]
valleys = get_valleys(prices, 10)
print(valleys)
# [(113, 6), (113, 8), (97, 16), (107, 19)]
```

## License
`PyTechnicalIndicators` is available under the GNU AFFERO GENERAL PUBLIC LICENSE.

The following information was taken from [choosealicense.com](choosealicense.com/licenses/agpl-3.0/)

> Under GNU AGPLv3 copyright and license notices must be preserved. Contributor provide an express grant of patent 
> rights. When a modified version is used to provide a service over a network, the complete source code of the modified
> version must be made available.

For more information go look at the `License`

## Contributing

To contribute to `PyTechnicalIndicators` follow these simple steps:
* Raise a PR with your changes
* If there is a new function make sure that a test covers it
* Assign 0100101001010000 to the PR

For ideas on how to contribute go to `Contributing.md` and pick an item from the TODO list. 
