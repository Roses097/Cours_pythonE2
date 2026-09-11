def fizzbuzz():
    ans = []
    n = int(input("Nombre de tours : "))

    while n <= 0:
        n = int(
            input("Nombre incorrect !!\nVeuillez saisir un nombre entier positif : ")
        )

    for i in range(1, n + 1):
        a = ""
        if i % 3 == 0:
            a += "Fizz"
        if i % 5 == 0:
            a += "Buzz"
        if a == "":
            a = str(i)

        ans.append(a)

    print(ans)


fizzbuzz()
