df2=df.copy()

df2["tax"] = df2["income"].apply(lambda x :"20%" if x >=5000 else "10%")


gendermap={"Male":"M","Female":"F","Unknown":"u"}
df2["gender"].map(gendermap)
df2=df.rename(columns={"name":"mazz_nav"})
df2
df2=df.copy()
newcolorder=[col for col in df2.columns if col != "id"] +["id"]
print(newcolorder)
df2[newcolorder]
df2=df.copy()

df2=df2.drop_duplicates()

df2=df2.fillna(0)
df2=df2.sort_values("income")
df2=df2.reset_index(drop=True)
df2.to_csv("sorted_data.csv")
df.groupby("country")["income"].mean()
df.groupby("country")["income"].min()
df.groupby("country")["income"].max()
df.groupby("gender")["income"].min()
df.groupby("country")["income"].agg(["mean","max"])
df.groupby("country").agg({
    "income":"mean",
    "age":"mean"
})
df
