#postive and negative in separate sets
s={1,4,-5,3,6,7,-9,-7,-55}
pos=set()
neg=set()
for i in s:
    if i<0:
        neg.add(i)
    else:
        pos.add(i)
print(pos,neg)