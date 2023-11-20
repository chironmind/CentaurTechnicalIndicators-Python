from src.PyTechnicalIndicators.Single import other_indicators as other_single
from src.PyTechnicalIndicators.Bulk import other_indicators as other_bulk


def test_single_return_on_investment_no_previous():
    roi = other_single.return_on_investment(100, 200)
    assert roi == (2000, 100)


def test_single_return_on_investment_previous():
    roi = other_single.return_on_investment(200, 250, 2000)
    assert roi == (2500, 25)


def test_single_true_range():
    assert other_single.true_range(190, 120, 150) == 70
    assert other_single.true_range(190, 150, 120) == 70
    assert other_single.true_range(150, 120, 190 == 70)


def test_single_average_range_constant():
    assert other_single.average_range_constant(10) == 30
    assert other_single.average_range_constant(10, 2) == 20


def test_single_significant_close():
    close = [100, 105, 109, 106]
    assert other_single.significant_close(close) == 109


def test_single_stop_and_reverse():
    assert other_single.stop_and_reverse(100, 110, 10) == 100
    assert other_single.stop_and_reverse(100, 110, 10, 110) == 110


def test_bulk_return_on_investment():
    prices = [100, 200, 250, 250, 100]
    roi = other_bulk.return_on_investment(prices)
    assert roi == [(2000, 100), (2500, 25), (2500, 0), (1000, -60)]


def test_bulk_true_range():
    high = [190, 190, 150]
    low = [120, 150, 120]
    close = [150, 120, 190]
    assert other_bulk.true_range(high, low, close) == [70, 70, 70]


def test_bulk_significant_close():
    close = [100, 105, 109, 106, 107, 110]
    assert other_bulk.significant_close(close, 4) == [109, 109, 110]


def test_bulk_average_range_constant():
    average_true_range = [10, 11]
    assert other_bulk.average_range_constant(average_true_range, 2) == [20, 22]
