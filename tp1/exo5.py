def base210():
    base2 = ""
    while True:
        try:
            base10 = int(input("Saisisser un nombre entier"))
            if base10 < 0:
                print("Veuillez saisir un nombre positif ")
            else:
                break
        except ValueError:
            print("Veuillez saisir un nombre entier positif ")

    while True:
        r = base10 % 2
        base2 += str(r)
        if r == 1:
            base10 -= 1

        base10 = base10 // 2

        if base10 == 0:
            break

    base2 = base2[::-1]
    print("Voici votre nombre en base binaire : ", base2)
