"""SQLAlchemy ORM models for the timing VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy import DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class _Model(DeclarativeBase):
    __bind_key__ = "timing"


class DBContent(_Model):
    __tablename__ = "DBContent"

    Release: Mapped[str] = mapped_column(String(50), primary_key=True)
    ScriptName: Mapped[str] = mapped_column(String(50), primary_key=True)
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class DBSchema(_Model):
    __tablename__ = "DBSchema"

    Version: Mapped[str] = mapped_column(String(50), primary_key=True)
    Release: Mapped[str] = mapped_column(String(50))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class MessageTiming(_Model):
    __tablename__ = "MessageTiming"

    MessageTimingID: Mapped[int] = mapped_column(Integer, primary_key=True)
    P1max: Mapped[int] = mapped_column(Integer)
    P3min: Mapped[int] = mapped_column(Integer)
    P4min: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))


class Requests(_Model):
    __tablename__ = "Requests"

    # No PK
    ECU_variant: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B1: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B2: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    B3: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    MessageTimingId: Mapped[int] = mapped_column(Integer)
    TimeoutAndResendId: Mapped[int] = mapped_column(Integer)
    Commet: Mapped[str] = mapped_column(String(500))


class TimeoutAndResend(_Model):
    __tablename__ = "TimeoutAndResend"

    TimeoutAndResendId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Timeout: Mapped[int] = mapped_column(Integer)
    Resend: Mapped[int] = mapped_column(Integer)
    Comment: Mapped[str] = mapped_column(String(500))
