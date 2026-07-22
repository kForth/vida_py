"""SQLAlchemy mappings for SQL views in the diag VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class diagnostic_ImageWithProfile:  # noqa: N801
    __bind_key__ = "diag"
    __viewname__ = "diagnostic_ImageWithProfile"

    Expr1: Mapped[str] = mapped_column(String(16))
    FullTitle: Mapped[str] = mapped_column(String(2337))


class ProfileDescription:
    __bind_key__ = "diag"
    __viewname__ = "ProfileDescription"

    Id: Mapped[str] = mapped_column(String(16))
    NavTitle: Mapped[str] = mapped_column(String(1309))
