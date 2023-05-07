import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("eStoreData.csv",header=0)
df.drop(df.index[(df["email"] == "agan")],axis=0,inplace=True)
