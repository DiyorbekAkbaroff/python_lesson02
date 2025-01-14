number = int(input("sonnni kiriting: "))

for i in range(2, number+1):
    count = 0
    for j in range(2, i):
        if i != 2 and i % j == 0:
            count+=1
    if count == 0:
        print("tub son: ", i)
