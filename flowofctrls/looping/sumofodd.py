initial=int(input("Enter initial value"))
final=int(input("Enter final value"))
sum=0
for i in range(initial,final+1):
    if i%2!=0:
        sum=sum+i
print(sum)