matn = input("Matn kiriting: ")

natija = ""
sanash = 1

for i in range(1, len(matn)):
    if matn[i] == matn[i - 1]:
        sanash += 1
    else:
        natija += matn[i - 1] + str(sanash)
        sanash = 1

natija += matn[-1] + str(sanash)

print(natija)