from xml.dom import minidom

import click
from sqlalchemy.orm import aliased

from vida_py.carcom import (
    Session,
    T100_EcuVariant,
    T120_Config_EcuVariant,
    T121_Config,
    T123_Bus,
    T141_Block,
    T144_BlockChild,
    T148_BlockMetaPARA,
)

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
@click.argument("identifiers", type=click.STRING, nargs=-1)
@click.option(
    "--language",
    "-l",
    type=click.Choice(LANGUAGES, case_sensitive=False),
    default="en-US",
)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(identifiers, language, outfile):

    with Session() as session:
        ecus: list[
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
                    T148_BlockMetaPARA.showAsFreezeFrame == True,
                )
                .order_by(T141_Block.id)
                .all()
            )
            ecus.append((identifier, variant, config, params))

        root = minidom.Document()

        xml = root.createElement("LoggingConfiguration")
        root.appendChild(xml)

        createTextNode(root, xml, "LogTimestamps", "True")

        modules = root.createElement("Modules")
        xml.appendChild(modules)

        for identifier, variant, config, params in ecus:
            module = root.createElement("LoggingModuleConfiguration")
            modules.appendChild(module)
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

    xml_str = root.toprettyxml(indent="\t")
    if outfile:
        with open(outfile, "w+", encoding="utf-8") as out:
            out.write(xml_str)
    else:
        click.echo(xml_str)


if __name__ == "__main__":
    main()
