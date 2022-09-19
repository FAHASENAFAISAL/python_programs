for i in range(5):
    if i==2:
        continue
    print(i)
print("outside loop")

for i in range(5):
    for j in range(3):
        if j==2:
            break
        else:
            print(i,j)
    print("last")