# Github at https://github.com/DanielOng2603635/inf1103-labs

# Initalizing inventory and stock
inventory = 0
stock = 0
processed = 0
failed = 0

# Start user input loop
while stock != "quit" and inventory < 500:
    stock = input("Enter a stock quantity:")

    # Check if user inputs quit
    if stock == "quit":
        print("Exiting program.")
        break

    # Integer check
    elif stock.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
        failed += 1

    else:
        # Convert to integer if valid
        stock = int(stock)

        # Negative check
        if stock < 0:
            print("Please enter a non-negative number.")
            failed += 1
        else:
            # Add to inventory
            inventory += stock
            processed += 1
            print("The current inventory is at " + str(inventory))

    print("----------------------------------------------")

# Overstocked case
if inventory > 500:
    print("The current inventory is overstocked. Exiting program.")

# Normal quit case
else:
    print("Total Units Processed: " + str(processed))
    print("Total Failed Entries: " + str(failed))

print("----------------------------------------------")