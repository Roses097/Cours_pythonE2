def doghuman():
    while True:
        try:
            yearsHuman = int(input("Entrez votre age en annes humaines : "))
            if yearsHuman < 0:
                print("Veuillez entrer un age valide.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    if yearsHuman > 2:
        yearsDog = 2 * 10.5 + (yearsHuman - 2) * 4

    else:
        yearsDog = yearsHuman * 10.5

    print(f"Voici votre age en annees de chien :", yearsDog)
