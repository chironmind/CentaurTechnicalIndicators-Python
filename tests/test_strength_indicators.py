import pytest

from src.PyTechnicalIndicators.Single import strength_indicators as strength_indicators_single
from src.PyTechnicalIndicators.Bulk import strength_indicators as strength_indicators_bulk


# TODO: Test adi non personal for errors, missing a bunch of tests
def test_single_accumulation_distribution_indicator():
    adi = strength_indicators_single.accumulation_distribution_indicator(140, 90, 110, 1250, 1800)
    assert adi == 1550


def test_single_average_directional_index_no_previous_adi():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    adi = strength_indicators_single.personalised_average_directional_index(high, low, close, 0, 3)
    assert adi == ['0']


def test_single_average_directional_index_previous_adi():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    adi = strength_indicators_single.personalised_average_directional_index(high, low, close, 105, 3)
    assert adi == ['0']


def test_single_average_directional_index_mismatch_length_exception():
    high = [130, 145, 156, 139, 140]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]

    with pytest.raises(Exception) as e:
        strength_indicators_single.personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122]
    with pytest.raises(Exception) as e:
        strength_indicators_single.personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'

    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125]
    with pytest.raises(Exception) as e:
        strength_indicators_single.personalised_average_directional_index(high, low, close, 105, 3)
    assert str(e.value) == f'Lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}'


def test_single_average_directional_index_period_length_exception():
    high = [130, 145, 156, 139, 140, 166]
    low = [109, 105, 123, 118, 122, 135]
    close = [125, 120, 137, 128, 125, 142]
    with pytest.raises(Exception) as e:
        strength_indicators_single.personalised_average_directional_index(high, low, close, 105, 30)
    assert str(e.value) == f'Period ({30}) needs to be smaller or equal length of lists ({len(high)})'


def test_bulk_accumulation_distribution_indicator():
    high = [190, 220, 215]
    low = [160, 180, 170]
    close = [165, 200, 200]
    volume = [1200, 1500, 1200]
    adi = strength_indicators_bulk.accumulation_distribution_indicator(high, low, close, volume)
    assert len(adi) == 3
    assert adi == [-800, -800, -400]


def test_bulk_accumulation_distribution_indicator_length_exception():
    high = [190, 220]
    low = [160, 180, 170]
    close = [165, 200, 200]
    volume = [1200, 1500, 1200]

    with pytest.raises(Exception) as e:
        strength_indicators_bulk.accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    high = [190, 220, 215]
    low = [160, 180]

    with pytest.raises(Exception) as e:
        accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    low = [160, 180, 170]
    close = [165, 200]

    with pytest.raises(Exception) as e:
        strength_indicators_bulk.accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    close = [165, 200, 200]
    volume = [1200, 1500]

    with pytest.raises(Exception) as e:
        strength_indicators_bulk.accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'


def test_bulk_average_directional_index():
    high = [130, 145, 156, 139, 140, 166, 152, 156, 148, 143, 139, 135]
    low = [109, 105, 123, 118, 122, 135, 136, 140, 132, 128, 133, 125]
    close = [125, 120, 137, 128, 125, 142, 139, 152, 139, 140, 135, 120]

    adi = strength_indicators_bulk.personalised_average_directional_index(high, low, close, 3)

    assert adi == [0]
