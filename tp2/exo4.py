def calculScore(scores):
    final = []
    lastscore = []
    for i in range(len(scores)):
        if scores[i].isnumeric():
            final.append(int(scores[i]))
            lastscore = final
        if scores[i] == "D":
            final.append(final[-1] * 2)
        if scores[i] == "C":
            final.pop()
        if scores[i] == "+":
            final.append(final[-1] + final[-2])
    print(final)
    total = sum(final)
    print(total)
    return total


score = []
print("Pour quitter, entrez FIN")

while True:
    s = input("Entrer un score : ")
    if s == "FIN":
        break
    score.append(s)


calculScore(score)
