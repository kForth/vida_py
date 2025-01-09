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
    component = (
        session.query(CatalogueComponents)
        .filter(CatalogueComponents.fkPartItem == part.Id)
        .one()
    )
    descriptions = (
        session.query(Lexicon)
        .outerjoin(
            ComponentDescriptions,
            ComponentDescriptions.DescriptionId == Lexicon.DescriptionId,
        )
        .filter(
            Lexicon.fkLanguage == language,
            ComponentDescriptions.fkCatalogueComponent == component.Id,
        )
        .all()
    )
    print(component.Id)
    parent_component = (
        session.query(CatalogueComponents)
        .filter(CatalogueComponents.Id == component.ParentComponentId)
        .one()
    )
    conditions = (
        session.query(ComponentConditions)
        .filter(ComponentConditions.fkCatalogueComponent == component.Id)
        .all()
    )
    profiles = [
        _basedata.query(VehicleProfile).filter(VehicleProfile.Id == e.fkProfile).one()
        for e in conditions
    ]
    # print(run_func(session, "GetPartText", part.Id, language).all())

    print(f"PartNumber: {part.ItemNumber}")
    print(f"Title: {title.Description}")
    if descriptions:
        print("Description:")
        for d in descriptions:
            print(f"  {d.Description}")
    if profiles:
        print("Profiles:")
        for p in profiles:
            print(f"  {p.Description}")

    session.close()
    _basedata.close()


if __name__ == "__main__":
    main()
