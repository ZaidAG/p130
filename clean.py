import pandas as pd
import csv
df=pd.read_csv('final.csv')
print(df.shape)
del df["luminosity"]
print(df.shape)
df.to_csv('main.csv')