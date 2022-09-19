#regular expressions
# import re
# matcher=re.finditer('ab','abaabbbbbbbabbbbab')
# count=0
# for i in matcher:
#     print(i.group()) #to know the matched group
#     print(i.start()) #to know matching started
#     count+=1
# print(count)

#basic rules
#first rule '[abc]'
import re
rule='[abc]'
matcher=re.finditer(rule,'ABC abcd @123')
count=0
for i in matcher:
    print(i.group())
    print(i.start())
    count+=1
print("toatal count",count)

#second rule '[^abc]'
# import re
# rule='[^abc]'
# matcher=re.finditer(rule,'ABC abcd @123')
# count=0
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count+=1
# print("total count",count)

#third rule '[a-z]'
import re
rule='[a-z]'
matcher=re.finditer(rule,'ABC abcd @123')
count=0
for i in matcher:
    print(i.group())
    print(i.start())
    count+=1
print("total count",count)

#combination of two rules
import re
rule='[\s\d]'
matcher=re.finditer(rule,'ABC abcd @123')
count=0
for i in matcher:
    print(i.group())
    print(i.start())
    count+=1
print("total count",count)

#quantifiers-->for set limit
rule='a+' #'[abc]+'
matcher=re.finditer(rule,'aaaaa abc aaa abca@123')
count=0
for i in matcher:
    print(i.group())
    print(i.start())
    count+=1
print("total count",count)

rule='a*' #'[abc]*'
matcher=re.finditer(rule,'aaaaa abc aaa abca@123')
count=0
for i in matcher:
    print(i.group())
    print(i.start())
    count+=1
print("total count",count)