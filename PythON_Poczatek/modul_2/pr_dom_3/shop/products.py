
class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def print_self(self):
        print(f"Produkt dostepny w sklepie: {self.name}; kategoria: {self.category}, cena jednostkowa: {self.price}")


def products():
    print("Rodzaje produktow dostepne w sklepie:")
    product1 = Product("parowki", "spozywcze", 8)
    product1.print_self()
    product2 = Product("bulki", "spozywcze", 1.5)
    product2.print_self()
    product3 = Product("ser cheddar", "spozywcze", 15)
    product3.print_self()


# products()
