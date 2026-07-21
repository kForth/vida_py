import os

import click
from sqlalchemy.sql import or_

from vida_py import ImageRepoSession
from vida_py.images import Graphics, LocalizedGraphics
from vida_py.images.models import GraphicFormats


@click.command()
@click.argument("outdir", type=click.Path(file_okay=False, writable=True))
@click.option(
    "--t",
    "--type",
    "img_type",
    type=click.Choice(("*", "JPEG", "GIF", "CGM", "SVG", "JPG")),
    default="*",
)
def main(outdir, img_type):
    with ImageRepoSession() as session:
        images = [
            dict(zip(("graphicId", "languageId", "title", "type"), e, strict=True))
            for e in session.query(
                Graphics.id,
                LocalizedGraphics.languageId,
                LocalizedGraphics.title,
                GraphicFormats.description,
            )
            .join(Graphics, Graphics.id == LocalizedGraphics.fkGraphic)
            .join(GraphicFormats, GraphicFormats.id == Graphics.fkGraphicFormat)
            .filter(or_(img_type == "*", GraphicFormats.description == img_type))
            .all()
        ]

        os.makedirs(outdir, exist_ok=True)
        with click.progressbar(images) as bar_:
            for image in bar_:
                for i, img_data in enumerate(
                    session.query(LocalizedGraphics.imageData)
                    .filter(
                        LocalizedGraphics.fkGraphic == image["graphicId"],
                        LocalizedGraphics.languageId == image["languageId"],
                    )
                    .all()
                ):
                    suffix = "" if i == 0 else f" ({i})"
                    outfile = os.path.join(outdir, f"{image['title']}{suffix}.{image['type']}")
                    with open(outfile, "wb+") as out:
                        out.write(img_data[0])


if __name__ == "__main__":
    main()
