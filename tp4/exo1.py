class Product:
    
    def __init__(self,code : str, name : str, priceET : int):
        self.code = code
        self.name = name
        self.priceET = priceET
        
    def get_price_it(self, tax : float = 0.2):
        return self.priceET * (1 + tax)
        

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

