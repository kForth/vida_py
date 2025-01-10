import click
from sqlalchemy import or_

from vida_py.db import basedata_session, diag_session
from vida_py.models.basedata import (
    Engine,
    ModelYear,
    Transmission,
    VehicleModel,
    VehicleProfile,
)
from vida_py.scripts.diag import get_vin_components


@click.command()
@click.argument("vin", type=click.STRING)
def main(vin):
    with basedata_session() as _basedata, diag_session() as _diag:
        (
            model_id,
            model_str,
            model_year,
            engine_id,
            engine_str,
            transm_id,
            transm_str,
        ) = get_vin_components(_diag, vin)[0]
        print(model_id, engine_id, transm_id)
        query = (
            _basedata.query(VehicleProfile)
            .outerjoin(VehicleModel, VehicleModel.Id == VehicleProfile.fkVehicleModel)
            .outerjoin(ModelYear, ModelYear.Id == VehicleProfile.fkModelYear)
            .outerjoin(Engine, Engine.Id == VehicleProfile.fkEngine)
            .outerjoin(Transmission, Transmission.Id == VehicleProfile.fkTransmission)
            .where(
                or_(
                    VehicleProfile.fkVehicleModel == None,
                    VehicleModel.Cid == model_id,
                ),
                or_(
                    VehicleProfile.fkModelYear == None,
                    ModelYear.Cid == model_year,
                ),
                or_(VehicleProfile.fkEngine == None, Engine.Cid == engine_id),
                or_(
                    VehicleProfile.fkTransmission == None,
                    Transmission.Cid == transm_id,
                ),
            )
        )
        for e in query.all():
            print(f"{e.Id}: {e.Description}")


if __name__ == "__main__":
    main()
