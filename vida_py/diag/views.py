from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class diagnostic_ImageWithProfile(Model):
    __bind_key__ = "diag"
    __tablename__ = "diagnostic_ImageWithProfile"

    Expr1: Mapped[str] = mapped_column(String(16))
    FullTitle: Mapped[str] = mapped_column(String(2337))


class ProfileDescription(Model):
    __bind_key__ = "diag"
    __tablename__ = "ProfileDescription"

    Id: Mapped[str] = mapped_column(String(16))
    NavTitle: Mapped[str] = mapped_column(String(1309))
