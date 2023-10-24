import pytest

from src.PyTechnicalIndicators.Single import strength_indicators as strength_indicators_single
from src.PyTechnicalIndicators.Bulk import strength_indicators as strength_indicators_bulk

# TODO: Reorg to match functions order


def test_single_rsi():
    prices = [100, 103, 110, 115, 123, 115, 116, 112, 110, 106, 116, 116, 126, 130]
    rsi = strength_indicators_single.relative_strength_index(prices)
    assert rsi == 60.44650041420754


def test_single_personalised_rsi_no_negative():
    prices = [106, 116, 116, 126, 130]
    rsi = strength_indicators_single.relative_strength_index(prices)
    assert rsi == 100


def test_single_personalised_rsi():
    prices = [112, 110, 106, 116, 116, 126, 130]
    rsi = strength_indicators_single.relative_strength_index(prices)
    assert rsi == 68.22742474916387


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
        strength_indicators_bulk.accumulation_distribution_indicator(high, low, close, volume)

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


def test_single_directional_movement():
    assert strength_indicators_single.directional_movement(103, 100, 93, 90) == (3, 'positive')
    assert strength_indicators_single.directional_movement(100, 103, 90, 93) == (3, 'negative')
    assert strength_indicators_single.directional_movement(103, 103, 93, 93) == (0, 'none')


def test_single_period_directional_indicator():
    high = [127, 107, 130, 109, 120]
    low = [87, 97, 85, 81, 80]
    close = [115, 106, 124, 90, 88]
    pdi = strength_indicators_single.directional_indicator(high, low, close)
    assert pdi == (20.858895705521473, 2.4539877300613497, 163, 34, 4)


def test_single_period_directional_indicator_known_previous():
    known_previous_di = strength_indicators_single.directional_indicator_known_previous(110, 120, 75, 80, 79, 163, 34, 4, 5)
    assert known_previous_di == (16.444981862152358, 4.9576783555018135, 165.4, 27.2, 8.2)


def test_single_known_previous_directional_indicator():
    assert strength_indicators_single.known_previous_directional_movement(0, 34, 5) == 27.2
    assert strength_indicators_single.known_previous_directional_movement(5, 4, 5) == 8.2


def test_single_directional_index():
    assert strength_indicators_single.directional_index(16.444981862152358, 4.9576783555018135) == 0.536723163841808
    assert strength_indicators_single.directional_index(4.9576783555018135, 16.444981862152358) == 0.536723163841808


def test_single_average_directional_index():
    adx = strength_indicators_single.average_directional_index([0.789473684210526, 0.536723163841808], 'ma')
    assert adx == 0.663098424026167


def test_bulk_directional_indicator():
    high = [127, 107, 130, 109, 120, 110, 125, 110, 105, 103]
    low = [87, 97, 85, 81, 80, 75, 85, 70, 60, 50]
    close = [115, 106, 124, 90, 88, 79, 90, 85, 83, 45]
    di = strength_indicators_bulk.directional_indicator(high, low, close, 5)
    assert di == [
        (20.858895705521473, 2.4539877300613497, 163),
        (16.444981862152358, 4.9576783555018135, 165.4),
        (21.332404828226554, 3.8068709377901575, 172.32),
        (16.534724721122704, 11.384490824037423, 177.856),
        (12.561830965460091, 13.988535108027989, 187.2848),
        (9.056111058075762, 14.89632957740407, 207.82783999999998)
    ]


def test_bulk_directional_index():
    positive_directional_indicator = [20.858895705521473, 16.444981862152358, 21.332404828226554, 16.534724721122704, 12.561830965460091, 9.056111058075762]
    negative_directional_indicator = [2.4539877300613497, 4.9576783555018135, 3.8068709377901575, 11.384490824037423, 13.988535108027989, 14.89632957740407]
    idx = strength_indicators_bulk.directional_index(positive_directional_indicator, negative_directional_indicator)
    assert idx == [0.7894736842105263, 0.536723163841808, 0.6971375807940905, 0.18446914773642656, 0.053735761632022705, 0.24382561293889254]


def test_bulk_average_directional_index():
    idx = [0.7894736842105263, 0.536723163841808, 0.6971375807940905, 0.18446914773642656, 0.053735761632022705, 0.24382561293889254]
    adx = strength_indicators_bulk.average_directional_index(idx, 3, 'ma')
    assert adx == [0.6744448096154749, 0.47277663079077503, 0.31178083005417995, 0.16067684076911393]


def test_bulk_average_directional_index_rating():
    adx = [0.6744448096154749, 0.47277663079077503, 0.31178083005417995, 0.16067684076911393]
    adxr = strength_indicators_bulk.average_directional_index_rating(adx, 3)
    assert adxr == [0.49311281983482746, 0.3167267357799445]


def test_bulk_rsi():
    prices = [100, 103, 110, 115, 123, 115, 116, 112, 110, 106, 116, 116, 126, 130, 118]
    rsi = strength_indicators_bulk.relative_strength_index(prices)
    assert rsi == [60.44650041420754, 49.98706804800788]


def test_bulk_personal_rsi():
    prices = [100, 103, 110, 115, 123, 115, 116, 112, 110, 106, 116, 116, 126, 130, 118]
    rsi = strength_indicators_bulk.relative_strength_index(prices, 13, 'ma')
    assert rsi == [58.27814569536424, 58.82352941176471, 51.35135135135135]
