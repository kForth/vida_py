from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vida_py.models import Model


class _ProfileParam:
    __bind_key__ = "basedata"
    __bind_key__ = "basedata"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class AMYProfileMap(Model):
    __bind_key__ = "basedata"
    __tablename__ = "AMYProfileMap"

    fkSourceProfile: Mapped[str] = mapped_column(
        ForeignKey("VehicleProfile.Id"), primary_key=True
    )
    fkTargetProfile: Mapped[str] = mapped_column(
        ForeignKey("VehicleProfile.Id"), primary_key=True
    )


class BodyStyle(_ProfileParam, Model):
    __tablename__ = "BodyStyle"


class BrakeSystem(_ProfileParam, Model):
    __tablename__ = "BrakeSystem"


class Engine(_ProfileParam, Model):
    __tablename__ = "Engine"


class ModelYear(_ProfileParam, Model):
    __tablename__ = "ModelYear"


class NodeECU(_ProfileParam, Model):
    __tablename__ = "NodeECU"


class PartnerGroup(_ProfileParam, Model):
    __tablename__ = "PartnerGroup"

    Cid: Mapped[str] = mapped_column(String(10))


class SelectedProfiles(Model):
    __bind_key__ = "basedata"
    __tablename__ = "SelectedProfiles"

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    SelectedProfiles: Mapped[str] = mapped_column(String(255))


class SpecialVehicle(_ProfileParam, Model):
    __tablename__ = "SpecialVehicle"


class Steering(_ProfileParam, Model):
    __tablename__ = "Steering"


class StructureWeek(_ProfileParam, Model):
    __tablename__ = "StructureWeek"

    Cid: Mapped[str] = mapped_column(String(50))


class Suspension(_ProfileParam, Model):
    __tablename__ = "Suspension"


class Transmission(_ProfileParam, Model):
    __tablename__ = "Transmission"


class ValidProfiles(Model):
    __bind_key__ = "basedata"
    __tablename__ = "ValidProfiles"

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    ValidProfile: Mapped[str] = mapped_column(String(255), primary_key=True)


class VehicleModel(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VehicleModel"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ImagePath: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class VehicleProfile(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VehicleProfile"

    Id: Mapped[str] = mapped_column(String(16), primary_key=True)
    FolderLevel: Mapped[int] = mapped_column(SmallInteger)
    Description: Mapped[str] = mapped_column(String(255))
    Title: Mapped[str] = mapped_column(String(255))
    ChassisNoFrom: Mapped[int] = mapped_column(Integer)
    ChassisNoTo: Mapped[int] = mapped_column(Integer)
    fkNodeECU: Mapped[int] = mapped_column(ForeignKey("NodeECU.Id"))
    fkVehicleModel: Mapped[int] = mapped_column(ForeignKey("VehicleModel.Id"))
    fkBodyStyle: Mapped[int] = mapped_column(ForeignKey("BodyStyle.Id"))
    fkSteering: Mapped[int] = mapped_column(ForeignKey("Steering.Id"))
    fkTransmission: Mapped[int] = mapped_column(ForeignKey("Transmission.Id"))
    fkSuspension: Mapped[int] = mapped_column(ForeignKey("Suspension.Id"))
    fkEngine: Mapped[int] = mapped_column(ForeignKey("Engine.Id"))
    fkStructureWeek: Mapped[int] = mapped_column(ForeignKey("StructureWeek.Id"))
    fkBrakeSystem: Mapped[int] = mapped_column(ForeignKey("BrakeSystem.Id"))
    fkPartnerGroup: Mapped[int] = mapped_column(ForeignKey("PartnerGroup.Id"))
    fkModelYear: Mapped[int] = mapped_column(ForeignKey("ModelYear.Id"))
    fkSpecialVehicle: Mapped[int] = mapped_column(ForeignKey("SpecialVehicle.Id"))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)

    NodeECU: Mapped["NodeECU"] = relationship()
    VehicleModel: Mapped["VehicleModel"] = relationship()
    BodyStyle: Mapped["BodyStyle"] = relationship()
    Steering: Mapped["Steering"] = relationship()
    Transmission: Mapped["Transmission"] = relationship()
    Suspension: Mapped["Suspension"] = relationship()
    Engine: Mapped["Engine"] = relationship()
    StructureWeek: Mapped["StructureWeek"] = relationship()
    BrakeSystem: Mapped["BrakeSystem"] = relationship()
    PartnerGroup: Mapped["PartnerGroup"] = relationship()
    ModelYear: Mapped["ModelYear"] = relationship()
    SpecialVehicle: Mapped["SpecialVehicle"] = relationship()


class VehicleProfilePartnerGroup(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VehicleProfilePartnerGroup"

    fkVehicleProfile: Mapped[str] = mapped_column(
        ForeignKey("VehicleProfile.Id"), primary_key=True
    )
    PartnerGroupCID: Mapped[str] = mapped_column(String(10), primary_key=True)


class VINDecodeModel(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VINDecodeModel"

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    VinStartPos: Mapped[int] = mapped_column(SmallInteger)
    VinEndPos: Mapped[int] = mapped_column(SmallInteger)
    VinCompare: Mapped[str] = mapped_column(String(8))
    fkVehicleModel: Mapped[int] = mapped_column(ForeignKey("VehicleModel.Id"))
    fkModelYear: Mapped[int] = mapped_column(ForeignKey("ModelYear.Id"))
    fkBodyStyle: Mapped[int] = mapped_column(ForeignKey("BodyStyle.Id"))
    fkPartnerGroup: Mapped[int] = mapped_column(ForeignKey("PartnerGroup.Id"))
    ChassisNoFrom: Mapped[int] = mapped_column(Integer)
    ChassisNoTo: Mapped[int] = mapped_column(Integer)
    YearCodePos: Mapped[int] = mapped_column(SmallInteger)
    YearCode: Mapped[str] = mapped_column(String(1))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class VINDecodeVariant(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VINDecodeVariant"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    VinStartPos: Mapped[int] = mapped_column(SmallInteger)
    VinEndPos: Mapped[int] = mapped_column(SmallInteger)
    VinCompare: Mapped[str] = mapped_column(String(8))
    fkVehicleModel: Mapped[int] = mapped_column(ForeignKey("VehicleModel.Id"))
    fkModelYear: Mapped[int] = mapped_column(ForeignKey("ModelYear.Id"))
    fkPartnerGroup: Mapped[int] = mapped_column(ForeignKey("PartnerGroup.Id"))
    fkEngine: Mapped[int] = mapped_column(ForeignKey("Engine.Id"))
    fkTransmission: Mapped[int] = mapped_column(ForeignKey("Transmission.Id"))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class VINVariantCodes(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VINVariantCodes"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    VINVariantCode: Mapped[str] = mapped_column(String(8))
    fkEngine: Mapped[int] = mapped_column(ForeignKey("Engine.Id"))
    fkBodyStyle: Mapped[int] = mapped_column(ForeignKey("BodyStyle.Id"))
    fkTransmission: Mapped[int] = mapped_column(ForeignKey("Transmission.Id"))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)
