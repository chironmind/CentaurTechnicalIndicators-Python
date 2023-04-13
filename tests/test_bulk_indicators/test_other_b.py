from src.PyTechnicalIndicators.Bulk.other import value_added_personalised_index


def test_value_added_personalised_index():
    prices = [100, 210, 270, 250, 180, 220]
    vapi = value_added_personalised_index(prices)
    assert vapi == [111000, 6771000, -128649000, 8876781000, 363948021000]
