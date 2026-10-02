# Github at https://github.com/DanielOng2603635/inf1103-labs

FILENAME = "inventory.txt"

# Initalizing counters
stock = 0
processed = 0
failed = 0

def load_inventory():
    # Read the saved total (line 1) and history (line 2) from the file.
    # If the file does not exist, start with an empty inventory.
    try:
        with open(FILENAME, "r") as file:
            lines = file.read().splitlines()
        total = 0
        history = []
        if len(lines) > 0 and lines[0].strip() != "":
            total = int(lines[0])
        if len(lines) > 1 and lines[1].strip() != "":
            for value in lines[1].split(","):
                history.append(int(value))
        print("Loaded saved inventory: " + str(total))
        print("Loaded transaction history: " + str(history))
        return total, history
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
        return 0, []

def save_inventory(total, history):
    # Write the final total on line 1 and the history on line 2.
    with open(FILENAME, "w") as file:
        file.write(str(total) + "\n")
        history_text = []
        for value in history:
            history_text.append(str(value))
        file.write(",".join(history_text) + "\n")
    print("Inventory successfully saved to " + FILENAME)

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

# Load the previous inventory and history at the start of the program
inventory, history = load_inventory()
print("----------------------------------------------")

while stock != "quit":
    stock = get_valid_input()
    if isinstance(stock, int) == True:
        inventory = process_delivery(inventory, stock)
        history.append(stock)          # record every valid transaction
        processed += 1
        tax = calculate_tax(stock)
        print("The tax is " + str(tax))
        print("The current inventory is at " + str(inventory))
        print("Transaction history: " + str(history))
    elif stock == "error":
        failed += 1
    print("----------------------------------------------")

generate_report(processed, failed)

# Write-back: save the final total and history when the user quits
save_inventory(inventory, history)
print("Final inventory: " + str(inventory))
print("Transaction history: " + str(history))