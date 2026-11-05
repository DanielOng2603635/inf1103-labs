# Github at https://github.com/DanielOng2603635/inf1103-labs

from product import Product


class DigitalProduct(Product):
    # A product delivered by download. Does not implement CanBeShipped.

    def __init__(self, product_id, name, price, stock, download_size):
        # Reuse the Product constructor for the common attributes
        super().__init__(product_id, name, price, stock)

        download_size = float(download_size)
        if download_size <= 0:
            raise ValueError("Download size must be a positive number.")
        self.__download_size = download_size  # in MB

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        # Parent prints the common information, child adds the download size
        super().display_information()
        print("    Type: Digital | Download Size: " + format(self.__download_size, ".1f") + " MB")

    def get_fulfilment_info(self):
        return ("Delivered digitally by download ("
                + format(self.__download_size, ".1f") + " MB).")
