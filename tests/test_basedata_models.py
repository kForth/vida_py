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


def test_BodyStyle():
    """Test the BodyStyle class"""
    from vida_py.basedata import BodyStyle, Session

    with Session() as session:
        result = session.query(BodyStyle).filter(BodyStyle.Id == 1005).one()
        assert result is not None and result.Description == "2DRS W/O S.R"


def test_BrakeSystem():
    """Test the BrakeSystem class"""
    from vida_py.basedata import BrakeSystem, Session

    with Session() as session:
        result = session.query(BrakeSystem).count()
        assert result is not None and result == 0


def test_Engine():
    """Test the Engine class"""
    from vida_py.basedata import Engine, Session

    with Session() as session:
        result = session.query(Engine).filter(Engine.Id == 1100).one()
        assert result is not None and result.Description == "D5244T8"


def test_ModelYear():
    """Test the ModelYear class"""
    from vida_py.basedata import ModelYear, Session

    with Session() as session:
        result = session.query(ModelYear).filter(ModelYear.Id == 1182).one()
        assert result is not None and result.Description == "1996"


def test_NodeECU():
    """Test the NodeECU class"""
    from vida_py.basedata import NodeECU, Session

    with Session() as session:
        result = session.query(NodeECU).filter(NodeECU.Id == 1009).one()
        assert result is not None and result.Description == "AUM"


def test_PartnerGroup():
    """Test the PartnerGroup class"""
    from vida_py.basedata import PartnerGroup, Session

    with Session() as session:
        result = session.query(PartnerGroup).filter(PartnerGroup.Id == 1002).one()
        assert result is not None and result.Cid == "EUR"


def test_SelectedProfiles():
    """Test the SelectedProfiles class"""
    from vida_py.basedata import SelectedProfiles, Session

    with Session() as session:
        result = session.query(SelectedProfiles).filter(SelectedProfiles.ID == 4).one()
        assert (
            result is not None
            and result.SelectedProfiles == "0b00c8af80207b7a,0b00c8af802068db"
        )


def test_SpecialVehicle():
    """Test the SpecialVehicle class"""
    from vida_py.basedata import Session, SpecialVehicle

    with Session() as session:
        result = session.query(SpecialVehicle).filter(SpecialVehicle.Id == 1003).one()
        assert result is not None and result.Cid == 12


def test_Steering():
    """Test the Steering class"""
    from vida_py.basedata import Session, Steering

    with Session() as session:
        result = session.query(Steering).filter(Steering.Id == 1001).one()
        assert result is not None and result.Cid == 1


def test_StructureWeek():
    """Test the StructureWeek class"""
    from vida_py.basedata import Session, StructureWeek

    with Session() as session:
        result = session.query(StructureWeek).count()
        assert result is not None and result == 0


def test_Suspension():
    """Test the Suspension class"""
    from vida_py.basedata import Session, Suspension

    with Session() as session:
        result = session.query(Suspension).count()
        assert result is not None and result == 0


def test_Transmission():
    """Test the Transmission class"""
    from vida_py.basedata import Session, Transmission

    with Session() as session:
        result = session.query(Transmission).filter(Transmission.Id == 1035).one()
        assert result is not None and result.Description == "M66 AWD"


def test_ValidProfiles():
    """Test the ValidProfiles class"""
    from vida_py.basedata import Session, ValidProfiles

    with Session() as session:
        result = (
            session.query(ValidProfiles)
            .filter(
                ValidProfiles.ID == 10, ValidProfiles.ValidProfile == "0b00c8af8020665c"
            )
            .one()
        )
        assert result is not None


def test_VehicleModel():
    """Test the VehicleModel class"""
    from vida_py.basedata import Session, VehicleModel

    with Session() as session:
        result = session.query(VehicleModel).filter(VehicleModel.Id == 1006).one()
        assert result is not None and result.Cid == 295


def test_VehicleProfile():
    """Test the VehicleProfile class"""
    from vida_py.basedata import Session, VehicleProfile

    with Session() as session:
        result = (
            session.query(VehicleProfile)
            .filter(VehicleProfile.Id == "0b00c8af82475d9e")
            .one()
        )
        assert result is not None and result.fkVehicleModel == 1006


def test_VehicleProfilePartnerGroup():
    """Test the VehicleProfilePartnerGroup class"""
    from vida_py.basedata import Session, VehicleProfilePartnerGroup

    with Session() as session:
        result = (
            session.query(VehicleProfilePartnerGroup)
            .filter(VehicleProfilePartnerGroup.fkVehicleProfile == "0b00c8af80206397")
            .all()
        )
        assert result is not None and [e.PartnerGroupCID for e in result] == [
            "EUR",
            "INT",
            "NOR",
        ]


def test_VINDecodeModel():
    """Test the VINDecodeModel class"""
    from vida_py.basedata import Session, VINDecodeModel

    with Session() as session:
        result = (
            session.query(VINDecodeModel).filter(VINDecodeModel.ID == -2119928368).one()
        )
        assert result is not None and result.VinCompare == "245"


def test_VINDecodeVariant():
    """Test the VINDecodeVariant class"""
    from vida_py.basedata import Session, VINDecodeVariant

    with Session() as session:
        result = (
            session.query(VINDecodeVariant)
            .filter(VINDecodeVariant.Id == -2109248038)
            .one()
        )
        assert result is not None and result.VinCompare == "9"


def test_VINVariantCodes():
    """Test the VINVariantCodes class"""
    from vida_py.basedata import Session, VINVariantCodes

    with Session() as session:
        result = (
            session.query(VINVariantCodes).filter(VINVariantCodes.Id == -2119929684).one()
        )
        assert result is not None and result.VINVariantCode == "98"
