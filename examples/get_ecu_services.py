import json

import click

from vida_py.carcom import (
    Session,
    T100_EcuVariant,
    T110_Service_EcuVariant,
    T111_Service,
    T120_Config_EcuVariant,
    T121_Config,
)
from vida_py.carcom.models import T101_Ecu

@click.command()
@click.argument("identifier", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifier, outfile):
    with Session() as session:
        services = session.query(
            T100_EcuVariant, T111_Service, T121_Config
        ).join(
            T110_Service_EcuVariant, T110_Service_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id
        ).join(
            T111_Service, T111_Service.id == T110_Service_EcuVariant.fkT111_Service
        ).join(
            T120_Config_EcuVariant, T120_Config_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id
        ).join(
            T121_Config, T121_Config.id == T120_Config_EcuVariant.fkT121_Config
        ).filter(
            T100_EcuVariant.identifier == identifier,
        ).order_by(
            T111_Service.service, T111_Service.mode
        )

        _services = []
        for variant, service, config in services:
            _services.append({
                "id": service.id,
                "service": f"0x{service.service}" if service.service else None,
                "mode": f"0x{service.mode}" if service.mode else None,
                "service_name": service.serviceName,
                "mode_name": service.modeName,
                "description": service.description,
                "definition": bytearray(service.definition).decode("utf-8") if service.definition else None,
                "func_address": f"0x{config.functionalAddress}" if config.functionalAddress else None,
                "comm_address": f"0x{config.commAddress}" if config.commAddress else None,
            })

        if outfile:
            with open(outfile, "w+", encoding="utf-8") as out:
                json.dump(_services, out, indent=2)
        else:
            click.echo(json.dumps(_services, indent=2))


if __name__ == "__main__":
    main()
