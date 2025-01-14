a = input("Matn kiriting: ")
text = a.split()

uzun = max(text, key=len)
print(uzun)
