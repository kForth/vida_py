from sqlalchemy import Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class RequestTimeoutAndResendView:
    __bind_key__ = "timing"
    __viewname__ = "RequestTimeoutAndResendView"

    ECU_variant: Mapped[int] = mapped_column(Integer)
    B1: Mapped[int] = mapped_column(SmallInteger)
    B2: Mapped[int] = mapped_column(SmallInteger)
    B3: Mapped[int] = mapped_column(SmallInteger)
    Timeout: Mapped[int] = mapped_column(Integer)
    Resend: Mapped[int] = mapped_column(Integer)


class RequestTimingView:
    __bind_key__ = "timing"
    __viewname__ = "RequestTimingView"

    ECU_variant: Mapped[int] = mapped_column(Integer)
    B1: Mapped[int] = mapped_column(SmallInteger)
    B2: Mapped[int] = mapped_column(SmallInteger)
    B3: Mapped[int] = mapped_column(SmallInteger)
    P1max: Mapped[int] = mapped_column(Integer)
    P3max: Mapped[int] = mapped_column(Integer)
    P4max: Mapped[int] = mapped_column(Integer)
