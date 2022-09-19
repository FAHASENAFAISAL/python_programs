#findout out pair which can get sum put by user that is sum=9 pair= 4 5 and 5 4
l=[1,2,3,4,5]
count=0
sum=int(input("enter sum: "))
for i in l:
    for j in l:
        count+=1
        if (i+j)==sum:
            print(i,j)
print(count)