import json

from model_info import ENGINES_BY_NAME, MODELS_BY_NAME, MODELS_SHORT_BY_ID
from parse_vida_tables import extract_identifiers

year = 2005
model = "V70 XC (01-) / XC70 (-07)"
engine = "B5254T2"

_model = MODELS_BY_NAME[model]
_engine = ENGINES_BY_NAME[engine]

profile = f"mdl{_model}yr{year}eng{_engine}"
filename = f"{year} {MODELS_SHORT_BY_ID[_model]} {engine}"

scripts = []
print("Loading Script List")
with open('cache/scripts.json') as src_file:
    scripts = json.load(src_file)

print("Filtering Vehicle Scripts")
scripts = list(filter(lambda s: any([e in profile for e in s['profiles']]), scripts))
with open(f'vehicles/{filename} - Scripts.json', 'w+') as out_file:
    _scripts = list(scripts)
    for _s in _scripts:
        del _s['profiles']
    json.dump(_scripts, out_file, indent=2)

identifiers = extract_identifiers(scripts)
with open(f'vehicles/{filename} - Conf.json', 'w+', encoding='utf-8') as out_file:
    json.dump(identifiers, out_file, indent=2)

print("Done.")
