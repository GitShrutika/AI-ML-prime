import pandas as pd
df=pd.read_csv("raw_data (1).csv")

print(df,type(df))
print(df.head())
print(df.tail())
print(df.sample())
print(df.info())
print(df.shape)
print(df.describe())
df=pd.read_csv("airqual.csv")
df.head
df[ df["aqi"] > 100]
df[(df["aqi"]>100) & (df["temperature"]>30)]
df[ df["aqi"] > 100][["city","aqi"]]
df.query("aqi > 100 & temperature > 30") [["city","aqi"]]
df=pd.read_csv("raw_data (1).csv")
df.isnull().sum()
df.dropna()
df.fillna(123)
df.ffill()
df.bfill()
df.duplicated()
df.dtypes
df["gender"].str.lower()
