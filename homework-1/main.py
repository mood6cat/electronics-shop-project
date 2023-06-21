from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000: Общая стоимость товара
    print(item2.calculate_total_price())  # 100000: Общая стоимость товара

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all)  # [<src.item.Item object at 0x000002161DCC7FD0>, <src.item.Item object at 0x000002161DCC7F70>]
