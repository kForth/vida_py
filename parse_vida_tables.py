import csv
import glob
import io
import json
import os
import re
import xml.dom.minidom as minidom
import zipfile as zipfile

from model_info import ECU_CODE_RE, IDENTIFIER_RE, PROFILE_RE


class Script:
    type: str
    id: str
    name: str
    data: str
    profiles: list[str]
    data_bytes: bytearray
    models: list[str]
    years: list[str]

    def __init__(self, type, id, name, data=[], profiles=[]):
        self.type = type
        self.id = id
        self.name = name
        self.data = data
        self.profiles = profiles

    @property
    def data_bytes(self):
        return bytes.fromhex(self.data[2:])

    def fn(self, ext="", n=0):
        _name = self.name.replace("/", "-") \
                    .replace(">", "+") \
                    .replace("?", "x") \
                    .replace("\"", "")
        _n = f" - {n}" if n != 0 else ""
        return f'scripts/{self.id} - {_name}{_n} ({self.type}){ext}'

    EXPL_PROFILE_RE = re.compile(r'nevis:expl-profile="([^\"]*)"', )
    EXPL_PROFILE_RE2 = re.compile(r'^(mdl\d+)?(yr\d+)?$')

    def load_profiles(self):
        profiles = set()
        for fp in glob.glob(self.fn(ext=".xml")):
            with open(fp, encoding='utf-8') as src_file:
                text = src_file.read()
                for match in self.EXPL_PROFILE_RE.findall(text):
                    for profile in match.split(","):
                        profiles.add(profile.strip())
        self.profiles = sorted(list(profiles))

    def to_dict(self):
        return dict(
            type=self.type,
            id=self.id,
            name=self.name,
            profiles=self.profiles,
            fn=self.fn(),
            # data=self.data,
        )

    @staticmethod
    def from_dict(d):
        return Script(
            type=d.get('type', ''),
            id=d.get('id', ''),
            name=d.get('name', ''),
            profiles=d.get('profiles', ''),
        )


def load_script_type_list():
    """Create dict of script type id and script type names"""
    print("Loading Script Type List")
    types = {}
    with open('tables/ScriptType.csv') as src_file:
        src_file.readline()  # Skip Header Row
        while line := src_file.readline():
            _id, desc = line.strip().split(",")
            types[_id] = desc
    return types

def load_script_types(types):
    """Create a dict of script ids and script types"""
    print("Loading Script List")
    script_types = {}
    with open('tables/Script.csv') as src_file:
        src_file.readline()  # Skip Header Row
        while line := src_file.readline():
            _id, type_id = line.strip().split(",")
            script_types[_id] = types[type_id]
    return script_types

def create_script_list(script_types):
    """Create a list of script information and content"""
    print("Loading Script Content")
    scripts = []
    with open('tables/ScriptContent.csv') as src_file:
        # fkScript,fkLanguage,DisplayText,XmlDataCompressed,checksum
        scripts = [
            Script(script_types[e[0]], e[0], e[2], e[3])
            for e in csv.reader(
                src_file.readlines()[1:],
                quotechar='"',
                delimiter=',',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True
            )
        ]
    return scripts

def extract_script_xml_files(scripts):
    # Extract xml file from XmlDataCompressed
    print("Extracting Script Content")
    for script in scripts:
        data_bytes = script.data_bytes
        try:
            zf = zipfile.ZipFile(io.BytesIO(data_bytes))
            for i, fileinfo in enumerate(zf.infolist()):
                # Write formatted XML
                dom = minidom.parseString(zf.read(fileinfo).decode('utf-8'))
                with open(script.fn(".xml", i), 'wb') as data_file:
                    data_file.write(dom.toprettyxml(encoding='ascii'))
        except zipfile.BadZipFile:
            if len(data_bytes) > 0:
                print(f'Script "{script.name}" has bad zipfile')
                with open(script.fn(".zip"), 'wb+') as data_file:
                    data_file.write(data_bytes)
            else:
                print(f'Script "{script.name}" is empty.')
                with open(script.fn(), 'wb+'):
                    pass

    # Read the script XML files to find the associated vehicle profiles
    print("Extracting Script Profiles")
    for script in scripts:
        script.load_profiles()

    # Export list of script info
    print("Saving")
    with open('cache/scripts.json', 'w+', encoding='utf-8') as data_file:
        json.dump([e.to_dict() for e in scripts], data_file, indent=2)

    return scripts

def _parse_ecu_code(desc):
    if _re := ECU_CODE_RE.search(desc):
        return _re.group(1)
    else:
        return None

def load_ecu_list():
    print("Loading ECU List")
    with open('tables/EcuDescription.csv', encoding='utf-8') as src_file:
        ecus = {
            id: {
                'desc': desc,
                'code': _parse_ecu_code(desc),
            }
            for desc, _, id in csv.reader(
                src_file.readlines()[1:],
                quotechar='"',
                delimiter=',',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True
            )
        }
    return ecus

def _extract_identifier_property(match, name):
    if _re := re.search(f'{name}="([^\\"]+)"', match):
        return _re.group(1)
    else:
        return None

def extract_identifiers(scripts: list[Script]):
    # Find all unique identifiers within the scripts
    ecus = load_ecu_list()

    print("Collecting identifiers")
    identifiers = []
    for script in scripts:
        fp = script.fn(".xml")
        if not os.path.isfile(fp):
            continue
        with open(fp, encoding='utf-8') as src_file:
            text = src_file.read()
            for match in IDENTIFIER_RE.findall(text):
                ident = {
                    e: _extract_identifier_property(match, e)
                    for e in ('ecu', 'read', 'write', 'value')
                }
                name = _extract_identifier_property(match, 'name')
                textid = _extract_identifier_property(match, 'textid')
                existing = [
                    e for e in identifiers
                    if all(e[k] == ident[k] for k in ('ecu', 'value', 'read', 'write'))
                ]
                if len(existing):  # Add name and textid to existing identifier
                    e = existing[0]
                    if name not in e['names'] or textid not in e['textids']:
                        e['names'].append(name)
                        e['textids'].append(textid)
                else:  # Create new identifier
                    ecu = ecus.get(ident['ecu'], None)
                    ident['names'] = [name]
                    ident['textids'] = [textid]
                    ident['ecudesc'] = ecu['desc'] if ecu else None
                    ident['ecucode'] = ecu['code'] if ecu else None
                    identifiers.append(ident)

    identifiers.sort(key=lambda e: (e['ecu'], e['value']))

    with open('cache/identifiers.json', 'w+', encoding='utf-8') as out_file:
        json.dump(identifiers, out_file, indent=2)

    return identifiers

def extract_textids(identifiers):
    # Extract the list of textids and names for each ecu
    print("Extracting ECU Text IDs")
    textids = set()
    for ident in identifiers:
        for textid, name in zip(ident['textids'], ident['names']):
            textids.add((ident['ecu'], textid, name))
    textids = sorted(list(textids), key=lambda e: (e[0], e[1]))
    with open('cache/textids.json', 'w+', encoding='utf-8') as out_file:
        json.dump(textids, out_file, indent=2)
    return textids

def extract_vehicle_profiles():
    # Create a list of unique profiles
    print("Collecting vehicle profiles")
    profiles = set()
    for fp in glob.glob('scripts/*.xml'):
        with open(fp, encoding='utf-8') as src_file:
            text = src_file.read()
            for match in PROFILE_RE.findall(text):
                for profile in match.split(","):
                    profiles.add(profile.strip())
    profiles = sorted(list(profiles))
    with open('cache/profiles.json', 'w+', encoding='utf-8') as out_file:
        json.dump(profiles, out_file, indent=2)
    return profiles


if __name__ == "__main__":
    print("Parsing VIDA Tables")
    types = load_script_type_list()
    script_types = load_script_types(types)
    scripts = create_script_list(script_types)
    scripts = extract_script_xml_files(scripts)
    identifiers = extract_identifiers(scripts)
    textids = extract_textids(identifiers)
    profiles = extract_vehicle_profiles()
    print("Done.")
