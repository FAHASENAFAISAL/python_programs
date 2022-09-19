#take phone numbers from phone.txt and print only valid phone numbers in another txt file
f=open("phone.txt",'r')
f1 = open("validnum.txt", 'w')
for i in f:
    d=i.rstrip("\n") #bcz otherwise len=11
    if (len(d)==10):
        f1.write(i)