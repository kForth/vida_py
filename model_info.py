import re

IDENTIFIER_RE = re.compile(r'<identifier (?:\w+=".*")+>\n\s*<parameter (?:\w+=".*")+/>\n\s*</identifier>', re.MULTILINE)
PROFILE_RE = re.compile(r'nevis:expl-profile="([^\"]*)"')
ECU_CODE_RE = re.compile(r'\((\w+)\)$')

MODELS_BY_ID = {
    850: "850",
    874: "S70",
    875: "V70 (-00)",
    872: "C70 Coupe (-02)",
    873: "C70 Conv (-05)",
    644: "S40 (-04)",
    645: "V40 (-04)",
    940: "940",
    965: "V90",
    876: "V70 XC (-00)",
    960: "960",
    964: "S90",
    946: "940 SE",
    184: "S80 (-06)",
    295: "V70 XC (01-) / XC70 (-07)",
    384: "S60 (-09)",
    285: "V70 (00-08)",
    275: "XC90",
    760: "760",
    240: "240",
    260: "260",
    440: "440",
    460: "460",
    360: "360",
    740: "740",
    480: "480",
    780: "780",
    340: "340",
    544: "S40 (04-)",
    545: "V50",
    542: "C70 (06-)",
    124: "S80 (07-)",
    533: "C30",
    135: "V70 (08-)",
    136: "XC70 (08-)",
    156: "XC60",
    144: "S80L",
    134: "S60 (11-)",
    155: "V60",
    525: "V40 (13-)",
    526: "V40 Cross Country",
    530: "C30 Electric",
    138: "S60L",
    256: "XC90 (16-)",
    234: "V541",
    235: "V542",
    236: "V543",
    157: "V60 Cross Country",
}

MODELS_BY_NAME = {
    "850": 850,
    "S70": 874,
    "V70 (-00)": 875,
    "C70 Coupe (-02)": 872,
    "C70 Conv (-05)": 873,
    "S40 (-04)": 644,
    "V40 (-04)": 645,
    "940": 940,
    "V90": 965,
    "V70 XC (-00)": 876,
    "960": 960,
    "S90": 964,
    "940 SE": 946,
    "S80 (-06)": 184,
    "V70 XC (01-) / XC70 (-07)": 295,
    "S60 (-09)": 384,
    "V70 (00-08)": 285,
    "XC90": 275,
    "760": 760,
    "240": 240,
    "260": 260,
    "440": 440,
    "460": 460,
    "360": 360,
    "740": 740,
    "480": 480,
    "780": 780,
    "340": 340,
    "S40 (04-)": 544,
    "V50": 545,
    "C70 (06-)": 542,
    "S80 (07-)": 124,
    "C30": 533,
    "V70 (08-)": 135,
    "XC70 (08-)": 136,
    "XC60": 156,
    "S80L": 144,
    "S60 (11-)": 134,
    "V60": 155,
    "V40 (13-)": 525,
    "V40 Cross Country": 526,
    "C30 Electric": 530,
    "S60L": 138,
    "XC90 (16-)": 256,
    "V541": 234,
    "V542": 235,
    "V543": 236,
    "V60 Cross Country": 157,
}

MODELS_SHORT_BY_ID = {
    850: "850",
    874: "S70",
    875: "V70",
    872: "C70 Coupe",
    873: "C70 Conv",
    644: "S40",
    645: "V40",
    940: "940",
    965: "V90",
    876: "V70 XC",
    960: "960",
    964: "S90",
    946: "940 SE",
    184: "S80",
    295: "XC70",
    384: "S60",
    285: "V70",
    275: "XC90",
    760: "760",
    240: "240",
    260: "260",
    440: "440",
    460: "460",
    360: "360",
    740: "740",
    480: "480",
    780: "780",
    340: "340",
    544: "S40",
    545: "V50",
    542: "C70",
    124: "S80",
    533: "C30",
    135: "V70",
    136: "XC70",
    156: "XC60",
    144: "S80L",
    134: "S60",
    155: "V60",
    525: "V40",
    526: "V40 Cross Country",
    530: "C30 Electric",
    138: "S60L",
    256: "XC90",
    234: "V541",
    235: "V542",
    236: "V543",
    157: "V60 Cross Country",
}

ENGINES_BY_ID = {
    4: "B5204FS",
    66: "B5254FS M 4.3",
    6: "B5234FS",
    99: "B5234T2",
    94: "B5204T2",
    3: "B5252FS",
    95: "B5254T",
    2: "B5254FS LH 3.2",
    98: "B5204T3",
    1: "B5234FT",
    60: "B5202FS",
    5: "B5204FT",
    61: "B5234T5",
    91: "B5254FS M 4.4",
    92: "D5252T MSA 15.7",
    100: "B5234T3",
    93: "B5234T4",
    130: "B5204T4",
    151: "B5244T",
    131: "B5254S DENSO",
    134: "B5244S2",
    133: "D5252T MSA 15.8",
    111: "B5244S",
    129: "GB5252S",
    107: "B5234T7",
    146: "B5244SG2",
    144: "GB5252S2",
    147: "B5244SG",
    142: "B4194T2",
    143: "B4204T2",
    139: "B4164S2",
    155: "B4204T3",
    159: " (CA) (US ",
    156: "B4204T5",
    105: "B4204T",
    141: "B4204S2",
    174: "B4204T4",
    140: "B4184S2",
    145: "B4184S3",
    69: "D4192T",
    28: "B6254GS",
    30: "B6304GS",
    33: "B6244FS",
    103: "B4194T",
    152: "B4204T2 CVVT",
    29: "B6304FS",
    67: "B4184S",
    68: "B4204S",
    27: "B6254FS",
    19: "B230FT",
    157: "D4192T3",
    160: "B4184S9",
    102: "B4164S",
    161: "B4184S10",
    158: "D4192T4",
    108: "B4184SM",
    154: "B4184SJ",
    132: "B5234T8",
    136: "B5244T2",
    106: "B5234T6",
    170: "B5254T4",
    165: "B5254T2",
    149: "B5244T3",
    148: "B5204T5",
    172: "B5234T9",
    173: "B5244T7",
    163: "B6294T",
    164: "B6294S2",
    109: "B6304S3",
    171: "B5244S6",
    137: "B6294S",
    110: "B6284T",
    101: "B6304FS2",
    153: "D5244T",
    162: "D5244T2",
    135: "D4192T2",
    36: "B17A",
    31: "D24TIC",
    71: "B18KP",
    72: "B18KPD",
    70: "B18K",
    74: "B18KD",
    97: "B230F REGINA",
    12: "B204FT",
    9: "B200FT",
    11: "B204E",
    17: "B230FB",
    22: "B230GT",
    23: "B234F",
    24: "B234G",
    32: "B200F",
    10: "B200G",
    21: "B230G",
    96: "B230F LH 2.4",
    18: "B230FD",
    62: "B230FK",
    90: "B230GK",
    41: "B20A",
    42: "B20F",
    37: "B19A",
    38: "B19E",
    45: "B21E",
    44: "B21A",
    47: "B21F",
    55: "B27E",
    63: "B27A",
    64: "B27F",
    50: "B23E",
    46: "B21ET",
    48: "B21FT",
    49: "B23A",
    39: "B19ET",
    52: "B23F",
    40: "B19K",
    57: "B28E",
    56: "B28A",
    58: "B28F",
    34: "D24",
    59: "D20",
    7: "B200E",
    14: "B230E",
    16: "B230F",
    43: "B200K",
    53: "B230A",
    54: "B230K",
    20: "B230FX",
    112: "B14.4S",
    113: "B14.3E",
    114: "B14.4E",
    117: "B14.4O",
    119: "B14.4ED",
    115: "D16",
    116: "B172K",
    118: "B172KD",
    121: "B200KO",
    122: "B200KE",
    123: "B200KS",
    124: "B200EO",
    125: "B200EE",
    126: "B200ES",
    127: "B200EA",
    128: "B200KD",
    120: "B13.4E",
    77: "B18E",
    88: "B18ES",
    89: "B18ED",
    82: "B18F",
    78: "B18EP",
    83: "B18FP",
    84: "B18FT",
    73: "B18FTM",
    81: "B16F",
    80: "B18U-103/113",
    75: "B18U(M)-200/203",
    76: "B18U(M)-103/113",
    79: "B18U-200/203",
    86: "D19T EGR",
    85: "B20F(M      ",
    87: "D19T",
    51: "B23ET",
    65: "B23FT",
    35: "D24T",
    8: "B200ET",
    15: "B230ET",
    25: "B280E",
    26: "B280F",
    13: "B204GT",
    104: "B200GT",
    169: "B5244S4",
    168: "B5244S5",
    175: "B5244S7",
    167: "B5254T3",
    166: "D4204T",
    176: "D5244T3",
    177: "D4204T2",
    182: "B5244T5",
    183: "B5244T4",
    180: "B4184S11",
    181: "D4164T",
    184: "B8444S",
    178: "B4184S8",
    179: "B4164S3",
    185: "D5244T4",
    188: "D5244T7",
    187: "D5244T6",
    186: "D5244T5",
    189: "D5244T8",
    190: "D4164T2",
    191: "B5254T6",
    193: "B6324S",
    195: "D5244T9",
    194: "B4204S3",
    197: "B6304T2",
    196: "B4204S4",
    198: "D5244T13",
    199: "B5254T7",
    200: "B5254T8",
    201: "D5244T10",
    204: "D5244T14",
    203: "B4204T6",
    206: "B6324S2",
    202: "B4204S7",
    205: "D4204T3",
    207: "B4164S4",
    208: "B4204S6",
    209: "D4164T DRIVe",
    210: "D5244T12",
    211: "D5244T16",
    212: "B4204T7",
    213: "B5254T11",
    214: "B5254T10",
    215: "D5244T19",
    216: "D5204T",
    217: "B6324S5",
    218: "B4164T",
    219: "B4164T2",
    223: "B4164T3",
    220: "D5204T2",
    221: "B6304T4",
    222: "B6324S4",
    224: "D5204T3",
    226: "D5204T5",
    227: "D4162T",
    225: "B5254T5",
    228: "D5244T18",
    229: "D5244T15",
    230: "D5244T11",
    231: "D5244T17",
    232: "D5204T6",
    234: "B5204T9",
    233: "D5204T4",
    235: "B5204T6",
    236: "E400V1",
    237: "D82PHEV",
    238: "B5254T9",
    239: "B5254T12",
    240: "B5204T8",
    241: "D5204T7",
    242: "B4204T12",
    245: "B4204T9",
    244: "B4204T11",
    243: "B4204T10",
    246: "D4204T5",
    247: "E400V2",
    248: "B49HEV",
    249: "B27HEV",
    250: "B5254T14",
    251: "B4164T4",
    252: "B4204T27",
    253: "D4204T11",
    254: "B4204T28",
    255: "B4204T15",
    256: "B4204T21",
    257: "D4204T14",
    259: "B6304T3",
    258: "D5244T23",
    260: "BASPHEV",
    262: "B4204T19",
    261: "B4154T4",
    263: "D4204T8",
    264: "D4204T20",
    266: "B6304T5",
    269: "D4204T4",
    267: "B4204T32",
    268: "D5244T22",
    270: "D5244T20",
    271: "BA2PHEV",
    272: "B4204T20",
    273: "B4204T23",
    274: "B46PHEV",
    275: "B4204T29",
    265: "D4204T9",
    277: "D97PHEV",
    276: "D5244T21",
    278: "B4154T5",
    279: "D87PHEV",
    280: "D4204T6",
}
ENGINES_BY_NAME = {v: k for k, v in ENGINES_BY_ID.items()}
