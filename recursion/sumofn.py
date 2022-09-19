# sum of n
def sumofn(n):
    if n==1:
        return n
    else:
        return n+sumofn(n-1)
print(sumofn(9))

