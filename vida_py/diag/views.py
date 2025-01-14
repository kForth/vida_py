from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class diagnostic_ImageWithProfile:
    __bind_key__ = "diag"
    __viewname__ = "diagnostic_ImageWithProfile"

    Expr1: Mapped[str] = mapped_column(String(16))
    FullTitle: Mapped[str] = mapped_column(String(2337))


class ProfileDescription:
    __bind_key__ = "diag"
    __viewname__ = "ProfileDescription"

    Id: Mapped[str] = mapped_column(String(16))
    NavTitle: Mapped[str] = mapped_column(String(1309))
