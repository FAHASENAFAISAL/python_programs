initial=int(input("Enter initial value"))
final=int(input("Enter final value"))
sum=0
while initial<=final:
    if initial%2!=0:
       sum=sum+initial
    initial+=1
print(sum)