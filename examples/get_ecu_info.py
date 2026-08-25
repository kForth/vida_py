import json
import os

import click
from sqlalchemy.orm import Session as sa_orm_Session

from vida_py.carcom import Session
from vida_py.carcom.models import (
    T100_EcuVariant,
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
)


def get_child_blocks(session: sa_orm_Session, language: int, ecu_var: int, parent: int):
    return [
        {
            "id": b.id,
            "blocktype": b.type.identifier,
            "datatype": b.datatype.name,
            "name": b.name,
            "text": b.fkT190_Text,
            "offset": b.offset // 8,
            "length": b.length // 8,
            "exclude": b.exclude,
            "composite": b.composite,
            "range": [
                {
                    "min": float(m) if (m := r.asMinRange) is not None else m,
                    "max": float(m) if (m := r.asMaxRange) is not None else m,
                    "freezeframe": r.showAsFreezeFrame,
                }
                for r in session.query(T148_BlockMetaPARA)
                .filter(
                    T148_BlockMetaPARA.fkT141_Block == b.id,
                    T148_BlockMetaPARA.fkT100_EcuVariant == ecu_var,
                )
                .all()
            ],
            "values": [
                {
                    "id": v.Id,
                    "value": v.CompareValue,
                    "text": session.query(T191_TextData)
                    .outerjoin(T193_Language, T193_Language.id == T191_TextData.fkT193_Language)
                    .filter(
                        T191_TextData.fkT190_Text == v.fkT190_Text_Value,
                        T193_Language.identifier == language,
                    )
                    .one()
                    .data,
                    "unit": session.query(T191_TextData)
                    .outerjoin(T193_Language, T193_Language.id == T191_TextData.fkT193_Language)
                    .filter(
                        T191_TextData.fkT190_Text == v.fkT190_Text_Unit,
                        T193_Language.identifier == language,
                    )
                    .one()
                    .data,
                    "scaling": {
                        "def": v.scaling.definition,
                        "type": (
                            {
                                "id": t.id,
                                "name": t.name,
                            }
                            if (
                                t := session.query(T143_BlockDataType)
                                .filter(T143_BlockDataType.id == v.scaling.type)
                                .one_or_none()
                            )
                            is not None
                            else None
                        ),
                    },
                    "ppe": {
                        "text": session.query(T191_TextData)
                        .outerjoin(
                            T193_Language,
                            T193_Language.id == T191_TextData.fkT193_Language,
                        )
                        .filter(
                            T191_TextData.fkT190_Text == v.fkT190_Text_ppeValue,
                            T193_Language.identifier == language,
                        )
                        .one()
                        .data,
                        "unit": session.query(T191_TextData)
                        .outerjoin(
                            T193_Language,
                            T193_Language.id == T191_TextData.fkT193_Language,
                        )
                        .filter(
                            T191_TextData.fkT190_Text == v.fkT190_Text_ppeUnit,
                            T193_Language.identifier == language,
                        )
                        .one()
                        .data,
                        "scaling": v.ppe_scaling.definition,
                    },
                }
                for v in session.query(T150_BlockValue)
                .filter(T150_BlockValue.fkT141_Block == b.id)
                .all()
            ],
            "children": get_child_blocks(session, language, ecu_var, b.id),
        }
        for b in session.query(T141_Block)
        .outerjoin(T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id)
        .filter(
            T144_BlockChild.fkT100_EcuVariant == ecu_var,
            T144_BlockChild.fkT141_Block_Parent == parent,
        )
        .all()
    ]


@click.command()
@click.argument("identifier", type=click.STRING)
@click.option("--language", "-l", type=click.STRING, default="en-US")
@click.option("--outdir", "-o", type=click.Path(file_okay=False, dir_okay=True))
def main(identifier, language, outdir):
    with Session() as session:
        variant = (
            session.query(T100_EcuVariant).filter(T100_EcuVariant.identifier == identifier).one()
        )
        ecu = {
            "variant": {
                "id": variant.id,
                "identifier": variant.identifier,
                "status": variant.status,
            },
            "ecu": {
                "identifier": variant.ecu.identifier,
                "name": variant.ecu.name,
                "type": variant.ecu.type.description,
            },
            "configs": [
                {
                    "bus": conf.bus.name,
                    "protocol": conf.protocol.identifier,
                    "physical_address": conf.physicalAddress,
                    "functional_address": conf.functionalAddress,
                    "can_address": conf.canAddress,
                    "comm_address": conf.commAddress,
                    "priority": conf.priority,
                }
                for conf in session.query(T121_Config)
                .outerjoin(
                    T120_Config_EcuVariant,
                    T120_Config_EcuVariant.fkT121_Config == T121_Config.id,
                )
                .filter(T120_Config_EcuVariant.fkT100_EcuVariant == variant.id)
                .all()
            ],
            "security_codes": [
                {
                    "id": s.id,
                    "code": s.code,
                    "description": s.description,
                    "type": {
                        "id": s.type.id,
                        "identifier": s.type.identifier,
                        "description": s.type.description,
                    },
                }
                for s in session.query(T171_SecurityCode)
                .outerjoin(
                    T170_SecurityCode_EcuVariant,
                    T170_SecurityCode_EcuVariant.fkT171_SecurityCode == T171_SecurityCode.id,
                )
                .filter(T170_SecurityCode_EcuVariant.fkT100_EcuVariant == variant.id)
                .all()
            ],
            "blocks": get_child_blocks(session, language, variant.id, 1),
        }

    if outdir:
        os.makedirs(outdir, exist_ok=True)
        outfile = os.path.join(outdir, f"{ecu['ecu']['type']} - {identifier} - Info.json")
        with open(outfile, "w+", encoding="utf-8") as out:
            json.dump(ecu, out, indent=4)
    else:
        click.echo(json.dumps(ecu, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
