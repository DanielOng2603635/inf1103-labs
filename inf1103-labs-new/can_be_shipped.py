# Github at https://github.com/DanielOng2603635/inf1103-labs

from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    # Interface for anything that can be shipped

    @abstractmethod
    def calculate_shipping_cost(self):
        pass
