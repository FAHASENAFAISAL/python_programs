#person name,age,place-->parent class
#student roll,dep,coll-->child class
class Person:
    def setvalue(this,name,age,place):
        this.name=name
        this.ag=age
        this.loc=place
    def printvalue(this):
        print(this.name)
        print(this.ag)
        print(this .loc)
class Student(Person):
    coll="luminar"
    def Setstud(self,roll,dep):
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll,self.ag,self.loc)

s1=Student()
s1.Setstud(1,"cse")
s1.setvalue("anu",23,"kochi")
s1.printStudent()

