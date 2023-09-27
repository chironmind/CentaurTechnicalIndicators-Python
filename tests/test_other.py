from src.PyTechnicalIndicators.Single import other as other_single
from src.PyTechnicalIndicators.Bulk import other as other_bulk


def test_value_added_personalised_index_no_previous():
    vapi = other_single.value_added_personalised_index(100, 210)
    assert vapi == 111000


def test_value_added_personalised_index_previous():
    vapi = other_single.value_added_personalised_index(210, 270, 111000)
    assert vapi == 6771000


def test_value_added_personalised_index():
    prices = [100, 210, 270, 250, 180, 220]
    vapi = other_bulk.value_added_personalised_index(prices)
    assert vapi == [111000, 6771000, -128649000, 8876781000, 363948021000]
