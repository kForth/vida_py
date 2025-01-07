import io
import os
import zipfile
import click

from sqlalchemy.orm import sessionmaker

from PyVIDA.database import service
from PyVIDA.models.service import *

@click.command()
@click.argument("doc", type=click.INT)
@click.option("--outdir", "-o", type=click.Path(file_okay=False))
def main(doc, outdir):
    service_session = sessionmaker(bind=service)()

    document = service_session.query(Document).filter(Document.id == doc).first()
    _zip = zipfile.ZipFile(io.BytesIO(document.XmlContent))

    if outdir:
        os.makedirs(outdir, exist_ok=True)
        for _file in _zip.filelist:
            with open(os.path.join(outdir, _file.filename), "wb+") as out:
                out.write(_zip.read(_file))
    else:
        for _file in _zip.filelist:
            click.echo(_file.filename)

if __name__ == "__main__":
    main()
