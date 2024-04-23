import pandas as pd

def export_csv(dataframe, name):
    if not name.endswith(".csv"):
        name = name+".csv"
    dataframe.to_csv("data/"+name, index=False)

def format_dataframe(dataframe):
    dataframe["value"] = pd.to_numeric(dataframe["value"])
    dataframe["date"] = pd.to_datetime(dataframe["date"]).dt.date
    return dataframe
    