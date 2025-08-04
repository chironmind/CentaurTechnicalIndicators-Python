import pytest

from pytechnicalindicators import moving_average

"""The purpose of these tests are just to confirm that the bindings work.

These tests are not meant to be in depth, nor to test all edge cases, those should be
done in [RustTI](https://github.com/chironmind/RustTI). These tests exist to confirm whether an update in the bindings, or
RustTI has broken functionality.

To run the tests `maturin` needs to have built the egg. To do so run the following from
your CLI

```shell
$ source you_venv_location/bin/activate

$ pip3 install -r test_requirements.txt

$ maturin develop

$ pytest .
```
"""

prices = [100.0, 102.0, 103.0, 101.0, 99.0]

def test_single_moving_average():
    assert moving_average.single.moving_average(prices, "simple") == 101.0
    assert moving_average.single.moving_average(prices, "smoothed") == 100.81627796287482
    assert moving_average.single.moving_average(prices, "exponential") == 100.61137440758296
    with pytest.raises(ValueError):
        moving_average.single.moving_average(prices, "")

def test_bulk_moving_average():
    assert moving_average.bulk.moving_average(prices, "simple", 3) == [101.66666666666667, 102.0, 101.0]
    assert moving_average.bulk.moving_average(prices, "smoothed", 3) == [102.05263157894737, 101.8421052631579, 100.47368421052633]
    assert moving_average.bulk.moving_average(prices, "exponential", 3) == [102.28571428571429, 101.71428571428571, 100.14285714285714]
    with pytest.raises(ValueError):
        moving_average.bulk.moving_average(prices, "", 3)

def test_single_mcginley_dynamic():
    assert moving_average.single.mcginley_dynamic(prices[-1], 0.0, 3) == 99.0

def test_bulk_mcginley_dynamic():
    assert moving_average.bulk.mcginley_dynamic(prices, 0.0, 3) == [103.0, 102.2789387706985, 101.03380467203097]
