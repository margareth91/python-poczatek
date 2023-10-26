
class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


def print_product(product):
    print(f"Produkt dostepny w sklepie: {product.name}; kategoria: {product.category}, cena jednostkowa: {product.price}")


def products():
    print("Rodzaje produktow dostepne w sklepie:")
    product1 = Product("parowki", "spozywcze", 8)
    print_product(product1)
    product2 = Product("bulki", "spozywcze", 1.5)
    print_product(product2)
    product3 = Product("ser cheddar", "spozywcze", 15)
    print_product(product3)
