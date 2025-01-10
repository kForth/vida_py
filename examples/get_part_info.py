import click

from vida_py.db import basedata_session, epc_session
from vida_py.models.basedata import VehicleProfile
from vida_py.models.epc import (
    CatalogueComponents,
    ComponentConditions,
    ComponentDescriptions,
    Lexicon,
    PartItems,
)


@click.command()
@click.argument("partnumber", type=click.STRING)
@click.argument("language", type=click.INT, default=15)
def main(partnumber, language):
    with epc_session() as _epc, basedata_session() as _basedata:

        part = _epc.query(PartItems).filter(PartItems.ItemNumber == partnumber).one()
        title = (
            _epc.query(Lexicon)
            .filter(
                Lexicon.DescriptionId == part.DescriptionId,
                Lexicon.fkLanguage == language,
            )
            .one()
        )
        components = [
            (
                component,
                _epc.query(Lexicon)
                .outerjoin(
                    ComponentDescriptions,
                    ComponentDescriptions.DescriptionId == Lexicon.DescriptionId,
                )
                .filter(
                    Lexicon.fkLanguage == language,
                    ComponentDescriptions.fkCatalogueComponent == component.Id,
                )
                .all(),
                (
                    [
                        _basedata.query(VehicleProfile)
                        .filter(VehicleProfile.Id == e.fkProfile)
                        .one()
                        for e in _epc.query(ComponentConditions)
                        .filter(
                            ComponentConditions.fkCatalogueComponent
                            == component.ParentComponentId
                        )
                        .all()
                    ]
                ),
            )
            for component in (
                _epc.query(CatalogueComponents)
                .filter(CatalogueComponents.fkPartItem == part.Id)
                .all()
            )
        ]
        print(f"PartNumber: {part.ItemNumber}")
        print(f"Title: {title.Description}")
        print("Components:")
        for component, descriptions, profiles in components:
            if descriptions:
                print("  Description:")
                for e in descriptions:
                    print(f"    {e.Description}")
                print("  Profiles:")
                for e in profiles:
                    print(f"    {e.Description}")
                print()


if __name__ == "__main__":
    main()
