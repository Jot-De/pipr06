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

        self._name = name
        #ADD MORE HERE

    @property
    def name(self):
        #This method is already done
        return self._name

    @property
    def price(self):
        pass

    @property
    def barcode(self):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


def random_item() -> Item:
    """Generate a random item"""


def generate_items(num_items: int) -> List[Item]:
    """Generates a given number of random items"""
