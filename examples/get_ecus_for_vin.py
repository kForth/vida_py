import json
import click
from sqlalchemy import or_
from sqlalchemy.orm import aliased

from vida_py.carcom.models import (
    T100_EcuVariant,
    T101_Ecu,
    T160_DefaultEcuVariant,
    T161_Profile,
    T162_ProfileValue
)
from vida_py.diag import Session, get_vin_components
from vida_py.carcom import Session as CarcomSession


@click.command()
@click.argument("vin", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(vin, outfile):
    with Session() as session:
        (_, model_str, model_year, _, engine_str, _, transm_str) = get_vin_components(session, vin)[0]

        with CarcomSession() as session:
            profileValueModel = aliased(T162_ProfileValue)
            profileValueYear = aliased(T162_ProfileValue)
            profileValueEngine = aliased(T162_ProfileValue)
            profileValueTrans = aliased(T162_ProfileValue)

            ecus = session.query(
                T100_EcuVariant,
                T101_Ecu,
                profileValueModel,
                profileValueYear,
                profileValueEngine,
                profileValueTrans,
            ).join(
                T160_DefaultEcuVariant, T160_DefaultEcuVariant.fkT100_EcuVariant == T100_EcuVariant.id
            ).join(
                T101_Ecu, T101_Ecu.id == T100_EcuVariant.fkT101_Ecu
            ).join(
                T161_Profile, T161_Profile.id == T160_DefaultEcuVariant.fkT161_Profile
            ).outerjoin(
                profileValueModel, profileValueModel.id == T161_Profile.fkT162_ProfileValue_Model
            ).outerjoin(
                profileValueYear, profileValueYear.id == T161_Profile.fkT162_ProfileValue_Year
            ).outerjoin(
                profileValueEngine, profileValueEngine.id == T161_Profile.fkT162_ProfileValue_Engine
            ).outerjoin(
                profileValueTrans, profileValueTrans.id == T161_Profile.fkT162_ProfileValue_Transmission
            ).filter(
                or_(
                    T161_Profile.fkT162_ProfileValue_Model == None,
                    profileValueModel.description == model_str
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Year == None,
                    profileValueYear.description == model_year,
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Engine == None,
                    profileValueEngine.description == engine_str,
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Transmission == None,
                    profileValueTrans.description == transm_str,
                ),
            ).all()

        _ecus = [
            {
                "profile": {
                    "model": model.description if model else None,
                    "year": year.description if year else None,
                    "engine": engine.description if engine else None,
                    "transmission": transm.description if transm else None,
                },
                "variant": variant.id,
                "id": ecu.id,
                "type": ecu.identifier,
                "description": ecu.name,
                "identifier": variant.identifier,
            }
            for variant, ecu, model, year, engine, transm in ecus
        ]
        if outfile:
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(_ecus, out, indent=4)
        else:
            click.echo(json.dumps(_ecus, indent=4))


if __name__ == "__main__":
    main()
