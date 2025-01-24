import json

import click
from sqlalchemy.orm import Session as sa_orm_Session

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
)
from vida_py.carcom.models import T155_Scaling


def get_child_blocks(session: sa_orm_Session, language: int, ecu_var: int, parent: int):
    return [
        {
            "id": b.id,
            "blocktype": b.type.identifier,
            "datatype": b.datatype.name,
            "name": b.name,
            "text": b.fkT190_Text,
            "offset": b.offset,
            "length": b.length,
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
                    .outerjoin(
                        T193_Language, T193_Language.id == T191_TextData.fkT193_Language
                    )
                    .filter(
                        T191_TextData.fkT190_Text == v.fkT190_Text_Value,
                        T193_Language.identifier == language,
                    )
                    .one()
                    .data,
                    "unit": session.query(T191_TextData)
                    .outerjoin(
                        T193_Language, T193_Language.id == T191_TextData.fkT193_Language
                    )
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
            .join(T155_Scaling, T155_Scaling.id == T150_BlockValue.scaling)
            .join(T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id)
            .join(
                T100_EcuVariant, T100_EcuVariant.id == T144_BlockChild.fkT100_EcuVariant
            )
            .filter(
                T141_Block.fkT142_BlockType == 5,
                T100_EcuVariant.identifier == identifier,
            )
            .all()
        )

        _params = []
        for block, value, scaling in params:
            _params.append({"name": block.name})

        with open(outfile, "w+", encoding="utf-8") as out:
            json.dump(params, out, indent=4)


if __name__ == "__main__":
    main()
