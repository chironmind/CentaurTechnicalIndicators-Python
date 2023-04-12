import pytest

from src.PyTechnicalIndicators.Single.strength_indicators import accumulation_distribution_indicator, personalised_average_directional_index


def test_accumulation_distribution_indicator():
    adi = accumulation_distribution_indicator(140, 90, 110, 1250, 1800)
    assert adi == 1550


def test_average_directional_index_no_previous_adi():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    adi = personalised_average_directional_index(high, low, close, 0, 3)
    assert adi == ['0']


def test_average_directional_index_previous_adi():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    adi = personalised_average_directional_index(high, low, close, 105, 3)
    assert adi == ['0']


def test_average_directional_index_mismatch_length_exception():
    high = [130, 145, 156, 139, 140]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]

    with pytest.raises(Exception) as e:
        personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122]
    with pytest.raises(Exception) as e:
        personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125]
    with pytest.raises(Exception) as e:
        personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'


def test_average_directional_index_period_length_exception():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    with pytest.raises(Exception) as e:
        personalised_average_directional_index(high, low, close, 105, 30)
    assert str(e.value) == f'Period ({30}) needs to be smaller or equal length of lists ({len(high)})'
