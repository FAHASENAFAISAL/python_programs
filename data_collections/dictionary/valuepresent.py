#check key value input by user is present/not present in the dictionary
d={1:0,2:1,3:2,4:3}
value=int(input("enter a key value: "))
if value in d.values():
    print("present")
else:
    print("not present")
