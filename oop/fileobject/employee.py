class Employee:
    company="ABC"
    def __init__(self,id ,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printEmployee(self):
        print(self.id,self.name,self.salary,Employee.company)
f=open("employee.txt","r")
for i in f:
    d=i.rstrip("\n").split(",")
    id=d[0]
    name=d[1]
    salary=d[2]
    obj=Employee(id,name,salary)
    obj.printEmployee()