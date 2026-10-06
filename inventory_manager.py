# Github at https://github.com/DanielOng2603635/inf1103-labs

def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def format_price(price):
    return "$" + format(price, ".2f")


def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    if len(inventory) == 0:
        print("(no products yet)")
    for product in inventory:
        print("ID: " + product["id"]
              + " | Name: " + product["name"]
              + " | Price: " + format_price(product["price"])
              + " | Stock: " + str(product["stock"]))
    print("------------------------------------------------")


def search_product(inventory, product_id):
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product
    return None


def add_product(inventory, product_id, name, price, stock):
    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    return new_product


def update_stock(product, new_stock):
    product["stock"] = new_stock


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
    if stock.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
        return None
    stock = int(stock)
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
    if search_product(inventory, product_id) != None:
        print("Product ID " + product_id + " already exists.")
        return

    name = input("Product Name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return

    price = get_valid_price("Price: ")
    if price == None:
        return

    stock = get_valid_stock("Stock Quantity: ")
    if stock == None:
        return

    add_product(inventory, product_id, name, price, stock)
    print("Product added successfully!")


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = search_product(inventory, product_id)
    if product == None:
        print("Product not found.")
        return

    print("Product Found:")
    print("Name: " + product["name"])
    print("Current Stock: " + str(product["stock"]))

    new_stock = get_valid_stock("New Stock Quantity: ")
    if new_stock == None:
        return

    update_stock(product, new_stock)
    print("Stock updated successfully!")


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = search_product(inventory, product_id)
    if product == None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    print("ID: " + product["id"])
    print("Name: " + product["name"])
    print("Price: " + format_price(product["price"]))
    print("Stock: " + str(product["stock"]))
    print("------------------------------------------------")


# Main program
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

# Putting in placeholder inventory
inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

show_menu()

while True:
    option = input("Enter option: ").strip()

    if option == "1":
        display_all(inventory)
    elif option == "2":
        handle_add(inventory)
    elif option == "3":
        handle_update(inventory)
    elif option == "4":
        handle_search(inventory)
    elif option == "5":
        print("Save feature not available yet.")
    elif option == "6":
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 6.")