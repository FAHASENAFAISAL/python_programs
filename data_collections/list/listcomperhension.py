#list comperhension
l=[1,5,7,8,2,3]
square=[]
for i in l:
    square.append(i**2)
print(square)

#list comperhension
l=[1,5,7,8,2,3]
square=[i**2 for i in l]
print(square)

#even numbers using comperhension
l=[1,5,7,8,2,3]
even=[i for i in l if i%2==0]
print(even)

#odd
l=[1,5,7,8,2,3]
odd=[i for i in l if i%2!=0]
print(odd)

# 1 to 20 even list
even=[i for i in range(1,20) if i%2==0]
print(even)