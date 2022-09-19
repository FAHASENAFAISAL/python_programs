#class creation
class Person:
    def setvalue(self,name,age,place): #here name,age,place-->called as attributes
    #if want pass attributes then pass it as instance variable then only it reuses
        self.name=name
        self.ag=age
        self.loc=place
    def printvalue(self):
        print(self.name)
        print(self.ag)
        print(self.loc)
pe1=Person()
pe1.setvalue("anu",23,"kochi")
pe1.printvalue()
print(".....")
print(pe1.name)
print("....")

pe2=Person()
pe2.setvalue("amal",22,"calicut")
pe2.printvalue()

#we can replace self by ourself but change in all places,it cames as defaultly
# class Person:
#     def setvalue(this,name,age,place): #here name,age,place-->called as attributes
#     #if want pass attributes then pass it as instance variable then only it reuses
#         this.name=name
#         this.ag=age
#         this.loc=place
#     def printvalue(this:
#         print(this.name)
#         print(this.ag)
#         print(this.loc)