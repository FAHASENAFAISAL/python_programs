# pattern 1
k=6
for i in range(5):
    for j in range(k-i-1):
        print(end=" ")
    for l in range(i):
        if i==3 and l==1:
            print(end="  ")
        else:
            print("*",end=" ")
    print()

#pattern 2
n=5
for i in range(5):
    for j in range(n-i-1):
        print("",end="")
    for l in range(i):
        if i==3 and l==1:
            print(end="  ")
        else:
            print("*",end=" ")
    print()

#pattern 3
r= 4
for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

#pattern 4
n=4
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(' ',end='')
    for k in range(0,i):
        if i==3 and k==1:
            print(end="  ")
        else:
            print('*',end=' ')
    print()

#pattern 5
n=4
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(' ',end='')
    for k in range(0,i):
        print('*',end=' ')
    print()

#pttern 6
r=5
c=5
for i in range(r):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(c):
        print("*", end=" ")
    print()
