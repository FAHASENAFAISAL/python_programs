#print student name from student.txt only first letter is 'a'
f=open("student.txt",'r')
for i in f:
    data = i.rstrip("\n")
    if i[0]=='a':
        print(data)