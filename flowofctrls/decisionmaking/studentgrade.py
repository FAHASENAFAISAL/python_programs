score=int(input("Enter your score out of 100: "))
if score>100:
    print("Invalid")
elif score>=90:
    print("A+")
elif score>=80:
    print("A")
elif score>=70:
    print("B+")
elif score>=60:
    print("B")
elif score>=50:
    print("C+")
elif score>0:
    print("Fail")
else:
    print("Invalid")
