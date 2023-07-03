import csv
from os import path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    @property
    def getter_name(self):
        return self.__name

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return f"{total_cost}: Общая стоимость товара"

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @name.setter
    """в сеттере name проверять, что длина наименования товара не больше 10 симвовов. 
    В противном случае, обрезать строку (оставить первые 10 символов)."""
    def name(self, lenght):
        if len(lenght) <= 10:
            self.__name = lenght
    @classmethod
    def instantiate_from_csv(path)
    with open(path, newline='items.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for row in reader:
                path(row['name'], row['price'],
                    row['quantity'])  # это дернет инит нашего класса, инит с тремя параметрами
        except KeyError:
            raise InstantiateCSVError("item.csv file is corrupted")