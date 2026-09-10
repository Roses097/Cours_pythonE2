ope = str(
    input("Choisissez votre opération : \n(a)ddition\n(s)oustraction\n(m)ultiplication\n(d)ivision"))

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

result = eval(x + signe + y)
print(result)
