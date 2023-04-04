import pytest

from src.PyTechnicalIndicators.Bulk.oscillators import personalised_money_flow_index
# No need to test money_flow_index as it just calls the personalised function with a period of 14


def test_standard_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = personalised_money_flow_index(typical_prices, volume, 14)

    assert len(mfi) == 3
    assert mfi == [39.58136997172759, 33.33167997619165,33.54593097992682]


def test_personalised_money_flow_index():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200, 1300]

    mfi = personalised_money_flow_index(typical_prices, volume, 3)

    assert len(mfi) == 14
    assert mfi == [99.00990099009901, 51.75879396984925, 57.608695652173914, 52.6381129733085, 57.681641708264, 51.92211682476285, 0, 0, 0, 0, 57.465091299677766, 51.958562641631595, 0, 52.7027027027027]


def test_money_flow_index_incorrect_size():
    typical_prices = [100, 105, 103, 104, 106, 109, 104, 107, 111, 115, 109, 108, 107, 106, 105, 108]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        personalised_money_flow_index(typical_prices, volume, 20)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be at least 20 periods in length"


def test_money_flow_index_mismatch_list_error():
    typical_prices = [100, 105, 103, 104, 106, 109]
    volume = [1200, 1200, 1300, 1200, 1600, 1400, 2000, 1800, 1600, 1500, 1200, 1100, 1500, 1400, 1200]

    with pytest.raises(Exception) as e:
        personalised_money_flow_index(typical_prices, volume, 3)

    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be of same length"
