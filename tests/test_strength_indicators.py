import pytest

from src.PyTechnicalIndicators.Single import strength_indicators as strength_indicators_single
from src.PyTechnicalIndicators.Bulk import strength_indicators as strength_indicators_bulk


def test_single_directional_movement():
    assert strength_indicators_single.directional_movement(103, 100, 93, 90) == 3
    assert strength_indicators_single.directional_movement(100, 103, 90, 93) == 3
    assert strength_indicators_single.directional_movement(103, 103, 93, 93) == 0


def test_single_directional_indicator():
    assert strength_indicators_single.directional_indicator(103, 100, 93, 90, 95) == 0.3
    assert strength_indicators_single.directional_indicator(100, 103, 90, 93, 95) == 0.3
    assert strength_indicators_single.directional_indicator(103, 103, 93, 93, 95) == 0


def test_single_period_directional_indicator():
    high = [127, 107, 130, 109, 120]
    low = [87, 97, 85, 81, 80]
    close = [115, 106, 124, 90, 88]
    pdi = strength_indicators_single.period_directional_indicator(high, low, close)
    assert pdi == (0.2085889570552147, 0.024539877300613498, 163)


def test_single_period_directional_indicator_known_previous():
    known_previous_di = strength_indicators_single.period_directional_indicator_known_previous(110, 120, 75, 80, 79, (34, 4, 163), 5)
    assert known_previous_di == (0.16444981862152358, 0.049576783555018135, 165.4)


def test_single_known_previous_directional_indicator():
    assert strength_indicators_single.known_previous_directional_indicator(0, 34, 5) == 27.2
    assert strength_indicators_single.known_previous_directional_indicator(5, 4, 5) == 8.2


def test_single_directional_index():
    assert strength_indicators_single.directional_index(16.444981862152358, 4.9576783555018135) == 0.536723163841808
    assert strength_indicators_single.directional_index(4.9576783555018135, 16.444981862152358) == 0.536723163841808


def test_single_average_directional_index():
    adx = strength_indicators_single.average_directional_index([0.789473684210526, 0.536723163841808], 'ma')
    assert adx == 0.663098424026167


# TODO: Test adi non personal for errors, missing a bunch of tests
def test_single_accumulation_distribution_indicator():
    adi = strength_indicators_single.accumulation_distribution_indicator(140, 90, 110, 1250, 1800)
    assert adi == 1550


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
