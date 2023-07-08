"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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

def test_string_to_number(item):
    assert isinstance(item.string_to_number(item.quantity), int)

def test_name_setter(item):
    item.name="Смартфон"
    assert item.name=="Смартфон"
    item.neme = "СуперСмартфон"
    assert item.name == "Смартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
