import pytest

from src.PyTechnicalIndicators.Bulk.strength_indicators import accumulation_distribution_indicator


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
