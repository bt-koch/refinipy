def export_csv(dataframe, name):
    if not name.endswith(".csv"):
        name = name+".csv"
    dataframe.to_csv("data/"+name, index=False)