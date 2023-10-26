

class Potato:

    def __init__(self, species_name, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.species_name = species_name

    def price_potatoes(self, qty):
        return self.price_for_kg * qty

    def __repr__(self):
        return f"<Potato species name='{self.species_name}', size='{self.size}', price_for_kg='{self.price_for_kg}'>"
