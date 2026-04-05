f=open("sample.txt","a+")

#data = f.read()
#data=f.readline()
f.write("text to override 3223e")
print(f.read())
#print(data)
#print(type(data))
f.close()
