#person nameage,loc
#parent phn,adrs
#employee id desig sal
class Person:
    def setPerson(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc
    def printPerson(self):
        print(self.name,self.age,self.loc)
class Parent:
    def setParent(self,phn,adrs):
        self.phn=phn
        self.adrs=adrs
    def printParent(self):
        print(self.phn,self.adrs)
class Employee(Person,Parent):
    def setEmployee(self,id,desig,sal):
        self.id=id
        self.desig=desig
        self.sal=sal
    def printEmployee(self):
        print("Employee Details")
        print("id:",self.id,"name:",self.name,"age:",self.age)
        print("designation:",self.desig,"salary:",self.sal)
        print("phone number:",self.phn,"Address:",self.adrs,"Location:",self.loc)
e1=Employee()
e1.setPerson("anu",23,"kochi")
e1.setParent(89765434,"block 11")
e1.setEmployee(101,"Developer",50000)
e1.printEmployee()