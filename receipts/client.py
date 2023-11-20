from typing import List
from .price import Price
from .receipt import Receipt

class Client:
    def __init__(self, name, user_id, receipts: list[Receipt] = None):
        self._name = name
        # Add more here

    @property
    #this method is already done
    def name(self):
        return self._name

    @property
    def user_id(self):
        pass

    @property
    def receipts(self):
        pass

    def add_receipt(self, receipt: Receipt):
        pass

    @property
    def total_spending(self):
        # HINT try to use sum() built-in function here
        # HINT you can also use a list comprehension
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


def random_client() -> Client:
    """Generates a random user"""


def generate_clients(
    num_clients: int, with_receipts=False, num_receipts=10
) -> List[Client]:
    """Generates a given number of fake clients with optional fake receipts"""
