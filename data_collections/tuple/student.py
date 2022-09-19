student=(("anu",1,45),("amal",2,32),("arun",3,50),("anaga",4,23))

#print student name above 40 mark
for i in student:
    if i[-1]>=40:
        print(i[0])
        
