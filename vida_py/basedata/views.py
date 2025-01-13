from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class VehicleProfileDescriptions:
    __bind_key__ = "basedata"
    __viewname__ = "VehicleProfileDescriptions"

    Id: Mapped[str] = mapped_column(String(16))
    FullTitle: Mapped[str] = mapped_column(String(2337))
    NavTitle: Mapped[str] = mapped_column(String(1823))
    VehicleModelDesc: Mapped[str] = mapped_column(String(255))
    ModelYearDesc: Mapped[str] = mapped_column(String(255))
    EngineDesc: Mapped[str] = mapped_column(String(255))
    TransmissionDesc: Mapped[str] = mapped_column(String(255))
    BodyStyleDesc: Mapped[str] = mapped_column(String(255))
    SteeringDesc: Mapped[str] = mapped_column(String(255))
    PartnerGroupDesc: Mapped[str] = mapped_column(String(255))
    BrakesSystemDesc: Mapped[str] = mapped_column(String(255))
    StructureWeekDesc: Mapped[str] = mapped_column(String(255))
    SpecialVehicleDesc: Mapped[str] = mapped_column(String(255))
    ChassiNoFrom: Mapped[int] = mapped_column(Integer)
    ChassiNoTo: Mapped[int] = mapped_column(Integer)
