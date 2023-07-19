"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture  # Вот так пишется pytest к классу!!!
def item():
    return Item("test_item", 2500.0, 10)


def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == '25000.0: Общая стоимость товара'


def test_apply_discount(item):
    # устанавливаем новый уровень цен
    item.pay_rate = 2
    item.apply_discount()
    assert item.price == 5000.0
    assert item.price * item.pay_rate == 10000.0


def test_string_to_number(item):
    assert isinstance(item.string_to_number(item.quantity), int)


def test_name_setter(item):
    item.name = "Смартфон"
    assert item.name == "Смартфон"
    item.neme = "СуперСмартфон"
    assert item.name == "Смартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr(item):
    assert repr(item) == "Item('test_item', 2500.0, 10)"


def rest_str(item):
    assert str(item.__name) == 'test_item'

def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10




