from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_cnt: int):
        super().__init__(name, price, quantity)
        self.__sim_cnt = sim_cnt

    @property
    def sim_cnt(self):
        return self.__sim_cnt

    # @sim_cnt.setter
    # def sim_cnt(self):

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}, {self.price}, {self.quantity}, {self.sim_cnt}')"
        # "Phone('iPhone 14', 120000, 5, 2)"

    def __add__(self, other):
        """Сложить по количеству товара"""
        if isinstance(other, Item):  # Реализуйте проверки, чтобы нельзя было сложить
            # Phone или Item с экземплярами не Phone или Item классов.
            return self.quantity + other.quantity
        else:
            raise TypeError("Имена не совпадают")

# if __name__ == '__main__':
#     phone1 = Item('iPhone 14', 120000, 5)
#     phone2 = Phone('iPhone 3', 12000, 3, 1)
#     print(phone1 + phone2)
