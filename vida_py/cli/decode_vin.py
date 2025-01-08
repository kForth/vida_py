import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import diag
from vida_py.scripts.diag import get_vin_components


@click.command()
@click.argument("vin", type=click.STRING)
def main(vin):
    session = sessionmaker(bind=diag)()

    profile = get_vin_components(session, vin)[0]

    click.echo(f"VIN: {vin}")
    click.echo(f"Model: {profile[1]} [{profile[0]}]")
    click.echo(f"Year: {profile[2]}")
    click.echo(f"Engine: {profile[4]} [{profile[3]}]")
    click.echo(f"Transmission: {profile[6]} [{profile[5]}]")
    click.echo(f"Chassis: {vin[-6:]}")

    session.close()


if __name__ == "__main__":
    main()
