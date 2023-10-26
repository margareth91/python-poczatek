class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_line_price(self):
        return self.quantity * self.product.price

    def print_self(self):
        self.product.print_self()
        print(f"\t\t x {self.quantity}")
