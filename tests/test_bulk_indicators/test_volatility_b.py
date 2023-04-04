from src.PyTechnicalIndicators.Bulk.volatility import average_true_range


def test_average_true_range():
    high = [124, 136, 140, 138, 135, 142]
    low = [111, 115, 105, 123, 128, 130]
    close = [115, 122, 127, 128, 130, 132]

    atr = average_true_range(high, low, close, 3)

    assert len(atr) == 4
    assert atr == [18.666666666666664, 17.444444444444443, 13.962962962962962, 13.30864197530864]#
