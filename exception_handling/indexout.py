#unexpected error in list when we index out of range
l=[1,2,3]
index=int(input("enter index: "))
try:
    print(l[index])
# except:
#     print("index is not present")

# #how to findout the error
except Exception as e:
    print(e)