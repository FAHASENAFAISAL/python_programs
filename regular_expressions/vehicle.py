#car number validation
#KL23AS3789
import re
num=input("Enter your car number: ")
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
matcher=re.fullmatch(rule,num)
if matcher is not None:
    print("Valid")
else:
    print("Not valid")