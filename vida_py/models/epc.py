from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class AttachmentData(Model):
    __bind_key__ = "epc"
    __tablename__ = "AttachmentData"

    Code: Mapped[str] = mapped_column(String(16))
    URL: Mapped[str] = mapped_column(String(100))
    MIME: Mapped[str] = mapped_column(String(64))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class CCLexicon(Model):
    __bind_key__ = "epc"
    __tablename__ = "CCLexicon"

    DescriptionId: Mapped[int] = mapped_column(Integer)
    Note: Mapped[int] = mapped_column(SmallInteger)
    ParentComponentId: Mapped[int] = mapped_column(Integer)


class CCPartnerGroup(Model):
    __bind_key__ = "epc"
    __tablename__ = "CCPartnerGroup"

    PartnerGroup: Mapped[str] = mapped_column(String(50))
    ID: Mapped[str] = mapped_column(String(50))


class CatalogueComponents(Model):
    __bind_key__ = "epc"
    __tablename__ = "CatalogueComponents"

    TypeId: Mapped[int] = mapped_column(Integer)
    PSCode: Mapped[str] = mapped_column(String(6))
    Code: Mapped[str] = mapped_column(String(16))
    VariantCode: Mapped[str] = mapped_column(String(16))
    ComponentPath: Mapped[str] = mapped_column(String(100), default="Inserted by trigger")
    fkPartItem: Mapped[int] = mapped_column(Integer)
    AssemblyLevel: Mapped[int] = mapped_column(Integer)
    ParentComponentId: Mapped[int] = mapped_column(Integer)
    Quantity: Mapped[float] = mapped_column(Numeric)
    HotspotKey: Mapped[str] = mapped_column(String(10))
    SequenceId: Mapped[int] = mapped_column(Integer, default=0)
    IndentationLevel: Mapped[int] = mapped_column(Integer)
    IndentationType: Mapped[str] = mapped_column(String(32))
    DescriptionId: Mapped[int] = mapped_column(Integer)
    FunctionGroupLabel: Mapped[str] = mapped_column(String(10))
    FunctionGroupPath: Mapped[str] = mapped_column(String(50))
    TargetComponentCode: Mapped[str] = mapped_column(String(16))
    TargetComponentId: Mapped[int] = mapped_column(Integer)
    VCCSectionId: Mapped[str] = mapped_column(String(50))
    VersionUpdate: Mapped[str] = mapped_column(String(10))
    NEVISStatus: Mapped[int] = mapped_column(Integer)
    NEVISValidFrom: Mapped[datetime] = mapped_column(DateTime)
    NEVISVersion: Mapped[str] = mapped_column(String(32))


class CodeDictionary(Model):
    __bind_key__ = "epc"
    __tablename__ = "CodeDictionary"

    CodeId: Mapped[int] = mapped_column(Integer)
    ValueText: Mapped[str] = mapped_column(String(50))


class ComponentAttachments(Model):
    __bind_key__ = "epc"
    __tablename__ = "ComponentAttachments"

    fkAttachmentData: Mapped[int] = mapped_column(Integer)
    AttachmentTypeId: Mapped[int] = mapped_column(Integer)
    SequenceId: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class ComponentDescriptions(Model):
    __bind_key__ = "epc"
    __tablename__ = "ComponentDescriptions"

    DescriptionId: Mapped[int] = mapped_column(Integer)
    DescriptionTypeId: Mapped[int] = mapped_column(Integer)
    SequenceId: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class Languages(Model):
    __bind_key__ = "epc"
    __tablename__ = "Languages"

    Code: Mapped[str] = mapped_column(String(10))
    VersionUpdate: Mapped[str] = mapped_column(String(10), default=1.0)


class Lexicon(Model):
    __bind_key__ = "epc"
    __tablename__ = "Lexicon"

    fkLanguage: Mapped[int] = mapped_column(Integer)
    Code: Mapped[str] = mapped_column(String(21))
    Description: Mapped[str] = mapped_column(String(2000))
    VersionUpdate: Mapped[str] = mapped_column(String(10), default=0.4)
    TransDate: Mapped[datetime] = mapped_column(DateTime)


class LexiconNoteWords(Model):
    __bind_key__ = "epc"
    __tablename__ = "LexiconNoteWords"

    DescriptionId: Mapped[int] = mapped_column(Integer)
    fkWord: Mapped[int] = mapped_column(Integer)


class LexiconPartWords(Model):
    __bind_key__ = "epc"
    __tablename__ = "LexiconPartWords"

    fkWord: Mapped[int] = mapped_column(Integer)


class NoteWords(Model):
    __bind_key__ = "epc"
    __tablename__ = "NoteWords"

    word: Mapped[str] = mapped_column(String(100))
    revword: Mapped[str] = mapped_column(String(100))


class PartItems(Model):
    __bind_key__ = "epc"
    __tablename__ = "PartItems"

    Code: Mapped[str] = mapped_column(String(16))
    ItemNumber: Mapped[str] = mapped_column(String(50))
    SupersessionIndicator: Mapped[bool] = mapped_column(Boolean, default=0)
    DescriptionId: Mapped[int] = mapped_column(Integer)
    IsSoftware: Mapped[bool] = mapped_column(Boolean)
    StockRate: Mapped[int] = mapped_column(SmallInteger)
    UnitType: Mapped[str] = mapped_column(String(32))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class PartWords(Model):
    __bind_key__ = "epc"
    __tablename__ = "PartWords"

    fkLanguage: Mapped[int] = mapped_column(Integer)
    word: Mapped[str] = mapped_column(String(100))
    revword: Mapped[str] = mapped_column(String(100))


class StructuredNoteTypes(Model):
    __bind_key__ = "epc"
    __tablename__ = "StructuredNoteTypes"

    Param: Mapped[str] = mapped_column(String(20))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class StructuredNoteValues(Model):
    __bind_key__ = "epc"
    __tablename__ = "StructuredNoteValues"

    fkStructuredNoteType: Mapped[int] = mapped_column(Integer)
    ValueCode: Mapped[str] = mapped_column(String(16))
    NoteValue: Mapped[str] = mapped_column(String(255))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class StructuredNotes(Model):
    __bind_key__ = "epc"
    __tablename__ = "StructuredNotes"

    fkStructuredNoteValues: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class TableCodes(Model):
    __bind_key__ = "epc"
    __tablename__ = "TableCodes"

    Name: Mapped[str] = mapped_column(String(50))


class VirtualToShared(Model):
    __bind_key__ = "epc"
    __tablename__ = "VirtualToShared"

    fkCatalogueComponent_Parent: Mapped[int] = mapped_column(Integer)
    AlternateComponentPath: Mapped[str] = mapped_column(String(100))
