import pytest
from pipr06.receipts.price import Price


def test_if_price_negative():
    with pytest.raises(ValueError):
        Price(-100)


def test_price():
    price = Price(100)
    assert price.value_gr == 100


def test_price_wrong_value():
    with pytest.raises(TypeError):
        Price('asdsa')


def test_add():
    price = Price(100)
    price1 = Price(10)
    new_price = price + price1
    assert new_price.value_gr == 110


def test_mul():
    price = Price(20)
    new_price = price * 2
    assert new_price.value_gr == 40


def test_rmul():
    price = Price(20)
    new_price = 3 * price
    assert new_price.value_gr == 60


def test_lt():
    price = Price(10)
    price1 = Price(20)
    price2 = Price(30)
    assert price < price1
    assert not (price2 < price1)
