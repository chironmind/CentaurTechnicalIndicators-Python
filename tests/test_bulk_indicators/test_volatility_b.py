from src.PyTechnicalIndicators.Bulk.volatility import average_true_range, ulcer_index


def test_average_true_range():
    high = [124, 136, 140, 138, 135, 142]
    low = [111, 115, 105, 123, 128, 130]
    close = [115, 122, 127, 128, 130, 132]

    atr = average_true_range(high, low, close, 3)

    assert len(atr) == 4
    assert atr == [18.666666666666664, 17.444444444444443, 13.962962962962962, 13.30864197530864]#


def test_ulcer_index():
    close_prices = [103, 105, 106, 104, 101, 99, 93]
    ui = ulcer_index(close_prices, 5)
    assert ui == [2.2719989771306217, 3.7261165392700946, 6.630672977662482]
