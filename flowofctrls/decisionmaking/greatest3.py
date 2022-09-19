#greatest among three numbers
num1=int(input("first number: "))
num2=int(input("second number: "))
num3=int(input("third number: "))

# if num1>num2 and num1>num3:
#     print("first number is greatest")
# elif num2>num1 and num2>num3:
#     print("second number is greatest")
# elif num3>num1 and num3>num2:
#     print("third number is greatest")
# else:
#     print("Equal numbers")

if num1==num2==num3:
    print("Equal numbers")
elif num2>=num1 and num2>=num3:
    print("second number is greatest")
elif num3>=num1 and num3>=num2:
    print("third number is greatest")
else:
    print("first number is greatest")

# n=5
# if n>0:
#     if n>5:
#         print(n) #not print bcz n=5
#     else:
#         print(n) #prints 5
# else:
#     print("last") #it only works when n<0
