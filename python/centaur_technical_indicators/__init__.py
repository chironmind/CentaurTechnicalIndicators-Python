from .centaur_technical_indicators import *
from . import centaur_technical_indicators as _ext

__doc__ = _ext.__doc__
if hasattr(_ext, "__all__"):
    __all__ = list(_ext.__all__)

from importlib.metadata import version as _version, PackageNotFoundError as _PNFE

try:
    __version__ = _version("centaur_technical_indicators")
except _PNFE:  # source tree without installed dist-info
    __version__ = "0.0.0+unknown"

del _ext, _version, _PNFE
