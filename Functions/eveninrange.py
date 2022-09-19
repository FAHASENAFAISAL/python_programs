#even in range
# def evenlist(n1,n2):
#     for i in range(n1,n2+1):
#         if i%2==0:
#             print(i)
# evenlist(1,10)

#sum of odd numbers in a range
def oddsum(r1,r2):
    sum=0
    for i in range(r1,r2+1):
        if i%2!=0:
            sum=sum+i
    return(sum)
print(oddsum(1,10))
