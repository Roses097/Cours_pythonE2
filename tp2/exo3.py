from random import *

tableau = []
tableau += [randint(0,500) for _ in range(2,100)]

def verif(table):
    for i in range(len(table)):
        temp = table[i]
        for j in range(i+1, len(table)):
            if temp == table[j]:
                print("False")
                print(table)
                return False
    print("True")
    print(table)
    return True
    
verif(tableau)