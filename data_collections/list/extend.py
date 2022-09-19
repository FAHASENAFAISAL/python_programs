a=[1,2,3]
b=[4,5,6]
# a.append(b)
# print(a)
a.extend(b)
print(a)

# remove middle element my code
a=[1,5,3,6,7,8,9]
print(a)
mid=a[int(len(a)/2)] # len(a)//2 to remove float
a.remove(mid)
print(a)

# remove middle element miss code
a=[1,5,3,6,9,10,11]
mid=len(a)//2
a.remove(a[mid])
print(a)