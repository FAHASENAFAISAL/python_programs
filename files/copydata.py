#write program to take data from data.txt and paste in another program
f1=open("data.txt",'r')
f2=open("copydata.txt", 'w')
for i in f1:
    f2.write(i)

