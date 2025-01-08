import click
from sqlalchemy.orm import sessionmaker

from PyVIDA.database import diag
from PyVIDA.diag import GetVINcomponents


@click.command()
@click.argument("vin", type=click.STRING)
def main(vin):
    session = sessionmaker(bind=diag)()

    profile = GetVINcomponents(session, vin)

    click.echo(f"VIN: {vin}")
    click.echo(f"Model: {profile.model} [{profile.model_id}]")
    click.echo(f"Year: {profile.year}")
    click.echo(f"Engine: {profile.engine} [{profile.engine_id}]")
    click.echo(f"Transmission: {profile.transmission} [{profile.transmission_id}]")

    session.close()


if __name__ == "__main__":
    main()
