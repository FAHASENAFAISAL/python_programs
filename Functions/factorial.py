# factorial with first type
# def fact():
#     fact = 1
#     n=int(input("Enter the number:"))
#     for i in range(1, n + 1):
#         fact = fact * i #fact*=i
#     print(fact)
# fact()

#factorial with argumnets
# def fact(n):
#     fact=1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print(fact)
# fact(9)

#factorial with argumnets and return
def fact(n):
    fact=1
    for i in range(1, n + 1):
        fact*=i
    return (fact)
# print(fact(9))
