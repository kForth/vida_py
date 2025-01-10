from datetime import datetime

from sqlalchemy import BINARY, VARBINARY, BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class ActionItem(Model):
    __bind_key__ = "session"
    __tablename__ = "ActionItem"

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


class CommToolInfo(Model):
    __bind_key__ = "session"
    __tablename__ = "CommToolInfo"

    WorkshopSessionId: Mapped[int] = mapped_column(Integer)
    Type: Mapped[str] = mapped_column(String(50))
    Name: Mapped[str] = mapped_column(String(50))
    FirmwareVersion: Mapped[str] = mapped_column(String(80))
    DllVersion: Mapped[str] = mapped_column(String(80))
    ApiVersion: Mapped[str] = mapped_column(String(80))


class CryptKey(Model):
    __bind_key__ = "session"
    __tablename__ = "CryptKey"

    Version: Mapped[int] = mapped_column(Integer)
    KeyData: Mapped[bytes] = mapped_column(VARBINARY)


class DiagnosticScript(Model):
    __bind_key__ = "session"
    __tablename__ = "DiagnosticScript"

    ScriptId: Mapped[str] = mapped_column(String(32))
    fkPiePackage: Mapped[int] = mapped_column(BigInteger)
    XmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class DownloadConfirmation(Model):
    __bind_key__ = "session"
    __tablename__ = "DownloadConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    VehicleConfig: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))


class DroLog(Model):
    __bind_key__ = "session"
    __tablename__ = "DroLog"

    Id: Mapped[int] = mapped_column(Integer)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    EcuAddress: Mapped[int] = mapped_column(Integer)
    Request: Mapped[bytes] = mapped_column(VARBINARY)
    Response: Mapped[bytes] = mapped_column(VARBINARY)


class Dtc(Model):
    __bind_key__ = "session"
    __tablename__ = "Dtc"

    Id: Mapped[int] = mapped_column(Integer)
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


class DtcReadout(Model):
    __bind_key__ = "session"
    __tablename__ = "DtcReadout"

    Id: Mapped[int] = mapped_column(Integer)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    Timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    GlobalTime: Mapped[int] = mapped_column(Integer)
    EcuType: Mapped[int] = mapped_column(Integer)
    IsFirst: Mapped[bool] = mapped_column(Boolean)


class ESWDL(Model):
    __bind_key__ = "session"
    __tablename__ = "ESWDL"

    PartsId: Mapped[str] = mapped_column(String(16))
    CheckSum: Mapped[str] = mapped_column(String(50))
    Filename: Mapped[str] = mapped_column(String(500))
    InstallDate: Mapped[datetime] = mapped_column(DateTime)
    Installed: Mapped[bool] = mapped_column(Boolean)


class EcuInfo(Model):
    __bind_key__ = "session"
    __tablename__ = "EcuInfo"

    Id: Mapped[int] = mapped_column(Integer)
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


class EcuSoftware(Model):
    __bind_key__ = "session"
    __tablename__ = "EcuSoftware"

    Id: Mapped[int] = mapped_column(Integer)
    fkEcuInfoId: Mapped[int] = mapped_column(Integer)
    softwareName: Mapped[str] = mapped_column(String(50))
    softwarePartNo: Mapped[str] = mapped_column(String(50))


class FaultCounter(Model):
    __bind_key__ = "session"
    __tablename__ = "FaultCounter"

    Id: Mapped[int] = mapped_column(Integer)
    fkDtc: Mapped[int] = mapped_column(Integer)
    countername: Mapped[str] = mapped_column(String(100))
    countervalue: Mapped[int] = mapped_column(Integer)
    countertextid: Mapped[int] = mapped_column(Integer)


class FreezeFrameParam(Model):
    __bind_key__ = "session"
    __tablename__ = "FreezeFrameParam"

    Id: Mapped[int] = mapped_column(Integer)
    fkDtcId: Mapped[int] = mapped_column(Integer)
    paramId: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(500))
    value: Mapped[str] = mapped_column(String(500))
    blockId: Mapped[int] = mapped_column(Integer)


class GblPackage(Model):
    __bind_key__ = "session"
    __tablename__ = "GblPackage"

    SwPartNumber: Mapped[int] = mapped_column(BigInteger)
    fkPiePackage: Mapped[int] = mapped_column(BigInteger)
    Gbl: Mapped[bytes] = mapped_column(BINARY(2147483647))
    Code: Mapped[bytes] = mapped_column(BINARY(2147483647))


class HistoryItem(Model):
    __bind_key__ = "session"
    __tablename__ = "HistoryItem"

    Id: Mapped[int] = mapped_column(Integer)
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


class HistoryLoadedEcuItem(Model):
    __bind_key__ = "session"
    __tablename__ = "HistoryLoadedEcuItem"

    fkHistoryItem: Mapped[int] = mapped_column(Integer)
    LoadedEcu: Mapped[str] = mapped_column(String(30))


class HistoryVehicleOrderItem(Model):
    __bind_key__ = "session"
    __tablename__ = "HistoryVehicleOrderItem"

    fkHistoryItem: Mapped[int] = mapped_column(Integer)
    SwProdId: Mapped[int] = mapped_column(BigInteger)


class KeyValue(Model):
    __bind_key__ = "session"
    __tablename__ = "KeyValue"

    key: Mapped[str] = mapped_column(String(250))
    value: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))


class ObservedSymptom(Model):
    __bind_key__ = "session"
    __tablename__ = "ObservedSymptom"

    Id: Mapped[int] = mapped_column(Integer)
    symptomId: Mapped[int] = mapped_column(Integer)
    fkworkshopSessionId: Mapped[int] = mapped_column(Integer)
    Note: Mapped[str] = mapped_column(String(256))


class OrderVehicle(Model):
    __bind_key__ = "session"
    __tablename__ = "OrderVehicle"

    Id: Mapped[int] = mapped_column(Integer)
    VIN: Mapped[str] = mapped_column(String(17))
    ChassisNumber: Mapped[str] = mapped_column(String(6))
    Model: Mapped[int] = mapped_column(Integer)
    ModelYear: Mapped[str] = mapped_column(String(10))
    FYON: Mapped[int] = mapped_column(Integer)


class OrderVehiclePackage(Model):
    __bind_key__ = "session"
    __tablename__ = "OrderVehiclePackage"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    SpScriptXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    PieVehConfigXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VerifyTime: Mapped[int] = mapped_column(BigInteger)
    ConfirmTime: Mapped[int] = mapped_column(BigInteger)


class Parameter(Model):
    __bind_key__ = "session"
    __tablename__ = "Parameter"

    Id: Mapped[int] = mapped_column(Integer)
    fkVehConfigId: Mapped[int] = mapped_column(Integer)
    ParamName: Mapped[str] = mapped_column(String(50))
    ParamValue: Mapped[str] = mapped_column(String(50))
    CarConfigParam: Mapped[bool] = mapped_column(Boolean)


class PendingConfirmation(Model):
    __bind_key__ = "session"
    __tablename__ = "PendingConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    ConfirmPackageXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class PieDownloadConfirmation(Model):
    __bind_key__ = "session"
    __tablename__ = "PieDownloadConfirmation"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ConfirmTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class PieOrder(Model):
    __bind_key__ = "session"
    __tablename__ = "PieOrder"

    PieOrderId: Mapped[int] = mapped_column(BigInteger)
    VcpOrderNumber: Mapped[str] = mapped_column(String(17))
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ReceiveTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class PieOrderAttempt(Model):
    __bind_key__ = "session"
    __tablename__ = "PieOrderAttempt"

    Id: Mapped[int] = mapped_column(Integer)
    DummySomething: Mapped[str] = mapped_column(String(1))
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class PiePackage(Model):
    __bind_key__ = "session"
    __tablename__ = "PiePackage"

    fkPieOrder: Mapped[int] = mapped_column(BigInteger)


class RestoreableParameter(Model):
    __bind_key__ = "session"
    __tablename__ = "RestoreableParameter"

    Id: Mapped[int] = mapped_column(Integer)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    EcuType: Mapped[int] = mapped_column(Integer)
    Identifier: Mapped[str] = mapped_column(String(10))
    Value: Mapped[str] = mapped_column(String(255))


class RestoredParameter(Model):
    __bind_key__ = "session"
    __tablename__ = "RestoredParameter"

    pieOrderId: Mapped[int] = mapped_column(BigInteger)
    Name: Mapped[str] = mapped_column(String(100))
    Value: Mapped[str] = mapped_column(String(100))


class SlaveEcuInfo(Model):
    __bind_key__ = "session"
    __tablename__ = "SlaveEcuInfo"

    Id: Mapped[int] = mapped_column(Integer)
    fkEcuInfoId: Mapped[int] = mapped_column(Integer)
    HwPartNumber: Mapped[str] = mapped_column(String(50))
    HwSerialNumber: Mapped[str] = mapped_column(String(50))
    HwPartNumberName: Mapped[str] = mapped_column(String(200))
    HwSerialNumberName: Mapped[str] = mapped_column(String(200))


class StatusIdentifier(Model):
    __bind_key__ = "session"
    __tablename__ = "StatusIdentifier"

    Id: Mapped[int] = mapped_column(Integer)
    fkDtc: Mapped[int] = mapped_column(Integer)
    statusidentifierid: Mapped[int] = mapped_column(Integer)
    statusidentifiername: Mapped[str] = mapped_column(String(100))
    statusidentifiervalue: Mapped[int] = mapped_column(Integer)
    statusidentifiertext: Mapped[str] = mapped_column(String(250))


class UpdateOrder(Model):
    __bind_key__ = "session"
    __tablename__ = "UpdateOrder"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ReceiveTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)


class UpdateOrderAttempt(Model):
    __bind_key__ = "session"
    __tablename__ = "UpdateOrderAttempt"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    Lock: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class UpdateOrderDelivery(Model):
    __bind_key__ = "session"
    __tablename__ = "UpdateOrderDelivery"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)


class UpdateVehiclePackage(Model):
    __bind_key__ = "session"
    __tablename__ = "UpdateVehiclePackage"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    SpScriptXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    PieVehConfigXmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VehicleCodes: Mapped[bytes] = mapped_column(BINARY(2147483647))
    VerifyTime: Mapped[int] = mapped_column(BigInteger)
    ConfirmTime: Mapped[int] = mapped_column(BigInteger)


class Vbf(Model):
    __bind_key__ = "session"
    __tablename__ = "Vbf"

    SwPartNumber: Mapped[int] = mapped_column(BigInteger)
    fkPiePackage: Mapped[int] = mapped_column(BigInteger)
    fkCryptKeyVersion: Mapped[int] = mapped_column(Integer)
    XmlData: Mapped[bytes] = mapped_column(BINARY(2147483647))


class VehConfig(Model):
    __bind_key__ = "session"
    __tablename__ = "VehConfig"

    Id: Mapped[int] = mapped_column(Integer)
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


class VehicleOrder(Model):
    __bind_key__ = "session"
    __tablename__ = "VehicleOrder"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    ErrorReturnCode: Mapped[int] = mapped_column(Integer)
    ErrorDetails: Mapped[str] = mapped_column(String(100))


class VehicleOrderDelivery(Model):
    __bind_key__ = "session"
    __tablename__ = "VehicleOrderDelivery"

    fkVehicleOrderSpec: Mapped[int] = mapped_column(Integer)
    fkPieOrder: Mapped[int] = mapped_column(BigInteger)
    PieTransactionId: Mapped[int] = mapped_column(BigInteger)


class VehicleOrderSpec(Model):
    __bind_key__ = "session"
    __tablename__ = "VehicleOrderSpec"

    fkOrderVehicleId: Mapped[int] = mapped_column(Integer)
    fkPieOrderAttempt: Mapped[int] = mapped_column(Integer)
    UserId: Mapped[str] = mapped_column(String(20))
    OrderRef: Mapped[str] = mapped_column(String(10))
    PreOrderedOrderId: Mapped[int] = mapped_column(BigInteger)


class VehicleOrderSpecItem(Model):
    __bind_key__ = "session"
    __tablename__ = "VehicleOrderSpecItem"

    fkOrderVehicleId: Mapped[int] = mapped_column(Integer)
    SwProductId: Mapped[int] = mapped_column(BigInteger)


class VehicleParameter(Model):
    __bind_key__ = "session"
    __tablename__ = "VehicleParameter"

    Id: Mapped[int] = mapped_column(Integer)
    fkWorkshopSessionId: Mapped[int] = mapped_column(Integer)
    Name: Mapped[str] = mapped_column(String(250))
    Value: Mapped[str] = mapped_column(String(250))
    type: Mapped[int] = mapped_column(Integer)


class WorkshopSession(Model):
    __bind_key__ = "session"
    __tablename__ = "WorkshopSession"

    Id: Mapped[int] = mapped_column(Integer)
    Started: Mapped[datetime] = mapped_column(DateTime)
    VehicleIdentifier: Mapped[str] = mapped_column(String(50))
    SymptomsObservationNote: Mapped[str] = mapped_column(String(256))
