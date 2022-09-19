import re
f=open("phone.txt","r")
rule='[+][9][1][0-9]{10}'
for i in f:
    data=i.rstrip("\n")
    matcher=re.fullmatch(rule,data)
    if matcher is not None:
        print(data)

