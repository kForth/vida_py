from xml.dom import minidom

import click
from sqlalchemy import distinct, or_
from sqlalchemy.orm import aliased

from vida_py.carcom import Session as CarComSession
from vida_py.carcom import (
    T100_EcuVariant,
    T101_Ecu,
    T120_Config_EcuVariant,
    T121_Config,
    T123_Bus,
    T141_Block,
    T144_BlockChild,
    T148_BlockMetaPARA,
    T160_DefaultEcuVariant,
    T161_Profile,
    T162_ProfileValue,
)
from vida_py.diag import Session as DiagSession
from vida_py.diag import get_vin_components

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


def createTextNode(root, parent, name, value):
    el = root.createElement(name)
    el.appendChild(root.createTextNode(str(value)))
    parent.appendChild(el)


@click.command()
@click.argument("vin", type=click.STRING)
@click.option(
    "--language",
    "-l",
    type=click.Choice(LANGUAGES, case_sensitive=False),
    default="en-US",
)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(vin, language, outfile):
    with DiagSession() as session:
        (_, model_str, model_year, _, engine_str, _, transm_str) = get_vin_components(
            session, vin
        )[0]

    with CarComSession() as session:
        profileValueModel = aliased(T162_ProfileValue)
        profileValueYear = aliased(T162_ProfileValue)
        profileValueEngine = aliased(T162_ProfileValue)
        profileValueTrans = aliased(T162_ProfileValue)

        identifiers = [
            e[0]
            for e in session.query(distinct(T100_EcuVariant.identifier))
            .join(
                T160_DefaultEcuVariant,
                T160_DefaultEcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
            )
            .join(T101_Ecu, T101_Ecu.id == T100_EcuVariant.fkT101_Ecu)
            .join(T161_Profile, T161_Profile.id == T160_DefaultEcuVariant.fkT161_Profile)
            .outerjoin(
                profileValueModel,
                profileValueModel.id == T161_Profile.fkT162_ProfileValue_Model,
            )
            .outerjoin(
                profileValueYear,
                profileValueYear.id == T161_Profile.fkT162_ProfileValue_Year,
            )
            .outerjoin(
                profileValueEngine,
                profileValueEngine.id == T161_Profile.fkT162_ProfileValue_Engine,
            )
            .outerjoin(
                profileValueTrans,
                profileValueTrans.id == T161_Profile.fkT162_ProfileValue_Transmission,
            )
            .outerjoin(
                T120_Config_EcuVariant,
                T120_Config_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
            )
            .outerjoin(
                T121_Config,
                T121_Config.id == T120_Config_EcuVariant.fkT121_Config,
            )
            .outerjoin(T123_Bus, T123_Bus.id == T121_Config.fkT123_Bus)
            .filter(
                or_(
                    T161_Profile.fkT162_ProfileValue_Model == None,
                    profileValueModel.description == model_str,
                    model_str == None,
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Year == None,
                    profileValueYear.description == model_year,
                    model_year == None,
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Engine == None,
                    profileValueEngine.description == engine_str,
                    engine_str == None,
                ),
                or_(
                    T161_Profile.fkT162_ProfileValue_Transmission == None,
                    profileValueTrans.description == transm_str,
                    transm_str == None,
                ),
                T123_Bus.name.like("High s%"),
            )
            .all()
        ]

        modules: list[
            tuple[
                str,
                T100_EcuVariant,
                T121_Config,
                list[tuple[T141_Block, T148_BlockMetaPARA, T141_Block]],
            ]
        ] = []
        for identifier in identifiers:
            variant, config = (
                session.query(T100_EcuVariant, T121_Config)
                .outerjoin(
                    T120_Config_EcuVariant,
                    T120_Config_EcuVariant.fkT100_EcuVariant == T100_EcuVariant.id,
                )
                .outerjoin(
                    T121_Config,
                    T121_Config.id == T120_Config_EcuVariant.fkT121_Config,
                )
                .outerjoin(T123_Bus, T123_Bus.id == T121_Config.fkT123_Bus)
                .filter(
                    T100_EcuVariant.identifier == identifier,
                    T123_Bus.name.like("High s%"),
                )
                .one()
            )

            T141_Block_Parent = aliased(T141_Block)
            params = (
                session.query(T141_Block, T148_BlockMetaPARA, T141_Block_Parent)
                .join(
                    T148_BlockMetaPARA, T148_BlockMetaPARA.fkT141_Block == T141_Block.id
                )
                .join(
                    T100_EcuVariant,
                    T100_EcuVariant.id == T148_BlockMetaPARA.fkT100_EcuVariant,
                )
                .join(
                    T144_BlockChild, T144_BlockChild.fkT141_Block_Child == T141_Block.id
                )
                .join(
                    T141_Block_Parent,
                    T141_Block_Parent.id == T144_BlockChild.fkT141_Block_Parent,
                )
                .filter(
                    T100_EcuVariant.identifier == identifier,
                    # T148_BlockMetaPARA.showAsFreezeFrame == True,
                )
                .order_by(T141_Block.id)
                .all()
            )
            modules.append((identifier, variant, config, params))

        root = minidom.Document()

        xml = root.createElement("LoggingConfiguration")
        xml.setAttribute("xmlns", "https://additiveperformance.ca")
        xml.setAttribute("xmlns:i", "http://www.w3.org/2001/XMLSchema-instance")
        root.appendChild(xml)

        createTextNode(root, xml, "LogTimestamps", "true")

        ecu_modules = root.createElement("Modules")
        xml.appendChild(ecu_modules)

        for identifier, variant, config, params in modules:
            module = root.createElement("LoggingModuleConfiguration")
            ecu_modules.appendChild(module)
            createTextNode(root, module, "EcuVariant", identifier)
            createTextNode(root, module, "Name", variant.ecu.type.description)
            createTextNode(root, module, "Description", variant.ecu.name)
            createTextNode(root, module, "ModuleAddress", "0x" + config.commAddress)
            parameters = root.createElement("Parameters")
            module.appendChild(parameters)

            for block, meta, parent in params:
                param = root.createElement("LoggingParameter")
                parameters.appendChild(param)

                createTextNode(
                    root,
                    param,
                    "Name",
                    (
                        block.name
                        if block.fkT190_Text == 0
                        else [
                            e.data
                            for e in block.text.data
                            if e.language.identifier == language
                        ][0]
                    ),
                )
                createTextNode(root, param, "Description", "")
                createTextNode(root, param, "Identifier", parent.values[0].CompareValue)
                createTextNode(root, param, "Offset", block.offset)
                createTextNode(root, param, "Length", block.length)
                createTextNode(root, param, "DataType", block.datatype.name)

                vals = root.createElement("Values")
                param.appendChild(vals)

                for val in block.values:
                    param_val = root.createElement("LoggingParameterValue")
                    vals.appendChild(param_val)
                    createTextNode(
                        root,
                        param_val,
                        "Text",
                        [
                            e.data
                            for e in (
                                val.ppe_text_value.data
                                if val.fkT155_Scaling == 0
                                else val.text_value.data
                            )
                            if e.language.identifier == language
                        ][0],
                    )
                    createTextNode(
                        root,
                        param_val,
                        "Formula",
                        (
                            val.ppe_scaling if val.fkT155_Scaling == 0 else val.scaling
                        ).definition,
                    )
                    createTextNode(
                        root,
                        param_val,
                        "Units",
                        [
                            e.data
                            for e in (
                                val.ppe_text_unit.data
                                if val.fkT155_Scaling == 0
                                else val.text_unit.data
                            )
                            if e.language.identifier == language
                        ][0],
                    )
                    createTextNode(root, param_val, "CompareValue", val.CompareValue)
                    createTextNode(root, param_val, "Operator", val.Operator)
                    createTextNode(root, param_val, "Precision", 0)

    if outfile:
        with open(outfile, "wb+") as out:
            out.write(root.toprettyxml(encoding="utf-8", indent="\t"))
    else:
        click.echo(root.toprettyxml(indent="\t"))


if __name__ == "__main__":
    main()
