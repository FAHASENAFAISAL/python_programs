#1. keep order
d={"name":"anu","place":"kochi"}
print(d)

# 2.heterogeneous
d={"name":"anu","place":"kochi",2:"hi","age":24}
print(d)

#3. value-->support duplication  key-->does not support duplication
d={"name":"anu","place":"kochi",2:"hi","age":24,1:"anu"} #value duplicate
d={"name":"anu","place":"kochi",2:"hi","age":24,"name":"anaga"} #key duplicate
#if do key duplication replace second one with first one anu-->anaga,so key must be unique
print(d)

#4 does not support indexing
#print(d[1])-->wrong
print(d["name"])
print(d["age"])#use key values

#5.support nesting
d={"name":"anu","place":"kochi",2:"hi","age":24,1:{1:2,3:5}}
#1:{1:2,3:5}-->elements can give only after mentioning key, here key is 1 and elements in{}
print(d)

#6. mutable

