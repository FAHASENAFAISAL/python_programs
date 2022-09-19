#sum of prime numbers in a range
r1=int(input("Enter the ranges:"))
r2=int(input())
sum=0
for i in range(r1,r2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+i
print(sum)
