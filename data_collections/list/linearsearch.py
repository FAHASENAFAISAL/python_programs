#linear search
l=[1,3,7,2,4,6,8,9,10,22,44,77,12,43,31,45]
e=int(input("Enter the number to seaarch: "))
for i in l:
    if i==e:
        print("present")
        break
else:
    print("not present")