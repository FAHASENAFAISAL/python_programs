#count the number of user input
s="aaaabbbabc"
e=input("Enter the elemt to count")
count=0
for i in s:
    if i in e:
        count+=1
print(count)