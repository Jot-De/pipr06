from typing import List
from .price import Price

BARCODE_LENGTH = 13

BARCODE_LENGTH = 13


class Item:
    def __init__(self, name, price: Price, barcode: str = "1234567890123"):
        if not name:
            raise ValueError("Name cannot be empty")
        #ADD MORE HERE
        # HINT barcode must be valid and have 13 digits 
        if type(barcode) is not str:
            raise TypeError('Barcode must be string')
        if len(barcode) != 13:
            raise ValueError('Barcode must be 13 digits long.')

        self._name = name
        #ADD MORE HERE
        self._price = price
        self._barcode = barcode

    @property
    def name(self):
        #This method is already done
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def barcode(self):
        return self._barcode

    def __str__(self) -> str:
        description = f"Item's name: {self.name} (price: {self.price})."
        return description

    def __repr__(self) -> str:
        info = f'Name: {self.name}, price: {self.price}, barcode: {self.barcode}.'
        return info


def random_item() -> Item:
    """Generate a random item"""
    


def generate_items(num_items: int) -> List[Item]:
    """Generates a given number of random items"""
