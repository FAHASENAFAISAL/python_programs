#option 1.add 2.sub 3.mul 4. div 5.stop
#num1=200 and num2=100


def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
while True:
    print("Select operation\n1.ADD\n2.Substract\n3.Multiplication\n4.Division\n5.Exit\n")
    option=int(input())
    if option==5:
        print("Exit")
        break
    elif option>=1 and option<=4:
        num1=int(input("Enter 2 numbers:"))
        num2=int(input())
        if option==1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            mul(num1,num2)
        else:
            div(num1,num2)
    else:
        print("Invalid")