import json

import click

from vida_py.basedata import Session as BaseDataSession
from vida_py.basedata import get_valid_profile_manager
from vida_py.carcom import Session as CarcomSession
from vida_py.carcom.models import (
    T100_EcuVariant,
    T101_Ecu,
    T120_Config_EcuVariant,
    T121_Config,
    T123_Bus,
    T160_DefaultEcuVariant,
    T161_Profile,
)


@click.command()
@click.argument("profile_id", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(profile_id, outfile):
    with BaseDataSession() as session:
        profiles_ids = [e[0] for e in get_valid_profile_manager(session, profile_id)]

    with CarcomSession() as session:
        addrs = (
            session.query(
                T101_Ecu.identifier,
                T101_Ecu.name,
                T100_EcuVariant.identifier,
                T121_Config.commAddress,
                T123_Bus.name,
            )
            .join(T100_EcuVariant, T100_EcuVariant.fkT101_Ecu == T101_Ecu.id)
            .join(
                T120_Config_EcuVariant,
                T120_Config_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
            )
            .join(T121_Config, T121_Config.id == T120_Config_EcuVariant.fkT121_Config)
            .join(T123_Bus, T123_Bus.id == T121_Config.fkT123_Bus)
            .join(
                T160_DefaultEcuVariant,
                T160_DefaultEcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
            )
            .join(T161_Profile, T161_Profile.id == T160_DefaultEcuVariant.fkT161_Profile)
            .filter(T161_Profile.identifier.in_(profiles_ids))
            .order_by(T101_Ecu.identifier)
            .all()
        )
    ecu_addresses = [
        {
            "ECU Identifier": ecu_ident,
            "ECU Name": ecu_name,
            "ECU Variant": ecu_var,
            "Comm Address": comm_addr,
            "BUS Name": bus_name,
        }
        for ecu_ident, ecu_name, ecu_var, comm_addr, bus_name in addrs
    ]

    if outfile:
        with open(outfile, "w+") as f:
            json.dump(ecu_addresses, f, indent=4)
    else:
        click.echo(ecu_addresses)


if __name__ == "__main__":
    main()
