
class Potato:

    def __init__(self, species_name, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.species_name = species_name

    def print_self(self):
        print(f"Ziemniaki: odmiana: {self.species_name}; rozmiar: {self.size}; cena za kg: {self.price_for_kg}")

    def price_potatoes(self, qty):
        return self.price_for_kg * qty


def potatoes():
    print("Rodzaje ziemniakow dostepne w sklepie:")
    potato1 = Potato("na frytki", "duze", 5.5)
    potato1.print_self()
    potato2 = Potato("na puree", "male", 4)
    potato2.print_self()
    potato3 = Potato("salatkowe", "srednie", 4.5)
    potato3.print_self()


# potatoes()
