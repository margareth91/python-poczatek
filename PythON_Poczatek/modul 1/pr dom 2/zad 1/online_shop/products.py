
products = {
    "chleb": {
        "price": 9.90,
        "qty": 50
    },
    "bulki": {
        "price": 1.50,
        "qty": 200
    },
    "drozdzowki": {
        "price": 3,
        "qty": 75
     }
}


def update_product_qty(product_name, ordered_qty):
    products[product_name]["qty"] -= ordered_qty