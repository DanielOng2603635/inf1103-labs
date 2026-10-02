# Github at https://github.com/DanielOng2603635/inf1103-labs

FILENAME = "inventory.txt"

# Initalizing counters
stock = 0
processed = 0
failed = 0

def load_inventory():
    # Read the saved total from the inventory file.
    # If the file does not exist, start with an empty inventory.
    try:
        with open(FILENAME, "r") as file:
            lines = file.read().splitlines()
        total = 0
        if len(lines) > 0 and lines[0].strip() != "":
            total = int(lines[0])
        print("Loaded saved inventory: " + str(total))
        return total
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
        return 0

def get_valid_input():
    stock = input("Enter a stock quantity:")

    # Check if user inputs quit
    if stock == "quit":
        print("Exiting program.")
        return "quit"

    # Integer check
    elif stock.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
        return "error"

    else:
        stock = int(stock)
        # Negative check
        if stock < 0:
            print("Please enter a non-negative number.")
            return "error"
        else:
            return stock

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount/10

def generate_report(total_units, failed_attempts):
    print("----------------------------------------------")
    print("Total Units Processed: " + str(total_units))
    print("Total Failed Entries: " + str(failed_attempts))
    print("----------------------------------------------")

# Load the previous inventory at the start of the program
inventory = load_inventory()
print("----------------------------------------------")

while stock != "quit":
    stock = get_valid_input()
    if isinstance(stock, int) == True:
        inventory = process_delivery(inventory, stock)
        processed += 1
        tax = calculate_tax(stock)
        print("The tax is " + str(tax))
        print("The current inventory is at " + str(inventory))
    elif stock == "error":
        failed += 1
    print("----------------------------------------------")

generate_report(processed, failed)