s="hello hi hello"
data=s.split(" ")
print(data)

s="hello,hi,hello"
data=s.split(" ")
print(data)

s="hello,hi,hello"
data=s.split(",")
print(data)
print()

# qstn word count dict
s='hello hi hello'
#op-->{hello:2,hi:1}
word={}
data=s.split((" "))
print(data)
for i in data:
    if i not in word:
        word.update({i:1})
    else:
        val=word[i]
        val=val+1
        word.update({i:val})
print(word)