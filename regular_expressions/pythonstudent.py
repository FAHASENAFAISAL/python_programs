import  re
f1=open("register.txt","r")
f2=open("pythonreg.txt","w")
rule='[P][Y]\d{4}'
for i in f1:
    data=i.rstrip("\n")
    matcher=re.fullmatch(rule,data)
    if matcher is not None:
        f2.write(i)