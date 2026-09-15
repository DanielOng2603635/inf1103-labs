inventory = 0
stock = 0
while stock != "quit":
    stock = input("Enter a stock quantity:")
    if stock == "quit":
        break
    elif stock.isdigit() == False:
        print("Please enter a valid integer.")
    else:
        stock = int(stock)
