from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if sim > 0:
            self.__number_of_sim = sim
        else:
            raise ValueError('Количество SIM-карт должно быть целым числом и больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
        # "Phone('iPhone 14', 120000, 5, 2)"



# if __name__ == '__main__':
#     phone = Item('iPhone 14', 120000, 5)
#     phone2 = Phone('iPhone 3', 12000, 3, 1)
#     print(phone + phone2)
