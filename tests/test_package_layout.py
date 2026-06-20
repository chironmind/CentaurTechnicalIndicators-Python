"""Package-layout / typing contract tests (S7 mixed layout).

These guard the public package surface the `.pyi` stubs advertise: a resolvable
`__version__`, `__all__` == the nine submodules, and that every submodule is
importable by its qualified path at runtime (not only as an attribute) — so the
stubs do not promise import paths that raise `ModuleNotFoundError`.
"""

import importlib

import centaur_technical_indicators as cti

SUBMODULES = [
    "candle_indicators",
    "chart_trends",
    "correlation_indicators",
    "momentum_indicators",
    "moving_average",
    "other_indicators",
    "strength_indicators",
    "trend_indicators",
    "volatility_indicators",
]


def test_version_resolves():
    assert isinstance(cti.__version__, str)
    assert cti.__version__ not in ("", "0.0.0+unknown")


def test_all_is_the_nine_submodules():
    assert sorted(cti.__all__) == sorted(SUBMODULES)
    assert cti.__doc__


def test_submodules_importable_by_qualified_path():
    for name in SUBMODULES:
        mod = importlib.import_module(f"centaur_technical_indicators.{name}")
        assert mod is getattr(cti, name)


def test_from_submodule_imports_work():
    from centaur_technical_indicators.chart_trends import peaks
    from centaur_technical_indicators.momentum_indicators import single

    assert callable(peaks)
    assert hasattr(single, "relative_strength_index")
