#string manipulation
# s="luminar technolab"
# for i in s:
#     print(i)

#check the element present or not
#method 1
# e=input("Enter the element to search")
# s="luminar technolab"
# for i in s:
#     if e==i:
#         print("present")
#         break
# else:
#     print("not prsent")
#method 2 through this method we can avoid multiple print statements inside for,the pblm extra variable so memory cnception
# e=input("Enter element to search")
# s="luminar technolab"
# flag=0
# for i in s:
#     if i==e:
#         flag=1
#         break
# if flag==0:
#     print("Not found")
# else:
#     print("Found")

#method 3
e=input("Enter element to search:")
s="luminar technolab"
if e in s:
    print("present")
else:
    print("not present")

e=input("Enter element to search:")
s="luminar technolab"
if e not in s:
    print("not present")
else:
    print("present")