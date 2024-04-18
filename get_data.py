import json
import requests

def test2():
    print("test2")

def read_meta():
    url = "https://raw.githubusercontent.com/bt-koch/ivolR/main/input/banks.json"
    response = requests.get(url)
    json_data = response.json()
    return json_data


def ric_equity(banks_meta):
    
    ric_list = []

    for b in banks_meta:
        try:
            ric_list.append(b["RIC"])
        except KeyError:
            print("no RIC available for " + b["name"])

    ric_list = [item for sublist in ric_list for item in (sublist if isinstance(sublist, list) else [sublist])]
    ric_list = [item for item in ric_list if item != "NA"]

    return ric_list

def ric_cds(ric_equity):
    ric_cds, error = ek.get_data(ric_list, "TR.CDSPrimaryCDSRic")
    ric_cds = ric_cds["Primary CDS RIC"].to_list()
    ric_cds = [x for x in ric_cds if x != ""]
    return ric_cds



