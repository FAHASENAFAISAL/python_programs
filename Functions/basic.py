#functions
# def add():
#     n1=int(input("enter the numbr 1:"))
#     n2=int(input("enter the numbr 2:"))
#     sum=n1+n2
#     print(sum)
# add()
# add()

#2. function with arguments
# def add(num1,num2):
#     sum=num1+num2
#     print(sum)
# add(100,200) # with no input,
# no1=int(input("enter")) # when we wanted the input by user
# no2=int(input("Enter"))
# add(no1,no2)

#3 function with argumnets and return it uses when we didn't want show the output it for other purpouse
#it is most important function
# def add(num1,num2):
#     sum=num1+num2
#     return sum # after define return we cannot enter anything in that specefic block
# # print(add(7,9))
# a=add(8,9)
# print(a)

#program for print 1 to 10
# def printi():
#     for i in range(1,10+1):
#         return i
# print(printi())

#example for only one return
def posneg(n):
    if n>0:
        return  "pos"#here we use 3 return and it works bcz three in different block
    elif n<0:
        return "neg"
    else:
        return "zero"
print(posneg(3))
print(posneg(-9))
print(posneg(0))

