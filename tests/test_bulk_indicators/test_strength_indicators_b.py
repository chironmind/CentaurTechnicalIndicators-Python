import pytest

from src.PyTechnicalIndicators.Bulk.strength_indicators import accumulation_distribution_indicator, personalised_average_directional_index


def test_accumulation_distribution_indicator():
    high = [190, 220, 215]
    low = [160, 180, 170]
    close = [165, 200, 200]
    volume = [1200, 1500, 1200]
    adi = accumulation_distribution_indicator(high, low, close, volume)
    assert len(adi) == 3
    assert adi == [-800, -800, -400]


def test_accumulation_distribution_indicator_length_exception():
    high = [190, 220]
    low = [160, 180, 170]
    close = [165, 200, 200]
    volume = [1200, 1500, 1200]

    with pytest.raises(Exception) as e:
        accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    high = [190, 220, 215]
    low = [160, 180]

    with pytest.raises(Exception) as e:
        accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    low = [160, 180, 170]
    close = [165, 200]

    with pytest.raises(Exception) as e:
        accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'

    close = [165, 200, 200]
    volume = [1200, 1500]

    with pytest.raises(Exception) as e:
        accumulation_distribution_indicator(high, low, close, volume)

    assert str(e.value) == f'lengths needs to match, high: {len(high)}, low: {len(low)}, close {len(close)}, volume{len(volume)}'


def test_average_directional_index():
    high = [130, 145, 156, 139, 140, 166, 152, 156, 148, 143, 139, 135]
    low = [109, 105, 123, 118, 122, 135, 136, 140, 132, 128, 133, 125]
    close = [125, 120, 137, 128, 125, 142, 139, 152, 139, 140, 135, 120]

    adi = personalised_average_directional_index(high, low, close, 3)

    assert adi == [0]