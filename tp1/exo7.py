from random import *

notAlloweds = "IOU"
# Ox41 = 65 = A
# 0x5A = 90 = Z


def immatri():
    letters = []
    numbers = []
    imma = ""
    numb = ""

    for _ in range(3):
        numbers += str(randint(0, 9))

    numb = "".join(numbers)

    for i in range(1):
        for j in range(2):
            letter = ""
            while True:
                lett = chr(randint(65, 90))
                if lett not in notAlloweds:
                    pass
                print(lett)
                lett += chr(randint(65, 90))

                if lett not in notAlloweds:
                    print(f"lett is : {lett}")
                    letter += lett
                    break
            letters.append(letter.upper())
            # print(letters)

        imma += letters[i].join("")
        # print(imma)

    imma = letters[0] + "-" + numb + "-" + letters[1]
    print(f"voici votre plaque d'immatriculation : {imma}")
