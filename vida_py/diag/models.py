from sqlalchemy import BINARY, NVARCHAR, BigInteger, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
    pass


class ECU(Model):
    __bind_key__ = "diag"
    __tablename__ = "ECU"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)


class EcuDescription(Model):
    __bind_key__ = "diag"
    __tablename__ = "EcuDescription"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Not in DB
    DisplayText: Mapped[str] = mapped_column(NVARCHAR(256))
    fkLanguage: Mapped[int] = mapped_column(ForeignKey("Language.Id"))
    fkEcu: Mapped[int] = mapped_column(ForeignKey("Ecu.Id"))


class ECUInformationReference(Model):
    __bind_key__ = "diag"
    __tablename__ = "ECUInformationReference"

    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"), primary_key=True)
    fkECU: Mapped[int] = mapped_column(ForeignKey("ECU.Id"), primary_key=True)
    fkInformationQualifier: Mapped[int] = mapped_column(Integer, primary_key=True)


class IE(Model):
    __bind_key__ = "diag"
    __tablename__ = "IE"

    Id: Mapped[str] = mapped_column(String(16), primary_key=True)
    VCCId: Mapped[str] = mapped_column(String(16))
    fkIEType: Mapped[int] = mapped_column(ForeignKey("IEType.id"))
    FirstTestgrpId: Mapped[str] = mapped_column(String(50), default="")
    fkInformationQualifier: Mapped[int] = mapped_column(
        ForeignKey("InformationQualifier.Id")
    )
    ProjectDocumentId: Mapped[str] = mapped_column(String(16))
    Version: Mapped[str] = mapped_column(String(10))


class IECustomerFunction(Model):
    __bind_key__ = "diag"
    __tablename__ = "IECustomerFunction"

    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"), primary_key=True)
    CF: Mapped[int] = mapped_column(Integer)


class IEGenericComponent(Model):
    __bind_key__ = "diag"
    __tablename__ = "IEGenericComponent"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Not in DB
    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"))
    GCID: Mapped[str] = mapped_column(String, primary_key=True)
    GLID: Mapped[str] = mapped_column(String, primary_key=True)


class IEParentChildMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "IEParentChildMap"

    fkIEparent: Mapped[str] = mapped_column(ForeignKey("IE.id"), primary_key=True)
    fkIEchild: Mapped[str] = mapped_column(ForeignKey("IE.id"), primary_key=True)


class IEProfileMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "IEProfileMap"

    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"), primary_key=True)
    fkProfile: Mapped[str] = mapped_column(ForeignKey("Profile.id"), primary_key=True)


class IETitle(Model):
    __bind_key__ = "diag"
    __tablename__ = "IETitle"

    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"), primary_key=True)
    fkLanguage: Mapped[int] = mapped_column(ForeignKey("Language.Id"), primary_key=True)
    DisplayText: Mapped[str] = mapped_column(NVARCHAR(256))


class IEType(Model):
    __bind_key__ = "diag"
    __tablename__ = "IEType"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(64))


class Image(Model):
    __bind_key__ = "diag"
    __tablename__ = "Image"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Path: Mapped[str] = mapped_column(String(255))
    Description: Mapped[str] = mapped_column(String(50))


class ImageProfileMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "ImageProfileMap"

    fkImage: Mapped[str] = mapped_column(ForeignKey("Image.Id"), primary_key=True)
    fkProfile: Mapped[str] = mapped_column(ForeignKey("Profile.id"), primary_key=True)


class InformationQualifier(Model):
    __bind_key__ = "diag"
    __tablename__ = "InformationQualifier"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(64))


class InformationQualifierDescription(Model):
    __bind_key__ = "diag"
    __tablename__ = "InformationQualifierDescription"

    fkInformationQualifier: Mapped[int] = mapped_column(
        ForeignKey("InformationQualifier.Id"), primary_key=True
    )
    fkLanguage: Mapped[int] = mapped_column(ForeignKey("Language.Id"), primary_key=True)
    DisplayText: Mapped[str] = mapped_column(NVARCHAR(256))


class Language(Model):
    __bind_key__ = "diag"
    __tablename__ = "Language"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[str] = mapped_column(String(10))


class Script(Model):
    __bind_key__ = "diag"
    __tablename__ = "Script"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkScriptType: Mapped[int] = mapped_column(ForeignKey("ScriptType.Id"))


class ScriptCarFunction(Model):
    __bind_key__ = "diag"
    __tablename__ = "ScriptCarFunction"

    fkScript: Mapped[str] = mapped_column(ForeignKey("Script.Id"), primary_key=True)
    FunctionGroup: Mapped[int] = mapped_column(Integer, primary_key=True)


class ScriptContent(Model):
    __bind_key__ = "diag"
    __tablename__ = "ScriptContent"

    fkScript: Mapped[str] = mapped_column(ForeignKey("Script.Id"), primary_key=True)
    fkLanguage: Mapped[int] = mapped_column(ForeignKey("Language.Id"), primary_key=True)
    DisplayText: Mapped[str] = mapped_column(NVARCHAR(256))
    XmlDataCompressed: Mapped[bytes] = mapped_column(BINARY(2147483647))
    checksum: Mapped[str] = mapped_column(NVARCHAR(256))


class ScriptProfileMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "ScriptProfileMap"

    fkScript: Mapped[str] = mapped_column(ForeignKey("Script.Id"), primary_key=True)
    fkProfile: Mapped[str] = mapped_column(ForeignKey("Profile.id"), primary_key=True)


class ScriptType(Model):
    __bind_key__ = "diag"
    __tablename__ = "ScriptType"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Description: Mapped[str] = mapped_column(String(50))


class ScriptVariant(Model):
    __bind_key__ = "diag"
    __tablename__ = "ScriptVariant"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkScript: Mapped[str] = mapped_column(ForeignKey("Script.Id"))


class SmartToolScript(Model):
    __bind_key__ = "diag"
    __tablename__ = "SmartToolScript"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Not in DB
    SmartToolId: Mapped[str] = mapped_column(String, primary_key=True)
    ScriptId: Mapped[str] = mapped_column(String, primary_key=True)
    SmartToolName: Mapped[str] = mapped_column(String(255))


class SoftwareProduct(Model):
    __bind_key__ = "diag"
    __tablename__ = "SoftwareProduct"

    Id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    Name: Mapped[str] = mapped_column(String(64))
    PieId: Mapped[str] = mapped_column(String(30))
    EmissionRelated: Mapped[bool] = mapped_column(Boolean)


class SoftwareProductNote(Model):
    __bind_key__ = "diag"
    __tablename__ = "SoftwareProductNote"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    NoteText: Mapped[str] = mapped_column(String(2000))
    fkSoftwareProduct: Mapped[int] = mapped_column(ForeignKey("SoftwareProduct.Id"))


class SoftwareProductTitle(Model):
    __bind_key__ = "diag"
    __tablename__ = "SoftwareProductTitle"

    fkSoftwareProduct: Mapped[int] = mapped_column(
        ForeignKey("SoftwareProduct.Id"), primary_key=True
    )
    fkLanguage: Mapped[int] = mapped_column(ForeignKey("Language.Id"), primary_key=True)
    DisplayText: Mapped[str] = mapped_column(NVARCHAR(256))


class SWProductProfileMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "SWProductProfileMap"

    fkSoftwareProduct: Mapped[int] = mapped_column(
        ForeignKey("SoftwareProduct.Id"), primary_key=True
    )
    fkVehicleProfile: Mapped[str] = mapped_column(
        ForeignKey("VehicleProfile.id"), primary_key=True
    )


class SymptomIEMap(Model):
    __bind_key__ = "diag"
    __tablename__ = "SymptomIEMap"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkSymptom: Mapped[int] = mapped_column(ForeignKey("Symptom.id"))
    fkIE: Mapped[str] = mapped_column(ForeignKey("IE.Id"))
    Type: Mapped[str] = mapped_column(String(2))
    fkProfile: Mapped[str] = mapped_column(ForeignKey("Profile.id"))
    CarFunction: Mapped[int] = mapped_column(Integer)
    DTCId: Mapped[int] = mapped_column(Integer, primary_key=True)
    DTCComponentNameId: Mapped[int] = mapped_column(Integer, primary_key=True)
    DFCId: Mapped[int] = mapped_column(Integer, primary_key=True)
    DFSId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Probability: Mapped[int] = mapped_column(Integer)
    Periods: Mapped[int] = mapped_column(Integer)
    Qualified: Mapped[bool] = mapped_column(Boolean)
    Order: Mapped[bool] = mapped_column(Boolean)
