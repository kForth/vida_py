from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class MessageTiming(Model):
    __bind_key__ = "timing"
    __tablename__ = "MessageTiming"

    P1max: Mapped[int] = mapped_column(Integer)
    P3min: Mapped[int] = mapped_column(Integer)
    P4min: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))


class RequestTimeoutAndResendView(Model):
    __bind_key__ = "timing"
    __tablename__ = "RequestTimeoutAndResendView"

    B1: Mapped[int] = mapped_column(SmallInteger)
    B2: Mapped[int] = mapped_column(SmallInteger)
    B3: Mapped[int] = mapped_column(SmallInteger)
    Timeout: Mapped[int] = mapped_column(Integer)
    Resend: Mapped[int] = mapped_column(Integer)


class Requests(Model):
    __bind_key__ = "timing"
    __tablename__ = "Requests"

    B1: Mapped[int] = mapped_column(SmallInteger)
    B2: Mapped[int] = mapped_column(SmallInteger)
    B3: Mapped[int] = mapped_column(SmallInteger)
    MessageTimingId: Mapped[int] = mapped_column(Integer)
    TimeoutAndResendId: Mapped[int] = mapped_column(Integer)
    Commet: Mapped[str] = mapped_column(String(500))


class TimeoutAndResend(Model):
    __bind_key__ = "timing"
    __tablename__ = "TimeoutAndResend"

    Timeout: Mapped[int] = mapped_column(Integer)
    Resend: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))
