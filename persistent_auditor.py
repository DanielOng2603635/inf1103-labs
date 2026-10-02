# Github at https://github.com/DanielOng2603635/inf1103-labs

FILENAME = "inventory.txt"
STARTING_ID = 1001

# Initalizing counters
processed = 0
failed = 0

def load_inventory():
    # Read every saved order from the file into a list.
    # Each order is a list: [order_id, product_name, quantity]
    # If the file does not exist, start with an empty inventory.
    orders = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                order_id = int(parts[0].strip())
                product = parts[1].strip()
                quantity = int(parts[2].strip())
                orders.append([order_id, product, quantity])
    except FileNotFoundError:
        print("No orders file found. Starting with an empty inventory.")
    return orders

def save_inventory(orders):
    with open(FILENAME, "w") as file:
        for order in orders:
            file.write(str(order[0]) + "," + order[1] + "," + str(order[2]) + "\n")

def show_orders(orders):
    print("Current Orders:")
    print()
    if len(orders) == 0:
        print("(no orders yet)")
    for order in orders:
        print(str(order[0]) + ", " + order[1] + ", " + str(order[2]))
    print()

def get_next_id(orders):
    if len(orders) == 0:
        return STARTING_ID
    return orders[-1][0] + 1

def get_product_name():
    product = input("Enter Product Name: ").strip()

    # Check if user inputs quit
    if product.lower() == "quit":
        return "quit"

    if product == "" or "," in product:
        print("Please enter a valid product name (not empty, no commas).")
        return "error"

    return product

def get_valid_quantity():
    quantity = input("Enter Quantity: ").strip()

    if quantity.lower() == "quit":
        return "quit"

    # Integer check
    if quantity.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
        return "error"

    quantity = int(quantity)

    # Must be a positive number
    if quantity <= 0:
        print("Please enter a positive number.")
        return "error"

    return quantity

def add_order(orders, product, quantity):
    new_order = [get_next_id(orders), product, quantity]
    orders.append(new_order)
    return new_order

def generate_report(total_orders, failed_attempts):
    print("----------------------------------------------")
    print("Total Orders Added: " + str(total_orders))
    print("Total Failed Entries: " + str(failed_attempts))
    print("----------------------------------------------")

# Load the saved orders at the start of the program
orders = load_inventory()
show_orders(orders)

while True:
    product = get_product_name()
    if product == "quit":
        print("Exiting program.")
        break
    if product == "error":
        failed += 1
        print()
        continue

    quantity = get_valid_quantity()
    if quantity == "quit":
        print("Exiting program.")
        break
    if quantity == "error":
        failed += 1
        print()
        continue

    new_order = add_order(orders, product, quantity)
    processed += 1
    print()
    print("New Order Added:")
    print(str(new_order[0]) + "," + new_order[1] + "," + str(new_order[2]))
    print()

    # Save after every new order
    save_inventory(orders)
    print("Order successfully saved to " + FILENAME)
    print()

# Final save when the user quits
save_inventory(orders)
generate_report(processed, failed)