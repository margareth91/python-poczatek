
from orders import Order
from order_element import OrderElement
from products import Product


def run_homework():
    ciabuk = Product(name="boba", category="buble", price=2.5)
    bable = Product(name="babu", category="bable", price=10)
    first_order_elements = [
        OrderElement(product=ciabuk, quantity=10),
        OrderElement(product=bable, quantity=20)
    ]
    second_order_elements = [
        OrderElement(product=bable, quantity=15),
        OrderElement(product=bable, quantity=100)
    ]

    first_order = Order(buyer_first_last_name="Ala Makota", order_elements=first_order_elements)
    second_order = Order(buyer_first_last_name="Ala Makota", order_elements=second_order_elements)

    if first_order == second_order:
        print("To dokladnie takie same zamowienia!")
    else:
        print("to dwa calkiem rozne zamowienia")


if __name__ == '__main__':
    run_homework()
