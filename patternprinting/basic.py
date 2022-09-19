#hole creation in between pattern

k=6
for i in range(5):
    for j in range(k):
        print(end=" ")
    k=k-1
    for l in range(i):
        if i==3 and l==1:
            print(end="  ")
        else:
            print("*",end=" ")
    print()