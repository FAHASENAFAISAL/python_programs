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
    def __init__(self,name,roll,dep,age,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dep=dep

    def printStudent(self):
        print(self.name,self.roll,self.dep,Student.coll,self.ag,self.loc)
s1=Student("anu",1,"cse",23,"kochi")
s1.printStudent()