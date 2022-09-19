fixed_amount=1000000
# withdraw=int(input("Enter the amount to withdraw"))
# balance=int(fixed_amount-withdraw)
# print(balance,"is your balance amount") my code

# amt=int(input("Enter amount to withdraw"))
# print("Your ac balance",fixed_amount-amt)

# if else
amt=int(input("Enter amount to withdraw"))
if amt>fixed_amount:
    print("Insufficient balance")
else:
    print("Your ac balance", fixed_amount - amt)
