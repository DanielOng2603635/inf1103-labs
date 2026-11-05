# Github at https://github.com/DanielOng2603635/inf1103-labs

from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    # Interface: any class that can be shipped must implement these methods.
    # No attributes or shipping details here, it is only the contract.

    @abstractmethod
    def calculate_shipping_cost(self):
        # Return the cost of shipping this item
        pass
