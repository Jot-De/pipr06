from receipts.item import Item
import pytest


def test__init__():
    with pytest.raises(ValueError):
        Item('', 15)

def test__init__typical():
    item = Item('Mleko', 15)
    assert item.name == 'Mleko'

def test__init__price():
    item = Item('Mleko', 15)
    assert item.price == 15


def test__init__invalid_barcode():
    with pytest.raises(TypeError):
        Item('Mleko', 15, 15267215)


def test__init__invalid_length():
    with pytest.raises(ValueError):
        Item('Mleko', 15, '123456')


def test_valid_barcode():
    item = Item('Mleko', 15, '1234563890523')
    assert item.barcode == '1234563890523'


def test__str__():
    item = Item('Mleko', 15)
    info = "Item's name: Mleko (price: 15)."
    assert item.__str__() == info


def test__repr__():
    item = Item('Mleko', 15)
    description = 'Name: Mleko, price: 15, barcode: 1234567890123.'
    assert item.__repr__() == description
