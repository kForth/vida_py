import io
import os
import zipfile

import click

from vida_py.service import Document, Session


@click.command()
@click.argument("doc", type=click.INT)
@click.option("--outdir", "-o", type=click.Path(file_okay=False))
def main(doc, outdir):
    with Session() as session:

        document = session.query(Document).filter(Document.id == doc).first()
        with zipfile.ZipFile(io.BytesIO(document.XmlContent)) as _zip:

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
