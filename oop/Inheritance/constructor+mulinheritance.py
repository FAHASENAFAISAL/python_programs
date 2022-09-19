#person nameage,loc
#parent phn,adrs
#employee id desig sal
class Person:
    def __init__(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc
    def printPerson(self):
        print(self.name,self.age,self.loc)
class Parent:
    def __init__(self,phn,adrs):
        self.phn=phn
        self.adrs=adrs
    def printParent(self):
        print(self.phn,self.adrs)
class Employee(Person,Parent):
    def __init__(self,id,desig,sal,name,age,loc,phn,adrs):
#more than one constructor can't call by super, it can use simply use the class name,can't remove self here
        Person.__init__(self,name,age,loc)
        Parent.__init__(self,phn,adrs)
        self.id=id
        self.desig=desig
        self.sal=sal
    def printEmployee(self):
        print("Employee Details")
        print("id:",self.id,"name:",self.name,"age:",self.age)
        print("designation:",self.desig,"salary:",self.sal)
        print("phone number:",self.phn,"Address:",self.adrs,"Location:",self.loc)
e1=Employee(1,"dev",980000,"amal",26,"kochi",90887679,"blck 11")
e1.printEmployee()