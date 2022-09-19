a=100
b=200
print("First number is"+str(a)+"second number is"+str(b)) #here needs to covert to string for concantenate that
# that is concatenate only same type


a=input("Enter 2 numbers")
b=input()
print("Hi, first number is "+ a+" second number is"+b ) #here no need conversion bcz input takes data as string

# sum=a+b #here we want conversion to int otherwise print just 2+3=23
# print("result is"+sum)

sum=int(a)+int(b)
print("result is"+str(sum)) #here again we convert sum to str because concantenate