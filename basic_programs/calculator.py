#option 1.add 2.sub 3.mul 4. div 5.stop
#num1=200 and num2=100

# def addoper():
#     add=num1+num2
#     print(add)
# def suboper():
#     sub=num1-num2
#     print(sub)
# def muloper():
#     mul=num1*num2
#     print(mul)
# def divoper():
#     div=num1/num2
#     print(div)
# while True:
#     print("Enter your option 1.ADD 2.Substract 3.Multiplication 4.Division 5.Exit")
#     opt = int(input())
#     if opt==5:
#         break
#     num1 = int(input("Enter 2 numbers"))
#     num2 = int(input())
#     if opt==1:
#         addoper()
#     elif opt==2:
#         suboper()
#     elif opt==3:
#         muloper()
#     elif opt==4:
#         divoper()
#     else:
#         print("invalid")

#miss code
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