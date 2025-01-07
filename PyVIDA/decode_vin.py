import click

from sqlalchemy import or_, select, text
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

from PyVIDA.database import basedata
from PyVIDA.models.basedata import *

@click.command()
@click.argument("vin", type=click.STRING)
def main(vin):
    session = sessionmaker(bind=basedata)()

    profile = session.execute(select(
        VehicleModel.Cid,
        VehicleModel.Description,
        ModelYear.Cid,
        Engine.Cid,
        Engine.Description,
        Transmission.Cid,
        Transmission.Description,
    ).distinct().select_from(
        VINDecodeModel.__table__
        .outerjoin(VehicleModel, VINDecodeModel.fkVehicleModel == VehicleModel.Id)
        .outerjoin(ModelYear, VINDecodeModel.fkModelYear == ModelYear.Id)
        .join(VINDecodeVariant)
        .outerjoin(Engine, VINDecodeVariant.fkEngine == Engine.Id)
        .outerjoin(Transmission, VINDecodeVariant.fkTransmission == Transmission.Id)
    ).filter(
        VINDecodeModel.fkVehicleModel == VINDecodeVariant.fkVehicleModel,
        func.substring(vin, VINDecodeModel.VinStartPos, VINDecodeModel.VinEndPos - VINDecodeModel.VinStartPos + 1) == VINDecodeModel.VinCompare,
        func.substring(vin, VINDecodeVariant.VinStartPos, VINDecodeVariant.VinEndPos - VINDecodeVariant.VinStartPos + 1) == VINDecodeVariant.VinCompare,
        VINDecodeModel.ChassisNoFrom <= func.right(vin, 6),
        func.right(vin, 6) <= VINDecodeModel.ChassisNoTo,
        or_(VINDecodeModel.YearCode == None, VINDecodeModel.YearCode == func.substring(vin, VINDecodeModel.YearCodePos, 1)),
    )).first()

    click.echo("VIN: " + vin)
    print(f"Year: {profile.Cid_1}")
    print(f"Model: {profile.Description}")
    print(f"Engine: {profile.Description_1}")
    print(f"Transmission: {profile.Description_2}")

if __name__ == "__main__":
    main()
