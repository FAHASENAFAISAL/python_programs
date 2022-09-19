#hw
#remove special characters from string
s=input("Enter string")
new=""
special='''!@#$%^&*()_+-={}[]:"|;'<>?,./'''
for i in s:
    if i not in special:
        new=new+i
print(new)