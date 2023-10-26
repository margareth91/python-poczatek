import random
from .products import Product
from .order_element import OrderElement


class Order:

    # def __init__(self, buyer_first_last_name, products=None):
    #     self.buyer_first_last_name = buyer_first_last_name
    #
    #     if products is None:
    #         products = []
    #     self.products = products
    #
    #     total_price = 0
    #     for product in products:
    #         total_price += product.price
    #     self.total_price = total_price

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

    # def print_order(self):
    #     print("=" * 20)
    #     print("Zamowienie:")
    #     print(f"dane kupujacego: {self.buyer_first_last_name},")
    #     print(f"zakupione produkty:")
    #     for product in self.products:
    #         print("\t", end="")
    #         product.print_product()
    #     print(f"laczna cena produktow: {self.total_price}")
    #     print("=" * 20)

    def print_self(self):
        print("=" * 20)
        print("Zamowienie:")
        print(f"dane kupujacego: {self.buyer_first_last_name}",)
        print("zamowione produkty:")
        for order_element in self.order_elements:
            print("\t", end="")
            order_element.print_self()
        print(f"laczna cena produktow: {self.total_price}")
        print("=" * 20)


# def orders():
#     order1 = Order("Jan Kowalski", ['parowki', 'bulki', 'ser cheddar'])
#     order1.print_order()
#     order2 = Order("Fiodus Miodus", ['bulki'])
#     order2.print_order()
#     order3 = Order("Dziosiaki Bobaki", ['parowki', 'bulki'])
#     order3.print_order()
#
#
# orders()


# def random_orders():
#     number_of_products = random.randint(1, 5)
#     products = []
#     for product_number in range(number_of_products):
#         product_name = f"Product-{product_number}"
#         category_name = "Blabla"
#         price = random.randint(1, 40)
#         product = Product(product_name, category_name, price)
#         # qty = random.randint(1, 10)
#         products.append(product)
#
#     order = Order(buyer_first_last_name="Dziob Aki", products=products)
#     return order


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
