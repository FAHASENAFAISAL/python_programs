#how to create exception
#here we create a negative error that is first value less than second value
num1=int(input("enter num1: "))
num2=int(input("Enter num2: "))
if num1<num2:
    raise Exception("negative value")
else:
    print(num1-num2)