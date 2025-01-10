import click

from vida_py.db import BaseData
from vida_py.funcs import run_func
from vida_py.models.basedata import VehicleProfile


@click.command()
@click.argument("profile_id", type=click.STRING)
def main(profile_id):
    with BaseData() as session:

        profiles_ids = [
            e[0] for e in run_func(session, "GetValidProfileManager", profile_id).all()
        ]
        profiles = (
            session.query(VehicleProfile).where(VehicleProfile.Id.in_(profiles_ids)).all()
        )

        for profile in profiles:
            print(f"{profile.Id}: {profile.Description}")


if __name__ == "__main__":
    main()
