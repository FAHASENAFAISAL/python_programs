class A:
    def printa(self):
        print("Inside A class")
class B(A):
    def printb(self):
        print("Inside B class")
class C(B):
    def printc(self):
        print("Inside C class")
objc=C()
objc.printa()
objc.printb()
objc.printc()
