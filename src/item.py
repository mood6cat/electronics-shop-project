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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, lenght: str):
        """в сеттере name проверять, что длина наименования товара не больше 10 симвовов.
            В противном случае, обрезать строку (оставить первые 10 символов)."""
        if len(lenght) <= 10:
            self.__name = lenght

    @staticmethod
    def string_to_number(value: str):
        return int(value)
    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, newline='items.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])

                cls.all.append(cls(name, price, quantity))  # создаем экзмляры классы и кладем их в список

