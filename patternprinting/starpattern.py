#right angle triangle
# n=int(input("Enter the of rows: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print()#new line

# i-->number of rows
# j-->to print elements

#reverse right angle
# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1): #n=3 (3,0,-1)
#     for j in range(0,i): #(0,1) j=0
#         print('*',end=" ")
#     print()

#combination
# n=5
# for i in range(n-1):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()#new line
# for i in range(n,0,-1): #n=3 (3,0,-1)
#     for j in range(i): #(0,1) j=0
#         print('*',end=" ")
#     print()

# #square pattern printing
# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()

#pyramid pattern printing
n=4 #int(input("Enter the number of rows: ")) #3
for i in range(n): #0,1,2
    for j in range(n-i-1): #(0,3-0-1) (0,2) j=0,1 for space
        print(' ',end='')
    for k in range(i+1):# (0,0+1) k=0
        print('*',end=' ')
    print()

#    * j=2 k=1
#   * * j=1 k=2
#  * * * j=0 k=3