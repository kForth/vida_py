import os

import click
from genericpath import isdir

from vida_py.images import LocalizedGraphics, Session


@click.command()
@click.argument("path", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False), default=None)
def main(path, outfile):
    """
    Convert a string of bytes to a file.
    """
    with Session() as session:
        img = (
            session.query(LocalizedGraphics).filter(LocalizedGraphics.path == path).one()
        )

    # Write the bytes to a file
    if outfile is None:
        outfile = path
    elif os.path.isdir(outfile):
        outfile = os.path.join(outfile, path)
    with open(outfile, "wb") as f:
        f.write(img.imageData)

    click.echo(f"Bytes written to {outfile}")


if __name__ == "__main__":
    main()
