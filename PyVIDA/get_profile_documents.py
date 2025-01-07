import json
import click

from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from PyVIDA.database import service, basedata
from PyVIDA.models.basedata import VehicleProfile
from PyVIDA.models.service import *

@click.command()
def main():
    basedata_session = sessionmaker(bind=basedata)()
    service_session = sessionmaker(bind=service)()

    year=1190  # 2004
    market=1001  # AME
    steering=1001  # LHD
    transmission=1033  # AW50/51 AWD
    engine=1074  # B5254T2
    model=1006  # "V70 XC (01-) / XC70 (-07)"
    body=1004  # 5DRS S.R

    profiles = basedata_session.query(VehicleProfile).filter(
        VehicleProfile.fkEngine == engine,
        VehicleProfile.fkVehicleModel == model,
        # or_(VehicleProfile.fkModelYear == year), #, VehicleProfile.fkModelYear == None),
        # or_(VehicleProfile.fkPartnerGroup == market), #, VehicleProfile.fkPartnerGroup == None),
        # or_(VehicleProfile.fkSteering == steering, VehicleProfile.fkSteering == None),
        # or_(VehicleProfile.fkTransmission == transmission, VehicleProfile.fkTransmission == None),
        # or_(VehicleProfile.fkEngine == engine, VehicleProfile.fkEngine == None),
        # or_(VehicleProfile.fkVehicleModel == model), #, VehicleProfile.fkVehicleModel == None),
        # or_(VehicleProfile.fkBodyStyle == body, VehicleProfile.fkBodyStyle == None)
    ).all()
    print(f"Found {len(profiles)} matching profiles.")

    documents = service_session.query(DocumentProfile).filter(DocumentProfile.profileId.in_([e.Id for e in profiles])).all()
    print(f"Found {len(documents)} matching documents.")

    for doc in documents:
        print(doc.document.title, doc.fkDocument)

if __name__ == "__main__":
    main()
