from sqlalchemy import BINARY, NVARCHAR, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vida_py.models import Model


class Document(Model):
    __bind_key__ = "service"
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


class DocumentIndexedWord(Model):
    __bind_key__ = "service"
    __tablename__ = "DocumentIndexedWord"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    fkIndexedWord: Mapped[int] = mapped_column(
        ForeignKey("IndexedWord.id"), primary_key=True
    )

    document: Mapped["Document"] = relationship()
    indexed_word: Mapped["IndexedWord"] = relationship()


class DocumentLink(Model):
    __bind_key__ = "service"
    __tablename__ = "DocumentLink"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    projectDocumentTo: Mapped[str] = mapped_column(String(16), primary_key=True)
    elementFrom: Mapped[str] = mapped_column(String(50), primary_key=True)
    elementTo: Mapped[str] = mapped_column(String(50))
    isInclusion: Mapped[bool] = mapped_column(Boolean)
    targetTitle: Mapped[str] = mapped_column(NVARCHAR(500))

    document: Mapped["Document"] = relationship()


class DocumentLinkTitle(Model):
    __bind_key__ = "service"
    __tablename__ = "DocumentLinkTitle"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    element: Mapped[str] = mapped_column(String(50), primary_key=True)
    title: Mapped[str] = mapped_column(NVARCHAR(500))

    document: Mapped["Document"] = relationship()


class DocumentProfile(Model):
    __bind_key__ = "service"
    __tablename__ = "DocumentProfile"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    profileId: Mapped[str] = mapped_column(String(16), primary_key=True)

    document: Mapped["Document"] = relationship()


class DocumentType(Model):
    __bind_key__ = "service"
    __tablename__ = "DocumentType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(50))


class DroppedWord(Model):
    __bind_key__ = "service"
    __tablename__ = "DroppedWord"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(NVARCHAR(2000))


class FunctionGroupText(Model):
    __bind_key__ = "service"
    __tablename__ = "FunctionGroupText"

    functionGroup: Mapped[str] = mapped_column(NVARCHAR(50), primary_key=True)
    title: Mapped[str] = mapped_column(NVARCHAR(100))


class IndexDelimiter(Model):
    __bind_key__ = "service"
    __tablename__ = "IndexDelimiter"

    delimiter: Mapped[str] = mapped_column(NVARCHAR(50), primary_key=True)


class IndexedWord(Model):
    __bind_key__ = "service"
    __tablename__ = "IndexedWord"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(NVARCHAR(2000))


class Qualifier(Model):
    __bind_key__ = "service"
    __tablename__ = "Qualifier"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    qualifierCode: Mapped[str] = mapped_column(String(32))
    fkQualifierGroup: Mapped[int] = mapped_column(ForeignKey("QualifierGroup.id"))
    qualifierType: Mapped[str] = mapped_column(String(10))
    title: Mapped[str] = mapped_column(NVARCHAR(100))
    visible: Mapped[bool] = mapped_column(Boolean)

    group: Mapped["QualifierGroup"] = relationship()


class QualifierAttachment(Model):
    __bind_key__ = "service"
    __tablename__ = "QualifierAttachment"

    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"), primary_key=True)
    url: Mapped[str] = mapped_column(NVARCHAR(255))
    InstallationType: Mapped[str] = mapped_column(
        NVARCHAR(50), default="ALL", primary_key=True
    )

    qualifier: Mapped["Qualifier"] = relationship()


class QualifierDocument(Model):
    __bind_key__ = "service"
    __tablename__ = "QualifierDocument"

    fkQualifier: Mapped[int] = mapped_column(ForeignKey("Qualifier.id"), primary_key=True)
    documentPDId: Mapped[str] = mapped_column(String(16), primary_key=True)
    linkType: Mapped[str] = mapped_column(String(10))

    qualifier: Mapped["Qualifier"] = relationship()


class QualifierGroup(Model):
    __bind_key__ = "service"
    __tablename__ = "QualifierGroup"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(50))
    displayOrder: Mapped[int] = mapped_column(Integer)


class Resource(Model):
    __bind_key__ = "service"
    __tablename__ = "Resource"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkResourceType: Mapped[int] = mapped_column(ForeignKey("ResourceType.id"))
    ResourceData: Mapped[bytes] = mapped_column(BINARY(2147483647))
    filename: Mapped[str] = mapped_column(NVARCHAR(100))

    type: Mapped["ResourceType"] = relationship()


class ResourceType(Model):
    __bind_key__ = "service"
    __tablename__ = "ResourceType"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Title: Mapped[str] = mapped_column(String(50))


class SymptomIEMap(Model):
    __bind_key__ = "service"
    __tablename__ = "SymptomIEMap"

    fkDocument: Mapped[int] = mapped_column(ForeignKey("Document.id"), primary_key=True)
    Symptom: Mapped[int] = mapped_column(Integer, primary_key=True)
    ProfileId: Mapped[str] = mapped_column(String(50), primary_key=True)

    document: Mapped["Document"] = relationship()


class TreeItem(Model):
    __bind_key__ = "service"
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


class TreeItemDocument(Model):
    __bind_key__ = "service"
    __tablename__ = "TreeItemDocument"

    fkTreeItem: Mapped[int] = mapped_column(ForeignKey("TreeItem.id"), primary_key=True)
    projectDocumentTo: Mapped[str] = mapped_column(String(16), primary_key=True)

    item: Mapped["TreeItem"] = relationship()


class TreeItemProfile(Model):
    __bind_key__ = "service"
    __tablename__ = "TreeItemProfile"

    fkTreeItem: Mapped[int] = mapped_column(ForeignKey("TreeItem.id"), primary_key=True)
    profileId: Mapped[str] = mapped_column(String(16), primary_key=True)

    item: Mapped["TreeItem"] = relationship()


class UnIndexedWord(Model):
    __bind_key__ = "service"
    __tablename__ = "UnIndexedWord"

    word: Mapped[str] = mapped_column(NVARCHAR(200), primary_key=True)
