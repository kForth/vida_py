import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import carcom
from vida_py.scripts.carcom import service___get_blocks


@click.command()
@click.argument("ecu", type=click.STRING)
@click.option("--outdir", "-o", type=click.Path(file_okay=False))
def main(ecu, outdir):
    session = sessionmaker(bind=carcom)()

    blocks = service___get_blocks(session, ecu)

    print(blocks)


if __name__ == "__main__":
    main()
