
import random
from products import Product
from order_element import OrderElement


class Order:

    def __init__(self, buyer_first_last_name, order_elements=None):
        self.buyer_first_last_name = buyer_first_last_name

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for order_element in self.order_elements:
            total_price += order_element.total_line_price()
        return total_price

    def __str__(self):
        mark_line = "-" * 20
        order = "Zamowienie:"
        buyer = f"Dane kupujacego: {self.buyer_first_last_name}"
        ordered = "zamowione produkty"
        value_total = f"o lacznej cenie produktow: {self.total_price}:"
        for order_element in self.order_elements:
            product_details = f"\t{order_element}\n"

        result = "\n".join([mark_line, order, buyer, ordered, value_total, product_details, mark_line])
        return result

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self.order_elements) != len(other.order_elements):
            return False

        if self.buyer_first_last_name != other.buyer_first_last_name:
            return False

        for order_element in self.order_elements:
            if order_element not in other.order_elements:
                return False
        return True


def random_orders():
    number_of_products = random.randint(1, 5)
    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Produkt-{product_number}"
        category_name = "Blablabla"
        price = random.randint(1, 50)
        product = Product(product_name, category_name, price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))

    order = Order(buyer_first_last_name="Fiodus Miodus", order_elements=order_elements)
    return order
