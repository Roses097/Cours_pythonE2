list = []
while True:
    n = int(input("Saisissez un nombre entier : "))
    if n < 0:
        break
    list += [n]


for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]


print("Voici votre liste de nombres en ordre croissant :", list)
print("Voici le maximum :", max(list))
print("Voici le minimum :", min(list))
print("Voici la moyenne :", sum(list) / len(list))
