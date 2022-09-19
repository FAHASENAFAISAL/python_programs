#create a single list where the items from data.txt each word as each elemnt in the list
f=open("data.txt",'r')
l=[]
for i in f:
    word=i.rstrip("\n").split(" ")
    l.extend(word) #if use append that is print nested list
print(l)
