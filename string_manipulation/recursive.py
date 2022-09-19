#print first recursive element
# s=input("Enter string")
# new=""
# for i in s:
#     if i not in new:
#         new=new+i
#     else:
#         print("first recursive element:",i)
#         break

#print last recursive
# s = input("Enter string")
# new = ""
# rep = ""
# for i in s:
#     if i not in new:
#         new = new + i
#     else:
#         rep = rep + i
# print(rep[-1])

#aaabbcc recursive is-aabc unique storage-abc,print b
s = input("Enter string")
new = ""
rep = ""
for i in s:
    if i not in new:
        new = new + i
    else:
        if i not in rep: #logic is important
            rep = rep + i
print(rep[1])
