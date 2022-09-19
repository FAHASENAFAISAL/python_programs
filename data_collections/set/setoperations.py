#common elements
s1={1,2,3,4,5}
s2={3,4,5,6,7}
for i in s1:
    if i in s2:
        print(i)

#set operations
# 1.union-->joining
#2. intersection-->common
#3. difference-->deleting
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a.union(b))
print(a.intersection(b)) #-->here b deletef from a
print(a.difference(b))
print(b.difference(a))