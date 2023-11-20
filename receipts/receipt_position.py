from .item import Item
from .price import Price
from typing import List

class ReceiptPosition:
    def __init__(self, amount: float, item: Item):
        if amount <= 0:
            raise ValueError("Amount cannot be negative")
        self._amount = amount
        #Add more here

    @property
    def amount(self):
        # already done
        return self._amount
    
    @property
    def item(self):
       pass

    @property
    def total_price(self) -> Price:
        pass

    def __lt__(self, other: "ReceiptPosition"):
        # HINT this should allow sorting ReceiptPositions by their total price
        # HINT https://docs.python.org/3/library/operator.html
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def _format_position(self):
        # FIXME this is hacky but simple and not super important
        result = (
            f"{self.item.name:<20}"
            f"{self.amount:<5} * {str(self.item.price):<9} | "
            f"{str(self.total_price):>10}"
        )
        result += "\n"
        return result


def random_position() -> ReceiptPosition:
    """Generates a random receipt position"""


def generate_positions(num_positions: int) -> List[ReceiptPosition]:
    """Generates a given number of random fake receipt positions"""
