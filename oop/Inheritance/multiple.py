# multiple inheritnce-->more than one parent class
class A:
    def printa(self):
        print("Inside A class")
class B:
    def printb(self):
        print("Inside B class")
class C(A,B):
    def printc(self):
        print("Inside C class")
objc=C()
objc.printa()
objc.printb()
objc.printc()

