"""Public package API exposing session factory aliases for VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from vida_py.access import Session as AccessServerSession
    from vida_py.basedata import Session as BaseDataSession
    from vida_py.carcom import Session as CarComSession
    from vida_py.diag import Session as DiagRepoSession
    from vida_py.epc import Session as EpcSession
    from vida_py.images import Session as ImageRepoSession
    from vida_py.service import Session as ServiceRepoSession
    from vida_py.session import Session as DiagSessionSession
    from vida_py.timing import Session as DiceTimingSession

__version__ = "0.2.0"

__all__ = [
    "AccessServerSession",
    "BaseDataSession",
    "CarComSession",
    "DiagRepoSession",
    "DiagSessionSession",
    "DiceTimingSession",
    "EpcSession",
    "ImageRepoSession",
    "ServiceRepoSession",
]

_SESSION_EXPORTS = {
    "AccessServerSession": ("vida_py.access", "Session"),
    "BaseDataSession": ("vida_py.basedata", "Session"),
    "CarComSession": ("vida_py.carcom", "Session"),
    "DiagRepoSession": ("vida_py.diag", "Session"),
    "DiagSessionSession": ("vida_py.session", "Session"),
    "DiceTimingSession": ("vida_py.timing", "Session"),
    "EpcSession": ("vida_py.epc", "Session"),
    "ImageRepoSession": ("vida_py.images", "Session"),
    "ServiceRepoSession": ("vida_py.service", "Session"),
}


def __getattr__(name: str) -> Any:
    if name not in _SESSION_EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attribute_name = _SESSION_EXPORTS[name]
    return getattr(import_module(module_name), attribute_name)
