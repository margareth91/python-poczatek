import random
from . import Products


class Order:

    def __init__(self, buyer_first_last_name, total_price, products_list=None):
        self.buyer_first_last_name = buyer_first_last_name

        if products_list is None:
            products_list = []
        self.products_list = products_list

        # total_price = 0
        # for product in products_list:
        #     total_price += product.price
        self.total_price = total_price


def print_order(order):
    print("Lista zamowien w sklepie:")
    print("Zamowienie:")
    print(f"dane kupujacego: {order.buyer_first_last_name},")
    print(f"nazwy kupionych produktow: {order.products_list},")
    print(f"laczna cena produktow: {order.total_price}")


def orders():
    order1 = Order("Jan Kowalski", 24.5, ['parowki', 'bulki', 'ser cheddar'])
    print_order(order1)
    order2 = Order("Fiodus Miodus", 1.5, ['bulki'] )
    print_order(order2)
    order3 = Order("Dziosiaki Bobaki", 9.5, ['parowki', 'bulki'])
    print_order(order3)


# def random_orders():
#     number_of_products = random.randint(1, 5)
#     products_list = []
#     for product_number in range(number_of_products):
#         product_name = f"Product-{product_number}"
#         category_name = "Blabla"
#         price = random.randint(1, 40)
#         product_list = Products.Product(product_name, category_name, price)
#         # qty = random.randint(1, 10)
#         products_list.append(product_list)
#
#     order = Order(buyer_first_last_name="Dziob Aki", total_price=20, products_list=products_list)
#     return order
#
#
# def random_order():
#     first_order = random_orders()
#     print_order(first_order)
#     second_order = random_orders()
#     print_order(second_order)
