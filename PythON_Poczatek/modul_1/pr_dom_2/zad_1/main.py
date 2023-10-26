
from online_shop.sales_order import create_sales_order


def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Jaki artykul chcesz kupic? ")
    qty = int(input("Jaka ilosc chcesz kupic? "))

    result = create_sales_order(product_name, qty)
    if result is not None:
        total_price = result["total_price"]
        print(f"Laczny koszt wyniesie {total_price} zl.")


if __name__ == '__main__':
    run_shop()