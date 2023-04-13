from src.PyTechnicalIndicators.Single.other import value_added_personalised_index


def test_value_added_personalised_index_no_previous():
    vapi = value_added_personalised_index(100, 210)
    assert vapi == 111000


def test_value_added_personalised_index_previous():
    vapi = value_added_personalised_index(210, 270, 111000)
    assert vapi == 6771000
