# Github at https://github.com/DanielOng2603635/inf1103-labs


class Inventory:
    # Collection of product objects.

    def __init__(self):
        self.__products = []  # list of product objects

    def add_product(self, product):
        # Add a product. Returns False if that product ID is already used.
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        # Return the product with this ID 
        product_id = product_id.strip().upper()
        for product in self.__products:
            if product.get_product_id().upper() == product_id:
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        if len(self.__products) == 0:
            print("(no products yet)")
        for product in self.__products:
            product.display_information()
        print("------------------------------------------------")

    def get_products(self):
        # Return a copy of the product list.
        return list(self.__products)
