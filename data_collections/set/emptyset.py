# empty set
# s=set()
# s.add(5)
# s.add("hi")
# s.add(9.7)
# s.add(input("enter a number to add to set")) #my code
# print(s)
# print((type(s)))





# n>5 n+1 n<5 n-1
#num={6,3,8,2,9,1} o/p--> {7,2,9,1,10,0)
num={6,3,8,2,9,1}
new=set()
for i in num:
    if i<5:
        new.add(i-1)
    else:
        new.add(i+1)
print(new)

