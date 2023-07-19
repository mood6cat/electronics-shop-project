import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('iPhone 14', 120_000, 5, 2)


def test_repr(phone):

    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

def test_number_of_sim_setter(phone):
    
    assert phone.number_of_sim == 2





