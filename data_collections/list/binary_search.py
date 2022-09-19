l=[1,3,7,2,4,6,8,9,10,22,44,77,12,43,31,45]
# first step in binary search is sorting
e=100
flag=0
l.sort()
print(l)
count=0
low=0
upper=len(l)-1
while low<=upper:
    count=count+1
    middle=(low+upper)//2
    if l[middle]==e:
        flag=1
        break
    elif e>l[middle]:
        low=middle+1
    elif e<l[middle]:
        upper=middle-1
if flag==1:
    print("present")
else:
    print("not present")
print(count)