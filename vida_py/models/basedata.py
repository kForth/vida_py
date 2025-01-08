from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vida_py.models import Model


class AMYProfileMap(Model):
    __bind_key__ = "basedata"
    __tablename__ = "AMYProfileMap"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkSourceProfile: Mapped[str] = mapped_column(ForeignKey("VehicleProfile.Id"))
    fkTargetProfile: Mapped[str] = mapped_column(ForeignKey("VehicleProfile.Id"))


class BodyStyle(Model):
    __bind_key__ = "basedata"
    __tablename__ = "BodyStyle"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class BrakeSystem(Model):
    __bind_key__ = "basedata"
    __tablename__ = "BrakeSystem"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class Engine(Model):
    __bind_key__ = "basedata"
    __tablename__ = "Engine"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class ModelYear(Model):
    __bind_key__ = "basedata"
    __tablename__ = "ModelYear"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class NodeECU(Model):
    __bind_key__ = "basedata"
    __tablename__ = "NodeECU"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class PartnerGroup(Model):
    __bind_key__ = "basedata"
    __tablename__ = "PartnerGroup"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[str] = mapped_column(String(10))
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class SelectedProfiles(Model):
    __bind_key__ = "basedata"
    __tablename__ = "SelectedProfiles"

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    SelectedProfiles: Mapped[str] = mapped_column(String(255))


class SpecialVehicle(Model):
    __bind_key__ = "basedata"
    __tablename__ = "SpecialVehicle"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class Steering(Model):
    __bind_key__ = "basedata"
    __tablename__ = "Steering"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class StructureWeek(Model):
    __bind_key__ = "basedata"
    __tablename__ = "StructureWeek"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class Suspension(Model):
    __bind_key__ = "basedata"
    __tablename__ = "Suspension"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class Transmission(Model):
    __bind_key__ = "basedata"
    __tablename__ = "Transmission"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Cid: Mapped[int] = mapped_column(Integer)
    Description: Mapped[str] = mapped_column(String(255))
    ObjVersion: Mapped[datetime] = mapped_column(DateTime)


class ValidProfiles(Model):
    __bind_key__ = "basedata"
    __tablename__ = "ValidProfiles"

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    ValidProfile: Mapped[str] = mapped_column(String(255))


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

    Id: Mapped[str] = mapped_column(String(1), primary_key=True)
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

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkVehicleProfile: Mapped[str] = mapped_column(ForeignKey("VehicleProfile.Id"))
    PartnerGroupCID: Mapped[str] = mapped_column(String(10))


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


class VehicleProfileDescriptions(Model):
    __bind_key__ = "basedata"
    __tablename__ = "VehicleProfileDescriptions"

    Id: Mapped[str] = mapped_column(String(1), primary_key=True)
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
