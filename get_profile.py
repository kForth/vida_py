from model_info import ENGINES_BY_NAME, MODELS_BY_NAME

year = 2004
model = "V70 XC (01-) / XC70 (-07)"
# model = "V70 (00-08)"
engine = "B5254T2"

_model = MODELS_BY_NAME[model]
_engine = ENGINES_BY_NAME[engine]

profile = f"mdl{_model}yr{year}eng{_engine}"

print(profile)
