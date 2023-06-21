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
