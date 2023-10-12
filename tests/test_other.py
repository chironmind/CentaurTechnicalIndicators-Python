from src.PyTechnicalIndicators.Single import other as other_single
from src.PyTechnicalIndicators.Bulk import other as other_bulk


def test_single_value_added_personalised_index_no_previous():
    vapi = other_single.value_added_personalised_index(100, 210)
    assert vapi == 111000


def test_single_value_added_personalised_index_previous():
    vapi = other_single.value_added_personalised_index(210, 270, 111000)
    assert vapi == 6771000


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


def test_bulk_value_added_personalised_index():
    prices = [100, 210, 270, 250, 180, 220]
    vapi = other_bulk.value_added_personalised_index(prices)
    assert vapi == [111000, 6771000, -128649000, 8876781000, 363948021000]


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
