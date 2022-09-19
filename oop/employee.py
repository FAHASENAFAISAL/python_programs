#emoloyee id name desig salary company_name
class Employee:
    company_name="ABC"
    def setEmployee(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    def printEmpolyee(self):
        print(self.id,self.name)
        print(self.desig,self.salary)
        print(Employee.company_name)
e1=Employee() #object creation
e1.setEmployee(101,"Amal","Manager","70000") #object initialize this point
e1.printEmpolyee()
e2=Employee()
e2.setEmployee(102,"Anu","Developer",50000)
e2.printEmpolyee()