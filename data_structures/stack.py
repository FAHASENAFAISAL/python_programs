#create stack by using list
#my code
l=[]
while True:
    print("Select operations 1.push 2.pop")
    option=int(input())
    if option==1:
        a=int(input("Enter the element to add to stack "))
        l.append(a)
        print(l)
    elif option==2:
        l.pop()
        print(l)
    else:
        print("Invalid")


