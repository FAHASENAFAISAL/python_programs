weight=int(input("Enter your weight: "))
option=input("select l if lbs and k if kg: ")
if (option=="l"):
    print(weight*2.2)
else:
    print(weight*.45359237)