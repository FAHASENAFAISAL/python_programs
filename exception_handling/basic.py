#create a division function
# def divide(n1,n2):
#     return n1/n2
# print(divide(9,8))
# print(divide(9,0))

#exception handling
n1=int(input("enter num1: "))
n2=int(input("enter nuum2: "))
try:
    print("inside try")
    print(n1/n2)
except Exception as e: # to findout the mode of exception
    print(e)
finally:
    print("in finally")