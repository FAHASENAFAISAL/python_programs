#person name,age,place-->parent class
#student roll,dep,coll-->child class
class Person:
    def __init__(this,name,age,place):
        this.name=name
        this.ag=age
        this.loc=place
    def printvalue(this):
        print(this.name)
        print(this.ag)
        print(this .loc)
class Student(Person):
    coll="luminar"
    def __init__(self,roll,dep,name,age,place):
        super().__init__(name,age,place)  #only one parent class use super()-->this constructor calling can remove self here
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll,self.ag,self.loc)

s1=Student(1,"cse","anu",23,"kochi")
s1.printStudent()
s1.printvalue()