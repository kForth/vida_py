import io
import os
import zipfile

import click

from vida_py.basedata import Session as BaseDataSession
from vida_py.basedata import get_valid_profile_manager
from vida_py.diag import Session as DiagSession
from vida_py.diag import get_script
from vida_py.diag.models import (
    Language,
    Script,
    ScriptContent,
    ScriptProfileMap,
    ScriptType,
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


@click.command()
@click.argument("profile_id", type=click.STRING)
@click.option("--outdir", "-o", type=click.Path(file_okay=False))
@click.option(
    "--language",
    "-l",
    type=click.Choice(LANGUAGES, case_sensitive=False),
    default="en-US",
)
def main(profile_id, outdir, language):
    with BaseDataSession() as session:
        profiles_ids = [e[0] for e in get_valid_profile_manager(session, profile_id)]

    with DiagSession() as session:
        scripts = (
            session.query(ScriptContent.DisplayText, ScriptContent.XmlDataCompressed)
            .join(Script, Script.Id == ScriptContent.fkScript)
            .join(ScriptProfileMap, ScriptProfileMap.fkScript == Script.Id)
            .join(ScriptType, ScriptType.Id == Script.fkScriptType)
            .join(Language, Language.Id == ScriptContent.fkLanguage)
            .filter(
                ScriptProfileMap.fkProfile.in_(profiles_ids),
                ScriptType.Description == "VehCommSpecification",
                Language.Code == language,
            )
            .all()
        )
        # script = get_script(session, script_type, profile_str, None, "en-US", None)

    for script in scripts:
        with zipfile.ZipFile(io.BytesIO(script[1])) as _zip:
            bytestr = _zip.read(_zip.filelist[0])
            if outdir:
                os.makedirs(outdir, exist_ok=True)
                outfile = os.path.join(outdir, f"{script[0].replace("/", "_")}.xml")
                with open(outfile, "wb") as f:
                    f.write(bytestr)
            else:
                click.echo(script[0])
                click.echo(bytestr)


if __name__ == "__main__":
    main()
