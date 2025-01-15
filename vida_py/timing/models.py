from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
    pass


class MessageTiming(Model):
    __bind_key__ = "timing"
    __tablename__ = "MessageTiming"

    MessageTimingID: Mapped[int] = mapped_column(Integer, primary_key=True)
    P1max: Mapped[int] = mapped_column(Integer)
    P3min: Mapped[int] = mapped_column(Integer)
    P4min: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))


class Requests(Model):
    __bind_key__ = "timing"
    __tablename__ = "Requests"

    # No PK
    ECU_variant: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B1: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B2: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B3: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    MessageTimingId: Mapped[int] = mapped_column(Integer)
    TimeoutAndResendId: Mapped[int] = mapped_column(Integer)
    Commet: Mapped[str] = mapped_column(String(500))


class TimeoutAndResend(Model):
    __bind_key__ = "timing"
    __tablename__ = "TimeoutAndResend"

    TimeoutAndResendId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Timeout: Mapped[int] = mapped_column(Integer)
    Resend: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))
