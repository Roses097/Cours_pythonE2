from Fraction import *

# equal
a = Fraction(12, 18)  # 12/18
b = Fraction(34, 51)  # 34/51

# not equal
c = Fraction(47, 61)
d = Fraction(125, 150)


print(a == b)
print(a == c)
print(c == d)
print(a != d)
print(a + c)
print(a * b)
print(d / b)
print(c < d)
print(d > a)

print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
from Product import *

products = [
    Product("A101", "Laptop", 800),
    Product("A102", "Smartphone", 599.90),
    Product("A103", "Tablet", 349),
    Product("B201", "Mouse", 19.90),
    Product("B202", "Keyboard", 49.99),
    Product("B203", "Headphones", 79.50),
    Product("C301", "Monitor", 250),
    Product("C302", "Webcam", 45),
    Product("C303", "USB Cable", 7.95),
    Product("D401", "External Hard Drive", 89.99),
]

for produc in products:
    print(f"{produc.code} - {produc.name} - {produc.get_price_it():.2f}")

print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
print("\n\n\n")
print("\n\n\n")


from exo3 import *

colors = []
for i in range(4):
    colors.append(CardColor(shades[i], shade_names[i], foreground_colors[i], Back.WHITE))

values = []
for i in range(13):
    values.append(CardValue(value_txts[i], value_points[i]))

deck = []
for color in colors:
    for value in values:
        deck.append(Card(value, color))

for card in deck:
    print(card, end=" ")
print()
print(len(deck))   # 52