#inheritance
#single inheritance
class A: #parent/super/base class
    def printa(self,n):
        self.n=n
        print("Inside A class ")
class B(A): #child/su/derived class
    def printb(self):
        print("inside B class",self.n)

objb=B()
objb.printa(100)
objb.printb()