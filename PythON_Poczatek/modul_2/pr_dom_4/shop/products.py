class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Produkt dostepny w sklepie: {self.name}; kategoria: {self.category}, cena jednostkowa: {self.price}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.price == other.price)
