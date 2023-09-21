import pytest

from src.PyTechnicalIndicators.Single import candle_indicators as single_candle_indicators
from src.PyTechnicalIndicators.Bulk import candle_indicators as bulk_candle_indicators


def test_single_bollinger_bands():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107]
    bbands = single_candle_indicators.bollinger_bands(prices)
    assert bbands == (96.36499833879442, 119.33500166120557)


def test_single_personalised_bollinger_bands():
    prices = [110, 107, 108, 105, 103, 106, 107]
    bbands = single_candle_indicators.personalised_bollinger_bands(prices, 'ema', 3)