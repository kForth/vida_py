import json

import click
from sqlalchemy.orm import aliased

from vida_py.carcom import (
    Session,
    T100_EcuVariant,
    T141_Block,
    T144_BlockChild,
    T150_BlockValue,
)


@click.command()
@click.argument("identifier", type=click.STRING)
@click.option("--language", "-l", type=click.STRING, default="en-US")
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifier, language, outfile):
    with Session() as session:

        T141_Block_2 = aliased(T141_Block)
        T150_BlockValue_2 = aliased(T150_BlockValue)
        T144_BlockChild_2 = aliased(T144_BlockChild)

        params = (
            session.query(T141_Block, T150_BlockValue, T141_Block_2, T150_BlockValue_2)
            .join(T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id)
            .join(T150_BlockValue, T150_BlockValue.fkT141_Block == T141_Block.id)
            .join(
                T144_BlockChild_2, T144_BlockChild_2.fkT141_Block_Parent == T141_Block.id
            )
            .join(T141_Block_2, T141_Block_2.id == T144_BlockChild_2.fkT141_Block_Child)
            .join(T150_BlockValue_2, T150_BlockValue_2.fkT141_Block == T141_Block_2.id)
            .join(
                T100_EcuVariant, T100_EcuVariant.id == T144_BlockChild.fkT100_EcuVariant
            )
            .where(
                T100_EcuVariant.identifier == identifier,
                T144_BlockChild.fkT141_Block_Parent == 1,
                T141_Block.fkT142_BlockType == 5,
            )
            .order_by(
                T144_BlockChild.fkT141_Block_Parent, T144_BlockChild.fkT141_Block_Child
            )
            .all()
        )

        _params = []
        for block, value, block2, value2 in params:
            _params.append(
                {
                    "id": block.id,
                    "type": block.type.identifier,
                    "datatype": block.datatype.name,
                    "name": block.name,
                    "offset": block.offset,
                    "length": block.length,
                    "exclude": block.exclude,
                    "composite": block.composite,
                    "value_id": value.Id,
                    "sort_order": value.SortOrder,
                    "identifier": value.CompareValue,
                    "operator": value.Operator,
                    "name2": block2.name,
                    "text": "".join(
                        e.data
                        for e in block2.text.data
                        if e.language.identifier == language
                    ),
                    "scaling": value2.ppe_scaling.definition,
                    "unit": "".join(
                        e.data
                        for e in value2.ppe_text_unit.data
                        if e.language.identifier == language
                    ),
                }
            )

        if outfile:
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(_params, out, indent=2)
        else:
            click.echo(json.dumps(_params, indent=2))


if __name__ == "__main__":
    main()
