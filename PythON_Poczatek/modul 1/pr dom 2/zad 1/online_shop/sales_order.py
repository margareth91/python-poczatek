
from online_shop.products import products, update_product_qty

orders = [
    {
        "product": "chleb",
        "quantity": 10,
        "total_price": 99.90
    }
]


def create_sales_order(product_name, qty):
    price = products[product_name]["price"]
    available_qty = products[product_name]["qty"]

    if available_qty < qty:
        print("Nie mamy tyle towaru!")
        return None

    total_price = qty * price
    new_order = {
        "product": product_name,
        "qty": qty,
        "total_price": total_price
    }
    update_product_qty(product_name, qty)
    orders.append(new_order)
    return new_order
