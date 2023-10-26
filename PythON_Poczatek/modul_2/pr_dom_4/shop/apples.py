

class Apple:

    def __init__(self, species_name, size, price_for_kg):
        self.species_name = species_name
        self.size = size
        self.price_for_kg = price_for_kg

    def price_apples(self, qty):
        return self.price_for_kg * qty

    def __repr__(self):
        return f"<Apple species name='{self.species_name}', size='{self.size}', price_for_kg='{self.price_for_kg}'>"
