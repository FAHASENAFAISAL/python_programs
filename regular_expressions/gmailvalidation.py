#mail validation
#name@gmail.com
import  re
mailid=input("Enter your mail id: ")
rule='[\w_]+@gmail.com' #_ that is _included symbols
matcher=re.fullmatch(rule,mailid)
if matcher is not None:
    print("Valid")
else:
    print("Not valid")