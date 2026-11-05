# Github at https://github.com/DanielOng2603635/inf1103-labs

from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    # A product that is stored and shipped.
    # Inherits from one class (Product) and implements one interface (CanBeShipped).

    # Shipping rule: flat fee per item plus a charge per kg
    BASE_SHIPPING_FEE = 5.00
    COST_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock, weight):
        # Reuse the Product constructor for the common attributes
        super().__init__(product_id, name, price, stock)

        weight = float(weight)
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        self.__weight = weight  # in kg

    def get_weight(self):
        return self.__weight

    def display_information(self):
        # Parent prints the common information, child adds the weight
        super().display_information()
        print("    Type: Physical | Weight: " + format(self.__weight, ".2f") + " kg")

    def get_fulfilment_info(self):
        return ("Requires physical shipping. Shipping cost: $"
                + format(self.calculate_shipping_cost(), ".2f"))

    def calculate_shipping_cost(self):
        return round(self.BASE_SHIPPING_FEE + self.COST_PER_KG * self.__weight, 2)
