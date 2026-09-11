from exo1 import imc
from exo2 import note
from exo3 import doghuman
from exo4 import pi
from exo5 import base210
from exo7 import immatri
from revision_ex1 import calc


def main():
    choice = int(
        input(
            "Choisissez le programme souhaité :\n\
        - 1 : IMC\n\
        - 2 : Note\n\
        - 3 : DogHuman\n\
        - 4 : Pi\n\
        - 5 : Base210\n\
        - 6 : IMMA\n\
        - 7 : Cacl\n"
        )
    )

    while True:
        if 0 <= choice <= 8:
            break
        choice = int(
            input("Programme Incorrecte !!\n Veuillez choisir un programme correcte : ")
        )
    match choice:
        case 1:
            imc()
        case 2:
            note()
        case 3:
            doghuman()
        case 4:
            pi()
        case 5:
            base210()
        case 6:
            immatri()
        case 7:
            calc()
    return 0


if __name__ == "__main__":
    main()
