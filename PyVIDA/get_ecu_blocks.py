import json
import click

from sqlalchemy.orm import sessionmaker

from PyVIDA.database import carcom
from PyVIDA.models.carcom import T100_EcuVariant, T141_Block, T144_BlockChild, T150_BlockValue

@click.command()
@click.argument("diag", type=click.STRING)
@click.option("--language", "-l", type=click.INT, default=19)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(diag, language, outfile):
    session = sessionmaker(bind=carcom)()

    ecu_variant = session.query(T100_EcuVariant).filter_by(identifier=diag).first()
    if not ecu_variant:
        click.echo("ERROR: Could not find matching ecu")
        return

    relations = session.query(T144_BlockChild).filter_by(fkT100_EcuVariant=ecu_variant.id).all()
    blocks = []
    for relation in relations:
        block = session.query(T141_Block).filter_by(id=relation.fkT141_Block_Child).first()

        info = {
            'id': block.id,
            'name': block.name,
            'type': block.fkT142_BlockType,
            'datatype': block.fkT143_BlockDataType,
            'offset': block.offset,
            'length': block.length,
            'text': block.fkT190_Text,
            'vals': []
        }
        vals = session.query(T150_BlockValue).filter_by(fkT141_Block=block.id).all()
        for val in vals:
            info['vals'].append({
                "val": val.CompareValue,
                "text": val.text_value.get_data(language).data
            })
        blocks.append(info)

    jsons = json.dumps({
        "variant": {
            "id": ecu_variant.id,
            "identifier": ecu_variant.identifier,
        },
        "ecu": {
            "id": ecu_variant.ecu.id,
            "identifier": ecu_variant.ecu.identifier,
            "name": ecu_variant.ecu.name,
        },
        "blocks": blocks
    }, indent=4)

    if outfile:
        with open(outfile, "w+") as out:
            out.write(jsons)
    else:
        print(jsons)

if __name__ == "__main__":
    main()
