
import requests
URL="https://stephen-king-api.onrender.com/api/books"
res=requests.get(URL)
json_data = res.json()
import pandas as pd
df=pd.json_normalize(json_data["data"])
df=df[['id','Title','ISBN']]
URL="https://api.bestbuy.com/click/5592e2b895800000/12345678/pdp"


resq=requests.get(URL)
json_data = resq.json()
df=pd.json_normalize(json_data["data"])
