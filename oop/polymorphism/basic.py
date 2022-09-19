#polymorphism-->many forms
#methods

#method overloading and method overriding

#method overloading-->same method name diff num of arguments
class Addition:
    def add(self,n1,n2):
        self.n1=n1
        self.n2 = n2
        print("add two nums ",self.n1+self.n2)
    def add(self, n1, n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        print("add three nums ", self.n1 + self.n2+self.n3)
add1=Addition()
add1.add(5,7) #method1
add1.add(5,7,8) #calls method 2
#if arguents 2 calls -->method 1 else 3 then calls the method 2 here makes an error
#that is python does not support method overloading
#these types issues solved by