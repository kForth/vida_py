import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import diag
from vida_py.scripts.diag import get_vin_components


@click.command()
@click.argument("vin", type=click.STRING)
def main(vin):
    session = sessionmaker(bind=diag)()

    (model_id, model_str, model_year, engine_id, engine_str, transm_id, transm_str) = (
        get_vin_components(session, vin)[0]
    )

    click.echo(f"VIN: {vin}")
    click.echo(f"Model: {model_str} [{model_id}]")
    click.echo(f"Year: {model_year}")
    click.echo(f"Engine: {engine_str} [{engine_id}]")
    click.echo(f"Transmission: {transm_str} [{transm_id}]")
    click.echo(f"Chassis: {vin[-6:]}")

    session.close()


if __name__ == "__main__":
    main()
