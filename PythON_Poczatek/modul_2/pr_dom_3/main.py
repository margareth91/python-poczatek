from shop.orders import random_orders


def run_orders():
    first_order = random_orders()
    first_order.print_self()
    second_order = random_orders()
    second_order.print_self()


if __name__ == '__main__':
    run_orders()
