def

clean ata(data):

text_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5)

for user in data:

#Clean ratings

raw_rating = user["rating"].strip().lower()

if(raw_rating in text_to_num): raw_rating text_to_num[raw_rating]

user["rating"] = raw_rating

#Handle missing vals

raw_age=user.get("age")
if (raw_age==none):
    user["age"]=none
