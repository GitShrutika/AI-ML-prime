import pandas as pd
info ={
"name":["shrutika","shiv","shri"],
"cgpa":[8.07,45.6,676.56]
}
df=pd.DataFrame(info)
print(df)
s=pd.Series([1,2,3,4,5])
print(s)
print(type(s))
print(s[1])
s=pd.Series([1,2,3],index=["shr","hin","shiv"])
print(s)
print(s.index)
s1=pd.Series([1,2,3,4,5])
s2=pd.Series([10,20,30,40,50])

print(s1+s2)
info ={
"name":["shrutika","shiv","shri"],
"cgpa":[8.07,45.6,676.56],
    "index":[1,2,3]
}
df=pd.DataFrame(info)
print(df)
df=pd.DataFrame([["shr",1],["shiv",2],["shri",3]],columns=["name","age"])
print(df)
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
