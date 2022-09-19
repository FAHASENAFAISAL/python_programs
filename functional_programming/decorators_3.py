#only admin can change the pin
#my code
# def pinadmin(func):
#     def wrapper(a,b):
#         if b[0]=='admin':
#             return func(a,b)
#         else:
#             raise Exception ("Only admin can access")
# @pinadmin
# def changepin(username,pin):
#     crntpin=pin
#     return crntpin
# print(changepin('admin',4567))

#code-->miss
def usercheck(func):
    def wrapper(a,b):
        if a=='admin':
            return func(a,b)
        else:
            raise Exception ("not allowed")
    return wrapper
@usercheck
def changepin(username,pin):
    crntpin=pin
    return crntpin
print(changepin('user',4567))