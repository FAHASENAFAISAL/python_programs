#constructor
#constructor is used to initialize an object at the time of object creation
#constructor method invoke automatically when creating object,no separate call
#constructor method __init__()
#it can only use code with insatnce variable and its set no other types
class Person:
    # def setvalue(self,name,age,place):-->this was our initialise method
    #-->convert in cnstructor
    def __init__(self,name,age,place): #__init__ is the constructor is an inbulit method,no need separate call
        self.name=name
        self.ag=age
        self.loc=place
    def printvalue(self):
        print(self.name)
        print(self.ag)
        print(self.loc)

pe1=Person("amal",23,"kochi") #craete and initialization at the same step
pe1.printvalue()

#constructor in student
class Student:
    coll="luminar" #satatic variable
    def __init__(self,name,roll,dep): #instance variables
        self.name=name
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll)
s1=Student("amal",101,"cse")
s1.printStudent()
