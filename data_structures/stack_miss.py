#miss code
stack=[]
size=int(input("Enter the size of stack: "))
top=0
def push():
    global top
    if top>=size:
        print("Stack is full")
    else:
        e=int(input("Enter the element to add: "))
        stack.append(e)
        top+=1
        print(stack)
def pop():
    global top
    if top==0:
        print("stack is empty")
    else:
        stack.pop()
        top-=1
        print(stack)

while True:
    print("Select operations 1.Push 2.Pop")
    option=int(input())
    if option==1:
        push()
    elif option==2:
        pop()
    else:
        print("invalid")
