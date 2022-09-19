employee=[
    [1,'anu','kochi','developer',67000,3],
    [2,'amal','calicut','tester',45000,2],
    [3,'arun','Trissur','developer',55000,3],
    [7, 'anaga', 'calicut', 'tester', 55000, 4],
    [4, 'vinay', 'kochi', 'Manager',78000, 2],
    [8, 'joy', 'Trissur', 'Hr', 50000, 3],
    [10, 'alan', 'calicut', 'tester', 57000, 4]
    ]
print(employee)
#create anew list with all employee names
employee_names=[]
for i in employee:
    employee_names.append(i[1])
print(employee_names)

#print the detils of employee whose location is kochi
for i in employee:
    if  i[2]=='kochi':
        print(i)

#print the names of employee who have less than  3 years of experience
for i in employee:
    if i[-1]<3:
        print(i[1])

#find maximum salary
max=0
for i in employee:
    if i[4]>max:
        max=i[4]
print(max)
