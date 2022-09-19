#1
l=[1,0,7,5,9,2,3,5,7,2,0,1,10]
l.sort()
d=[]
dup=[d.append(i) for i in l if i not in d]
print("sorted list is",l,"\n""After eliminate duplicate elements",d)

#3
lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,2,34,289,29,12,63,976]
lst.sort()
print("second largest elements is : ",lst[-2])

# #4
a=[1,2,3,45,6,7,33,11,77,9,0,5]
b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
common=[]
for i in a:
    for j in b:
        if i==j:
            common.append(i)
            break
print("common elements in both lists are : ",common)

#2.
word={}
f=open("count.txt","r")
for i in f:
    data=i.rstrip("\n").split(" ")
for i in data:
    if i not in word:
        word.update({i:1})
    else:
        val=word[i]
        val=val+1
        word.update({i:val})
print(word)