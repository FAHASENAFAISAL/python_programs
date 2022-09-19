#decorators-->to decorate the function
#to add extra rule in functions-->use decorators
#can use many functions a single decorator

#structure-->
def changevalue(func): #create a function with single argument
    def wrapper(a,b):  #create another function with no of arguments used in our desired function
        if a<b:
            a,b=b,a #the rule come under the inner function
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@changevalue
def sub(n1,n2):
    return n1-n2
print(sub(2,4))
@changevalue
def div(n1,n2):
    return n1/n2
print(div(2,8))
