#tuple
t=(1,2,3,4,5) # t=1,2,3,4,5 also correct
print(t)
print(type(t))
# keep order
t=8,7,3,2,1,5
print(t)
#hetreogeneous
t=4,5,6,"hi",9.8
print(t)
#nesting support
t=(1,2,3,5,(6,7,8))
print(t)
#indexing support
print(t[1])
#support duplication
t=3,5,3,4,1,3
print(t)
#immutable

#iteration
for i in t:
    print(i)
