from models.menu.eatery_menu import EateryMenu

class Drink(EateryMenu):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size