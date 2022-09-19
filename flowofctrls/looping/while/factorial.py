# n=int(input("Enter the number: "))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)

# range 1 to range 2 factorial example 9 t0 120
range1=int(input("Enter the initial number: "))
range2=int(input("Enter the final number: "))
fact=1
while range1<=range2:
    fact=fact*range1
    range1+=1
print(fact)