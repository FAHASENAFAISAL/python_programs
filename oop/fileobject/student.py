#how to create create objects from files
class Student:
    coll="luminar"
    def __init__(self,name,roll,dep): #instance variables
        self.name=name
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll)
f=open("student.txt","r")
for i in f:
    d=i.rstrip("\n").split(",")
    name=d[0]
    roll=d[1]
    dep=d[2]
    obj=Student(name,roll,dep)
    obj.printStudent()
