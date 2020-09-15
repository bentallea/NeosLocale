#!/bin/env python3

## All data is derived from distrowatch.com and wikipedia.

from googletrans import Translator, LANGUAGES
import json

LANGFOLDER = ""
t = Translator()
#for key in LANGUAGES:
#    print(key, "->", LANGUAGES[key])
lcount = 0
for item in LANGUAGES.items():
    lcount += 1
    with open(LANGFOLDER+'base.json') as JSONfile:
        DATA = json.load(JSONfile)
    print(f"Translating NEOS Language File to {item[0]}.")
    DATA["localeCode"] = item[0]
    kcount = 0
    for key in DATA["messages"].items():
        kcount += 1
        if key[1] != "":
            DATA["messages"][key[0]] = t.translate(key[1], src='en', dest=item[0]).text
            if DATA["messages"][key[0]] != key[1]:
                print(f"[{item[0]} {lcount}/{len(LANGUAGES.items())} {kcount}/{len(DATA['messages'].items())}] {key[0]}: {key[1]} -> \33[1;32m{DATA['messages'][key[0]]}\33[m")
            else:
                print(f"[{item[0]} {lcount}/{len(LANGUAGES.items())} {kcount}/{len(DATA['messages'].items())}] {key[0]}: \33[1;31mDid not translate.\33[m")
                DATA["messages"][key[0]]=""
    with open(LANGFOLDER+item[0]+".json",'w') as jsonfile:
        json.dump(DATA,jsonfile, indent=4, ensure_ascii=False)