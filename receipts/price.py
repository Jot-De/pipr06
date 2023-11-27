from typing import Tuple, List
from random import randint


class Price:
    # This is already done
    def __init__(self, value_gr):
        if value_gr < 0:
            raise ValueError("Price cannot be negative")
        self._value_gr = value_gr

    @property
    def value_gr(self):
        # This method is already done
        return self._value_gr

    def __add__(self, other: "Price") -> "Price":
        # This method is already done
        return Price(self.value_gr + other.value_gr)

    def __sub__(self, other: "Price") -> "Price":
        return Price(self.value_gr - other.value_gr)

    def __mul__(self, multiplier: float) -> "Price":
        return Price(self.value_gr * multiplier)

    def __rmul__(self, multiplier: float) -> "Price":
        return Price(self.value_gr * multiplier)

    def __lt__(self, other: "Price"):
        # HINT this should allow sorting Prices by value_gr
        return self.value_gr < other.value_gr
            
    @classmethod
    def from_float(cls, value: float) -> "Price":
        # HINT this will be called `p = Price.from_float(1.25)`
        # HINT we expect it to work like `p = Price(125)`
        # HINT notice cls instead of self!
        # HINT `cls(125)` will be `Price(125)` in this case!
        # HINT try using the round() built-in function
        cls._value_gr = round(value * 100)
        return cls

    def _split_price(self) -> Tuple[int, int]:
        return self.value_gr // 100, self.value_gr % 100

    def __str__(self) -> str:
        return self._format_price()

    def __repr__(self) -> str:
        # repr is a raw description of the instance
        # usually you implement it like this:
        return f"{self.__class__.__name__}(value_gr={self.value_gr})"

    def _format_price(self):
        # HINT zl, gr = self._split_price()
        zl, gr = self._split_price()
        return f'{zl} zł {gr} gr'

    def __eq__(self, other) -> bool:
        return self.value_gr == other.value_gr


def random_price() -> Price:
    """Generates a random Price object"""
    price = Price(randint(0, 9999))
    return price


def generate_prices(num_prices: int) -> List[Price]:
    """Generates a given number of random items"""
    list = []
    for i in range(num_prices):
        list.append(random_price())
    return list
