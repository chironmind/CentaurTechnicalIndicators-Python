from .centaur_technical_indicators import *
from . import centaur_technical_indicators as _ext

__doc__ = _ext.__doc__
if hasattr(_ext, "__all__"):
    __all__ = list(_ext.__all__)

# Register the compiled submodules under their qualified package names so the
# submodule import paths advertised by the .pyi stubs also work at runtime, e.g.
# `import centaur_technical_indicators.momentum_indicators` and
# `from centaur_technical_indicators.momentum_indicators import single`.
# (`from .<ext> import *` above only binds them as attributes of this package.)
import sys as _sys
import types as _types


def _register_submodules() -> None:
    g = globals()
    for _name in g.get("__all__", ()):
        _sub = g.get(_name)
        if isinstance(_sub, _types.ModuleType):
            _sys.modules.setdefault(__name__ + "." + _name, _sub)


_register_submodules()
del _register_submodules, _sys, _types

from importlib.metadata import version as _version, PackageNotFoundError as _PNFE

try:
    __version__ = _version("centaur_technical_indicators")
except _PNFE:  # source tree without installed dist-info
    __version__ = "0.0.0+unknown"

del _ext, _version, _PNFE
