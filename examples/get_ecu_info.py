import json

import click

from vida_py.carcom import (
    Session,
    T100_EcuVariant,
    T120_Config_EcuVariant,
    T121_Config,
    T170_SecurityCode_EcuVariant,
    T171_SecurityCode,
)


@click.command()
@click.argument("identifier", type=click.STRING)
@click.option("--language", "-l", type=click.STRING, default="en-US")
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifier, language, outfile):
    with Session() as session:
        variant = (
            session.query(T100_EcuVariant)
            .filter(T100_EcuVariant.identifier == identifier)
            .one()
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
                    T170_SecurityCode_EcuVariant.fkT171_SecurityCode
                    == T171_SecurityCode.id,
                )
                .filter(T170_SecurityCode_EcuVariant.fkT100_EcuVariant == variant.id)
                .all()
            ],
        }

    if outfile:
        with open(outfile, "w+", encoding="utf-8") as out:
            json.dump(ecu, out, indent=4)
    else:
        print(json.dumps(ecu, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
