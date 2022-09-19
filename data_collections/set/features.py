#set
# 1. doe not keep order
s={6,5,4,3,2,1}
print(s)

#2.heterogeneous
s={6,5,4,3,2,1,'hi',9.8}
print(s)

#3 does not support duplication
s={6,5,4,3,2,1,'hi',9.8,1,2,3,True,False}
print(s)

#4 it is mutable data collection-that is updation is possible

#5. does not support indexing, bcz it is not store like linear wise in string
# bcz indexing is not support either slicing also does not support
s={1,2,3,4,5}
print(s[0])

#6. nesting is not possible in set
s={1,2,3,4,{2,3,4}} #-->not possible

