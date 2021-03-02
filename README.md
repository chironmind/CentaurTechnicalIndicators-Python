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

### Single

Single is broken down into 4 sections:
    - basic_indicators: use of this is best avoided as it is just a wrapper for various statistics and math function,
        it was added so that Single and Bulk would match

    - moving_averages: contains the common moving averages (moving average, exponential ma, smoothed ma),
        as well as a personalised moving average.

    - strength_indicators: currently only has Relative Strength Index and Stochastic as well as their personalised variations.

    - candle_indicators: currently only has Bollinger Bands and the Ichimoku Cloud as well as their personalised variations.

By personalised variations we mean that we have allowed the user to determine how certain calculations were done.
For example, the RSI uses as smoothed MA to calculate the average gains, the personalised RSI allows you to choose your
MA model. Each personalised function will have more detail on how to use it and why.

#### Basic Indicators

_This is intentionally being skipped as we do not recommend its use and will most likely remove soon_

#### Moving Averages

moving_average

```python
from PyTechnicalIndicators.Single import moving_averages


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)