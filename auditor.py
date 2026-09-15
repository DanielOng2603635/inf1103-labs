inventory = 0
stock = 0

while stock != "quit":
    stock = input("Enter a stock quantity:")
    if stock == "quit":
        break
    elif stock.lstrip("-").isdigit() == False:
        print("Please enter a valid integer.")
    else:
        stock = int(stock)
        if stock < 0:
            print("Please enter a non-negative number.")
