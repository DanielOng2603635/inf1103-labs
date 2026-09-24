# Github at https://github.com/DanielOng2603635/inf1103-labs

# Initalizing inventory and stock
inventory = 0
stock = 0
processed = 0
failed = 0

def get_valid_input():
    stock = 0
    # Start user input loop
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
        # Convert to integer if valid
        stock = int(stock)

        # Negative check
        if stock < 0:
            print("Please enter a non-negative number.")
            return "error"
        else:
            # Add to inventory
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

while stock != "quit":
    stock = get_valid_input()
    # Add to inventory
    if isinstance(stock,int) == True:
        inventory = process_delivery(inventory,stock)
        processed += 1
        tax = calculate_tax(stock)
        print("The tax is " + str(tax))
        print("The current inventory is at " + str(inventory))
    else:
        failed += 1
    print("----------------------------------------------")

generate_report(processed,failed)
