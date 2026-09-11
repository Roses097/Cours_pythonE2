def calc():

    ope = str(
        input(
            "Choisissez votre opération : \n(a)ddition\n(s)oustraction\n(m)ultiplication\n(d)ivision"
        )
    )

    x = input("Saissiser un nombre x : ")
    y = input("Saissiser un nombre y : ")

    match ope:
        case "a":
            signe = "+"
        case "s":
            signe = "-"
        case "m":
            signe = "*"
        case "d":
            signe = "/"
            while true:
                if y != "0":
                    break
            y = input("Division impossible !!\n Choisisser un autre nombre : ")

    result = eval(x + signe + y)
    print(result)
    return 0
