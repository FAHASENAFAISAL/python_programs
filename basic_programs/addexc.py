#here we importing functions from modules in the packages_and_modules package
#from package name.module name import function names  // if we want all functions use '*'
from packages_and_modules.basic import add,sub
print(add(8,9))
print(sub(9,8))

#factorial function from Functions package
from Functions.factorial import fact
print(fact(8))