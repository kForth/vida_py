import click
from sqlalchemy.orm import sessionmaker

from vida_py.db import basedata, epc
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
    session = sessionmaker(bind=epc)()
    _basedata = sessionmaker(bind=basedata)()

    part = session.query(PartItems).filter(PartItems.ItemNumber == partnumber).one()
    title = (
        session.query(Lexicon)
        .filter(
            Lexicon.DescriptionId == part.DescriptionId, Lexicon.fkLanguage == language
        )
        .one()
    )
    components = [
        (
            component,
            session.query(Lexicon)
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
                    for e in session.query(ComponentConditions)
                    .filter(
                        ComponentConditions.fkCatalogueComponent
                        == component.ParentComponentId
                    )
                    .all()
                ]
            ),
        )
        for component in (
            session.query(CatalogueComponents)
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

    session.close()
    _basedata.close()


if __name__ == "__main__":
    main()
