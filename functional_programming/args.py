# *args
#args used -->code is created by programmer and used by user and they don't know about no of arguments if they
#put more than arguments creates error-->it can solve by using *args-->its o/p ttype is tuple
def add(*args):
    return args
print(sum(add(7,8,9))) #in built method

#without in built method
def add(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
print(add(7,8,9,10))

#python does not support method overloading-->if we want call a function a number of arguments using *args