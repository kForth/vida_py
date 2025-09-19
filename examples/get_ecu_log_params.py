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

LANGUAGES = (
    "de-DE",
    "en-GB",
    "es-ES",
    "fi-FI",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nl-NL",
    "pt-PT",
    "ru-RU",
    "sv-SE",
    "th-TH",
    "tr-TR",
    "en-US",
    "zh-TW",
    "zh-CN",
)


@click.command()
@click.argument("identifier", type=click.STRING)
@click.option(
    "--language",
    "-l",
    type=click.Choice(LANGUAGES, case_sensitive=False),
    default="en-US",
)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifier, language, outfile):
    with Session() as session:

        T141_Block_2 = aliased(T141_Block)
        T150_BlockValue_2 = aliased(T150_BlockValue)
        T144_BlockChild_2 = aliased(T144_BlockChild)

        # string cmdText = $"select
        # val=case fkt155_scaling
        #   when 0 then fkt190_text_ppevalue
        #   else fkt190_text_value
        #   end,
        # unit=case fkt155_scaling
        #   when 0 then fkt190_text_ppeunit
        #   else fkt190_text_unit
        #   end
        # from t150_blockvalue
        #  join t141_block t141
        #  on fkt141_block = t141.id
        #  where t141.fkt190_text in ({parameterIds}) and t141.fkt142_blocktype=8";

        # SELECT *
        # FROM [T150_BlockValue] AS Val
        # JOIN [T141_Block] AS Blk ON Blk.id = Val.fkT141_Block
        # JOIN [T144_BlockChild] Chld ON Chld.fkT141_Block_Parent = Blk.Id
        # JOIN [T148_BlockMetaPARA] AS Meta ON Meta.fkT141_Block = Chld.fkT141_Block_Child
        # JOIN [T141_Block] AS Blk2 ON Blk2.id = Chld.fkT141_Block_Child
        # JOIN [T143_BlockDataType] Typ ON Typ.id = Blk2.fkT143_BlockDataType
        # WHERE Meta.fkT100_EcuVariant = 348

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
                    "datatype": block2.datatype.name,
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
