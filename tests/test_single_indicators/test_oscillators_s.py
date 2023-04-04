import pytest

from src.PyTechnicalIndicators.Single.oscillators import money_flow_index, personalised_money_flow_index

def test_money_flow_index():
    typical_prices = [101, 100, 102, 103, 105, 106, 107, 110, 108, 109, 107, 106, 105, 108]
    volume = [1250, 1000, 800, 900, 1100, 1500, 1600, 1800, 2000, 1750, 1800, 1500, 1000, 1100]
    mfi = money_flow_index(typical_prices=typical_prices, volume=volume)
    print(mfi)
    assert mfi == 66.51053864168618


def test_money_flow_index_all_positive():
    # Unlikely for daily, but this could happen for tick
    typical_prices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
    volume = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
    mfi = money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 99.00990099009901


def test_money_flow_index_all_negative():
    # Unlikely for daily, but this could happen for tick
    typical_prices = [114, 113, 112, 110, 111, 109, 108, 107, 106, 105, 104, 103, 102, 101]
    volume = [2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700]
    mfi = money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 0


def test_money_flow_index_exception():
    typical_prices = [100, 101, 102]
    volume = [1000, 1100, 1200]
    with pytest.raises(Exception) as e:
        money_flow_index(typical_prices=typical_prices, volume=volume)
    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume ({len(volume)}) need to be 14 periods in length"


def test_personalised_money_flow_index():
    typical_prices = [100, 101, 100, 90, 103]
    volume = [1000, 1100, 1200, 1050, 1100]
    mfi = personalised_money_flow_index(typical_prices=typical_prices, volume=volume)
    assert mfi == 78.4688995215311


def test_personalised_money_flow_index_exception():
    typical_prices = [100, 101, 100, 90, 103]
    volume = [1000, 1100, 1200, 1050]
    with pytest.raises(Exception) as e:
        personalised_money_flow_index(typical_prices=typical_prices, volume=volume)
    assert str(e.value) == f"typical_prices ({len(typical_prices)}) and volume({len(volume)})  need to be of same length"
