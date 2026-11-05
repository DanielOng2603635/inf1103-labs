# Github at https://github.com/DanielOng2603635/inf1103-labs
#
# File Handling: loads and saves inventory data.

import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct


def load_inventory(inventory, filename):
    # Read products from a JSON file and add them to the given inventory.
    if not os.path.exists(filename):
        print(filename + " not found. Starting with an empty inventory.")
        return

    print(filename + " found.")
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Inventory file is damaged. Starting with an empty inventory.")
        return

    if not isinstance(data, list):
        print("Inventory file is damaged. Starting with an empty inventory.")
        return

    for item in data:
        # Turn each saved dictionary back into a product object
        # the type decides which class to use
        try:
            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
            elif item["type"] == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])
            else:
                print("Skipping a product with an unknown type.")
                continue
        except (KeyError, TypeError, ValueError):
            print("Skipping an invalid product entry in " + filename + ".")
            continue

        if not inventory.add_product(product):
            print("Skipping duplicate product ID " + product.get_product_id() + ".")

    print("Inventory loaded successfully.")


def save_inventory(inventory, filename):
    # Write every product in the inventory to a JSON file
    data = []
    for product in inventory.get_products():
        # Turn each product object into a dictionary JSON can store
        item = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }
        # Save the type and the extra info for that type
        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.get_weight()
        else:
            item["type"] = "digital"
            item["download_size"] = product.get_download_size()
        data.append(item)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
