import json

import click

from vida_py import BaeDataSession, ServiceRepoSession
from vida_py.basedata import VehicleProfile, get_valid_profile_manager
from vida_py.service import Document, DocumentProfile


@click.command()
@click.argument("profile_id", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(profile_id, outfile):
    with BaeDataSession() as _basedata, ServiceRepoSession() as _service:

        profile_ids = [e[0] for e in get_valid_profile_manager(_basedata, profile_id)]
        profiles = (
            _basedata.query(VehicleProfile)
            .where(VehicleProfile.Id.in_(profile_ids))
            .all()
        )

        docs: dict[str, Document] = {}
        for profile in profiles:
            profile_docs = (
                _service.query(Document)
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


if __name__ == "__main__":
    main()
