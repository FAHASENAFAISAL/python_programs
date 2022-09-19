#print common elements
# s1="abcd"
# s2="cdef"
# for i in s1:
#     if i in s2:
#         print(i)

#count the number of user input
s="aaaabbabc"
count=0
e=input("Enter a string")
for i in s:
    if i in e:
        count=count+1
print(count)