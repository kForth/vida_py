import json
from pydoc import Doc

import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import basedata, service
from vida_py.funcs import run_func
from vida_py.models.basedata import VehicleProfile
from vida_py.models.service import Document, DocumentProfile


@click.command()
@click.argument("profile_id", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(profile_id, outfile):
    basedata_session = sessionmaker(bind=basedata)()
    service_session = sessionmaker(bind=service)()

    profiles_ids = [
        e[0]
        for e in run_func(basedata_session, "GetValidProfileManager", profile_id).all()
    ]
    profiles = (
        basedata_session.query(VehicleProfile)
        .where(VehicleProfile.Id.in_(profiles_ids))
        .all()
    )

    docs: dict[str, Document] = {}
    for profile in profiles:
        profile_docs = (
            service_session.query(Document)
            .outerjoin(DocumentProfile, DocumentProfile.fkDocument == Document.id)
            .filter(DocumentProfile.profileId == profile.Id)
            .all()
        )
        docs[profile.Id] = [
            {
                "id": d.id,
                "chronicleId": d.chronicleId,
                "path": d.path,
                "title": d.title,
                "date": d.IEDate,
                "type": d.type.name,
                # "xml": d.XmlContent,
            }
            for d in profile_docs
        ]

    if outfile:
        with open(outfile, "w+", encoding="utf-8") as out:
            json.dump(docs, out, indent=4)
    else:
        print(docs)

    basedata_session.close()
    service_session.close()


if __name__ == "__main__":
    main()
