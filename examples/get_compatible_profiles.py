import click

from vida_py.basedata import Session, VehicleProfile, get_valid_profile_manager


@click.command()
@click.argument("profile_id", type=click.STRING)
def main(profile_id):
    with Session() as session:

        profiles_ids = [
            e[0]
            for e in get_valid_profile_manager(
                session, "GetValidProfileManager", profile_id
            )
        ]
        profiles = (
            session.query(VehicleProfile).where(VehicleProfile.Id.in_(profiles_ids)).all()
        )

        for profile in profiles:
            print(f"{profile.Id}: {profile.Description}")


if __name__ == "__main__":
    main()
