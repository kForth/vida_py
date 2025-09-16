import io
import zipfile

import click

from vida_py.basedata import Session as BaseDataSession
from vida_py.basedata import VehicleProfile, get_valid_profile_manager
from vida_py.diag import Session as DiagSession
from vida_py.diag import get_script


@click.command()
@click.argument("profile_id", type=click.STRING)
@click.argument("script_type", type=click.STRING)
@click.option("--outfile", "-o", type=click.Path(dir_okay=False))
def main(profile_id, script_type, outfile):
    with BaseDataSession() as session:
        profiles_ids = [e[0] for e in get_valid_profile_manager(session, profile_id)]
    profile_str = ",".join(profiles_ids)

    with DiagSession() as session:
        script = get_script(session, script_type, profile_str, None, "en-US", None)

    with zipfile.ZipFile(io.BytesIO(script[0][0])) as _zip:
        bytestr = _zip.read(_zip.filelist[0])
        if outfile:
            # byte_array = bytes.fromhex(bytestr[2 if bytestr.startswith("0x") else 0 :])
            with open(outfile, "wb") as f:
                f.write(bytestr)
        else:
            click.echo(bytestr)


if __name__ == "__main__":
    main()
