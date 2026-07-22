"""Public package API exposing session factory aliases for VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from vida_py.access import Session as AccessServerSession
from vida_py.basedata import Session as BaseDataSession
from vida_py.carcom import Session as CarComSession
from vida_py.diag import Session as DiagRepoSession
from vida_py.epc import Session as EpcSession
from vida_py.images import Session as ImageRepoSession
from vida_py.service import Session as ServiceRepoSession
from vida_py.session import Session as DiagSessionSession
from vida_py.timing import Session as DiceTimingSession

__version__ = "0.1.7"

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
