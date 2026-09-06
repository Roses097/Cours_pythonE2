

taille = eval(input("Entrez votre taille en mètres : "))
poids = eval(input("Entrez votre poids en kg : "))

print("Votre taille est de", taille, "mètres et votre poids est de", poids, "kg.")

imc = poids / (taille**2)
print(f"Votre IMC est de {imc:.2f}")
