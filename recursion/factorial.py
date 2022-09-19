def fact(n):
    if n==1:        #if n==0
        return n    #return n
    else:
        return n*fact(n-1)
print(fact(4))