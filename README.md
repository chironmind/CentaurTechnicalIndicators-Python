# PyTechnicalIndicators

PyTechnicalIndicators is a Python library with a number of common technical indicators used to analyse financial data.

This README will walk you through the Python functions used to calculate various technical indicators and how to call them.
It will not explain what each one is and when or where to use them. If you need more information use Google, Wikipedia,
or Investopedia.


## Table of Contents
- [Installation](https://github.com/0100101001010000/PyTechnicalIndicators#installation)
- [Usage](https://github.com/0100101001010000/PyTechnicalIndicators#usage)
- [Single](https://github.com/0100101001010000/PyTechnicalIndicators#single)
    - [Moving Averages](https://github.com/0100101001010000/PyTechnicalIndicators#moving-averages)
        - [moving_average(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#moving_averageprices)
        - [exponential_moving_average(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#exponential_moving_averageprices)
        - [smoothed_moving_average(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#smoothed_moving_averageprices)
        - [personalised_moving_average(prices, alpha_nominator, alpha_denominator)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_moving_averageprices)
        - [moving_average_divergence_convergence(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#moving_average_divergence_convergenceprices)
        - [signal_line(macd)](https://github.com/0100101001010000/PyTechnicalIndicators#signal_linemacd)
        - [personalised_macd(prices, short_period, long_period, ma_model='ema')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_macdprices)
        - [personalised_signal_line(macd, ma_model='ema')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_signal_linemacd)
    - [Strength Indicators](https://github.com/0100101001010000/PyTechnicalIndicators#strength-indicators)
        - [relative_strength_index(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#relative_strength_indexprices)
        - [personalised_rsi(prices, ma_model='sma')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_rsiprices-ma_modelsma)
        - [stochastic_oscillator(close_prices)](https://github.com/0100101001010000/PyTechnicalIndicators#stochastic_oscillatorclose_prices)
        - [personalised_stochastic_oscillator(close_prices)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_stochastic_oscillatorclose_prices)
    - [Candle Indicators](https://github.com/0100101001010000/PyTechnicalIndicators#candle-indicators)
        - [bollinger_bands(typical_prices)](https://github.com/0100101001010000/PyTechnicalIndicators#bollinger_bandstypical_prices)
        - [personalised_bollinger_bands(typical_price, ma_model='ma', stddev_multiplier=2)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_bollinger_bandstypical_price-ma_modelma-stddev_multiplier2)
        - [ichimoku_cloud(highs, lows)](https://github.com/0100101001010000/PyTechnicalIndicators#ichimoku_cloudhighs)
        - [personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_ichimoku_cloudhighs)
- [Bulk](https://github.com/0100101001010000/PyTechnicalIndicators#bulk)
    - [Basic Indicators](https://github.com/0100101001010000/PyTechnicalIndicators#basic-indicators)
        - [log(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#logprices)
        - [log_difference(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#log_differenceprices)
        - [stddev(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#stddevprices-period-fill_emptyfalse-fill_valuenone)
        - [mean(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#meanprices-period-fill_emptyfalse-fill_valuenone)
        - [median(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#medianprices-period-fill_emptyfalse-fill_valuenone)
        - [variance(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#varianceprices-period-fill_emptyfalse-fill_valuenone)
    - [Moving Averages](https://github.com/0100101001010000/PyTechnicalIndicators#moving-averages-1)
        - [moving_average(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#moving_averageprices-period-fill_emptyfalse-fill_valuenone)
        - [exponential_moving_average(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#exponential_moving_averageprices-period-fill_emptyfalse-fill_valuenone)
        - [smoothed_moving_average(prices, period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#smoothed_moving_averageprices-period-fill_emptyfalse-fill_valuenone)
        - [personalised_moving_average(prices, period, alpha_nominator, alpha_denominator, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_moving_averageprices-period-alpha_nominator-alpha_denominator-fill_emptyfalse-fill_valuenone)
        - [moving_average_divergence_convergence(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#moving_average_divergence_convergenceprices-1)
        - [signal_line(macd)](https://github.com/0100101001010000/PyTechnicalIndicators#signal_linemacd-1)
        - [personalised_macd(prices, short_period, long_period, ma_model='ema')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_macdprices-1)
        - [personalised_signal_line(macd, ma_model='ema')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_signal_linemacd-1)
    - [Strength Indicators](https://github.com/0100101001010000/PyTechnicalIndicators#strength-indicators-1)
        - [relative_strength_index(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#relative_strength_indexprices-1)
        - [personalised_rsi(prices, period, ma_model='sma')](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_rsiprices-period-ma_modelsma)
        - [stochastic_oscillator(close_prices)](https://github.com/0100101001010000/PyTechnicalIndicators#stochastic_oscillatorclose_prices-1)
        - [personalised_stochastic_oscillator(close_prices, period)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_stochastic_oscillatorclose_prices-period)
    - [Candle Indicators](https://github.com/0100101001010000/PyTechnicalIndicators#candle-indicators-1)
        - [bollinger_bands(typical_prices, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#bollinger_bandstypical_prices-fill_emptyfalse-fill_valuenone)
        - [personalised_bollinger_bands(typical_price, period, ma_model='ma', stddev_multiplier=2, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_bollinger_bandstypical_price-period-ma_modelma-stddev_multiplier2-fill_emptyfalse-fill_valuenone)
        - [ichimoku_cloud(highs, lows, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#ichimoku_cloudhighs-lows-fill_emptyfalse-fill_valuenone)
        - [personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period, fill_empty=False, fill_value=None)](https://github.com/0100101001010000/PyTechnicalIndicators#personalised_ichimoku_cloudhighs-lows-conversion_period-base_period-span_b_period-fill_emptyfalse-fill_valuenone)
- [Chart_Patterns](https://github.com/0100101001010000/PyTechnicalIndicators#chart_patterns)
    - [peaks](https://github.com/0100101001010000/PyTechnicalIndicators#peaks)
        - [get_peaks(prices, period=5)](https://github.com/0100101001010000/PyTechnicalIndicators#get_peaksprices-period5)
        - [get_highest_peak(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#get_highest_peakprices)
    - [pits](https://github.com/0100101001010000/PyTechnicalIndicators#pits)
        - [get_pits(prices, period=5)](https://github.com/0100101001010000/PyTechnicalIndicators#get_pitsprices-period5)
        - [get_lowest_pit(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#get_lowest_pitprices)
    - [trends](https://github.com/0100101001010000/PyTechnicalIndicators#trends)
        - [get_trend(p)](https://github.com/0100101001010000/PyTechnicalIndicators#get_trendp)
        - [get_peak_trend(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#get_peak_trendprices)
        - [get_pit_trend(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#get_peak_trendprices)
        - [get_overall_trend(prices)](https://github.com/0100101001010000/PyTechnicalIndicators#get_overall_trendprices)
        - [get_trend_angle(price_a, index_a, price_b, index_b)](https://github.com/0100101001010000/PyTechnicalIndicators#get_trend_angleprice_a-index_a-price_b-index_b)
        - [break_down_trends(prices, min_period=2, peaks_only=False, pits_only=False)](https://github.com/0100101001010000/PyTechnicalIndicators#break_down_trendsprices-min_period2-peaks_onlyfalse-pits_onlyfalse)
        - [merge_trends(typical_prices, min_period=2)](https://github.com/0100101001010000/PyTechnicalIndicators#merge_trendstypical_prices-min_period2)
- [Contributing](https://github.com/0100101001010000/PyTechnicalIndicators#contributing)
- [License](https://github.com/0100101001010000/PyTechnicalIndicators#license)
---
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyTechnicalIndicators.

```bash
pip install PyTechnicalIndicators
```
---
## Usage

The below is a break down of the various functions in the package, for a detailed example see the [Example](https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example).

The library is split into three sections Single, Bulk and Chart_Patterns.

Single and Bulk have identical functions, Single returns a single value, Bulk returns a list. This is to reduce compute
time if you only a single value returned for you series, or to avoid looping a call if you have a lot of data to process.

It is important to note that the functions expect a list of prices to work, with the oldest value at the beginning of the
 list and the most recent price at the end. An indexed Pandas DF will not work, you will have to `list()` before your variables
 you pass it into these functions, the [Example](https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example) has more details.

---

## Single

Single is broken down into 3 sections:

- moving_averages: contains the common moving averages (moving average, exponential ma, smoothed ma, macd),
        as well as a personalised moving average.
- strength_indicators: currently only has Relative Strength Index and Stochastic as well as their personalised variations.
- candle_indicators: currently only has Bollinger Bands and the Ichimoku Cloud as well as their personalised variations.

By personalised variations we mean that we have allowed the user to determine how certain calculations were done.
For example, the RSI uses as smoothed MA to calculate the average gains, the personalised RSI allows you to choose your
MA model. Each personalised function will have more detail on how to use it .

### Moving Averages

Calling moving_averages

```python
from PyTechnicalIndicators.Single import moving_averages
```

#### moving_average(prices)

The simple moving average of a series

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

__Example:__
```python
prices = [100, 102, 101 ... ]

ma = moving_averages.moving_average(prices)
```

#### exponential_moving_average(prices)

The exponential moving average (EMA), this is usually used when the latest prices are expected to have a greater impact

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

__Example:__
```python
prices = [100, 102, 101 ... ]

ema = moving_averages.exponential_moving_average(prices)
```

#### smoothed_moving_average(prices)

The smoothed moving average (SMA) is similar to the exponential moving average, the calculation of the alpha varies
 slightly (see personalised_moving_average for a more detailed explanation of the alpha)

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

__Example:__
```python
prices = [100, 102, 101 ... ]

sma = moving_averages.smoothed_moving_average(prices)
```

#### personalised_moving_average(prices, alpha_nominator, alpha_denominator)

The personalised moving average (PMA) allows you to determine your nominator and denominator values for the alpha.
The alpha determines the impact of previous prices, the higher the alpha the lower past values have an impact. The
calculation is as follows:

```python
alpha = alpha_nominator / (length_prices + alpha_denominator)
```
The alpha_denominator may be a little confusing as it isn't itself the entire denominator, it is a variable that gets
added to the length of the submitted prices to form the actual alpha_denominator.

The EMA used an alpha nominator of 2 and an alpha denominator of 1.
The SMA used an alpha nominator of 1 and an alpha denominator of 0.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n
- _alpha_nominator:_ float or int, can be 0, but it isn't recommended.
- _alpha_denominator:_ float or int, can be 0

__Example:__
```python
prices = [100, 102, 101 ... ]

pma = moving_averages.personalised_moving_average(prices, 3, 2)
```

#### moving_average_divergence_convergence(prices)

The moving average divergence convergence (MACD) only returns the MACD line, to get the single line you will need to
call signal_line (detailed below), the histogram is simply one minus the other, and isn't yet provided here.

The moving_average_divergence_convergence **requires** the length of prices to be at least 26 as that is the number of
periods taken into account, it accepts more, but discards the extra no passing them in will only impact your performance.

If you want to pass in a smaller or bigger period see personalised_macd.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n, must be at least
26 periods in length

__Example:__
```python
prices = [100, 102, 101 ... ]

macd = moving_averages.moving_average_divergence_convergence(prices)
```

#### signal_line(macd)

The signal line returns the line that is complementary to moving_average_divergence_convergence, and is required
to be 9 periods long, no more, no less. If you'd like to pass in a different amount see personalised_signal_line

__Parameters:__

- _macd:_ list of 9 macds retrieved from moving_average_divergence_convergence

__Example:__
```python
macd = [1.2, 1.45, 0.98 ... ]

signal = moving_averages.signal_line(macd[:-9])
```

#### personalised_macd(prices, short_period, long_period, ma_model='ema')

The personalised macd allows you to determine what the short period and long period are for the macd calculation.
Essentially the macd is the subsctraction of the EMA of the short period - the EMA of the long period, which are
12 and 26 respectively in the traditional MACD. Here we allow you to determine what those periods are.
We also allow you to chose you moving average model in the event where you would prefer something other than the EMA.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n, the length of prices
must be at least as big as the value for your long_period
- short_period: int, value strictly greater than 0 but smaller than your long_period.
- long_period: int, value strictly greater than the short period but smaller or equal to the length of prices.
- ma_model: _optional_ The moving average model of your choice (defaults to EMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
prices = [100, 102, 101 ... ]

pers_macd = moving_averages.personalised_macd(prices, 10, 20, 'smoothed moving average')
```

#### personalised_signal_line(macd, ma_model='ema')

The personalised signal line is similar to the personalised MACD in that it lets you decide of the length of the macds
that you want to pass in, however is doesn't require you to insert a variable, it will instead just calculate it based
on the length of the macd list provided.

You can also choose the MA model you would like to run, it is normally just a EMA but you are free to choose your model.personalised

__Parameters:__

- _macd:_ list of macds can be either from a normal macd or a personalised one. The length of the list needs to be greater
than 1 and can be as large as you like.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to EMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
macd = [1.2, 1.45, 0.98 ... ]

signal = moving_averages.personalised_signal_line(macd, 'moving_average')
```

### Strength Indicators

Calling stength indicators

```python
from PyTechnicalIndicators.Single import strength_indicators
```

#### relative_strength_index(prices)

Returns the relative strength index (RSI) of submitted prices, the length of prices needs to be 14 periods long, no more,
no less.

__Parameters:__

- _prices:_ list of floats or ints of prices that needs to be exactly 14 periods long.

__Example:__
```python
prices = [100, 102, 101 ... ]

rsi = strength_indicators.relative_strength_index(prices)
```

#### personalised_rsi(prices, ma_model='sma')

The personalised RSI allows you to choose which MA model to use as well as the number of periods. The traditional RSI 
uses 14 periods and a SMA model.

__Parameters__:

- _prices:_ list of floats or int, the length of prices needs to be exactly of length of the period that you want to evaluate.
than 1 and can be as large as you like.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to SMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
prices = [100, 102, 101 ... ]

pers_rsi = strength_indicators.personalised_rsi(prices, 'ema')
```

#### stochastic_oscillator(close_prices)

Returns the stochastic oscillator (SO) for submitted close prices which need to be 14 periods long, no more, no less.

__Parameters:__

- _close_prices:_ list of floats or ints of closing prices that needs to be exactly 14 periods long.

__Example:__
```python
close = [99, 103, 96 ... ]

so = strength_indicators.stochastic_oscillator(close)
```

#### personalised_stochastic_oscillator(close_prices)

The personalised version of the stochastic oscillator allows you to submit close prices of any length.

__Parameters:__

- _close_prices:_ list of floats or ints of closing prices, the length is of your choosing.

__Example:__
```python
close = [99, 103, 96 ... ]

pers_so = strength_indicators.personalised_stochastic_oscillator(close)
```

### Candle Indicators

Calling candle indicators

```python
from PyTechnicalIndicators.Single import candle_indicators 
```

#### bollinger_bands(typical_prices)

Returns the upper and lower Bollinger Band for a submitted typical prices, which need to be 20 periods long, no more, no
less.

The typical price is calculated by taking the average of the High, Low, and Close ( (High + Low + Close) / 3 ).

__Parameters:__

- _typical_prices:_ list of floats or ints of exactly 20 periods long.

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

bband = candle_indicators.bollinger_bands(typical_prices)
```

#### personalised_bollinger_bands(typical_price, ma_model='ma', stddev_multiplier=2)

The personalised version allows you to choose the length of typical prices to submit as well as the MA model to run.

The traditional Bollinger Band model uses a MA and 20 periods.

__Parameters:__

- _typical_prices:_ a list of floats or ints of exactly 20 periods long.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to MA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'
- _stddev_multiplier:_ int, number of standard deviations, defaults to 2.

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

pers_bband = candle_indicators.personalised_bollinger_bands(typical_prices, 'ema')
```

#### ichimoku_cloud(highs, lows)

Returns the leading span A and leading span B, using the highs and lows of a series, these need to be 52 periods long, no
more, no less.

__Parameters:__
- _highs:_ list of floats or ints of the highs of a series, needs to be 52 periods long.
- _lows:_ list of floats or ints of the lows of a series, needs to be 52 periods long.

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

icloud = candle_indicators.ichimoku_cloud(highs, lows)
```

#### personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period)
The personalised version of the Ichimoku Cloud allows you to play around with the variables of the Ichimoku Cloud. These
are rather involved so don't play around with them if you don't know what you're doing, or do, I won't judge.

__Parameters:__
- _highs:_ list of floats or ints of the highs of a series, needs to be 52 periods long.
- _lows:_ list of floats or ints of the lows of a series, needs to be 52 periods long.
- _conversion_period:_ 
- _base_period:_
- _span_b_period:_

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

pers_icloud = candle_indicators.personalised_ichimoku_cloud(highs, lows, , , )
```

---
## Bulk

Bulk is broken down into 4 sections, in a very similar way to Single, the only difference is that these are meant to run
against large datasets, and return a **list** of values as opposed to a single point like in Single.

- basic_indicators: These are a list of Python math and statistics functions that have been wrapped up in a loop to allow
  them to return a list. These are mostly to be used within the other functions.
- moving_averages: contains the common moving averages (moving average, exponential ma, smoothed ma, macd),
        as well as a personalised moving average.
- strength_indicators: currently only has Relative Strength Index and Stochastic as well as their personalised variations.
- candle_indicators: currently only has Bollinger Bands and the Ichimoku Cloud as well as their personalised variations.

By personalised variations we mean that we have allowed the user to determine how certain calculations were done.
For example, the RSI uses as smoothed MA to calculate the average gains, the personalised RSI allows you to choose your
MA model. Each personalised function will have more detail on how to use it.

### Basic Indicators

Calling basic_indicators

```python
from PyTechnicalIndicators.Bulk import basic_indicators
```

#### log(prices)

Returns a list of logs for the list of submitted prices. This is just the Python math log function wrapped in a loop to
return a list of logs.

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be exactly 14 periods long.

__Example:__
```python
prices = [100, 102, 101 ... ]

logs = basic_indicators.log(prices)
```

#### log_difference(prices)

Returns a list of log difference for the list of submitted prices. This substracts the log of t and t-1.

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be exactly 14 periods long.

__Example:__
```python
prices = [100, 102, 101 ... ]

log_diff = basic_indicators.log_diff(prices)
```

#### stddev(prices, period, fill_empty=False, fill_value=None)

Returns a list of standard deviations for the list of submitted prices. This uses the Python statistics stdev wrapped in
a loop. It expects a period to know how many prices to apply the stdev to. 

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be at least one in length.
- _period:_ int, the number of prices that you would like taken into account to calculate the standard deviation.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see 
  (Example)[] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

std_devs = basic_indicators.stddev(prices, 10, True, 0)
```

#### mean(prices, period, fill_empty=False, fill_value=None)

Returns a list of means for the list of submitted prices. This uses the Python statistics mean function wrapped in a 
loop. It expects a period to know how many prices to apply the mean to.

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be at least 1.
- _period:_ int, the number of prices that you would like taken into account to calculate the mean.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see 
  (Example)[] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

mean = basic_indicators.mean(prices, 5, True, None)
```

#### median(prices, period, fill_empty=False, fill_value=None)

Returns a list of medians for the list of submitted prices. This uses the Python statistics median function wrapped in a 
loop. It expects a period to know how many prices to apply the median to.

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be at least 1.
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see 
  (Example)[] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

medians = basic_indicators.median(prices, 12)
```

#### variance(prices, period, fill_empty=False, fill_value=None)

Returns a list of medians for the list of submitted prices. This uses the Python statistics variance function wrapped in a 
loop. It expects a period to know how many prices to apply the variance to.

__Parameters:__
- _prices:_ list of floats or ints of prices that needs to be at least 1.
- _period:_ int, the number of prices that you would like taken into account to calculate the variance.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see 
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

variances = basic_indicators.variance(prices, 5)
```


### Moving Averages

Calling moving_averages

```python
from PyTechnicalIndicators.Bulk import moving_averages
```

#### moving_average(prices, period, fill_empty=False, fill_value=None)

The simple moving average of a series

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

ma = moving_averages.moving_average(prices, 5, True, 0)
```

#### exponential_moving_average(prices, period, fill_empty=False, fill_value=None)

The exponential moving average (EMA), this is usually used when the latest prices are expected to have a greater impact

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

ema = moving_averages.exponential_moving_average(prices, 25)
```

#### smoothed_moving_average(prices, period, fill_empty=False, fill_value=None)

The smoothed moving average (SMA) is similar to the exponential moving average, the calculation of the alpha varies
 slightly (see personalised_moving_average for a more detailed explanation of the alpha)

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

__Example:__
```python
prices = [100, 102, 101 ... ]

sma = moving_averages.smoothed_moving_average(prices, 10, True)
```

#### personalised_moving_average(prices, period, alpha_nominator, alpha_denominator, fill_empty=False, fill_value=None)

The personalised moving average (PMA) allows you to determine your nominator and denominator values for the alpha.
The alpha determines the impact of previous prices, the higher the alpha the lower past values have an impact. The
calculation is as follows:

```python
alpha = alpha_nominator / (length_prices + alpha_denominator)
```
The alpha_denominator may be a little confusing as it isn't itself the entire denominator, it is a variable that gets
added to the length of the submitted prices to form the actual alpha_denominator.

The EMA used an alpha nominator of 2 and an alpha denominator of 1.
The SMA used an alpha nominator of 1 and an alpha denominator of 0.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _alpha_nominator:_ float or int, can be 0, but it isn't recommended.
- _alpha_denominator:_ float or int, can be 0
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
prices = [100, 102, 101 ... ]

pma = moving_averages.personalised_moving_average(prices, 15, 3, 2, True, prices[0])
```

#### moving_average_divergence_convergence(prices)

The moving average divergence convergence (MACD) only returns the MACD line, to get the single line you will need to
call signal_line (detailed below), the histogram is simply one minus the other, and isn't yet provided here.

The moving_average_divergence_convergence **requires** the length of prices to be at least 26 as that is the number of
periods taken into account, it accepts more, but discards the extra no passing them in will only impact your performance.

If you want to pass in a smaller or bigger period see personalised_macd.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n, must be at least
26 periods in length

__Example:__
```python
prices = [100, 102, 101 ... ]

macd = moving_averages.moving_average_divergence_convergence(prices)
```

#### signal_line(macd)

The signal line returns the line that is complementary to moving_average_divergence_convergence, and is required
to be 9 periods long, no more, no less. If you'd like to pass in a different amount see personalised_signal_line

__Parameters:__

- _macd:_ list of 9 macds retrieved from moving_average_divergence_convergence

__Example:__
```python
macd = [1.2, 1.45, 0.98 ... ]

signal = moving_averages.signal_line(macd[:-9])
```

#### personalised_macd(prices, short_period, long_period, ma_model='ema')

The personalised macd allows you to determine what the short period and long period are for the macd calculation.
Essentially the macd is the subsctraction of the EMA of the short period - the EMA of the long period, which are
12 and 26 respectively in the traditional MACD. Here we allow you to determine what those periods are.
We also allow you to chose you moving average model in the event where you would prefer something other than the EMA.

__Parameters:__

- _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n, the length of prices
must be at least as big as the value for your long_period
- short_period: int, value strictly greater than 0 but smaller than your long_period.
- long_period: int, value strictly greater than the short period but smaller or equal to the length of prices.
- ma_model: _optional_ The moving average model of your choice (defaults to EMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
prices = [100, 102, 101 ... ]

pers_macd = moving_averages.personalised_macd(prices, 10, 20, 'smoothed moving average')
```

#### personalised_signal_line(macd, period, ma_model='ema')

The personalised signal line is similar to the personalised MACD in that it lets you decide of the length of the macds
that you want to pass in, however is doesn't require you to insert a variable, it will instead just calculate it based
on the length of the macd list provided.

You can also choose the MA model you would like to run, it is normally just a EMA but you are free to choose your model.personalised

__Parameters:__

- _macd:_ list of macds can be either from a normal macd or a personalised one. The length of the list needs to be greater
than 1 and can be as large as you like.
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to EMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
macd = [1.2, 1.45, 0.98 ... ]

signal = moving_averages.personalised_signal_line(macd, 20, 'moving_average')
```

### Strength Indicators

Calling stength indicators

```python
from PyTechnicalIndicators.Single import strength_indicators
```

#### relative_strength_index(prices)

Returns the relative strength index (RSI) of submitted prices, the length of prices needs to be 14 periods long, no more,
no less.

__Parameters:__

- _prices:_ list of floats or ints of prices that needs to be exactly 14 periods long.

__Example:__
```python
prices = [100, 102, 101 ... ]

rsi = strength_indicators.relative_strength_index(prices)
```

#### personalised_rsi(prices, period, ma_model='sma')

The personalised RSI allows you to choose which MA model to use as well as the number of periods. The traditional RSI 
uses 14 periods and a SMA model.

__Parameters__:

- _prices:_ list of floats or int, the length of prices needs to be exactly of length of the period that you want to evaluate.
than 1 and can be as large as you like.
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to SMA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'

__Example:__
```python
prices = [100, 102, 101 ... ]

pers_rsi = strength_indicators.personalised_rsi(prices, 20,'ema')
```

#### stochastic_oscillator(close_prices)

Returns the stochastic oscillator (SO) for submitted close prices which need to be 14 periods long, no more, no less.

__Parameters:__

- _close_prices:_ list of floats or ints of closing prices that needs to be exactly 14 periods long.

__Example:__
```python
close = [99, 103, 96 ... ]

so = strength_indicators.stochastic_oscillator(close)
```

#### personalised_stochastic_oscillator(close_prices, period)

The personalised version of the stochastic oscillator allows you to submit close prices of any length.

__Parameters:__

- _close_prices:_ list of floats or ints of closing prices, the length is of your choosing.
- _period:_ int, the number of prices that you would like taken into account to calculate the median.

__Example:__
```python
close = [99, 103, 96 ... ]

pers_so = strength_indicators.personalised_stochastic_oscillator(close, 5)
```

### Candle Indicators

Calling candle indicators

```python
from PyTechnicalIndicators.Single import candle_indicators 
```

#### bollinger_bands(typical_prices, fill_empty=False, fill_value=None)

Returns the upper and lower Bollinger Band for a submitted typical prices, which need to be 20 periods long, no more, no
less.

The typical price is calculated by taking the average of the High, Low, and Close ( (High + Low + Close) / 3 ).

__Parameters:__

- _typical_prices:_ a list of floats or ints of exactly 20 periods long.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

bband = candle_indicators.bollinger_bands(typical_prices, True, 0)
```

#### personalised_bollinger_bands(typical_price, period, ma_model='ma', stddev_multiplier=2, fill_empty=False, fill_value=None)

The personalised version allows you to choose the length of typical prices to submit as well as the MA model to run.

The traditional Bollinger Band model uses a MA and 20 periods.

__Parameters:__

- _typical_prices:_ a list of floats or ints of a chosen period period.
- _period:_ int, the number of prices that you would like taken into account to calculate the median.
- _ma_model:_ _optional_ The moving average model of your choice (defaults to MA):
  - for moving average either of the following: 'ma', 'moving average', 'moving_average'
  - for smoothed moving average either of the following: 'sma', 'smoothed moving average', 'smoothed_moving_average'
  - for exponential moving average either of the following: 'ema', 'exponential moving average', 'exponential_moving_average'
- _stddev_multiplier:_ int or float, number of standard deviations, defaults to 2.  
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.  

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

pers_bband = candle_indicators.personalised_bollinger_bands(typical_prices, 10, 'ema', 1.5, True, None)
```

#### ichimoku_cloud(highs, lows, fill_empty=False, fill_value=None)

Returns the leading span A and leading span B, using the highs and lows of a series, these need to be 52 periods long, no
more, no less.

__Parameters:__
- _highs:_ list of floats or ints of the highs of a series, needs to be 52 periods long.
- _lows:_ list of floats or ints of the lows of a series, needs to be 52 periods long.
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces.  

__Example:__
```python
highs = [100, 102, 101 ... ]
lows = [90, 86, 92 ... ]

icloud = candle_indicators.ichimoku_cloud(highs, lows, True, 0)
```

#### personalised_ichimoku_cloud(highs, lows, conversion_period, base_period, span_b_period, fill_empty=False, fill_value=None)
The personalised version of the Ichimoku Cloud allows you to play around with the variables of the Ichimoku Cloud. These
are rather involved so don't play around with them if you don't know what you're doing, or do, I won't judge.

__Parameters:__
- _highs:_ list of floats or ints of the highs of a series, needs to be 52 periods long.
- _lows:_ list of floats or ints of the lows of a series, needs to be 52 periods long.
- _conversion_period:_ 
- _base_period:_
- _span_b_period:_
- _fill_empty:_ Boolean, whether you want to fill the list with a value to match the length of the submitted prices. This
  is helpful when using this with Pandas as it will allow to insert the returned list directly into your DataFrame (see
  (Example)[https://github.com/0100101001010000/PyTechnicalIndicators_Examples/tree/main/Notebook_Example] )
- _fill_value:_ The value that you want used to fill in the empty spaces. 

__Example:__
```python
highs = [100, 102, 101 ... ]
lows = [91, 95, 95 ... ]

pers_icloud = candle_indicators.personalised_ichimoku_cloud(highs, lows, , , )
```

---
## Chart_Patterns
Chart patterns is a collection of functions to help highlight and break down trends in the data. 

It is broken down in three parts:
- peaks: highlights the peaks (highs) of a series
- pits: highlights the pits (lows) of a series
- trends: a set of functions to retrieve the trend as an int, angle...

### peaks

Calling peaks

```python
from PyTechnicalIndicators.Chart_Patterns import peaks
```

#### get_peaks(prices, period=5)

Gets the highest prices of a series within a predetermined period, and returns them as a list.

__Parameters:__
- _prices:_ list of floats or ints of the prices of a series.
- _period:_ _optional_ int, number of prices before and after. 

__Example:__
```python
prices = [100, 102, 101 ... ]

peaks_list = peaks.get_peaks(prices, 2)
```

#### get_highest_peak(prices)

Returns the max of the previous function

__Parameters:__
- _prices:_ list of floats or ints of the prices of a series.

__Example:__
```python
prices = [100, 102, 101 ... ]

max_pit = peaks.get_highest_peak(prices)
```

### pits

Calling pits

```python
from PyTechnicalIndicators.Chart_Patterns import pits
```

#### get_pits(prices, period=5)

Gets the lowest prices of a series within a predetermined period, and returns them as a list.

__Parameters:__
- _prices:_ list of floats or ints of the prices of a series.
- _period:_ _optional_ int, number of prices before and after. 

__Example:__
```python
prices = [100, 102, 101 ... ]

pits_list = pits.get_pits(prices, 2)
```

#### get_lowest_pit(prices)

Returns the min of the previous function

__Parameters:__
- _prices:_ list of floats or ints of the prices of a series.

__Example:__
```python
prices = [100, 102, 101 ... ]

min_pit = peaks.get_highest_peak(prices)
```

### trends

Calling trends

```python
from PyTechnicalIndicators.Chart_Patterns import trends
```

#### get_trend(p)

Gets the trend of a set of prices, mostly to be used by other functions in trends,
but if you want to use it go for it. Returns a float.

__Parameters:__
- _p:_ list of floats or ints to retrieve a trend against.

__Example:__
```python
# We wouldn't recommend using it like this...
prices = [100, 102, 101 ... ]

trend = trends.get_trend(prices)
```

#### get_peak_trend(prices)

Gets the peaks and determines the trend of the peaks. Returns a float.

__Parameters:__
- _prices:_ list of floats or ints of prices.

__Example:__
```python
prices = [100, 102, 101 ... ]

peak_trend = trends.get_peak_trend(prices)
```

#### get_pit_trend(prices)

Gets the pits and determines the trend of the pits. Returns a float.

__Parameters:__
- _prices:_ list of floats or ints of prices.

__Example:__
```python
prices = [100, 102, 101 ... ]

pit_trend = trends.get_pit_trend(prices)
```

#### get_overall_trend(prices)

Gets the pits and peaks, gets the trend of each, then returns the average of the two. Returns a float.

__Parameters:__
- _prices:_ list of floats or ints of prices.

__Example:__
```python
prices = [100, 102, 101 ... ]

overall_trend = trends.get_overall_trend(prices)
```

#### get_trend_angle(price_a, index_a, price_b, index_b)

Determines the angle between two prices, price a should be the price and the start of the period, price b shoul be the 
price at the end of the period. Some people find this useful.

__Parameters:__
- _price_a:_ price a, needs to be before price b.
- _index_a:_ index of price a.
- _price_b:_ price b, needs to be after price a.
- _index_b:_ index of price b.

__Example:__
```python
angle = trends.get_trend_angle(100, 0, 105, 10)
```

#### break_down_trends(prices, min_period=2, peaks_only=False, pits_only=False)

Breaks down the different trends in a series of prices into periods whose trends ressemble one anothers the most. Choosing
peaks_only or pit_only will only return one otherwise the two will be returned by default. 

Returns a list of tuples with (trend_start_index, trend_end_index, trend)

The Example notebook will illustrate this in an obvious manner.

__Parameters:__
- _prices:_ price a, needs to be before price b.
- _min_period:_ _optional_ number of periods either side of the evaluated price to determine a pit or peak.
- _peaks_only:_ _optional_ whether or not you only want peaks returned.
- _pits_only:_ _optional_ whether or not you only want pits returned.

__Example:__
```python
prices = [100, 102, 101 ... ]

angle = trends.break_down_trends(prices, 5)
```

#### merge_trends(typical_prices, min_period=2)

This breaks down the price series into different sections when their trends differ. It is similar to the above but takes
into account both highs and lows and treats them as one.

Returns a list of tuples with (trend_start_index, trend_end_index, trend)

__Parameters:__
- _typical_prices:_ 
- _min_period:_ _optional_ number of periods either side of the evaluated price to determine a pit or peak

__Example:__
```python
typical_prices = [100, 102, 101 ... ]

merge_trends = trends.merge_trends(prices, 1)
```

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

If you need ideas on where to start go to [TODO](), there will always be something that needs to be done...

---

## License
[MIT](https://choosealicense.com/licenses/mit/)
