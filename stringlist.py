a=5
b=10
sum=a+b
print("language is {}".format("python"))
print("sum is{}".format())
marks=[99,88,77,66,55]
print(marks[3])
print(len(marks))
marks[2]=746
marks.append(678)
print(marks)
num=[1,2,3,4,5]
x=5
idx=0
for val in num:
    if (val==x):
        print(idx)
        break
    idx+=1
tup={1,2,3,4,5,"abc"}
print(tup)
print(type(tup))
dict= {
    "name":"shrutika",
    "cgpa":8.09
}
print(dict.keys())
print(dict.values())
print(dict.items())'''
#write a code for unique courses
info=[
    ("name","shrutika"),
    ("sas","math"),
     ("fzdf","eng"),
    ("sar","math"),
     ("nefsf","sci"),
    ("sarfa","eng"),
     ("dsfc","geo"),
    ("sasdssd","sci"),
    ]
uniquecourses=set()

for tup in info:
    uniquecourses.add(tup[1])
    print(uniquecourses)
    
