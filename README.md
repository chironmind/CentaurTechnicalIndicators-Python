# PyTechnicalIndicators

PyTechnicalIndicators is a Python library with a number of common technical indicators used to analyse financial data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install PyTechnicalIndicators
```

## Usage

The below is a break down of the various functions in the package, for a detailed example see the [Example]().

The library is split into three sections Single, Bulk and Chart_Patterns.

Single and Bulk have identical functions, Single returns a single value, Bulk returns a list. This is to reduce compute
time if you only a single value returned for you series, or to avoid looping a call if you have a lot of data to process.

It is important to note that the functions expect a list of prices to work, with the oldest value at the beginning of the
 list and the most recent price at the end. An indexed Pandas DF will not work, you will have to `list()` before your variables
 you pass it into these functions, the [Example]() has more details.

---

## Single

Single is broken down into 3 sections:

- moving_averages: contains the common moving averages (moving average, exponential ma, smoothed ma, macd),
        as well as a personalised moving average.
- strength_indicators: currently only has Relative Strength Index and Stochastic as well as their personalised variations.
- candle_indicators: currently only has Bollinger Bands and the Ichimoku Cloud as well as their personalised variations.

By personalised variations we mean that we have allowed the user to determine how certain calculations were done.
For example, the RSI uses as smoothed MA to calculate the average gains, the personalised RSI allows you to choose your
MA model. Each personalised function will have more detail on how to use it and why.


### Moving Averages

Calling moving_averages

```python
from PyTechnicalIndicators.Single import moving_averages
```


#### moving_average(prices)

The simple moving average of a series

__Parameters:__

    _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

__Example:__
```python
prices = [100, 102, 101 ... ]

ma = moving_averages.moving_average(prices)
```


#### exponential_moving_average(prices)

The exponential moving average (EMA), this is usually used when the latest prices are expected to have a greater impact

__Parameters:__
    _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

_-Example:__
```python
prices = [100, 102, 101 ... ]

ema = moving_averages.exponential_moving_average(prices)
```


#### smoothed_moving_average(prices)

The smoothed moving average (SMA) is similar to the exponential moving average, the calculation of the alpha varies
 slightly (see personalised_moving_average for a more detailed explanation of the alpha)

__Parameters:__

    _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

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

    _prices:_ list of floats or ints with oldest values at position 0 and newest value in position n

    _alpha_nominator:_ float or int, can be 0, but it isn't recommended.

    _alpha_denominator:_ float or int, can be 0

__Example:_
```python
prices = [100, 102, 101 ... ]

pma = moving_averages.personalised_moving_average(prices, 3, 2)
```


#### moving_average_divergence_convergence(prices)



#### **signal_line(macd)**

#### **personalised_macd(prices, short_period, long_period)**

#### **personalised_signal_line(macd)**
---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

---

## License
[MIT](https://choosealicense.com/licenses/mit/)