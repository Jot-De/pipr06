from datetime import datetime
from random import randint
from typing import List, Optional

from .item import Item
from .receipt_position import ReceiptPosition, generate_positions
from .price import Price
from datetime import datetime


class Receipt:
    # Already done
    def __init__(self, positions: list[ReceiptPosition] | None = None):
        self._positions = [] if positions is None else positions
        self._date = datetime.today()

    @property
    def date(self):
        # already done
        return self._date

    @property
    def positions(self):
        return self._positions

    @property
    def total_price(self) -> Price:
        # HINT try to use sum() built-in function here
        # HINT you can also use a list comprehension
        return sum([elem.total_price for elem in self._positions])

    def __iter__(self):
        # HINT this will allow you to write `for position in receipt:`
        # HINT you simply want to return the iterator over `positions`
        return self._positions.__iter__

    def __len__(self):
        # HINT this will allow you to write `len(receipt)`
        # HINT the length of the receipt is the number of positions
        return len(self._positions)

    def top_expensive_positions(self, num_positions=1):
        # HINT try sorting positions by their total price
        # HINT https://docs.python.org/3/howto/sorting.html
        sorted_positions = sorted(self._positions, key=ReceiptPosition.item.price.value_gr)
        return sorted_positions[0:num_positions - 1]

    def add_position(self, amount: float, item: Item):
        self._positions.append(ReceiptPosition(amount, item))

    def __repr__(self):
        return f'Receipt("{self._positions})'

    def __str__(self) -> str:
        # FIXME this is hacky but simple and not super important
        result = f"{self.date.strftime('%a, %d.%m.%Y, %H:%M:%S')}\n"
        separator = "-" * 50 + "\n"
        result += separator
        for position in self.positions:
            result += str(position)
        result += separator
        total_price = f"TOTAL: {str(self.total_price)}"
        result += f"{total_price:>{len(separator) - 1}}\n"
        return result


def random_receipt() -> Receipt:
    """Generates a random receipt"""
    position_num = randint(1, 10)
    return Receipt(positions=generate_positions(position_num))


def generate_receipts(num_receipts: int) -> List[Receipt]:
    """Generates a given number of fake receipts"""
    rec_list = []
    for i in range(0, num_receipts - 1):
        rec_list.append(random_receipt())
