#Encapsulation
#1. protected members
class Base1:
    def __init__(self):
        self._p=45
class Derived(Base1):
    def __init__(self):
        Base1.__init__(self)
        print("We will call the protected member of base class",self._p)
        self._p=456
        print("We will call the modified protected member outside the class",self._p)

obj1=Derived()
obj2=Base1()
print("Access the protected member of obj1",obj1._p)
print("Access the prtected member of obj2",obj2._p)