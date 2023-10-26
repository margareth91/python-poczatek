
class Apple:

    def __init__(self, species_name, size, price_for_kg):
        self.species_name = species_name
        self.size = size
        self.price_for_kg = price_for_kg

    def print_self(self):
        print(f"Jablka: odmiana: {self.species_name}; rozmiar: {self.size}; cena za kg: {self.price_for_kg}")

    def price_apples(self, qty):
        return self.price_for_kg * qty


def apples():
    print("Rodzaje jablek dostepne w sklepie:")
    apple1 = Apple("jonagold", "duze", 4.5)
    apple1.print_self()
    apple2 = Apple("papierowka", "male", 3)
    apple2.print_self()
    apple3 = Apple("szara reneta", "srednio duze", 3.5)
    apple3.print_self()


# apples()
