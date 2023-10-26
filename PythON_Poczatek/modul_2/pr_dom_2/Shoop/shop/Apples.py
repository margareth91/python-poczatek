
class Apple:

    def __init__(self, species_name, size, price_for_kg):
        self.species_name = species_name
        self.size = size
        self.price_for_kg = price_for_kg


def print_apple(apple):
    print(f"Jablka: odmiana: {apple.species_name}; rozmiar: {apple.size}; cena za kg: {apple.price_for_kg}")


def apples():
    print("Rodzaje jablek dostepne w sklepie:")
    apple1 = Apple("jonagold", "duze", 4.5)
    print_apple(apple1)
    apple2 = Apple("papierowka", "male", 3)
    print_apple(apple2)
    apple3 = Apple("szara reneta", "srednio duze", 3.5)
    print_apple(apple3)

