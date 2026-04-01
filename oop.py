#class and obj in python
class Student:
    subject ="python"
    a=10
    stud1=Student()
    print(stud1)
class Student:
    #instance attributesssss
    def __init__(self,name):
        self.name= name
        print("constructor was pass")
    
    sub = "python"

# Create object outside the class
stud1 = Student("sk")
stud2= Student("ffsf")
stud3 = Student("sfdawrf")

print(stud1.name)
print(stud2.name)
print(stud3.name)
    
