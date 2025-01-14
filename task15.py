num = input("Sonlani vergul bilan yozin : ")
numbers = num.split(',')

numbers = [int(son) for son in numbers]

for son in numbers:
    if son % 2 != 0 and son % 3 == 0:
        print(son)