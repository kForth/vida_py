import json
import os

import click
from sqlalchemy.orm import aliased

from vida_py.carcom import Session
from vida_py.carcom.models import (
    T100_EcuVariant,
    T141_Block,
    T142_BlockType,
    T144_BlockChild,
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
@click.option("--outdir", "-o", type=click.Path(file_okay=False, dir_okay=True))
def main(identifier: str, language: str, outdir: str) -> int:
    with Session() as session:
        ecu_variant = (
            session.query(T100_EcuVariant).filter(T100_EcuVariant.identifier == identifier).one()
        )

        T141_Block_Parent = aliased(T141_Block)

        params = (
            session.query(T141_Block, T141_Block_Parent, T142_BlockType)
            .join(T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id)
            .join(
                T100_EcuVariant,
                T100_EcuVariant.id == T144_BlockChild.fkT100_EcuVariant,
                isouter=True,
            )
            .join(
                T141_Block_Parent,
                T141_Block_Parent.id == T144_BlockChild.fkT141_Block_Parent,
            )
            .join(T142_BlockType, T142_BlockType.id == T141_Block.fkT142_BlockType)
            .filter(T100_EcuVariant.identifier == identifier)
            .all()
        )

        _params = []
        for block, parent, block_type in params:
            _params.append(
                {
                    "id": block.id,
                    "name": (
                        block.name
                        if block.fkT190_Text == 0
                        else [e.data for e in block.text.data if e.language.identifier == language][
                            0
                        ]
                    ),
                    "category": (
                        parent.name
                        if parent.fkT190_Text == 0
                        else [
                            e.data for e in parent.text.data if e.language.identifier == language
                        ][0]
                    ),
                    "blockType": {
                        "id": block_type.id,
                        "fkT142_BlockType_Parent": block_type.fkT142_BlockType_Parent,
                        "identifier": block_type.identifier,
                        "metaTable": block_type.metaTable,
                    },
                    "identifier": parent.values[0].CompareValue,
                    "offset": block.offset,
                    "length": block.length,
                    "type": block.type.identifier,
                    # "min": float(meta.asMinRange or 0),
                    # "max": float(meta.asMaxRange or 0),
                    # "freezeframe": meta.showAsFreezeFrame,
                    "datatype": block.datatype.name,
                    "values": [
                        {
                            "id": val.Id,
                            "compare": val.CompareValue,
                            "operator": val.Operator,
                            "scaling": (
                                val.ppe_scaling if val.fkT155_Scaling == 0 else val.scaling
                            ).definition,
                            "text": [
                                e.data
                                for e in (
                                    val.ppe_text_value.data
                                    if val.fkT155_Scaling == 0
                                    else val.text_value.data
                                )
                                if e.language.identifier == language
                            ][0],
                            "unit": [
                                e.data
                                for e in (
                                    val.ppe_text_unit.data
                                    if val.fkT155_Scaling == 0
                                    else val.text_unit.data
                                )
                                if e.language.identifier == language
                            ][0],
                        }
                        for val in block.values
                    ],
                }
            )

        if outdir:
            os.makedirs(outdir, exist_ok=True)
            outfile = os.path.join(
                outdir, f"{ecu_variant.ecu.type.description} - {identifier} - Blocks.json"
            )
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(_params, out, indent=4)
        else:
            click.echo(json.dumps(_params, indent=2))

        return 1


if __name__ == "__main__":
    main()
