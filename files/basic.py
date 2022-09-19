#files
#operations
#1.read 2.write 3.append

#1.read
f=open("file1.txt",'r') #here fis the reference name
print(f) #only shows the details of file
#for show the content we have to use iteration
# for i in f:
#     print(i)
#there is extra gap in output because of \n
#to remove it--.>
for i in f:
    data=i.rstrip("\n")
    print(data)