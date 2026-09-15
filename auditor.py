inventory = 0
stock = 0

while stock != "quit" and inventory < 500:
    stock = input("Enter a stock quantity:")
    if stock == "quit":
        print("Exiting program.")
        break
    elif stock.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
    else:
        stock = int(stock)
        if stock < 0:
            print("Please enter a non-negative number.")
        else:
            inventory += stock
            print("The current inventory is at " + str(inventory))
    print("----------------------------------------------")


if inventory > 500:
    print("The current inventory is overstocked. Exiting program.")
