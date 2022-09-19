#student={} #empty dictionary
#another method-->student=dict()
student=dict()
print(student)
print(type(student))

#adding-->method 1
student.update({"name":"anu","place":"kochi"}) # at a time can possible for couple of elements

#method 2
student["age"]=23 # at a time only one
student["age"]=24 #values can update but key can't
print(student)