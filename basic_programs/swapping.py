no1=5
no2=10
print("Value of no1 before swapping",no1)
print("Value of no2 before swapping",no2)
# method 1-pblm is extra memory consume, it is better not take extra memory
# temp=no1
# no1=no2
# no2=temp
# print("Value of no1 after swapping",no1)
# print("Value of no2 after swapping",no2)

# # method 2-concept is tuple unpacking only possible in python
# no1,no2=no2,no1
# print("Value of no1 after swapping",no1)
# print("Value of no2 after swapping",no2)

# method 3 no1=5,no2=10
no1=no1+no2 #no1=15
no2=no1-no2 #no2=5
no1=no1-no2 #no1=10
print("Value of no1 after swapping",no1)
print("Value of no2 after swapping",no2)

