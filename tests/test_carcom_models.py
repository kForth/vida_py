def test_AMYProfileMap():
    """Test the AMYProfileMap class"""
    from vida_py.basedata import AMYProfileMap, Session

    with Session() as session:
        result = (
            session.query(AMYProfileMap)
            .filter(AMYProfileMap.fkSourceProfile == "0b00c8af84eb823d")
            .one()
        )
        assert result is not None and result.fkTargetProfile == "0b00c8af855abaf4"
