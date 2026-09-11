#     FORMAT FIXE A 15
def pi15():
    piResult = 3
    for i in range(1, 16):
        print(f"Voici le resultat de pi a {i} = {piResult:.{i}f} ")
        piResult += (-1) ** (i + 1) * (4 / ((2 * i) * (i * 2 + 1) * (i * 2 + 2)))
    return piResult


#     FORMAT FLEXIBLE
def pin(n):
    piResult = 3
    for i in range(1, n + 1):
        print(f"Voici le resultat de pi a {i} = {piResult:.{i}f} ")
        piResult += (-1) ** (i + 1) * (4 / ((2 * i) * (i * 2 + 1) * (i * 2 + 2)))
    return piResult


def pi():
    while True:
        try:
            n = int(input("Saisissez l'approximation voulus : "))
            if n < 0:
                print("Veuillez saisir un nombre positif ")
            else:
                break
        except ValueError:
            print("Veuillez saisir un nombre entier positif ")

    print(pin(n))
