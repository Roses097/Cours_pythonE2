import collections
equa = collections.deque()


#1
def poly(equa, coeff):
    equa.insert(0,coeff)
    return equa


#2
def saisieEqua():
    poly = collections.deque()
    i = 0
    print(f"Saissisez le coefficient de degré {i}\n\
            Saisissez 'FIN' pour arrete ")
    while True:
        coeff = input(f"Degré {i} : ")
        if coeff == "FIN":
            break
        poly.append(int(coeff))
        i += 1
    poly.reverse()
    print(poly)
    return poly


#3
def displayPoly(poly):
    disp = []
    for i in range(len(poly)):
        coeff = poly[i]
        if coeff == 0:
            continue  
        if i == 0:
            disp.append(f"{coeff}")
        elif i == 1:
            disp.append(f"{coeff}x")
        else:
            disp.append(f"{coeff}x^{i}")
    result = " + ".join(disp)
    print(result)
    return result

#4
def popPoly(poly,indice):
    del poly[indice]
    return poly

#5
def addPoly(poly1, poly2):
    n = max(len(poly1), len(poly2))
    resultat = []
    for i in range(n):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        resultat.append(coeff1 + coeff2)
    return resultat


#6
def multPoly(poly,mono):
    coeff = 0
    degcoeff = 0
    for i in range(len(mono)):
        if mono[i] != 0:
            coeff = mono[i]
            degcoeff = i
            break
    result = [0] * degcoeff
    
    for coef in poly:
        result.append(coef * coeff)
    
    return result
            