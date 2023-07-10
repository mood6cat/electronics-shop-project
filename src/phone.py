from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    # @number_of_sim.setter
    # def sim_cnt(self):

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
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
