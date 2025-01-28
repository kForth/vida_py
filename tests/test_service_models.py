def test_Document():
    """Test the Document class"""
    from vida_py.service import Document, Session

    with Session() as session:
        result = session.query(Document).filter(Document.id == -2147023086).one()
        assert result is not None and result.vccNumber == "VCC-096466-1"


def test_DocumentIndexedWord():
    """Test the DocumentIndexedWord class"""
    from vida_py.service import DocumentIndexedWord, Session

    with Session() as session:
        result = (
            session.query(DocumentIndexedWord)
            .filter(DocumentIndexedWord.fkDocument == -2146654491)
            .one()
        )
        assert result is not None and result.fkIndexedWord == 0


def test_DocumentLink():
    """Test the DocumentLink class"""
    from vida_py.service import DocumentLink, Session

    with Session() as session:
        result = (
            session.query(DocumentLink)
            .filter(DocumentLink.fkDocument == -2147019261)
            .one()
        )
        assert result is not None and result.elementTo == "KC01283169"


def test_DocumentLinkTitle():
    """Test the DocumentLinkTitle class"""
    from vida_py.service import DocumentLinkTitle, Session

    with Session() as session:
        result = (
            session.query(DocumentLinkTitle)
            .filter(DocumentLinkTitle.fkDocument == -2147022493)
            .one()
        )
        assert result is not None and result.element == "KC01155440"


def test_DocumentProfile():
    """Test the DocumentProfile class"""
    from vida_py.service import DocumentProfile, Session

    with Session() as session:
        result = (
            session.query(DocumentProfile)
            .filter(DocumentProfile.fkDocument == -2147020561)
            .one()
        )
        assert result is not None and result.profileId == "0c00c8af80205920"


def test_DocumentType():
    """Test the DocumentType class"""
    from vida_py.service import DocumentType, Session

    with Session() as session:
        result = session.query(DocumentType).filter(DocumentType.id == 10).one()
        assert result is not None and result.name == "EPC"


# def test_DroppedWord():
#     """Test the DroppedWord class"""
#     from vida_py.service import DroppedWord, Session

#     with Session() as session:
#         result = session.query(DroppedWord).filter(DroppedWord.id == 0).one()
#         assert result is not None and result.id == 0


def test_FunctionGroupText():
    """Test the FunctionGroupText class"""
    from vida_py.service import FunctionGroupText, Session

    with Session() as session:
        result = (
            session.query(FunctionGroupText)
            .filter(FunctionGroupText.functionGroup == 160)
            .one()
        )
        assert result is not None and result.title == "general"


def test_IndexDelimiter():
    """Test the IndexDelimiter class"""
    from vida_py.service import IndexDelimiter, Session

    with Session() as session:
        result = (
            session.query(IndexDelimiter).filter(IndexDelimiter.delimiter == "?").one()
        )
        assert result is not None and result.delimeter == "?"


def test_IndexedWord():
    """Test the IndexedWord class"""
    from vida_py.service import IndexedWord, Session

    with Session() as session:
        result = session.query(IndexedWord).filter(IndexedWord.id == 18).one()
        assert result is not None and result.text == "code"


def test_Qualifier():
    """Test the Qualifier class"""
    from vida_py.service import Qualifier, Session

    with Session() as session:
        result = session.query(Qualifier).filter(Qualifier.id == 36).one()
        assert result is not None and result.qualifierCode == "13:00"


def test_QualifierAttachment():
    """Test the QualifierAttachment class"""
    from vida_py.service import QualifierAttachment, Session

    with Session() as session:
        result = (
            session.query(QualifierAttachment)
            .filter(QualifierAttachment.fkQualifier == 76)
            .one()
        )
        assert (
            result is not None
            and result.url
            == "http://accessories.volvocars.com/AccessoriesWeb/Accessories.mvc"
        )


def test_QualifierDocument():
    """Test the QualifierDocument class"""
    from vida_py.service import QualifierDocument, Session

    with Session() as session:
        result = (
            session.query(QualifierDocument)
            .filter(QualifierDocument.documentPDId == "0800c8af844c411f")
            .one()
        )
        assert result is not None and result.linkType == "Manual"


def test_QualifierGroup():
    """Test the QualifierGroup class"""
    from vida_py.service import QualifierGroup, Session

    with Session() as session:
        result = session.query(QualifierGroup).filter(QualifierGroup.id == 2).one()
        assert result is not None and result.name == "Parts"


def test_Resource():
    """Test the Resource class"""
    from vida_py.service import Resource, Session

    with Session() as session:
        result = session.query(Resource).filter(Resource.id == 0).one()
        assert result is not None and result.id == 0


def test_ResourceType():
    """Test the ResourceType class"""
    from vida_py.service import ResourceType, Session

    with Session() as session:
        result = session.query(ResourceType).filter(ResourceType.id == 0).one()
        assert result is not None and result.id == 0


def test_SymptomIEMap():
    """Test the SymptomIEMap class"""
    from vida_py.service import Session, SymptomIEMap

    with Session() as session:
        result = session.query(SymptomIEMap).filter(SymptomIEMap.id == 0).one()
        assert result is not None and result.id == 0


def test_TreeItem():
    """Test the TreeItem class"""
    from vida_py.service import Session, TreeItem

    with Session() as session:
        result = session.query(TreeItem).filter(TreeItem.id == 0).one()
        assert result is not None and result.id == 0


def test_TreeItemDocument():
    """Test the TreeItemDocument class"""
    from vida_py.service import Session, TreeItemDocument

    with Session() as session:
        result = session.query(TreeItemDocument).filter(TreeItemDocument.id == 0).one()
        assert result is not None and result.id == 0


def test_TreeItemProfile():
    """Test the TreeItemProfile class"""
    from vida_py.service import Session, TreeItemProfile

    with Session() as session:
        result = session.query(TreeItemProfile).filter(TreeItemProfile.id == 0).one()
        assert result is not None and result.id == 0


def test_UnIndexedWord():
    """Test the UnIndexedWord class"""
    from vida_py.service import Session, UnIndexedWord

    with Session() as session:
        result = session.query(UnIndexedWord).filter(UnIndexedWord.id == 0).one()
        assert result is not None and result.id == 0
