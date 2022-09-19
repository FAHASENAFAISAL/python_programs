#STRING
#lower case uppercase no special characters
#luminartechno-->valid Luminartechno-->valid luminar techno-->not valid
#always set quantifier other wise quantifier set as 1
# import  re
# string=input("Enter a string to validate: ")
# rule='[a-zA-Z]+'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("Valid")
# else:
#     print("Not valid")

#string can have lower,upper and numbers only
# import re
# string=input("Enter the string: ")
# rule='\w+'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("Not valid")

#string starts with number and then follow specail characters 123@#-->valid 4&-->valid 6-->not valid
# import  re
# string=input("Enter a string: ")
# rule='\d+\W+'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("Valid")
# else:
#     print("Not valid")

#string start with a and end with b abcb-->valid aihuyhguyhgvb-->valid
# import  re
# string=input("Enter a string: ")
# rule='^a[\w\W]*b$' #[\w\W]-->middle data *-->for if or not true
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("Valid")
# else:
#     print("Not valid")

#string start with 5 then upper case only total digit 6 5AFGRT-->valid
import  re
string=input("Enter a string: ")
rule='5[A-Z]{5}' #rule keeps order that is first 5 then A-z
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("Valid")
else:
    print("Not valid")
