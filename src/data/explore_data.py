import pandas as pd

data = pd.read_csv("../../data/raw/Largest German Companies.csv", encoding='latin-1') 

def data_transformation(data):
    data["Name"] = data["Name"].str.replace("W","WW").astype(str)
    
    return data

data_transformed = data_transformation(data)