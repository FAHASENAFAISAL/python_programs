# using for loop it is easy here
# for i in range(1,11):
#     if i%2==0:
#         print(i**2)
#     else:
#         print(i**3)

# using while loop
# i=1
# while i<=10:
#     if i%2==0:
#         print(i**2)
#     else:
#         print(i**3)
#     i=i+1
#
sum_e=0
sum_o=0
for i in range(1,11):
    if i%2==0:
        i**2
        sum_e+=i

    else:
        i**3
        sum_o+= i
print("Square of even numbers", sum_e)
print("Cube of odd number",sum_o)