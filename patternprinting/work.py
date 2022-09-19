#1. right angle triangle using 1
#2. reverese angle using #

#1 right triangle.
n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print('1',end="")
    print()
#
#2 reverese triangle
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(i):
        print('#',end="")
    print()

#3 reverse pyramid
n=int(input("Enter the number of rows: ")) #3
for i in range(n,0,-1): #0,1,2
    for j in range(0,n-i+1): #(0,3-0-1) (0,2) j=0,1 for space
        print(' ',end='')
    for k in range(0,i):# (0,0+1) k=0
        print('*',end=' ')
    print()
#4 pyramid using zero
n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(' ',end="")
    for k in range(0,i+1):
        print('0',end=" ")
    print()