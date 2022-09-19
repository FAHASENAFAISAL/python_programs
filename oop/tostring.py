#to string
class Student:
    coll="luminar"
    def __init__(self,name,roll,dep): #instance variables
        self.name=name
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll)
    # def __str__(self):
    #     return self.name
#here without str method print st1-->output is location of st1. for change that to something related to the object
#we use to str method.numbers can't give
#if we want to use numbers then covert to str
    # def __str__(self):
    #     return str(self.roll)
#if we want multiple then use concatenation
    def __str__(self):
        return str(self.roll)+self.name
st1=Student("anu",1,"cse")
print(st1)
st1.printStudent()

