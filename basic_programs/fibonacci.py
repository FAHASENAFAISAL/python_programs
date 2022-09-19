# 0 1 1 2 3 5 8
# fibonacci series range in 10
def fibonacci(nterms):
    n1=0
    n2=1
    for i in range(10):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
fibonacci(15)

# def fibonacci(n):
#     a=0
#     b=1
#     if n<1:
#         print("Invalid input")
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fibonacci(10)