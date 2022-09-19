#1
# def greatest():
#     num1=int(input("Enter 2 numbers:"))
#     num2=int(input())
#     if num1>num2:
#         print("First number is greatest")
#     elif num1<num2:
#         print("second number is larger")
#     else:
#         print("equal")
# greatest()

#2 with arguments
# def greatest(num1,num2):
#     if num1>num2:
#         print("First number is greatest")
#     elif num1<num2:
#         print("second number is larger")
#     else:
#         print("equal")
# greatest(4,2)

#3 with arguments and return
def greatest(num1,num2):
    if num1>num2:
        return ("First number is greatest")
    elif num1<num2:
        return ("second number is larger")
    else:
        return ("equal")
print(greatest(4,2))
