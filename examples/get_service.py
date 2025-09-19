import click

from vida_py.carcom import Session, T111_Service


@click.command()
@click.argument("service_id", type=click.INT)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(service_id, outfile):

    with Session() as session:
        service = (
            session.query(T111_Service.definition)
            .filter(T111_Service.id == service_id)
            .one()[0]
        )

    if outfile:
        with open(outfile, "wb") as f:
            f.write(service)
    else:
        click.echo(service)


if __name__ == "__main__":
    main()
