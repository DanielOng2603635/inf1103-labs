# Github at https://github.com/DanielOng2603635/inf1103-labs


class Product:
    # A single product in the store

    def __init__(self, product_id, name, price, stock):
        self.__product_id = str(product_id)
        self.__name = str(name)

        price = float(price)
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.__price = price

        # Stock goes through update_stock() so the same rules apply
        # when a product is created as when its stock is changed later.
        self.__stock = 0
        self.update_stock(stock)

    # ---------- Getters (read-only access to the private attributes) ----------

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # ---------- Behaviour ----------

    def update_stock(self, quantity):
        # Set the stock to a new quantity

        if not isinstance(quantity, int):
            raise ValueError("Stock must be a whole number.")
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print("ID: " + self.__product_id
              + " | Name: " + self.__name
              + " | Price: $" + format(self.__price, ".2f")
              + " | Stock: " + str(self.__stock))
