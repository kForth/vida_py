import json

import click

from vida_py.carcom import (
    Session,
    T100_EcuVariant,
    T110_Service_EcuVariant,
    T111_Service,
    T120_Config_EcuVariant,
    T121_Config,
    T141_Block,
    T143_BlockDataType,
    T144_BlockChild,
    T148_BlockMetaPARA,
    T150_BlockValue,
    T170_SecurityCode_EcuVariant,
    T171_SecurityCode,
    T191_TextData,
    T193_Language,
    T155_Scaling,
)

@click.command()
@click.argument("identifier", type=click.STRING)
@click.option("--language", "-l", type=click.STRING, default="en-US")
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifier, language, outfile):
    with Session() as session:
        """
        SELECT tbv.fkT155_Scaling, tbv.CompareValue, b.*FROM carcom.dbo.T141_Block b
        join carcom.dbo.T100_EcuVariant tev
        on tev.identifier = '08658507  H'
        join carcom.dbo.T150_BlockValue tbv
        on tbv.fkT141_Block = b.id
        WHERE
        b.name LIKE '%PLSOL%'
        AND
        b.fkT142_BlockType = 5
        """
        params = (
            session.query(T141_Block, T150_BlockValue, T155_Scaling)
            .join(T150_BlockValue, T150_BlockValue.fkT141_Block == T141_Block.id)
            .join(T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id)
            .join(T155_Scaling, T155_Scaling.id == T150_BlockValue.fkT155_Scaling)
            .join(
                T100_EcuVariant, T100_EcuVariant.id == T144_BlockChild.fkT100_EcuVariant
            )
            .filter(
                T141_Block.fkT142_BlockType == 5,
                T100_EcuVariant.identifier == identifier,
            )
            .order_by(
                T141_Block.id,
            )
            .all()
        )

        _params = []
        for block, value, scaling in params:
            _params.append({
                "name": block.name,
                "offset": block.offset,
                "length": block.length,
                "scaling": scaling.definition,
                "scaling_id": scaling.id,
                "scaling_type": scaling.type,
                "text_value": "\n".join(e.data for e in value.text_value.data),
                "text_unit": "\n".join(e.data for e in value.text_unit.data),
                "compare": value.CompareValue,
            })

        if outfile:
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(_params, out, indent=4)
        else:
            click.echo(json.dumps(_params, indent=4))


if __name__ == "__main__":
    main()
