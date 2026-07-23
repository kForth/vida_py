"""SQLAlchemy ORM models for the service VIDA database."""

# ruff: noqa: N815

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy import BINARY, NVARCHAR, Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class _Model(DeclarativeBase):
    __bind_key__ = "service"


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


class DBStageVersion(_Model):
    __tablename__ = "DBStageVersion"

    ID: Mapped[str] = mapped_column(String(50), primary_key=True)
    StageTag: Mapped[str] = mapped_column(String(50))
    StageDate: Mapped[datetime] = mapped_column(DateTime)


class Document(_Model):
    __tablename__ = "Document"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chronicleId: Mapped[str] = mapped_column(String(16))
    projectDocumentId: Mapped[str] = mapped_column(String(16))
    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"))
    version: Mapped[str] = mapped_column(NVARCHAR(50))
    vccNumber: Mapped[str] = mapped_column(NVARCHAR(50))
    nevisId: Mapped[str] = mapped_column(String(16))
    IEDate: Mapped[str] = mapped_column(String(32))
    fkDocumentType: Mapped[int] = mapped_column(ForeignKey("DocumentType.id"))
    conditionType: Mapped[str] = mapped_column(NVARCHAR(50))
    path: Mapped[str] = mapped_column(NVARCHAR(200))
    title: Mapped[str] = mapped_column(NVARCHAR(400))
    XmlContent: Mapped[bytes] = mapped_column(BINARY(2147483647))
    hasSibling: Mapped[bool] = mapped_column(Boolean)

    qualifier: Mapped["Qualifier"] = relationship()
    type: Mapped["DocumentType"] = relationship()


class DocumentIndexedWord(_Model):
    __tablename__ = "DocumentIndexedWord"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    fkIndexedWord: Mapped[int] = mapped_column(ForeignKey("IndexedWord.id"), primary_key=True)

    document: Mapped["Document"] = relationship()
    indexed_word: Mapped["IndexedWord"] = relationship()


class DocumentLink(_Model):
    __tablename__ = "DocumentLink"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    projectDocumentTo: Mapped[str] = mapped_column(String(16), primary_key=True)
    elementFrom: Mapped[str] = mapped_column(String(50), primary_key=True)
    elementTo: Mapped[str] = mapped_column(String(50))
    isInclusion: Mapped[bool] = mapped_column(Boolean)
    targetTitle: Mapped[str] = mapped_column(NVARCHAR(500))

    document: Mapped["Document"] = relationship()


class DocumentLinkTitle(_Model):
    __tablename__ = "DocumentLinkTitle"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    element: Mapped[str] = mapped_column(String(50), primary_key=True)
    title: Mapped[str] = mapped_column(NVARCHAR(500))

    document: Mapped["Document"] = relationship()


class DocumentProfile(_Model):
    __tablename__ = "DocumentProfile"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    profileId: Mapped[str] = mapped_column(String(16), primary_key=True)

    document: Mapped["Document"] = relationship()


class DocumentType(_Model):
    __tablename__ = "DocumentType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(50))


class DroppedWord(_Model):
    __tablename__ = "DroppedWord"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(NVARCHAR(2000))


class FunctionGroupText(_Model):
    __tablename__ = "FunctionGroupText"

    functionGroup: Mapped[str] = mapped_column(NVARCHAR(50), primary_key=True)
    title: Mapped[str] = mapped_column(NVARCHAR(100))


class IndexDelimiter(_Model):
    __tablename__ = "IndexDelimiter"

    delimiter: Mapped[str] = mapped_column(NVARCHAR(50), primary_key=True)


class IndexedWord(_Model):
    __tablename__ = "IndexedWord"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(NVARCHAR(2000))


class Qualifier(_Model):
    __tablename__ = "Qualifier"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    qualifierCode: Mapped[str] = mapped_column(String(32))
    fkQualifierGroup: Mapped[int] = mapped_column(ForeignKey("QualifierGroup.id"))
    qualifierType: Mapped[str] = mapped_column(String(10))
    title: Mapped[str] = mapped_column(NVARCHAR(100))
    visible: Mapped[bool] = mapped_column(Boolean)

    group: Mapped["QualifierGroup"] = relationship()


class QualifierAttachment(_Model):
    __tablename__ = "QualifierAttachment"

    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"), primary_key=True)
    url: Mapped[str] = mapped_column(NVARCHAR(255))
    InstallationType: Mapped[str] = mapped_column(NVARCHAR(50), default="ALL", primary_key=True)

    qualifier: Mapped["Qualifier"] = relationship()


class QualifierDocument(_Model):
    __tablename__ = "QualifierDocument"

    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"), primary_key=True)
    documentPDId: Mapped[str] = mapped_column(String(16), primary_key=True)
    linkType: Mapped[str] = mapped_column(String(10))

    qualifier: Mapped["Qualifier"] = relationship()


class QualifierGroup(_Model):
    __tablename__ = "QualifierGroup"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(50))
    displayOrder: Mapped[int] = mapped_column(Integer)


class Resource(_Model):
    __tablename__ = "Resource"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkResourceType: Mapped[int] = mapped_column(ForeignKey("ResourceType.id"))
    ResourceData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    filename: Mapped[str] = mapped_column(NVARCHAR(100))

    type: Mapped["ResourceType"] = relationship()


class ResourceType(_Model):
    __tablename__ = "ResourceType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Title: Mapped[str] = mapped_column(String(50))


class SymptomIEMap(_Model):
    __tablename__ = "SymptomIEMap"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    Symptom: Mapped[int] = mapped_column(Integer, primary_key=True)
    ProfileId: Mapped[str] = mapped_column(String(50), primary_key=True)

    document: Mapped["Document"] = relationship()


class TreeItem(_Model):
    __tablename__ = "TreeItem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    functionGroup1: Mapped[str] = mapped_column(NVARCHAR(50))
    functionGroup2: Mapped[str] = mapped_column(NVARCHAR(50))
    functionGroup3: Mapped[str] = mapped_column(NVARCHAR(50))
    tocLevel: Mapped[int] = mapped_column(Integer)
    isServInfo: Mapped[bool] = mapped_column(Boolean)
    vccNumber: Mapped[str] = mapped_column(String(50))
    version: Mapped[str] = mapped_column(String(10))
    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"))
    chronicleId: Mapped[str] = mapped_column(String(50))
    IEDate: Mapped[str] = mapped_column(String(50))
    NevisId: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(NVARCHAR(500))

    qualifier: Mapped["Qualifier"] = relationship()


class TreeItemDocument(_Model):
    __tablename__ = "TreeItemDocument"

    fkTreeItem: Mapped[int] = mapped_column(ForeignKey("TreeItem.id"), primary_key=True)
    projectDocumentTo: Mapped[str] = mapped_column(String(16), primary_key=True)

    item: Mapped["TreeItem"] = relationship()


class TreeItemProfile(_Model):
    __tablename__ = "TreeItemProfile"

    fkTreeItem: Mapped[int] = mapped_column(ForeignKey("TreeItem.id"), primary_key=True)
    profileId: Mapped[str] = mapped_column(String(16), primary_key=True)

    item: Mapped["TreeItem"] = relationship()


class UnIndexedWord(_Model):
    __tablename__ = "UnIndexedWord"

    word: Mapped[str] = mapped_column(NVARCHAR(200), primary_key=True)
