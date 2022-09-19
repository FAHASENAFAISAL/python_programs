#create student name,roll,dep,college

#oop variable types-->
#static variable-->related to class-->access using class name
#instance variable-->related to methods-->access using self

class Student:
    coll="luminar" #satatic variable
    def setStudent(self,name,roll,dep): #instance variables
        self.name=name
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll)
s1=Student()
s1.setStudent("anu",23,"cse")
s1.printStudent()
s2=Student()
s2.setStudent("amal",24,"ece")
s2.printStudent()