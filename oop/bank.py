#bank
#static bank name
#instance name,acno

#method-->deposit(amnt),withraw(amnt),balanace check()

class Bank:
    bname="SBI"
    def __init__(self,name,acno):
        self.name=name
        self.acno=acno
        self.minbalance=1000
        self.balance=self.minbalance
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("your",Bank.bname,"has bee credited with amount",self.amount)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-self.amt
            print("Your",Bank.bname,"has been debited with amount",self.amt)
    def checkbalance(self):
        print("your current balance is",self.balance)
ac1=Bank("anu",989756675)
ac1.checkbalance()
ac1.deposit(1500)
ac1.checkbalance()
ac1.withdraw(3000)
ac1.withdraw(1000)
ac1.checkbalance()

