# Github at https://github.com/DanielOng2603635/inf1103-labs
# Main Program

from product import Product
from inventory import Inventory
from file_handler import load_inventory, save_inventory

FILENAME = "inventory.json"


def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def get_valid_price(prompt):
    price = input(prompt).strip()
    try:
        price = float(price)
    except ValueError:
        print("Please enter a valid number for price.")
        return None
    if price <= 0:
        print("Price must be a positive number.")
        return None
    return price


def get_valid_stock(prompt):
    stock = input(prompt).strip()
    # Integer check
    try:
        stock = int(stock)
    except ValueError:
        print("Please enter a valid integer.")
        return None
    # Stock cannot be negative
    if stock < 0:
        print("Stock cannot be negative.")
        return None
    return stock


def handle_add(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    if inventory.search_product(product_id) is not None:
        print("Product ID " + product_id + " already exists.")
        return

    name = input("Product Name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return

    price = get_valid_price("Price: ")
    if price is None:
        return

    stock = get_valid_stock("Stock Quantity: ")
    if stock is None:
        return

    # Create a Product object and hand it to the Inventory to store
    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("Product added successfully!")


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print("Name: " + product.get_name())
    print("Current Stock: " + str(product.get_stock()))

    new_stock = get_valid_stock("New Stock Quantity: ")
    if new_stock is None:
        return

    # The product updates its own stock 
    product.update_stock(new_stock)
    print("Stock updated successfully!")


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    # Create the Inventory object, then fill it from the saved file
    inventory = Inventory()
    load_inventory(inventory, FILENAME)
    show_menu()

    while True:
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()
        elif option == "2":
            handle_add(inventory)
        elif option == "3":
            handle_update(inventory)
        elif option == "4":
            handle_search(inventory)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory, FILENAME)
            print("Inventory saved successfully to " + FILENAME + ".")
        elif option == "6":
            # Final save when the user exits
            print("Saving inventory before exit...")
            save_inventory(inventory, FILENAME)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
