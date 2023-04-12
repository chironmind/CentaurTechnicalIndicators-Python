from src.PyTechnicalIndicators.Bulk.moving_averages import mcginley_dynamic


def test_mcginley_dynamic():
    prices = [100, 110, 112, 115, 113, 111]
    md = mcginley_dynamic(prices, 10)
    assert md == [100, 100.68301345536507, 101.42207997889615, 102.24351258209249, 102.96445361554517, 103.55939307450244]