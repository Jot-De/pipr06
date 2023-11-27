from distutils.log import info
from typing import List
from price import Price
from receipt import Receipt, generate_receipts, random_receipt
import random
 
class Client:
    def __init__(self, name, user_id, receipts: list[Receipt] = None):
        self._name = name
        self._user_id = user_id
        self._receipts = receipts
 
    @property
    # this method is already done
    def name(self):
        return self._name
 
    @property
    def user_id(self):
        return self._user_id
 
    @property
    def receipts(self):
        return self._receipts
 
    def add_receipt(self, receipt: Receipt):
        self._receipts.append(receipt)
 
    @property
    def total_spending(self):
        total_spendings = 0
        for element in self._receipts:
            total_spendings += element.total_price()
        return total_spendings
 
        # total_spending = [element for element in self._receipts]
        # return sum(total_spendings)
        # HINT you can also use a list comprehension
 
    def info_user(self):
        name_ID = self._name
        spends = self.total_spending()
        return f"Client {name_ID} has spent {spends} zł."
 
    def __str__(self):
        return self.info_user()
 
    def info_developer(self):
        name_ID = self._name
        ID = self._user_id
        spends = self.total_spending()
        return f"Name: {name_ID}.\n Id: {ID}.\n Spends: {spends}zł."
 
    def __repr__(self):
        return self.info_developer()
 
 
def random_client() -> Client:
    """Generates a random user"""
    name_list = ["Mike", "Alex", "George", "Sally", "John", 'Max', 'Gregory']
    random_name = random.choice(name_list)
    random_id = random.randint(0, 100)
    random_receip = random_receipt()
    my_client = Client(random_name, random_id, random_receip)
    return my_client
 
 
def generate_clients(num_clients: int, with_receipts=False, num_receipts=10) -> List[Client]:
    """Generates a given number of fake clients with optional fake receipts"""
    client_list = []
    if bool(with_receipts):
        receipts = generate_receipts(num_clients)
        for number in range(0, num_clients):
            my_client = random_client()
            my_client.add_receipt(receipts[number])
            client_list.append(my_client)
    else:
        for number in range(0, num_clients):
            my_client = random_client()
            client_list.append(my_client)
    return client_list
 