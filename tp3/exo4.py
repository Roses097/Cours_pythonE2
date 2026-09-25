from random import *


falseLetter = []
trueLetter = []
health = ["♥", "♥", "♥"]

with open("dic.txt", "r") as f:
    lines = f.readlines()
    word = lines[randint(0, len(lines))].strip().upper()
    taille = len(word)


worldRev = [word[0]]

for letters in word[1:]:
    if letters == "-":
        worldRev.append("-")
    worldRev.append("_")
letterGuessed = []

print("\033[H\033[J")  # clear terminal command linux/mac
healthState = True

while "_" in worldRev or not healthState:
    print(worldRev)
    print(f"{word}\n")
    print(f"Lettres deja essayer : {set(letterGuessed)}")

    letterGuess = input("\nSaisissez une Lettre : ")

    while len(letterGuess) != 1 or not letterGuess.isalpha():
        letterGuess = input("\nVeuillez saisir UNE seule LETTRE : ")

    letterGuessed += letterGuess

    if letterGuess in word:
        for i, letters in enumerate(word):
            if letters == letterGuess:
                worldRev[i] = letterGuess
    else:
        print("hello")
        try:
            # print("\033[H\033[J")
            health.remove("♥")
            health.append("♡")
            print(f"\nYou lost a Life !\n{health}")
        except ValueError:
            health == ["♡", "♡", "♡"]
            healthState = False
            print("\033[H\033[J")
            print(health)
            print(f"\nYOU LOST")
            break


if healthState:
    print(f"\nGoodJob !! You found the word : {word}")
