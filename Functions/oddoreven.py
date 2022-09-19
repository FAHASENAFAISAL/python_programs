#odd or even with 3 types of function
#1
# def oddoreven():
#     n=int(input("enter a number"))
#     if n%2==0:
#         print("Even number")
#     else:
#         print("odd number")
# oddoreven()

#2.
def oddoreven(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
oddoreven(5)
 # with no input,
# no1=int(input("enter")) # when we wanted the input by user
# no2=int(input("Enter"))
# add(no1,no2)

#3
def oddoreven(n):
    if n%2==0:
        return ("Even")
    else:
        return ("Odd")
print(oddoreven(10))
