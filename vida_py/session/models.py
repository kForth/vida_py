"""SQLAlchemy ORM models for the session VIDA database."""

# ruff: noqa: N815

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy import BINARY, VARBINARY, BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class _Model(DeclarativeBase):
    __bind_key__ = "session"


class ActionItem(_Model):
    __tablename__ = "ActionItem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Not in DB
    fkCustomerSymptom: Mapped[int] = mapped_column(Integer)
    fkWorkshopSession: Mapped[int] = mapped_column(Integer)
    occuranceDate: Mapped[datetime] = mapped_column(DateTime)
    action: Mapped[str] = mapped_column(String(100))
    resultOk: Mapped[bool] = mapped_column(Boolean)
    actionSkipped: Mapped[bool] = mapped_column(Boolean)
    symptomIEMapId: Mapped[int] = mapped_column(Integer)
    infoType: Mapped[str] = mapped_column(String(64))
    userChoice: Mapped[bool] = mapped_column(Boolean)
    dtcReadoutConclusion: Mapped[int] = mapped_column(Integer)


class CommToolInfo(_Model):
    __tablename__ = "CommToolInfo"

    WorkshopSessionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Type: Mapped[str] = mapped_column(String(50))
    Name: Mapped[str] = mapped_column(String(50))
    FirmwareVersion: Mapped[str] = mapped_column(String(80))
    DllVersion: Mapped[str] = mapped_column(String(80))
    ApiVersion: Mapped[str] = mapped_column(String(80))


class CryptKey(_Model):
    __tablename__ = "CryptKey"

    Version: Mapped[int] = mapped_column(Integer, primary_key=True)
    KeyData: Mapped[bytes] = mapped_column(VARBINARY)


class DiagnosticScript(_Model):
    __tablename__ = "DiagnosticScript"

    ScriptId: Mapped[str] = mapped_column(String(32), primary_key=True)
    fkPiePackage: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    XmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class DownloadConfirmation(_Model):
    __tablename__ = "DownloadConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    VehicleConfig: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))


class DroLog(_Model):
    __tablename__ = "DroLog"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    EcuAddress: Mapped[int] = mapped_column(Integer)
    Request: Mapped[bytes] = mapped_column(VARBINARY)
    Response: Mapped[bytes] = mapped_column(VARBINARY)


class Dtc(_Model):
    __tablename__ = "Dtc"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkDtcReadoutId: Mapped[int] = mapped_column(Integer)
    fkEcuInfoId: Mapped[int] = mapped_column(Integer)
    Text: Mapped[str] = mapped_column(String(250))
    HexValue: Mapped[str] = mapped_column(String(50))
    Raw: Mapped[str] = mapped_column(String(50))
    Status: Mapped[str] = mapped_column(String(50))
    symptomId: Mapped[int] = mapped_column(Integer)
    timeFirstSet: Mapped[int] = mapped_column(Integer)
    permanentStatus: Mapped[int] = mapped_column(Integer)
    MileageKilometres: Mapped[int] = mapped_column(Integer)
    MileageMiles: Mapped[int] = mapped_column(Integer)
    ShowAlways: Mapped[bool] = mapped_column(Boolean)
    OkIfIntermittent: Mapped[bool] = mapped_column(Boolean)
    CalculateUsingCounters: Mapped[bool] = mapped_column(Boolean)
    IsActive: Mapped[bool] = mapped_column(Boolean)


class DtcReadout(_Model):
    __tablename__ = "DtcReadout"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    Timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    GlobalTime: Mapped[int] = mapped_column(Integer)
    EcuType: Mapped[int] = mapped_column(Integer)
    IsFirst: Mapped[bool] = mapped_column(Boolean)


class ESWDL(_Model):
    __tablename__ = "ESWDL"

    PartsId: Mapped[str] = mapped_column(String(16), primary_key=True)
    CheckSum: Mapped[str] = mapped_column(String(50))
    Filename: Mapped[str] = mapped_column(String(500))
    InstallDate: Mapped[datetime] = mapped_column(DateTime)
    Installed: Mapped[bool] = mapped_column(Boolean)


class EcuInfo(_Model):
    __tablename__ = "EcuInfo"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    SystemCode: Mapped[int] = mapped_column(Integer)
    EcuType: Mapped[int] = mapped_column(Integer)
    EcuAddress: Mapped[int] = mapped_column(Integer)
    EcuIdentifier: Mapped[str] = mapped_column(String(50))
    PartNo: Mapped[str] = mapped_column(String(50))
    DiagNo: Mapped[str] = mapped_column(String(50))
    SerialNo: Mapped[str] = mapped_column(String(50))
    EcuStatus: Mapped[int] = mapped_column(Integer)
    EcuVariantId: Mapped[str] = mapped_column(String(50))


class EcuSoftware(_Model):
    __tablename__ = "EcuSoftware"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkEcuInfoId: Mapped[int] = mapped_column(Integer)
    softwareName: Mapped[str] = mapped_column(String(50))
    softwarePartNo: Mapped[str] = mapped_column(String(50))


class FaultCounter(_Model):
    __tablename__ = "FaultCounter"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkDtc: Mapped[int] = mapped_column(Integer)
    countername: Mapped[str] = mapped_column(String(100))
    countervalue: Mapped[int] = mapped_column(Integer)
    countertextid: Mapped[int] = mapped_column(Integer)


class FreezeFrameParam(_Model):
    __tablename__ = "FreezeFrameParam"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkDtcId: Mapped[int] = mapped_column(Integer)
    paramId: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(500))
    value: Mapped[str] = mapped_column(String(500))
    blockId: Mapped[int] = mapped_column(Integer)


class GblPackage(_Model):
    __tablename__ = "GblPackage"

    SwPartNumber: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fkPiePackage: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    Gbl: Mapped[bytes] = mapped_column(BINARY(2147483647))
    Code: Mapped[bytes] = mapped_column(BINARY(2147483647))


class HistoryItem(_Model):
    __tablename__ = "HistoryItem"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[str] = mapped_column(String(20))
    OrderRef: Mapped[str] = mapped_column(String(10))
    VIN: Mapped[str] = mapped_column(String(17))
    ChassisNumber: Mapped[str] = mapped_column(String(6))
    Model: Mapped[int] = mapped_column(Integer)
    ModelYear: Mapped[str] = mapped_column(String(10))
    FinalStatus: Mapped[str] = mapped_column(String(20))
    OrderDate: Mapped[datetime] = mapped_column(DateTime)
    VcpOrderNumber: Mapped[str] = mapped_column(String(17))
    OrderId: Mapped[int] = mapped_column(BigInteger)


class HistoryLoadedEcuItem(_Model):
    __tablename__ = "HistoryLoadedEcuItem"

    # No PK
    fkHistoryItem: Mapped[int] = mapped_column(Integer, primary_key=True)
    LoadedEcu: Mapped[str] = mapped_column(String(30), primary_key=True)


class HistoryVehicleOrderItem(_Model):
    __tablename__ = "HistoryVehicleOrderItem"

    fkHistoryItem: Mapped[int] = mapped_column(Integer, primary_key=True)
    SwProdId: Mapped[int] = mapped_column(BigInteger, primary_key=True)


class KeyValue(_Model):
    __tablename__ = "KeyValue"

    key: Mapped[str] = mapped_column(String(250), primary_key=True)
    value: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))


class ObservedSymptom(_Model):
    __tablename__ = "ObservedSymptom"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    symptomId: Mapped[int] = mapped_column(Integer)
    fkworkshopSessionId: Mapped[int] = mapped_column(Integer)
    Note: Mapped[str] = mapped_column(String(256))


class OrderVehicle(_Model):
    __tablename__ = "OrderVehicle"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    VIN: Mapped[str] = mapped_column(String(17))
    ChassisNumber: Mapped[str] = mapped_column(String(6))
    Model: Mapped[int] = mapped_column(Integer)
    ModelYear: Mapped[str] = mapped_column(String(10))
    FYON: Mapped[int] = mapped_column(Integer)


class OrderVehiclePackage(_Model):
    __tablename__ = "OrderVehiclePackage"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    SpScriptXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    PieVehConfigXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VerifyTime: Mapped[int] = mapped_column(BigInteger)
    ConfirmTime: Mapped[int] = mapped_column(BigInteger)


class Parameter(_Model):
    __tablename__ = "Parameter"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkVehConfigId: Mapped[int] = mapped_column(Integer)
    ParamName: Mapped[str] = mapped_column(String(50))
    ParamValue: Mapped[str] = mapped_column(String(50))
    CarConfigParam: Mapped[bool] = mapped_column(Boolean)


class PendingConfirmation(_Model):
    __tablename__ = "PendingConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    ConfirmPackageXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class PieDownloadConfirmation(_Model):
    __tablename__ = "PieDownloadConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ConfirmTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class PieOrder(_Model):
    __tablename__ = "PieOrder"

    PieOrderId: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    VcpOrderNumber: Mapped[str] = mapped_column(String(17))
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ReceiveTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class PieOrderAttempt(_Model):
    __tablename__ = "PieOrderAttempt"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    DummySomething: Mapped[str] = mapped_column(String(1))
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class PiePackage(_Model):
    __tablename__ = "PiePackage"

    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)


class RestoreableParameter(_Model):
    __tablename__ = "RestoreableParameter"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    EcuType: Mapped[int] = mapped_column(Integer)
    Identifier: Mapped[str] = mapped_column(String(10))
    Value: Mapped[str] = mapped_column(String(255))


class RestoredParameter(_Model):
    __tablename__ = "RestoredParameter"

    # No PK
    pieOrderId: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    Name: Mapped[str] = mapped_column(String(100), primary_key=True)
    Value: Mapped[str] = mapped_column(String(100), primary_key=True)


class SlaveEcuInfo(_Model):
    __tablename__ = "SlaveEcuInfo"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkEcuInfoId: Mapped[int] = mapped_column(Integer)
    HwPartNumber: Mapped[str] = mapped_column(String(50))
    HwSerialNumber: Mapped[str] = mapped_column(String(50))
    HwPartNumberName: Mapped[str] = mapped_column(String(200))
    HwSerialNumberName: Mapped[str] = mapped_column(String(200))


class StatusIdentifier(_Model):
    __tablename__ = "StatusIdentifier"

    # No PK
    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkDtc: Mapped[int] = mapped_column(Integer)
    statusidentifierid: Mapped[int] = mapped_column(Integer)
    statusidentifiername: Mapped[str] = mapped_column(String(100))
    statusidentifiervalue: Mapped[int] = mapped_column(Integer)
    statusidentifiertext: Mapped[str] = mapped_column(String(250))


class UpdateOrder(_Model):
    __tablename__ = "UpdateOrder"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ReceiveTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class UpdateOrderAttempt(_Model):
    __tablename__ = "UpdateOrderAttempt"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class UpdateOrderDelivery(_Model):
    __tablename__ = "UpdateOrderDelivery"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)


class UpdateVehiclePackage(_Model):
    __tablename__ = "UpdateVehiclePackage"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    SpScriptXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    PieVehConfigXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VerifyTime: Mapped[int] = mapped_column(BigInteger)
    ConfirmTime: Mapped[int] = mapped_column(BigInteger)


class Vbf(_Model):
    __tablename__ = "Vbf"

    SwPartNumber: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fkPiePackage: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fkCryptKeyVersion: Mapped[int] = mapped_column(Integer)
    XmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class VehConfig(_Model):
    __tablename__ = "VehConfig"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkworkshopSessionId: Mapped[int] = mapped_column(Integer)
    VIN: Mapped[str] = mapped_column(String(50))
    Fyon: Mapped[int] = mapped_column(Integer)
    VehType: Mapped[str] = mapped_column(String(50))
    Chassis: Mapped[str] = mapped_column(String(50))
    FactoryCode: Mapped[str] = mapped_column(String(50))
    StructureWeek: Mapped[int] = mapped_column(Integer)
    DocNo: Mapped[int] = mapped_column(Integer)
    PackageId: Mapped[str] = mapped_column(String(50))
    IssueNo: Mapped[str] = mapped_column(String(50))


class VehicleOrder(_Model):
    __tablename__ = "VehicleOrder"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)
    ErrorDetails: Mapped[str] = mapped_column(String(100))


class VehicleOrderDelivery(_Model):
    __tablename__ = "VehicleOrderDelivery"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)


class VehicleOrderSpec(_Model):
    __tablename__ = "VehicleOrderSpec"

    fkOrderVehicleId: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPieOrderAttempt: Mapped[int] = mapped_column(Integer)
    UserId: Mapped[str] = mapped_column(String(20))
    OrderRef: Mapped[str] = mapped_column(String(10))
    PreOrderedOrderId: Mapped[int] = mapped_column(BigInteger)


class VehicleOrderSpecItem(_Model):
    __tablename__ = "VehicleOrderSpecItem"

    fkOrderVehicleId: Mapped[int] = mapped_column(Integer, primary_key=True)
    SwProductId: Mapped[int] = mapped_column(BigInteger, primary_key=True)


class VehicleParameter(_Model):
    __tablename__ = "VehicleParameter"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    Name: Mapped[str] = mapped_column(String(250))
    Value: Mapped[str] = mapped_column(String(250))
    type: Mapped[int] = mapped_column(Integer)


class WorkshopSession(_Model):
    __tablename__ = "WorkshopSession"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Started: Mapped[datetime] = mapped_column(DateTime)
    VehicleIdentifier: Mapped[str] = mapped_column(String(50))
    SymptomsObservationNote: Mapped[str] = mapped_column(String(256))
