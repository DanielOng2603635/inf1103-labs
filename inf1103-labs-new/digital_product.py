# Github at https://github.com/DanielOng2603635/inf1103-labs

from product import Product


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print("    Download Size: " + str(self.__download_size) + " MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally through a download link."
