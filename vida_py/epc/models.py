"""SQLAlchemy ORM models for the epc VIDA database."""

# ruff: noqa: N815

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class _Model(DeclarativeBase):
    __bind_key__ = "epc"


class AttachmentData(_Model):
    __tablename__ = "AttachmentData"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[str] = mapped_column(String(16))
    URL: Mapped[str] = mapped_column(String(100))
    MIME: Mapped[str] = mapped_column(String(64))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class CatalogueComponents(_Model):
    __tablename__ = "CatalogueComponents"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
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


class CCLexicon(_Model):
    __tablename__ = "CCLexicon"

    CCid: Mapped[int] = mapped_column(Integer, primary_key=True)
    DescriptionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Note: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    ParentComponentId: Mapped[int] = mapped_column(Integer)


class CCPartnerGroup(_Model):
    __tablename__ = "CCPartnerGroup"

    fkCatalogueComponent: Mapped[int] = mapped_column(Integer)
    PartnerGroup: Mapped[str] = mapped_column(String(50))
    ID: Mapped[str] = mapped_column(String(50), primary_key=True)


class CodeDictionary(_Model):
    __tablename__ = "CodeDictionary"

    fkTableCode: Mapped[int] = mapped_column(Integer, primary_key=True)
    CodeId: Mapped[int] = mapped_column(Integer, primary_key=True)
    ValueText: Mapped[str] = mapped_column(String(50))


class ComponentAttachments(_Model):
    __tablename__ = "ComponentAttachments"

    fkCatalogueComponent: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkAttachmentData: Mapped[int] = mapped_column(Integer, primary_key=True)
    AttachmentTypeId: Mapped[int] = mapped_column(Integer, primary_key=True)
    SequenceId: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class ComponentConditions(_Model):
    __tablename__ = "ComponentConditions"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkCatalogueComponent: Mapped[int] = mapped_column(Integer)
    ModuleTypeId: Mapped[int] = mapped_column(Integer, default=1)
    fkProfile: Mapped[str] = mapped_column(String(16))
    PartnerGroup: Mapped[str] = mapped_column(String(10))
    ModelCid: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class ComponentDescriptions(_Model):
    __tablename__ = "ComponentDescriptions"

    fkCatalogueComponent: Mapped[int] = mapped_column(Integer, primary_key=True)
    DescriptionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    DescriptionTypeId: Mapped[int] = mapped_column(Integer, primary_key=True)
    SequenceId: Mapped[int] = mapped_column(Integer)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class Languages(_Model):
    __tablename__ = "Languages"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[str] = mapped_column(String(10))
    VersionUpdate: Mapped[str] = mapped_column(String(10), default=1.0)


class Lexicon(_Model):
    __tablename__ = "Lexicon"

    DescriptionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkLanguage: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[str] = mapped_column(String(21))
    Description: Mapped[str] = mapped_column(String(2000))
    VersionUpdate: Mapped[str] = mapped_column(String(10), default=0.4)
    TransDate: Mapped[datetime] = mapped_column(DateTime)


class LexiconNoteWords(_Model):
    __tablename__ = "LexiconNoteWords"

    fkLanguage: Mapped[int] = mapped_column(Integer, primary_key=True)
    DescriptionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWord: Mapped[int] = mapped_column(Integer, primary_key=True)


class LexiconPartWords(_Model):
    __tablename__ = "LexiconPartWords"

    DescriptionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWord: Mapped[int] = mapped_column(Integer, primary_key=True)


class NoteWords(_Model):
    __tablename__ = "NoteWords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    word: Mapped[str] = mapped_column(String(100))
    revword: Mapped[str] = mapped_column(String(100))


class PartItems(_Model):
    __tablename__ = "PartItems"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Code: Mapped[str] = mapped_column(String(16))
    ItemNumber: Mapped[str] = mapped_column(String(50))
    SupersessionIndicator: Mapped[bool] = mapped_column(Boolean, default=0)
    DescriptionId: Mapped[int] = mapped_column(Integer)
    IsSoftware: Mapped[bool] = mapped_column(Boolean)
    StockRate: Mapped[int] = mapped_column(SmallInteger)
    UnitType: Mapped[str] = mapped_column(String(32))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class PartWords(_Model):
    __tablename__ = "PartWords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkLanguage: Mapped[int] = mapped_column(Integer)
    word: Mapped[str] = mapped_column(String(100))
    revword: Mapped[str] = mapped_column(String(100))


class StructuredNoteTypes(_Model):
    __tablename__ = "StructuredNoteTypes"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Param: Mapped[str] = mapped_column(String(20))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class StructuredNoteValues(_Model):
    __tablename__ = "StructuredNoteValues"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkStructuredNoteType: Mapped[int] = mapped_column(Integer)
    ValueCode: Mapped[str] = mapped_column(String(16))
    NoteValue: Mapped[str] = mapped_column(String(255))
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class StructuredNotes(_Model):
    __tablename__ = "StructuredNotes"

    fkCatalogueComponent: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkStructuredNoteValues: Mapped[int] = mapped_column(Integer, primary_key=True)
    VersionUpdate: Mapped[str] = mapped_column(String(10))


class TableCodes(_Model):
    __tablename__ = "TableCodes"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(50))


class VirtualToShared(_Model):
    __tablename__ = "VirtualToShared"

    fkCatalogueComponent: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkCatalogueComponent_Parent: Mapped[int] = mapped_column(Integer, primary_key=True)
    AlternateComponentPath: Mapped[str] = mapped_column(String(100))
