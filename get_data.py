import json
import requests
import eikon as ek
import pandas as pd

def test2():
    print("test2 asdf")

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
    ric_cds, error = ek.get_data(ric_equity, "TR.CDSPrimaryCDSRic")
    ric_cds = ric_cds.rename(columns={"Instrument": "ric_equity", "Primary CDS RIC": "ric_cds"})
    return ric_cds

def get_cds(ric_cds, start="2012-01-01", end="2023-06-30"):
    data = []
    for cds in ric_cds.itertuples():
        try:
            temp = ek.get_timeseries(cds.ric_cds,
                                     fields="*",
                                     start_date=start,
                                     end_date=end)
            temp.index.name = "date"
            temp.reset_index(inplace=True)
            temp = temp[["date", "CLOSE"]]
            temp = temp.rename(columns={"CLOSE": "value"})
            temp.loc[:, "ric_cds"] = cds.ric_cds
            temp.loc[:, "ric_equity"] = cds.ric_equity
            data.append(temp)
        except:
            temp = pd.DataFrame({
                "date": [start],
                "value": [pd.NA],
                "ric_cds": [cds.ric_cds],
                "ric_equity": [cds.ric_equity]
            })
            data.append(temp)
    return pd.concat(data)

def get_price_to_book(ric_equity, number_of_days = -365*4):

    df, err = ek.get_data(ric_equity,
                          ["TR.H.PriceToBVPerShare.date", "TR.H.PriceToBVPerShare"],
                          {"SDate": 0, "EDate": number_of_days, "FRQ": "D"})
    
    df = pd.DataFrame(df)
    df.columns = ["ric", "date", "value"]
    df = df.replace("NaN", pd.NA)
    return df




