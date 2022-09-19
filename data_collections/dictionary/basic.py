#dictionary
d={"name":"anu","place":"kochi","age":24}
print(d)
print(type(d))

#iteration
for i in d:
    print(i) #only print key
print()

for i in d:
    print(d[i]) #print values of key
print()

for i in d:
    print(i,d[i]) #print key and value

#in bult function for take both key and value
print(d.keys())
print(d.values())