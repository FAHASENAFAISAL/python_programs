#String start and end with special min 5 max 10
# @1234*->valid @123*-->valid @1ADggh23*-->valid
# import  re
# string=input("Enter a string: ")
# rule='\W[\w]{3,8}\W'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("Valid")
# else:
#     print("Not valid")

#start with one lowercase or specail character then numbers
# a56778-->valid $567890-->vaid a@12344-->invalid
import  re
string=input("Enter a string: ")
rule='[a-z\W]\d+'
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("Valid")
else:
    print("Not valid")