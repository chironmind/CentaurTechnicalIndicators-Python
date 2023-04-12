from src.PyTechnicalIndicators.Single.moving_averages import mcginley_dynamic


def test_mcginley_dynamic_no_previous():
    md = mcginley_dynamic(100, 10)
    assert md == 100


def test_mcginley_dynamic_previous():
    md = mcginley_dynamic(110, 10, 100)
    assert md == 100.68301345536507
