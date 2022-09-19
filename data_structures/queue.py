#queue
#fifo

#size
#enqueue
#dequeue
#list

#pgm for queue operations
queue=[]
size=int(input("Enter the size: "))
top=0
def enqueue():
    global top
    if top>=size:
        print("queue is full")
    else:
        e=int(input("Enter the element to add: "))
        queue.append(e)
        top+=1
        print(queue)
def dequeue():
    global top
    if top==0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        top=top-1
        print(queue)
while True:
    print("Select operations 1.Enqueue 2.Dequeue")
    option=int(input())
    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    else:
        print("invalid")



#oops
#regular expression
#functional programming
#decorators