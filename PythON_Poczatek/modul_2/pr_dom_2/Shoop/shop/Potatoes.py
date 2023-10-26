
class Potato:

    def __init__(self, species_name, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.species_name = species_name


def print_potato(potato):
    print(f"Ziemniaki: odmiana: {potato.species_name}; rozmiar: {potato.size}; cena za kg: {potato.price_for_kg}")


def potatoes():
    print("Rodzaje ziemniakow dostepne w sklepie:")
    potato1 = Potato("na frytki", "duze", 5.5)
    print_potato(potato1)
    potato2 = Potato("na puree", "male", 4)
    print_potato(potato2)
    potato3 = Potato("salatkowe", "srednie", 4.5)
    print_potato(potato3)
