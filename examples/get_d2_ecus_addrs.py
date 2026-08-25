import json
import os

import click

from vida_py.carcom import Session
from vida_py.carcom.models import (
    T100_EcuVariant,
    T120_Config_EcuVariant,
    T121_Config,
    T122_Protocol,
    T123_Bus,
)


@click.command()
@click.option("-o", "--outfile", type=click.Path(dir_okay=False))
def main(outfile):

    with Session() as session:
        ecus = (
            session.query(T100_EcuVariant, T121_Config, T123_Bus)
            .join(
                T120_Config_EcuVariant,
                T120_Config_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
            )
            .join(T121_Config, T121_Config.id == T120_Config_EcuVariant.fkT121_Config)
            .join(T123_Bus, T123_Bus.id == T121_Config.fkT123_Bus)
            .join(T122_Protocol, T122_Protocol.id == T121_Config.fkT122_Protocol)
            .filter(T122_Protocol.identifier == "D2")
            .order_by(T100_EcuVariant.identifier)
            .all()
        )

        ecus_by_type = {}
        for ecu, config, bus in ecus:
            ecu_type = ecu.ecu.type.description
            if ecu_type not in ecus_by_type:
                ecus_by_type[ecu_type] = {}
            if ecu.identifier not in ecus_by_type[ecu_type]:
                ecus_by_type[ecu_type][ecu.identifier] = {}
            ecus_by_type[ecu_type][ecu.identifier][bus.name] = config.functionalAddress

        if outfile:
            os.makedirs(os.path.split(outfile)[-1], exist_ok=True)
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(ecus_by_type, out, indent=2)
        else:
            click.echo(json.dumps(ecus_by_type, indent=2))


if __name__ == "__main__":
    main()
