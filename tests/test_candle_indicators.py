import pytest

from src.PyTechnicalIndicators.Single import candle_indicators as single_candle_indicators
from src.PyTechnicalIndicators.Bulk import candle_indicators as bulk_candle_indicators


def test_single_bollinger_bands():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107]
    bbands = single_candle_indicators.bollinger_bands(prices)
    assert bbands == (96.36499833879442, 119.33500166120557)


def test_single_bollinger_bands_length_error():
    prices = [110, 107, 108, 105, 103, 106, 107]
    with pytest.raises(Exception) as e:
        single_candle_indicators.bollinger_bands(prices)
    assert str(e.value) == 'Submitted length of prices (7) needs to be at least 20 periods long'


def test_single_personalised_bollinger_bands():
    prices = [110, 107, 108, 105, 103, 106, 107]
    bbands = single_candle_indicators.personalised_bollinger_bands(prices, 'ema', 3)
    assert bbands == (99.46018315489414, 112.81255052123461)


def test_single_ichimoku_cloud():
    highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120, 104, 111, 113, 114, 107, 102, 103, 111, 108, 107, 118, 106, 109, 118, 114, 108, 120, 103, 119, 119, 110, 100, 118, 111, 101, 105, 113, 112, 103, 117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115]
    lows = [114, 111, 103, 100, 103, 96, 100, 101, 91, 115, 93, 98, 107, 95, 104, 99, 95, 94, 96, 92, 114, 97, 108, 106, 107, 106, 97, 101, 92, 107, 110, 91, 101, 104, 93, 97, 92, 106, 102, 96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98]
    icloud = single_candle_indicators.ichimoku_cloud(highs, lows)
    assert icloud == (105.25, 105.5)


def test_single_ichimoku_cloud_high_length_error():
    highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120]
    lows = [114, 111, 103, 100, 103, 96, 100, 101, 91, 115, 93, 98, 107, 95, 104, 99, 95, 94, 96, 92, 114, 97, 108, 106, 107, 106, 97, 101, 92, 107, 110, 91, 101, 104, 93, 97, 92, 106, 102, 96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98]
    with pytest.raises(Exception) as e:
        single_candle_indicators.ichimoku_cloud(highs, lows)
    assert str(e.value) == 'Submitted highs (10) or lows (52)  needs to be at least 52 periods long'


def test_single_ichimoku_cloud_low_length_error():
    highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120, 104, 111, 113, 114, 107, 102, 103, 111, 108, 107, 118, 106, 109, 118, 114, 108, 120, 103, 119, 119, 110, 100, 118, 111, 101, 105, 113, 112, 103, 117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115]
    lows = [114, 111, 103, 100, 103, 96, 100, 101, 91]
    with pytest.raises(Exception) as e:
        single_candle_indicators.ichimoku_cloud(highs, lows)
    assert str(e.value) == 'Submitted highs (52) or lows (9)  needs to be at least 52 periods long'


def test_single_personalised_ichimoku_cloud():
    highs = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115]
    lows = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98]
    icloud = single_candle_indicators.personalised_ichimoku_cloud(highs, lows, 5, 3, 13)
    assert icloud == (105.0, 105.5)


def test_bulk_bollinger_bands():
    prices = [103, 105, 102, 107, 103, 111, 106, 104, 105, 108, 112, 120, 125, 110, 107, 108, 105, 103, 106, 107, 110, 108]
    bbands = bulk_candle_indicators.bollinger_bands(prices)
    assert bbands == [(96.36499833879442, 119.33500166120557), (96.91237286601877, 119.48762713398123), (97.16213062944371, 119.53786937055628)]


def test_bulk_personalised_bollinger_bands():
    prices = [110, 107, 108, 105, 103, 106, 107, 110, 108]
    bbands = bulk_candle_indicators.personalised_bollinger_bands(prices, 7, 'ema', 3)
    assert bbands == [(99.46018315489414, 112.81255052123461), (100.42609144537805, 113.77845881171852), (100.49915238054767, 114.23128362705957)]


def test_bulk_ichimoku_cloud():
    highs = [119, 117, 110, 100, 103, 104, 111, 103, 119, 120, 104, 111, 113, 114, 107, 102, 103, 111, 108, 107, 118,
             106, 109, 118, 114, 108, 120, 103, 119, 119, 110, 100, 118, 111, 101, 105, 113, 112, 103, 117, 107, 115,
             114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 113, 119]
    lows = [114, 111, 103, 100, 103, 96, 100, 101, 91, 115, 93, 98, 107, 95, 104, 99, 95, 94, 96, 92, 114, 97, 108, 106,
            107, 106, 97, 101, 92, 107, 110, 91, 101, 104, 93, 97, 92, 106, 102, 96, 100, 102, 109, 113, 109, 108, 95,
            95, 98, 94, 104, 98, 99, 103]
    icloud = bulk_candle_indicators.ichimoku_cloud(highs, lows)
    assert icloud == [(105.25, 105.5), (105.0, 105.5), (105.75, 105.5)]


def test_bulk_personalised_ichimoku_cloud():
    highs = [117, 107, 115, 114, 116, 110, 108, 103, 100, 100, 100, 116, 115, 118, 121]
    lows = [96, 100, 102, 109, 113, 109, 108, 95, 95, 98, 94, 104, 98, 95, 92]
    icloud = bulk_candle_indicators.personalised_ichimoku_cloud(highs, lows, 5, 3, 13)
    assert icloud == [(105.0, 105.5), (106.25, 106.0), (106.5, 106.5)]

