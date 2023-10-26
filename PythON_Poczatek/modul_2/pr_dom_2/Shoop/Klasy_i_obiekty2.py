
class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:

    def __init__(self, buyer_first_last_name, total_price, products_list=None):
        self.buyer_first_last_name = buyer_first_last_name
        self.total_price = total_price

        if products_list is None:
            products_list = []
        self.products_list = products_list


class Apple:

    def __init__(self, species_name, size, price_for_kg):
        self.species_name = species_name
        self.size = size
        self.price_for_kg = price_for_kg


class Potato:

    def __init__(self, species_name, size, price_for_kg):
        self.price_for_kg = price_for_kg
        self.size = size
        self.species_name = species_name


def print_product(product):
    print(f"Produkt dostepny w sklepie: {product.name}; kategoria: {product.category}, cena jednostkowa: {product.price}")


def products():
    print("Rodzaje produktow dostepne w sklepie:")
    product1 = Product("parowki", "spozywcze", 8)
    print_product(product1)
    product2 = Product("bulki", "spozywcze", 1.5)
    print_product(product2)
    product3 = Product("ser cheddar", "spozywcze", 15)
    print_product(product3)


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


def print_potato(potato):
    print(f"Ziemniaki: odmiana: {potato.species_name}; rozmiar: {potato.size}; cena za kg: {potato.price_for_kg}")


def potatoes():
    print("Rodzaje ziemniakow dostepne w sklepie:")
    potato1 = Potato("na frytki", "duze", 5.5)
    print_potato(potato1)
    potato2 = Potato("na puree", "male", 4)
    print_potato(potato2)
    potato3 = Potato("salatkowe", "srednie", 4.5)
    print_potato(potato3)


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


if __name__ == '__main__':
    products()
    apples()
    potatoes()
    orders()
