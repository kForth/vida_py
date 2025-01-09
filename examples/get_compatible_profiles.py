import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import basedata
from vida_py.funcs import run_func
from vida_py.models.basedata import VehicleProfile


@click.command()
@click.argument("profile_id", type=click.STRING)
def main(profile_id):
    basedata_session = sessionmaker(bind=basedata)()

    profiles_ids = [
        e[0]
        for e in run_func(basedata_session, "GetValidProfileManager", profile_id).all()
    ]
    profiles = (
        basedata_session.query(VehicleProfile)
        .where(VehicleProfile.Id.in_(profiles_ids))
        .all()
    )

    for profile in profiles:
        print(f"{profile.Id}: {profile.Description}")

    basedata_session.close()


if __name__ == "__main__":
    main()
