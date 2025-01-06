import json

from model_info import ENGINES_BY_NAME, MODELS_BY_NAME, MODELS_SHORT_BY_ID
from parse_vida_tables import Script, extract_identifiers

year = 2004
model = "V70 XC (01-) / XC70 (-07)"
# model = "V70 (00-08)"
engine = "B5254T2"

_model = MODELS_BY_NAME[model]
_engine = ENGINES_BY_NAME[engine]

profile = f"mdl{_model}yr{year}eng{_engine}"
filename = f"{year} {MODELS_SHORT_BY_ID[_model]} {engine}"

scripts = []
print("Loading Script List")
with open('cache/scripts.json') as src_file:
    scripts = list([Script.from_dict(e) for e in json.load(src_file)])

print("Collecting Vehicle Scripts")
scripts = list(filter(lambda s: any([e in profile for e in s.profiles]), scripts))
with open(f'vehicles/{filename} - Scripts.json', 'w+') as out_file:
    _scripts = [e.to_dict(False) for e in scripts]
    json.dump(_scripts, out_file, indent=2)

print("Extrating Identifiers from Scripts")
identifiers, vehicle_ecus = extract_identifiers(scripts)

print("Building ECU List")
with open('cache/ecus.json', encoding='utf-8') as src_file:
    ecus = json.load(src_file)
_ecus = []
for e in vehicle_ecus:
    ecu = ecus.get(e, None)
    _ecus.append({
        'id': e,
        'desc': ecu['desc'] if ecu is not None else None,
        'code': ecu['code'] if ecu is not None else None,
    })

config = {
    "info": {
        "year": year,
        "model": model,
        "engine": engine,
        "model_id": _model,
        "engine_id": _engine,
    },
    "identifiers": identifiers,
    "ecus": _ecus,
}
with open(f'vehicles/{filename} - Conf.json', 'w+', encoding='utf-8') as out_file:
    json.dump(config, out_file, indent=2)

print("Done.")
