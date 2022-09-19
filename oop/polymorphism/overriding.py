#overriding
#same  method name and same num of arguments
#child clas method overrides parent class method
class Parent:
    def buyPhone(self):
        print("Nokia")
class Child(Parent):
    def buyPhone(self):
        print("Iphone")
c=Child()
c.buyPhone()