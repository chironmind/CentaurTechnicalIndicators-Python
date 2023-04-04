from src.PyTechnicalIndicators.Single.strength_indicators import accumulation_distribution_indicator


def test_accumulation_distribution_indicator():
    adi = accumulation_distribution_indicator(140, 90, 110, 1250, 1800)
    assert adi == 1550
