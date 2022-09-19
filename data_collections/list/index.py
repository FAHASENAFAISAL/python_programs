# l=[1,5,8,9,10]
# print(l)
# l[2]=90
# print(l)
# l[0:2]=[100,200]
# print(l)
# l[0:2]=[100]
# print(l)
# l[0:2]=[100,200,300]
# print(l)
# print(l[::-1])
# print(l[1])
# print(l[-2])
# print(l[2:5])

#print duplicate elements
lst=[1,4,6,7,8,9,2,3,4,5,6,7]
dup=[]
new=list()
for i in lst:
    if i not in new:
        new.append(i)
    else:
        dup.append(i)
print(dup)