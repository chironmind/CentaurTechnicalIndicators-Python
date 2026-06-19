"""Pin the accepted string-alias sets for the three string-parsed regimes.

These tests lock the model-type / deviation-model / moving-average-type aliases to their
results so the mapping can't silently drift. Each alias is asserted to produce the *same*
result as its canonical one-word form, and invalid strings must raise ``ValueError``.

Three vocabularies are in play for ConstantModelType / DeviationModel: a primary one-word
form, a short abbreviation, and a long snake_case form. The notable traps are ``ma`` ->
Simple and ``sma`` -> Smoothed. MovingAverageType is deliberately stricter: it accepts only
the three one-word forms and rejects the abbreviations.
"""

import math

import pytest

from centaur_technical_indicators import momentum_indicators as mom
from centaur_technical_indicators import candle_indicators as can
from centaur_technical_indicators import moving_average as ma

PRICES = [100.0, 101.0, 102.0, 101.5, 102.5, 103.0, 102.0]


def same(a, b):  # NaN != NaN, so treat two NaNs as equal
    if isinstance(a, float) and isinstance(b, float):
        return a == b or (math.isnan(a) and math.isnan(b))
    return a == b  # tuples compare elementwise


def test_constant_model_aliases():
    rsi = lambda m: mom.single.relative_strength_index(PRICES, m)
    assert same(rsi("ma"), rsi("simple")) and same(rsi("simple_moving_average"), rsi("simple"))
    assert same(rsi("sma"), rsi("smoothed")) and same(rsi("smoothed_moving_average"), rsi("smoothed"))
    assert same(rsi("ema"), rsi("exponential")) and same(rsi("exponential_moving_average"), rsi("exponential"))
    assert same(rsi("smm"), rsi("median")) and same(rsi("simple_moving_median"), rsi("median"))
    assert same(rsi("simple_moving_mode"), rsi("mode"))
    with pytest.raises(ValueError):
        rsi("not_a_model")


def test_deviation_model_aliases():
    band = lambda d: can.single.moving_constant_bands(PRICES, "simple", d, 3.0)
    assert band("std") == band("standard") == band("standard_deviation")
    assert band("mean") == band("mean_absolute_deviation")
    assert band("median") == band("median_absolute_deviation")
    assert band("mode") == band("mode_absolute_deviation")
    assert band("ulcer") == band("ulcer_index")
    assert band("log") == band("logstd") == band("log_standard_deviation")
    assert band("laplace") == band("laplace_std_equivalent")
    assert band("cauchy") == band("cauchy_iqr_scale")
    with pytest.raises(ValueError):
        band("not_a_model")


def test_moving_average_type_only_three():
    mav = lambda m: ma.single.moving_average(PRICES, m)
    mav("simple"); mav("smoothed"); mav("exponential")  # accepted
    for rejected in ("ma", "sma", "ema", "simple_moving_average", "nope"):
        with pytest.raises(ValueError):
            mav(rejected)
