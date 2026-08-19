import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "orders.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def get_order(order_id):
    data = load_data()

    for order in data["orders"]:
        if order["order_id"] == order_id:
            return order

    return None


def get_product(product_id):
    data = load_data()

    for product in data["products"]:
        if product["product_id"] == product_id:
            return product

    return None


def add_return(order_id):
    data = load_data()

    for order in data["orders"]:
        if order["order_id"] == order_id:

            if not order["return_eligible"]:
                return False, "Order is not eligible for return."

            for existing_return in data["returns"]:
                if existing_return["order_id"] == order_id:
                    return False, "Return already initiated for this order."

            data["returns"].append({
                "order_id": order_id,
                "status": "Return Initiated"
            })

            save_data(data)

            return True, "Return initiated successfully."

    return False, "Order not found."