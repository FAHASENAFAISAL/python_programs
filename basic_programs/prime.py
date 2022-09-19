# for break else
#1
# for i in range(5):
#     if i==4:
#         print("inside if")
#         break
# else:
#     print("in else")

#2
# for i in range(5):
#     if i==9:
#         print("inside if")
#         break
# else:
#     print("in else")

# prime numbers
n=int(input("Enter number:"))
for i in  range(2,n):
    if n%i==0:
        print("Not prime")
        break
else:
    print("prime")

#prime numbers with function with arguments and return type
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return ("Not prime") #no need break bcz there is already return
#     else:
#         return ("prime")
# print(prime(5))

# print prime numbers from the range that user input
r1=int(input("Enter the ranges:"))
r2=int(input())
for i in range(r1,r2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



