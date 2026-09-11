from random import *

def cardMakes():
    cardValues = ["T","V","C","D","R","A",2,3,4,5,6,7,8,9]
    colors = ["♠","♣","♦","♥"]
    cards = []
    
    for color in colors:
        for values in cardValues:
            cards += [str(values) + color]
    return cards

def tour(n):
    cards = cardMakes()
    print(card)

    for i in range(n):
        card = (cards[randint(0,len(cards))])
        cards.remove(card)
        
        choice = input(" + ? - ?\n")
        newcard = card = (cards[randint(0,len(cards))])
        
        print(newcard)
        
        cards.remove(newcard)
        if card 


print(tour())